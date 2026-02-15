import json
import re

# Leer y limpiar el JSON original
print("Leyendo archivo JSON...")
with open('cartaslorcanajson.json', 'r', encoding='utf-8') as f:
    content = f.read().strip()
    if content[-1] != ']':
        content = content[:content.rfind(']') + 1]

cartas = json.loads(content)
print(f"Total de cartas: {len(cartas)}")

# Ordenar por Set_Num y luego por Card_Num
cartas_ordenadas = sorted(cartas, key=lambda x: (x.get('Set_Num', 0), x.get('Card_Num', 0)))

# Lista de keywords conocidas
keywords = [
    'Alert', 'Bodyguard', 'Boost', 'Challenger', 'Evasive', 'Reckless', 
    'Resist', 'Rush', 'Shift', 'Singer', 'Sing Together', 'Support', 
    'Vanish', 'Ward'
]

def procesar_body_text(body_text):
    """Divide el body_text en keywords y habilidades"""
    if not body_text:
        return [], []
    
    # Dividir por líneas dobles
    partes = body_text.split('\n\n')
    
    keywords_encontradas = []
    habilidades = []
    
    for parte in partes:
        parte_limpia = parte.strip()
        if not parte_limpia:
            continue
            
        # Buscar si es una keyword (con o sin texto recordatorio)
        es_keyword = False
        for kw in keywords:
            # Patrón: Keyword o Keyword +N (con texto recordatorio opcional)
            pattern = rf'^{kw}(\s+\+?\d+)?\s*(\(.*?\))?$'
            if re.match(pattern, parte_limpia, re.IGNORECASE | re.DOTALL):
                # Extraer solo la keyword sin el texto recordatorio
                match = re.match(rf'^({kw}(?:\s+\+?\d+)?)', parte_limpia, re.IGNORECASE)
                if match:
                    keywords_encontradas.append(match.group(1))
                    es_keyword = True
                    break
        
        if not es_keyword:
            habilidades.append(parte_limpia)
    
    return keywords_encontradas, habilidades

# Generar Markdown
output = []
output.append("# Cartas de Lorcana\n")

set_actual = None

for carta in cartas_ordenadas:
    # Encabezado de set si cambia
    if carta.get('Set_Name') != set_actual:
        set_actual = carta.get('Set_Name')
        set_id = carta.get('Set_ID', '')
        set_num = carta.get('Set_Num', '')
        output.append(f"\n# Set {set_num}: {set_actual} ({set_id})\n")
    
    # Nombre
    nombre = carta.get('Name', 'Sin nombre')
    output.append(f"## {nombre}\n")
    
    # Primera línea: Coste, Tipo, Color, Tinta, Rareza
    coste = carta.get('Cost', '?')
    tipo = carta.get('Type', '?')
    color = carta.get('Color', '?')
    inkable = '✓' if carta.get('Inkable') else '✗'
    rareza = carta.get('Rarity', '?')
    
    output.append(f"**Coste:** {coste} | **Tipo:** {tipo} | **Color:** {color} | **Tinta:** {inkable} | **Rareza:** {rareza}  ")
    
    # Segunda línea: Stats (si es personaje)
    stats_line = []
    if carta.get('Strength') is not None:
        stats_line.append(f"**Fuerza:** {carta['Strength']}")
    if carta.get('Willpower') is not None:
        stats_line.append(f"**Voluntad:** {carta['Willpower']}")
    if carta.get('Lore') is not None:
        stats_line.append(f"**Lore:** {carta['Lore']}")
    
    if stats_line:
        output.append(" | ".join(stats_line) + "  ")
    
    # Tercera línea: Set e Imagen
    imagen = carta.get('Image', '')
    if imagen:
        output.append(f"**Set:** {set_actual} ({set_id} #{set_num}) | [🖼️ Imagen]({imagen})\n")
    else:
        output.append(f"**Set:** {set_actual} ({set_id} #{set_num})\n")
    
    # Habilidades
    body_text = carta.get('Body_Text', '')
    if body_text:
        keywords_lista, habilidades_lista = procesar_body_text(body_text)
        
        output.append("\n**Habilidades:**")
        
        # Primero las keywords
        for kw in keywords_lista:
            output.append(f"- {kw}")
        
        # Luego las habilidades con nombre
        for hab in habilidades_lista:
            output.append(f"- {hab}")
        
        output.append("")
    
    output.append("---\n")

# Guardar archivo
with open('todas_las_cartas.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print(f"✓ Archivo generado: todas_las_cartas.md")
print(f"✓ Total de cartas procesadas: {len(cartas_ordenadas)}")
