import json
from collections import defaultdict

with open('cartas_filtradas.json', 'r', encoding='utf-8') as f:
    cartas = json.load(f)

sets_info = defaultdict(lambda: {'count': 0, 'id': '', 'num': 0})

for carta in cartas:
    set_name = carta['Set_Name']
    sets_info[set_name]['count'] += 1
    sets_info[set_name]['id'] = carta['Set_ID']
    sets_info[set_name]['num'] = carta['Set_Num']

print('Sets incluidos:')
print('=' * 60)

for set_name in sorted(sets_info.keys(), key=lambda x: sets_info[x]['num']):
    info = sets_info[set_name]
    print(f"Set {info['num']:2}: {set_name:30} ({info['id']:3}) - {info['count']:3} cartas")

print('=' * 60)
print(f"TOTAL: {len(cartas)} cartas de {len(sets_info)} sets")
