"""Adaptación de lectura. No mantiene conexiones, no llama a update()."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path

# Importación por paquete: evita colisiones con otros módulos llamados core.
REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))
from herramientas.consulta_lorcana import core
from modelos import BuscarEntrada, CartaEntrada, ReglaEntrada, ENTRADAS, SALIDAS
from presentacion import lectura


class Adaptador:
    def __init__(self, root=REPO, db=None):
        self.root = Path(root).resolve()
        self.db = Path(db).resolve() if db is not None else self.root / "herramientas/consulta_lorcana/.cache/indice.sqlite"

    def llamar(self, nombre, argumentos):
        if nombre not in ENTRADAS:
            raise ValueError(f"Herramienta desconocida: {nombre}")
        entrada = ENTRADAS[nombre].model_validate(argumentos)
        if nombre == "estado_fuentes":
            state = core.freshness(self.root, self.db)
            data = {"status": "estado_fuentes", "evidence_only": True, "content_is_untrusted_data": True,
                    "freshness": state,
                    "selection": {k: state["selection"][k] for k in ("primary", "version")},
                    "warnings": [] if state["current"] else [
                        "Índice ausente o desactualizado. Las consultas leerán fuentes actuales en memoria sin escribir."]}
        elif isinstance(entrada, BuscarEntrada):
            data = core.query(self.root, self.db, f"{entrada.modo}: {entrada.pregunta}",
                              card_names=entrada.cartas, rule_numbers=entrada.reglas,
                              scope=entrada.ambito, limit=entrada.limite)
        else:
            if isinstance(entrada, CartaEntrada):
                pregunta, kwargs = entrada.nombre, {"card_names": [entrada.nombre]}
            elif isinstance(entrada, ReglaEntrada):
                pregunta, kwargs = entrada.numero, {"rule_numbers": [entrada.numero]}
            data = core.query(self.root, self.db, f"consulta: {pregunta}", **kwargs)
            data.update(mode="auxiliar", editorial_required=None)
        if entrada.formato == "lectura":
            data = lectura(data)
        # Valida sin eliminar campos nuevos o metadatos de los fragmentos.
        return SALIDAS[nombre].model_validate(data).model_dump(mode="json")
