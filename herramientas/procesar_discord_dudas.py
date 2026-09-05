"""Procesamiento conservador de una captura DOM de Discord; no valida reglas."""
import collections
import hashlib
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

source = Path(sys.argv[1])
out = Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
raw = source.read_bytes()
data = json.loads(raw)
date_line = re.compile(r'(?:lunes|martes|miércoles|jueves|viernes|sábado|domingo), \d{1,2} de \w+ de \d{4}, \d{1,2}:\d{2}')
topics = {
    'torneos_arbitraje': r'tournament|judge|penalt|warning|infraction|deck.?list|slow play|conced|cheat|opponent.*sleeve|match slip|round|CCQ|DLC',
    'legalidad_formatos_documentacion': r'legal|banned|ban list|rotation|infinity|errata|document|app\b|comprehensive|CRD',
    'habilidades_tiempos_efectos': r'trigger|bag\b|replacement|resolve|resolving|effect|ability|abilities|simultaneous|turn|timing',
    'combate_dano': r'challeng|damage|resist|strength|willpower|banish',
    'jugar_costes_tinta': r'ink|cost|shift|sing|song|play.*card|exert|ready',
    'zonas_movimiento': r'discard|hand|deck|location|move|draw|reveal',
}
implicit = re.compile(r'\b(?:wondering|confused|not sure|unsure|unclear|clarif\w*|question|doubt|can someone|could someone|does anyone|anyone know|trying to understand|help me understand|how (?:does|do|would|can)|whether)\b', re.I)
rows = []
for i, m in enumerate(data['messages']):
    observed = m.get('observedText') or ''
    matches = [v for v in date_line.finditer(observed) if not re.search(r'\(editado\)\s*$', observed[:v.start()])]
    if m.get('timestamp'):
        local = datetime.fromisoformat(m['timestamp'].replace('Z', '+00:00')) + timedelta(hours=2)
        matching = [v for v in matches if re.search(rf', {local.day} de \w+ de {local.year}, {local.hour}:\d{{2}}$',v.group()) and v.group().endswith(f'{local.hour}:{local.minute:02d}')]
        matches = matching or matches
    text = observed[matches[0].end():].strip() if matches else (m.get('content') or '')
    # Remove only the recognizable trailing reaction widget, retain ambiguous UI.
    text = re.sub(r'(?:\n\d+)?\nAñadir reacción(?:\n.*)*$', '', text).strip()
    text = re.sub(r'(?::[\w+-]+:\s*Haz clic para reaccionar)+.*$', '', text, flags=re.S).strip()
    text = re.sub(r'\d*Añadir reacción(?:ResponderReenviarMás)?.*$', '', text, flags=re.S).strip()
    text = re.sub(r'\s*\(editado\)\s*(?:lunes|martes|miércoles|jueves|viernes|sábado|domingo), \d{1,2} de \w+ de \d{4}, \d{1,2}:\d{2}', '', text).strip()
    media = [u for u in m.get('mediaUrls', []) if not any(s in u for s in ['/role-icons/', '/clan-badges/', 'discord.com/assets/', '/avatars/', '/emojis/'])]
    detection_text = re.sub(r'https?://\S+', '', text)
    reasons = []
    if '?' in detection_text or '¿' in detection_text:
        reasons.append('interrogacion_explicita')
    if implicit.search(text):
        reasons.append('indicador_de_duda_o_peticion')
    if re.search(r'\b(?:can (?:i|you|they|he|she|we)|is there|in which order|want to confirm|please confirm|does (?:this|that|it)|would (?:this|that|it)|how to)\b', text, re.I):
        reasons.append('posible_pregunta_sin_interrogacion')
    if reasons:
        kind = 'duda_candidata'
    elif not text or text in ['Imagen', 'Image']:
        kind = 'multimedia_o_sin_texto'
    elif re.fullmatch(r'(?:thank.*|thanks.*|ty|yes[.! ]*|no[.! ]*|ok(?:ay)?[.! ]*|got it.*|agreed.*|👍)', text, re.I | re.S):
        kind = 'agradecimiento_o_confirmacion'
    elif re.search(r'https?://', text) and len(text) < 350:
        kind = 'enlace_o_recurso'
    else:
        kind = 'respuesta_debate_o_contexto'
    rows.append({
        'indice': i, 'id': m.get('id'), 'url': m.get('url'),
        'autor_original': m.get('author'), 'fecha': m.get('timestamp'),
        'texto': text, 'content_original': m.get('content'),
        'observedText_original': observed,
        'texto_recuperado_de_observedText': bool(matches),
        'content_difiere': text != (m.get('content') or '').strip(),
        'prefijo_cita_y_cabecera': observed[:matches[0].start()] if matches else None,
        'tipo_preliminar': kind, 'motivos_candidatura': reasons,
        'temas_preliminares': [k for k,v in topics.items() if re.search(v,text,re.I)],
        'enlaces_originales': m.get('links', []), 'media_urls_originales': m.get('mediaUrls', []),
        'media_sin_iconos_interfaz': media,
        'requiere_revision': True,
    })

candidates = []
for i, r in enumerate(rows):
    if r['tipo_preliminar'] == 'duda_candidata':
        candidates.append({**r, 'contexto_anterior_ids': [x['id'] for x in rows[max(0,i-2):i]],
                           'contexto_posterior_ids': [x['id'] for x in rows[i+1:i+4]],
                           'contexto_es_respuesta_verificada': False})
stats = {
    'mensajes': len(rows), 'ids_unicos': len({r['id'] for r in rows}),
    'sin_autor': sum(r['autor_original'] is None for r in rows),
    'sin_fecha': sum(r['fecha'] is None for r in rows),
    'textos_recuperados': sum(r['texto_recuperado_de_observedText'] for r in rows),
    'content_difiere_del_texto_recuperado': sum(r['content_difiere'] for r in rows),
    'mensajes_con_media_sin_iconos': sum(bool(r['media_sin_iconos_interfaz']) for r in rows),
    'tipos_preliminares': dict(collections.Counter(r['tipo_preliminar'] for r in rows)),
    'temas_candidatos_solapados': dict(collections.Counter(t for r in candidates for t in r['temas_preliminares'])),
    'fecha_minima': min(r['fecha'] for r in rows if r['fecha']),
    'fecha_maxima': max(r['fecha'] for r in rows if r['fecha']),
}
metadata = {'archivo_origen': str(source), 'sha256_origen': hashlib.sha256(raw).hexdigest(),
            'metadatos_originales': {k:v for k,v in data.items() if k != 'messages'},
            'metodo': 'Recuperación de texto tras fecha visible española y selección amplia por interrogaciones/indicadores de duda. Clasificación heurística, no revisión semántica exhaustiva. Un mensaje puede contener varias dudas; las citas internas pueden generar falsos positivos. Se conservan todos los mensajes para revisar omisiones.',
            'respuestas_validadas': False, 'estadisticas': stats}
for name, payload in [('mensajes_procesados.json', {**metadata, 'mensajes': rows}), ('dudas_candidatas.json', {**metadata, 'dudas': candidates})]:
    (out / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
(out / 'revision.txt').write_text('\n\n'.join(f"[{r['indice']}] {r['tipo_preliminar']}\n{r['texto']}" for r in rows), encoding='utf-8')
print(json.dumps(stats,ensure_ascii=True,indent=2))
