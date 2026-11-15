"""Proyección local previa a UNA acción. No descarga, publica ni ejecuta replays."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sys
# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo


SCHEMA = "duels-decision-view-v1"
CARD_SCALARS = {
    "id": str, "instanceId": str, "fullName": str, "name": str,
    "title": str, "type": str, "cost": int, "inkable": bool,
    "strength": int, "willpower": int, "lore": int, "moveCost": int,
    "damage": int, "exerted": bool, "justPlayed": bool,
}
EFFECT_SCALARS = {
    "type": str, "value": int, "duration": str, "sourceInstanceId": str,
    "sourceAbilityName": str, "expiresAtTurn": int, "expiresForPlayer": int,
}
PROMPT_SCALARS = {
    "id": str, "player": int, "type": str, "message": str,
    "sourceCardInstanceId": str, "sourceAbility": str, "required": bool,
    "minSelect": int, "maxSelect": int, "canDecline": bool,
    "yesLabel": str, "noLabel": str, "intent": str,
    "destinationLabel": str, "resolvingTriggerId": str,
}
PROMPT_ARRAYS = ("validTargets", "cardInstanceIds", "nonSelectableCardIds")
PROMPT_TYPES = {"select_target", "boolean", "select_card", "select_trigger", "order_cards"}
PUBLIC_CARD_EVENTS = {
    "CARD_PLAYED", "CARD_INKED", "CARD_DISCARDED", "CARD_DESTROYED",
    "CARD_RETURNED", "CARD_ATTACK", "CARD_QUEST", "SUPPORT_GIVEN",
}


def read_json(path):
    return json.loads(resolver_ruta(path).read_text(encoding="utf-8-sig"))


def scalars(obj, fields):
    # No recursive copying of unknown objects, including engine metadata.
    return {k: obj[k] for k, kind in fields.items() if type(obj.get(k)) is kind}


def project_card(card):
    if not isinstance(card, dict):
        raise ValueError("Carta sin estructura conocida")
    result = scalars(card, CARD_SCALARS)
    for key in ("subtypes", "colors"):
        if isinstance(card.get(key), list):
            result[key] = [s for s in card[key] if type(s) is str]
    if card.get("cardsUnder"):
        result["cardsUnder"] = [project_card(c) for c in card["cardsUnder"]]
    result["appliedEffectsRecordedByEngine"] = [
        scalars(e, EFFECT_SCALARS) for e in card.get("appliedEffects", [])
        if isinstance(e, dict)
    ]
    if isinstance(card.get("abilityCounters"), dict):
        result["abilityCountersRecordedByEngine"] = {
            k: v for k, v in card["abilityCounters"].items()
            if type(k) is str and type(v) in (int, bool)
        }
    return result


def project_player(player, own):
    result = scalars(player, {"lore": int, "inkDrops": int, "deckCount": int})
    if own:
        result["hand"] = [project_card(c) for c in player["hand"]]
        result["handCount"] = len(player["hand"])
    else:
        result["handCount"] = player.get("handCount")
        result["hiddenHand"] = "unknown"
    for zone in ("field", "items", "discard"):
        result[zone] = [project_card(c) for c in player.get(zone, [])]
    result["inkwell"] = []
    for entry in player.get("inkwell", []):
        # An accidentally attached full card on a hidden entry stays hidden.
        ink = scalars(entry, {"exerted": bool, "hidden": bool})
        if entry.get("hidden") is False and isinstance(entry.get("card"), dict):
            ink["card"] = project_card(entry["card"])
        result["inkwell"].append(ink)
    return result


def project_prompts(prompts, perspective):
    result, incomplete = [], False
    for p in prompts:
        if p.get("player") != perspective:
            continue
        q = scalars(p, PROMPT_SCALARS)
        incomplete |= p.get("type") not in PROMPT_TYPES
        for key in PROMPT_ARRAYS:
            if key in p:
                q[key] = [v for v in p[key] if type(v) is str]
        if "triggers" in p:
            q["triggers"] = [scalars(t, {
                "id": str, "sourceCardInstanceId": str, "sourceCardId": str,
                "sourceCardName": str, "abilityName": str,
                "optional": bool, "status": str,
            }) for t in p["triggers"]]
        # Fail closed for unfamiliar candidates/private look zones.
        incomplete |= bool(set(p) - set(PROMPT_SCALARS) - set(PROMPT_ARRAYS) - {"triggers"})
        result.append(q)
    return result, incomplete


def public_memory(events, game_id):
    """Observations, never a claim that a revealed card is still in hand."""
    result = []
    for e in events:
        revealed = e.get("type") == "CARD_REVEALED" and e.get("data", {}).get("revealDestination") == "hand"
        if e.get("type") not in PUBLIC_CARD_EVENTS and not revealed:
            continue
        refs = [scalars(c, {"id": str, "name": str}) for c in e.get("cardRefs", [])]
        if not refs:
            continue
        item = {"gameId": game_id, **scalars(e, {
            "index": int, "type": str, "player": int, "turnNumber": int,
            "instanceId": str,
        }), "cardsObserved": refs}
        if revealed:
            item["revealedDestination"] = "hand"
        result.append(item)
    return result


def project(snapshot, previous_events, identity, boundary, previous_games=()):
    perspective = snapshot["viewingAs"]
    prompts, incomplete = project_prompts(snapshot.get("pendingPrompts", []), perspective)
    context = scalars(snapshot, {
        "currentPlayer": int, "turnNumber": int, "hasInkedThisTurn": bool,
        "opponentHasPendingPrompts": bool,
    })
    # Base snapshots can already carry an eventual firstPlayer. Require a
    # preceding starting-player selection instead of trusting that field early.
    if boundary.get("startingPlayerSelectionAlreadyOccurred"):
        context.update(scalars(snapshot, {"firstPlayer": int}))
    else:
        starts = [e for e in previous_events if e.get("type") == "TURN_START"]
        if starts and starts[0].get("player") in (1, 2):
            context["firstPlayer"] = starts[0]["player"]
    return {
        "schema": SCHEMA, "position": identity, "boundary": boundary,
        "context": context, "own": project_player(snapshot["myPlayer"], True),
        "opponent": project_player(snapshot["opponent"], False),
        "pendingPrompts": prompts,
        "mulliganCountsAlreadyObserved": [
            {"index": e["index"], "player": e.get("player"),
             "count": e["data"]["mulliganCount"]}
            for e in previous_events if e.get("type") == "MULLIGAN"
            and type(e.get("data", {}).get("mulliganCount")) is int
        ],
        "publicObservationsEarlierThisGame": public_memory(previous_events, identity["gameId"]),
        "publicObservationsFromPreviousGames": list(previous_games),
        "limits": {
            "engineIsNotRulesAuthority": True,
            "pendingPromptIncomplete": incomplete,
            "revealedCardsNotGuaranteedStillInHand": True,
            "observationPlayerIsEventActorNotCardOwner": True,
            "unknownFieldsOmitted": True,
            "staticAbilitiesNeedCorpusVerification": True,
            "triggerBagAndPrivateLookZonesNotReconstructed": True,
            "firstPlayerNotProvenInPrefix": "firstPlayer" not in context,
        },
    }


def build_view(prefix, before_seq, previous_prefixes=()):
    prefix = resolver_ruta(prefix)
    path = lambda suffix: resolver_ruta(str(prefix) + suffix)
    actions_path, events_path, states_path, summary_path = [path(s) for s in (
        "-acciones.json", "-eventos.json", "-estados.jsonl.gz", "-resumen.json")]
    actions, events, summary = map(read_json, (actions_path, events_path, summary_path))
    if [a["seq"] for a in actions] != list(range(1, len(actions) + 1)):
        raise ValueError("Secuencia de acciones no continua")
    if not 1 <= before_seq <= len(actions):
        raise ValueError("Acción fuera de rango")
    action = actions[before_seq - 1]
    cutoff = action["logsFromInclusive"]
    if [e["index"] for e in events] != list(range(len(events))):
        raise ValueError("Índices de eventos no continuos")
    previous_cutoff = actions[before_seq - 2]["logsToExclusive"] if before_seq > 1 else cutoff
    if cutoff != previous_cutoff or not 0 <= cutoff <= len(events):
        raise ValueError("Frontera de logs incoherente")
    previous_events = events[:cutoff]
    if any(e["type"] in ("GAME_END", "GAME_CONCEDED") for e in previous_events):
        raise ValueError("No se revisan decisiones posteriores al final")
    snapshot = None
    with gzip.open(states_path, "rt", encoding="utf-8") as handle:
        for expected, line in enumerate(handle):
            row = json.loads(line)
            if row["seq"] != expected:
                raise ValueError("Secuencia de estados no continua")
            if row["seq"] == before_seq - 1:
                snapshot = row["snapshot"]
                break  # Never project the state after the selected action.
    if snapshot is None:
        raise ValueError("Falta el estado previo")
    if snapshot["viewingAs"] != summary["perspective"] or action["player"] != summary["perspective"]:
        raise ValueError("La acción no pertenece a la perspectiva solicitada")
    earlier_games = []
    previous_game_ids = set()
    for prior_prefix in previous_prefixes:
        prior = read_json(str(prior_prefix) + "-resumen.json")
        if prior["matchId"] != summary["matchId"] or prior["gameNumber"] >= summary["gameNumber"]:
            raise ValueError("Contexto BO3 fuera del encuentro o no anterior")
        if prior["gameId"] in previous_game_ids:
            raise ValueError("Contexto BO3 duplicado")
        if prior["perspective"] != summary["perspective"]:
            raise ValueError("Cambio de asiento: adaptar roles antes de incorporar memoria BO3")
        previous_game_ids.add(prior["gameId"])
        earlier_games.extend(public_memory(read_json(str(prior_prefix) + "-eventos.json"), prior["gameId"]))
    boundary = {
        "snapshotSeq": before_seq - 1, "eventsToExclusive": cutoff,
        "individualTurnOrdinal": sum(e["type"] == "TURN_START" for e in previous_events),
        "startingPlayerSelectionAlreadyOccurred": any(
            a["actionType"] == "CHOOSE_STARTING_PLAYER" for a in actions[:before_seq - 1]),
    }
    identity = {k: summary[k] for k in ("gameId", "matchId", "gameNumber", "perspective")}
    identity["beforeActionSeq"] = before_seq
    result = project(snapshot, previous_events, identity, boundary, earlier_games)
    # A list is legitimately known; only counts from the per-game summary,
    # never deckOrder. Keep printing distinctions for later audited normalization.
    result["ownRegisteredList"] = [scalars(c, {"id": str, "name": str, "copies": int})
                                   for c in summary["decklist"]]
    result["inputHashes"] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in (actions_path, events_path, states_path, summary_path)}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prefix", type=resolver_ruta, help="Ruta sin sufijo: .../partida-01")
    parser.add_argument("--before-seq", type=int, required=True)
    parser.add_argument("--previous-prefix", action="append", default=[], type=resolver_ruta)
    parser.add_argument("--out", type=resolver_ruta, required=True)
    args = parser.parse_args()
    result = build_view(args.prefix, args.before_seq, args.previous_prefix)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Vista previa guardada: {args.out}")


if __name__ == "__main__":
    main()
