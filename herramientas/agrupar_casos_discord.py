"""Consolida la revisión semántica y conserva trazabilidad por mensaje."""
import collections
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'analisis/discord-2026-09-05'

def read(name):
    return json.loads((OUT / name).read_text(encoding='utf-8'))

source = read('mensajes_procesados.json')
messages = {m['indice']: m for m in source['mensajes']}
decisions = read('decisiones_agrupacion.json')
cases = {}
reviewed = set()
unassigned = []
for part in range(1, 4):
    data = read(f'casos_parte_{part}.json')
    reviewed.update(data['mensajes_revisados'])
    unassigned.extend(data['sin_caso'])
    for number, case in enumerate(data['casos'], 1):
        key = f'P{part}-{number:02d}'
        cases[key] = copy.deepcopy(case)
        cases[key]['partes_origen'] = [key]

for group in decisions.get('fusiones', []):
    keys = group['partes']
    merged = cases[keys[0]]
    for key in keys[1:]:
        other = cases.pop(key)
        for field in ['preguntas_indices', 'respuestas_indices', 'contexto_indices', 'temas', 'cartas_mencionadas', 'notas', 'partes_origen']:
            merged[field] = list(dict.fromkeys(merged.get(field, []) + other.get(field, [])))
        merged['resumen_respuestas'] += '\n\n' + other['resumen_respuestas']
        for field in ['requiere_imagen', 'posible_set13', 'especulacion_prepublicacion']:
            merged[field] = bool(merged.get(field) or other.get(field))
    merged.update(group.get('ajustes', {}))

for key, adjustments in decisions.get('ajustes', {}).items():
    cases[key].update(adjustments)

ordered = sorted(cases.values(), key=lambda c: min(c['preguntas_indices'] or c['contexto_indices'] or c['respuestas_indices']))
assigned = set()
for number, case in enumerate(ordered, 1):
    case['id'] = f'CASO-{number:03d}'
    case.setdefault('decision_edicion', 'conservar')
    case.setdefault('motivo_edicion', 'No se ha identificado como consulta de Set 14 sin definición en la wiki. Los casos de Set 13 se conservan.')
    case['validacion_respuesta'] = {'estado': 'pendiente', 'fuente_oficial': None}
    case.setdefault('cobertura_wiki', {'estado': 'pendiente', 'paginas': []})
    case['fuentes'] = {}
    for role, field in [('preguntas', 'preguntas_indices'), ('respuestas', 'respuestas_indices'), ('contexto', 'contexto_indices')]:
        indices = sorted(set(case.get(field, [])))
        case[field] = indices
        assert all(i in messages for i in indices), (case['id'], indices)
        assigned.update(indices)
        case['fuentes'][role] = [{k: messages[i][k] for k in ['indice', 'id', 'fecha', 'url', 'autor_original', 'texto', 'media_sin_iconos_interfaz']} for i in indices]
    case['fecha_inicial'] = min(m['fecha'] for role in case['fuentes'].values() for m in role)

without_case = set()
for item in unassigned:
    without_case.update(item.get('indices', [item['indice']] if 'indice' in item else []))
assert reviewed == set(messages), ('Revision incompleta', set(messages) - reviewed)
assert assigned | without_case == set(messages), ('Sin clasificar', set(messages) - assigned - without_case)

kept = [c for c in ordered if c['decision_edicion'] == 'conservar']
excluded = [c for c in ordered if c['decision_edicion'] != 'conservar']
meta = {
    'fuente_sha256': source['sha256_origen'],
    'alcance': 'Listado y agrupación semántica. Respuestas del canal sin validar y cobertura wiki pendiente.',
    'criterio_edicion': decisions['criterio_edicion'],
    'mensajes_revisados': len(reviewed), 'casos_antes_filtro': len(ordered),
    'casos_conservados': len(kept), 'casos_apartados': len(excluded),
    'ambitos_conservados': dict(collections.Counter(c['ambito'] for c in kept)),
    'estado_respuestas_conservadas': dict(collections.Counter(c['estado_respuesta'] for c in kept)),
    'advertencia': 'Historial incompleto; adjuntos no leídos. Las respuestas son testimonios del canal, no conclusiones oficiales. La agrupación no implica corrección de las respuestas.',
}
for filename, payload in [('casos_agrupados.json', {**meta, 'casos': kept}), ('casos_apartados_edicion.json', {**meta, 'casos': excluded}), ('auditoria_agrupacion.json', {**meta, 'indices_asignados_a_caso': sorted(assigned), 'sin_caso': unassigned})]:
    (OUT / filename).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')

labels = {'reglas_juego': 'Reglas de juego', 'arbitraje_torneos': 'Arbitraje y torneos', 'organizacion_herramientas': 'Organización y herramientas', 'documentacion_formatos': 'Documentación y formatos'}
states = {'respuesta_presente': 'Con respuesta', 'debate_sin_cierre': 'Debate sin cierre', 'sin_respuesta': 'Sin respuesta', 'contexto_insuficiente': 'Falta contexto'}
lines = ['# Casos agrupados de Discord', '',
         f"Revisados **{len(reviewed)} mensajes**: **{len(ordered)} casos**, de los que **{len(kept)} se conservan** y **{len(excluded)} se apartan por edición**.", '',
         decisions['criterio_edicion'], '',
         'La revisión de corrección de respuestas y la comprobación de su existencia en la wiki quedan pendientes en todos los casos. «Con respuesta» solo significa que hay una respuesta en la captura.', '',
         'Los casos con imágenes o contexto incompleto se conservan identificados. La captura no garantiza todo el historial del canal.', '',
         '[JSON de casos conservados](casos_agrupados.json) · [JSON de casos apartados](casos_apartados_edicion.json) · [Auditoría de cobertura](auditoria_agrupacion.json)', '']
for scope, label in labels.items():
    scoped = [c for c in kept if c['ambito'] == scope]
    lines += [f'## {label} ({len(scoped)})', '', '| Caso | Consulta | Respuesta en captura |', '| --- | --- | --- |']
    for c in scoped:
        lines.append(f"| [{c['id']}](#{c['id'].lower()}) | {c['titulo'].replace('|', '/')} | {states[c['estado_respuesta']]}{' · Imagen necesaria' if c.get('requiere_imagen') else ''} |")
    lines.append('')
lines += ['## Detalle de los casos conservados', '']
for c in kept:
    lines += [f"### {c['id']}", '', f"**{c['titulo']}**", '', c['pregunta'], '',
              f"**Respuesta recogida ({states[c['estado_respuesta']].lower()}):** {c['resumen_respuestas']}", '']
    for role, label in [('preguntas', 'Consultas'), ('respuestas', 'Respuestas')]:
        if c['fuentes'][role]:
            lines += [label + ': ' + ', '.join(f"[{m['indice']}]({m['url']})" for m in c['fuentes'][role]) + '.', '']
    if c.get('requiere_imagen'):
        lines += ['Necesita revisar imágenes o adjuntos para completar el caso.', '']
    if c.get('notas'):
        lines += ['Observaciones: ' + ' '.join(c['notas']), '']
lines += ['## Casos apartados por edición', '', 'Se conservan en el JSON separado, con mensajes, respuestas y motivos. No se han eliminado del corpus.', '', '| Caso | Consulta | Motivo |', '| --- | --- | --- |']
for c in excluded:
    lines.append(f"| {c['id']} | {c['titulo'].replace('|', '/')} | {c['motivo_edicion'].replace('|', '/')} |")
(OUT / 'CASOS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(json.dumps(meta, ensure_ascii=True, indent=2))
