"""Diagnóstico reproducible y de solo lectura del corpus y recuperación."""
import sys
sys.dont_write_bytecode = True
import json
from contextlib import closing
import core as x

db = x.HERE / ".cache/indice.sqlite"
with closing(x.ro_connection(db)) as c:
    state = x.freshness(x.ROOT, db)
    print({k: v for k, v in state.items() if k != "selection"})
    for row in c.execute("select path,meta from sources where kind='cr'"):
        print(row["path"], json.loads(row["meta"]).get("extraction"))
    print("Cobertura", [tuple(r) for r in c.execute("select kind,count(*) from chunks group by kind")])
    print("Sets", [(r["path"],json.loads(r["meta"])["coverage"]) for r in c.execute("select * from sources where kind='card'")])
for q in ["¿Si robo tres cartas, ocurren tres robos?", "Belle - Exceptional Writer canta una canción",
          "Wasabi - Called into Battle y another chosen character", "Minnie Mouse - Practical Traveler y lore olvidado",
          "Coconut cuantas cartas debe tener un mazo", "reemplazos instead", "mover daño Resist"]:
    r = x.query(x.ROOT, db, q)
    print(q, {"ms": r["elapsed_ms"], "status": r["status"],
              "cards": [(z["requested"], z["status"]) for z in r["card_resolution"]],
              "rules": [p["rule"] for p in r["primary_rules"]], "policy": [p["pages"] for p in r["official_policy"]],
              "case": [p["title"] for p in r["case"]], "special": [p["title"] for p in r["special_format"]]})
