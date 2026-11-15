"""Inspecciona replays de Duels como datos; no ejecuta su contenido ni publica."""
import argparse
import copy
import gzip
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys

if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def collect_catalog(value, catalog):
    if isinstance(value, dict):
        if isinstance(value.get('id'), str) and (value.get('fullName') or value.get('name')):
            card_id = value['id']
            if re.fullmatch(r'\d+-[A-Za-z0-9-]+', card_id):
                name = value.get('fullName') or value['name']
                previous = catalog.get(card_id)
                if previous is None or value.get('fullName'):
                    catalog[card_id] = name
        for item in value.values():
            collect_catalog(item, catalog)
    elif isinstance(value, list):
        for item in value:
            collect_catalog(item, catalog)


def apply_operation(state, operation, upserts, missing_removals):
    # Duels también usa replace para crear ciertas propiedades de objetos.
    parts = [p.replace('~1', '/').replace('~0', '~') for p in operation['path'].split('/')[1:]]
    if not parts:
        raise ValueError('No se esperaba un parche sobre la raíz')
    parent = state
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    key = parts[-1]
    op = operation['op']
    if op not in ('add', 'replace', 'remove'):
        raise ValueError('Operación no soportada: ' + op)
    if isinstance(parent, list):
        index = len(parent) if key == '-' else int(key)
        if op == 'add':
            assert 0 <= index <= len(parent), operation
            parent.insert(index, copy.deepcopy(operation['value']))
        elif op == 'replace':
            assert 0 <= index < len(parent), operation
            parent[index] = copy.deepcopy(operation['value'])
        else:
            parent.pop(index)
    else:
        if op == 'remove':
            if key not in parent:
                missing_removals[operation['path']] += 1
            else:
                del parent[key]
        else:
            if op == 'replace' and key not in parent:
                upserts[operation['path']] += 1
            parent[key] = copy.deepcopy(operation['value'])


def render_message(log):
    refs = log.get('cardRefs', [])

    def replace(match):
        index = int(match[1])
        if index >= len(refs):
            raise ValueError('Referencia de carta fuera de rango: ' + log['id'])
        return refs[index]['name']

    return re.sub(r'\{card:(\d+)\}', replace, log['message'])


def timestamp(ms):
    if ms is None:
        return None
    # El 15/10/2026 Madrid está en UTC+02:00. No depende de la zona del host.
    return datetime.fromtimestamp(ms / 1000, tz=timezone(timedelta(hours=2))).isoformat(timespec='milliseconds')


def slim_card(card):
    fields = ('id','instanceId','fullName','name','title','cost','inkable','strength','willpower','lore','damage','exerted','justPlayed','subtypes','abilities','appliedEffects','abilityCounters')
    result = {key: card[key] for key in fields if key in card}
    if card.get('cardsUnder'):
        result['cardsUnder'] = [slim_card(c) if isinstance(c, dict) else c for c in card['cardsUnder']]
    return result


def slim_player(player):
    result = {k: player[k] for k in ('lore','inkDrops','deckCount','handCount') if k in player}
    for zone in ('hand','field','items','inkwell','discard'):
        if zone in player:
            result[zone] = [slim_card(c) if isinstance(c, dict) else c for c in player[zone]]
    return result


def extract(path, number, out, catalog):
    data = read_json(path)
    assert data['format'] == 'duels-replay-v1'
    assert data['perspective'] == data['baseSnapshot']['viewingAs']
    frames = data['frames']
    logs = data['logs']
    assert [f['seq'] for f in frames] == list(range(1, len(frames) + 1))
    assert all(a['logCountAfter'] <= b['logCountAfter'] for a,b in zip(frames, frames[1:]))
    assert frames[-1]['logCountAfter'] == len(logs)
    state = copy.deepcopy(data['baseSnapshot'])
    upserts = Counter()
    missing_removals = Counter()
    actions = []
    previous_count = data['baseSnapshotLogCount']
    prefix = f'partida-{number:02}'
    with gzip.open(out / f'{prefix}-estados.jsonl.gz', 'wt', encoding='utf-8') as handle:
        handle.write(json.dumps({'seq': 0, 'snapshot': state}, ensure_ascii=False) + '\n')
        for frame in frames:
            for operation in frame['patch']:
                try:
                    apply_operation(state, operation, upserts, missing_removals)
                except (KeyError, IndexError, AssertionError) as exc:
                    raise ValueError(f"Error en frame {frame['seq']}: {operation}") from exc
            count = frame['logCountAfter']
            assert previous_count <= count <= len(logs)
            assert len(state['myPlayer']['deckOrder']) == state['myPlayer']['deckCount']
            actions.append({
                'seq': frame['seq'], 'actionType': frame['actionType'],
                'player': frame['player'], 'turnNumber': frame['turnNumber'],
                'timestamp': frame['ts'], 'logsFromInclusive': previous_count,
                'logsToExclusive': count, 'currentPlayerAfter': state.get('currentPlayer'),
                'snapshotTurnNumberAfter': state.get('turnNumber'),
                'myPlayer': slim_player(state['myPlayer']),
                'opponent': slim_player(state['opponent']),
                'pendingPrompts': copy.deepcopy(state.get('pendingPrompts', [])),
                'clock': frame.get('clock'),
            })
            handle.write(json.dumps({'seq': frame['seq'], 'actionType': frame['actionType'], 'snapshot': state}, ensure_ascii=False) + '\n')
            previous_count = count
    assert state['status'] == 'finished'
    assert state['winner'] == data['winner']
    assert state['victoryReason'] == data['victoryReason']
    def card_weight(card):
        return 1 + sum(card_weight(c) if isinstance(c, dict) else 1 for c in card.get('cardsUnder', []))
    own = state['myPlayer']
    final_card_count = own['deckCount'] + sum(card_weight(c) for zone in ('hand','field','items','inkwell','discard') for c in own.get(zone, []))
    assert final_card_count == len(data['decklist'])
    events = [dict(log, resolvedMessage=render_message(log), index=index) for index,log in enumerate(logs)]
    assert len({e['id'] for e in events}) == len(events)
    starts = [log for log in logs if log['type'] == 'TURN_START']
    deck = Counter(data['decklist'])
    initial_cards = Counter(c['id'] for c in data['baseSnapshot']['myPlayer']['hand'])
    initial_cards.update(data['baseSnapshot']['myPlayer']['deckOrder'])
    assert initial_cards == deck, 'Mano inicial y orden inicial no coinciden con decklist'
    summary = {
        'source': str(path.resolve()), 'sourceBytes': path.stat().st_size,
        'sourceSha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'format': data['format'], 'gameId': data['gameId'], 'perspective': data['perspective'],
        'playerNames': data['playerNames'], 'firstPlayer': state['firstPlayer'],
        'matchId': state['matchView']['id'], 'formatMatch': state['matchView']['format'],
        'gameNumber': state['matchView']['currentGameNumber'],
        'matchScoreAfter': [state['matchView']['player1Wins'], state['matchView']['player2Wins']],
        'winner': state['winner'], 'victoryReason': state['victoryReason'],
        'loreAfter': {'1' if data['perspective']==2 else '2':state['opponent']['lore'], str(data['perspective']):state['myPlayer']['lore']},
        'exportedTurnCount': data['turnCount'], 'turnStartEvents': len(starts),
        'turnStartsByPlayer': dict(Counter(str(log['player']) for log in starts)),
        'startedAtMadrid': timestamp(state.get('gameStartedAt')),
        'endedAtMadrid': timestamp(state.get('gameEndedAt')),
        'durationSeconds': (state['gameEndedAt']-state['gameStartedAt'])/1000,
        'frames':len(frames), 'logs':len(logs),
        'patchOperations':dict(Counter(p['op'] for f in frames for p in f['patch'])),
        'replaceCreatingProperties':dict(upserts),
        'removeMissingProperties':dict(missing_removals),
        'logTypes':dict(Counter(log['type'] for log in logs)),
        'actionTypes':dict(Counter(f['actionType'] for f in frames)),
        'decklist': [{'id':key, 'name':catalog.get(key,'[nombre no localizado]'), 'copies':qty} for key,qty in sorted(deck.items())],
        'initialHand':[c.get('fullName', c.get('name')) for c in data['baseSnapshot']['myPlayer']['hand']],
        'mulligans':[e for e in events if e['type']=='MULLIGAN'],
        'unknownOpponentHandInFinalState': 'hand' not in state['opponent'],
        'ownDeckOrderAvailable': 'deckOrder' in state['myPlayer'],
        'gameEndEvents': len([e for e in events if e['type']=='GAME_END']),
        'validation': {'allFramesApplied':True, 'allLogsAccountedFor':True, 'deckOrderCountConsistent':True, 'initialDeckConservation':True, 'finalCardCount':final_card_count, 'resultMatchesHeader':True},
    }
    write_json(out / f'{prefix}-resumen.json', summary)
    write_json(out / f'{prefix}-eventos.json', events)
    write_json(out / f'{prefix}-acciones.json', actions)
    write_json(out / f'{prefix}-estado-final.json', state)
    readable = [f'# Registro extraído: partida {number}', '', 'Mensajes originales de Duels en inglés, con las referencias de cartas sustituidas por sus nombres. No contiene valoración de jugadas.', '']
    ordinal = 0
    for event in events:
        if event['type'] == 'TURN_START':
            ordinal += 1
            readable += ['', f"## Turno individual {ordinal} · etiqueta Duels {event['turnNumber']} · jugador {event['player']}", '']
        player = 'sistema' if event['player'] is None else f"J{event['player']}"
        readable.append(f"- [{event['index']:03}] {timestamp(event['timestamp'])[11:23]} · {player} · {event['type']}: {event['resolvedMessage']}")
    (out / f'{prefix}-registro.md').write_text('\n'.join(readable)+'\n', encoding='utf-8')
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('inputs', nargs='+', type=resolver_ruta)
    parser.add_argument('--out', type=resolver_ruta, default=ruta_trabajo('analisis/duels-2026-10-15'))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    catalog = {}
    for path in args.inputs:
        collect_catalog(read_json(path), catalog)
    results = [extract(path, index, args.out, catalog) for index,path in enumerate(args.inputs, 1)]
    assert len({r['matchId'] for r in results})==1, 'No pertenecen al mismo encuentro'
    assert all(r['decklist']==results[0]['decklist'] for r in results), 'Las listas difieren'
    write_json(args.out/'catalogo-observado.json',catalog)
    write_json(args.out/'encuentro-resumen.json',results)
    for result in results:
        brief = {k:result[k] for k in ('gameNumber','winner','victoryReason','loreAfter','frames','logs','turnStartEvents','exportedTurnCount','durationSeconds')}
        brief['replaceCreatingPropertiesCount'] = sum(result['replaceCreatingProperties'].values())
        brief['removeMissingPropertiesCount'] = sum(result['removeMissingProperties'].values())
        print(json.dumps(brief,ensure_ascii=False))


if __name__=='__main__':
    main()
