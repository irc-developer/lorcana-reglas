import json
import sys

try:
    # Leer el archivo JSON
    print("Leyendo archivo JSON...")
    with open('cartaslorcanajson.json', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Tamaño del archivo original: {len(content)} caracteres")
    
    # Limpiar el contenido: eliminar caracteres extra al final
    content = content.strip()
    # Si el último carácter no es ']', buscar el último ']' y cortar ahí
    if content[-1] != ']':
        print(f"Detectado carácter extra al final: '{content[-1]}'")
        last_bracket = content.rfind(']')
        if last_bracket != -1:
            content = content[:last_bracket + 1]
            print(f"Contenido limpiado hasta el último ']'")
    
    print(f"Tamaño después de limpiar: {len(content)} caracteres")
    
    # Intentar parsear el JSON
    print("\nParseando JSON...")
    cartas = json.loads(content)
    
    print(f"Total de cartas en el archivo: {len(cartas)}")
    
    # Campos a extraer
    campos_deseados = ['Name', 'Cost', 'Type', 'Color', 'Inkable', 'Body_Text', 'Rarity', 'Set_Name', 'Set_ID', 'Set_Num']
    
    # Extraer solo los campos deseados
    cartas_filtradas = []
    for i, carta in enumerate(cartas):
        if i < 3:  # Mostrar las primeras 3 para verificar
            print(f"Carta {i+1}: {carta.get('Name', 'Sin nombre')}")
        carta_filtrada = {}
        for campo in campos_deseados:
            carta_filtrada[campo] = carta.get(campo, None)
        cartas_filtradas.append(carta_filtrada)
    
    # Guardar el resultado en un nuevo archivo
    print(f"\nGuardando {len(cartas_filtradas)} cartas en cartas_filtradas.json...")
    with open('cartas_filtradas.json', 'w', encoding='utf-8') as f:
        json.dump(cartas_filtradas, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Archivo creado exitosamente!")
    print(f"✓ Total de cartas procesadas: {len(cartas_filtradas)}")

except json.JSONDecodeError as e:
    print(f"\nError al decodificar JSON: {e}")
    print(f"Posición del error: {e.pos}")
    if e.pos > 0:
        start = max(0, e.pos - 50)
        end = min(len(content), e.pos + 50)
        print(f"Contexto del error: {content[start:end]}")
    sys.exit(1)
except Exception as e:
    print(f"\nError: {e}")
    sys.exit(1)
