"""Genera el listado depurado a partir de los casos agrupados."""
import json
import shutil
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'analisis/discord-2026-09-05'
all_path = OUT / 'casos_agrupados.json'
all_data = json.loads(all_path.read_text(encoding='utf-8'))
all_cases = all_data['casos']

def unresolved_image(c):
    if not c.get('requiere_imagen', False):
        return False
    notes = ' '.join(c.get('notas', [])).lower()
    # Algunos adjuntos son solo apoyo visual. Estos patrones indican que
    # falta identificar la carta o su versión exacta para entender el caso.
    return any(term in notes for term in (
        'identificarla antes', 'identificable únicamente',
        'debe identificarse antes', 'no debe inventarse',
    ))

# Un caso se considera claro si la captura contiene una respuesta directa y
# una consulta identificable. Un adjunto incidental no lo elimina; sí lo hace
# una imagen imprescindible para identificar la carta o versión.
clear_cases = [
    c for c in all_cases
    if c.get('estado_respuesta') == 'respuesta_presente'
    and bool(c.get('preguntas_indices'))
    and not unresolved_image(c)
]
removed = [c for c in all_cases if c not in clear_cases]

# El listado anterior queda conservado con un nombre explícito para no perder
# los casos pendientes, aunque ya no se mezcle con el listado depurado.
old_md = OUT / 'CASOS.md'
if old_md.exists() and not (OUT / 'CASOS_TODOS.md').exists():
    shutil.copyfile(old_md, OUT / 'CASOS_TODOS.md')

meta = {
    'fuente_sha256': all_data['fuente_sha256'],
    'criterio_claridad': 'Se conserva únicamente estado_respuesta=respuesta_presente, con preguntas_indices no vacío y sin una dependencia no resuelta de imagen para identificar la carta o versión. Se eliminan debates sin cierre, casos sin respuesta, casos con contexto insuficiente y casos cuyo texto no permite validar la consulta sin el adjunto.',
    'casos_originales': len(all_cases),
    'casos_claros': len(clear_cases),
    'casos_eliminados_por_claridad': len(removed),
    'ambitos': dict(Counter(c['ambito'] for c in clear_cases)),
    'advertencia': 'La respuesta procede de la captura. La comprobación contra reglas oficiales y wiki se conserva en validacion_casos_102.json y VALIDACION_CASOS.md.',
}
(OUT / 'casos_claros.json').write_text(json.dumps({**meta, 'casos': clear_cases}, ensure_ascii=False, indent=2), encoding='utf-8')
(OUT / 'casos_eliminados_por_claridad.json').write_text(json.dumps({**meta, 'casos': removed}, ensure_ascii=False, indent=2), encoding='utf-8')

labels = {
    'reglas_juego': 'Reglas de juego',
    'arbitraje_torneos': 'Arbitraje y torneos',
    'organizacion_herramientas': 'Organización y herramientas',
    'documentacion_formatos': 'Documentación y formatos',
}
states = {'respuesta_presente': 'Respuesta presente'}
lines = [
    '# Casos claros de Discord', '',
    f"Se conservan **{len(clear_cases)} casos claros** de los {len(all_cases)} agrupados. Se han eliminado {len(removed)} por falta de claridad.", '',
    meta['criterio_claridad'], '',
    meta['advertencia'], '',
    '[JSON de casos claros](casos_claros.json) · [Casos eliminados](casos_eliminados_por_claridad.json) · [Listado completo conservado](CASOS_TODOS.md)', '',
]
for scope, label in labels.items():
    scoped = [c for c in clear_cases if c['ambito'] == scope]
    if not scoped:
        continue
    lines += [f'## {label} ({len(scoped)})', '', '| Caso | Consulta | Mensajes |', '| --- | --- | --- |']
    for c in scoped:
        links = ', '.join(f"[{i}]({next(m['url'] for m in c['fuentes']['preguntas'] if m['indice'] == i)})" for i in c['preguntas_indices'])
        lines.append(f"| {c['id']} | {c['titulo'].replace('|', '/')} | {links} |")
    lines.append('')
lines += ['## Detalle', '']
for c in clear_cases:
    lines += [f"### {c['id']}", '', f"**{c['titulo']}**", '', c['pregunta'], '',
              f"**Respuesta recogida:** {c['resumen_respuestas']}", '',
              '**Consultas:** ' + ', '.join(f"[{m['indice']}]({m['url']})" for m in c['fuentes']['preguntas']) + '.', '']
    if c['fuentes']['respuestas']:
        lines += ['**Respuestas:** ' + ', '.join(f"[{m['indice']}]({m['url']})" for m in c['fuentes']['respuestas']) + '.', '']
    if c.get('notas'):
        lines += ['Observaciones: ' + ' '.join(c['notas']), '']
(OUT / 'CASOS_CLAROS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

# CASOS.md es el punto de entrada visible y queda depurado. CASOS_TODOS.md
# conserva la versión anterior para auditoría.
shutil.copyfile(OUT / 'CASOS_CLAROS.md', OUT / 'CASOS.md')
print(json.dumps(meta, ensure_ascii=True, indent=2))
