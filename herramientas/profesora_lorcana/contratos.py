"""Identidad de artefactos compartida: contrato de integración 0.2 (sin red)."""
import hashlib
import json
from pathlib import Path

import sys
# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo

VERSION = '0.2'
HASH_KIND = 'canonical-json-v1'


def canonical(value):
    _shape(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'),
                      allow_nan=False).encode('utf-8')


def _shape(value):
    if isinstance(value, dict):
        if any(not isinstance(key, str) for key in value):
            raise ValueError('Las claves JSON deben ser strings')
        for item in value.values():
            _shape(item)
    elif isinstance(value, list):
        for item in value:
            _shape(item)
    elif value is not None and type(value) not in (str, int, float, bool):
        raise ValueError('Valor ajeno a JSON')


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def reference(artifact):
    if not isinstance(artifact, dict) or not isinstance(artifact.get('schema'), str) or not artifact['schema']:
        raise ValueError('Artefacto sin schema')
    return {'schema': artifact['schema'], 'sha256': digest(artifact)}


def check_reference(ref, artifact):
    if ref != reference(artifact):
        raise ValueError('Referencia de artefacto incompatible')


def _object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Claves JSON duplicadas')
        result[key] = value
    return result


def _constant(value):
    raise ValueError('Constante JSON no finita')


def read(path):
    return json.loads(resolver_ruta(path).read_text(encoding='utf-8-sig'),
                      object_pairs_hook=_object, parse_constant=_constant)


def file_digest(path):
    """Integridad de bytes, separada de las referencias semánticas entre agentes."""
    return hashlib.sha256(resolver_ruta(path).read_bytes()).hexdigest()
