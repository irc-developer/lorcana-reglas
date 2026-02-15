import json

# Leer el JSON limpiando el carácter extra
with open('cartaslorcanajson.json', 'r', encoding='utf-8') as f:
    content = f.read().strip()
    if content[-1] != ']':
        content = content[:content.rfind(']') + 1]

cartas = json.loads(content)

# Buscar Lythos - Rock Titan
carta = [c for c in cartas if c.get('Name') == 'Lythos - Rock Titan'][0]

# Extraer los campos necesarios
campos = ['Name', 'Cost', 'Type', 'Color', 'Inkable', 'Body_Text', 'Rarity', 
          'Set_Name', 'Set_ID', 'Set_Num', 'Strength', 'Willpower', 'Lore', 'Image']

resultado = {k: carta.get(k) for k in campos}
print(json.dumps(resultado, indent=2, ensure_ascii=False))
