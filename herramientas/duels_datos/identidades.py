"""Recupera nombres completos observados en replays ya descargados, sin red."""
import argparse
from collections import defaultdict
import gzip
import json
from pathlib import Path
import re
import unicodedata

from .catalogo import contained_ref, file_hash, read_json, source, verified_file

import sys
# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo


def observed_names(value, names):
    if isinstance(value, dict):
        card_id, name = value.get('id'), value.get('fullName')
        if isinstance(card_id, str) and re.fullmatch(r'\d+-[A-Za-z0-9-]+', card_id) and isinstance(name, str) and name.strip():
            names[card_id].add(unicodedata.normalize('NFKC', name).strip())
        for child in value.values():
            observed_names(child, names)
    elif isinstance(value, list):
        for child in value:
            observed_names(child, names)


def collect(manifests, game_ids=None):
    names, sources, seen = defaultdict(set), [], set()
    for path in manifests:
        manifest = read_json(path)
        if manifest.get('schema_version') != 1 or manifest.get('source') != 'https://duels.ink':
            raise ValueError('Manifiesto incompatible')
        for game_id, game in manifest['games'].items():
            if game_ids is not None and game_id not in game_ids:
                continue
            asset = game.get('assets', {}).get('replay', {})
            if asset.get('status') != 'downloaded':
                continue
            ref = asset['json']
            if ref['sha256'] in seen:
                continue
            local = contained_ref(resolver_ruta(path).resolve().parent, ref['path'])
            check = verified_file(local, ref['sha256'], 'replay', game_id, game['row'].get('your_player'))
            if check['status'] != 'verified_json':
                raise ValueError('Replay de identidades no verificado')
            seen.add(ref['sha256'])
            evidence = source(local, 'replay_card_identity_evidence')
            sources.append(evidence)
            observed_names(read_json(local), names)
    conflicts = {card: sorted(values) for card, values in sorted(names.items()) if len(values) > 1}
    return {'schema': 'duels-observed-identities-v1',
            'identities': {card: 'full-name:' + next(iter(values)) for card, values in sorted(names.items()) if len(values) == 1},
            'conflicts': conflicts, 'sources': sorted(sources, key=lambda s: s['path']),
            'method': 'Exact fullName only; NFKC and outer whitespace; observed simulator identity, not normative verification'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=resolver_ruta, action='append', required=True)
    parser.add_argument('--selection', type=resolver_ruta, help='Selección privada con target_game_ids; no incluye replays de otros mazos')
    parser.add_argument('--out', type=resolver_ruta, required=True)
    args = parser.parse_args()
    games = set(read_json(args.selection)['target_game_ids']) if args.selection else None
    output = collect(args.manifest, games)
    if args.out.exists() and read_json(args.out) != output:
        raise ValueError('Mapa existente distinto: elige otra ruta para conservar su versión')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if not args.out.exists():
        args.out.write_text(json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'replays': len(output['sources']), 'identified_ids': len(output['identities']), 'conflicting_ids': len(output['conflicts'])}))


if __name__ == '__main__':
    main()
