"""Rutas de trabajo fuera de la bóveda; no modifica las referencias archivadas.

LORCANA_TRABAJO permite elegir otra ubicación. Las rutas antiguas se traducen
solo para los cuatro árboles trasladados, sin enlaces dentro de la bóveda.
"""
from pathlib import Path
import os


REPO = Path(__file__).resolve().parents[1]
TRASLADOS = {
    "analisis/profesora-lorcana": "analisis/profesora-lorcana",
    "analisis/duels-2026-10-15": "analisis/duels-2026-10-15",
    "analisis/ancestral-guitar": "analisis/ancestral-guitar",
    "herramientas/duels/local": "adquisiciones/duels",
}


def carpeta_trabajo():
    configured = os.environ.get("LORCANA_TRABAJO")
    root = Path(configured).expanduser() if configured else REPO.parent / "lorcana-trabajo"
    if not root.is_absolute():
        raise ValueError("LORCANA_TRABAJO debe ser una ruta absoluta")
    root = root.resolve()
    if root == REPO or root.is_relative_to(REPO):
        raise ValueError("La carpeta de trabajo debe quedar fuera de la bóveda")
    return root


def ruta_trabajo(relative):
    """Destino nuevo, relativo a la carpeta externa (también para escrituras)."""
    root = carpeta_trabajo()
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError("Ruta fuera de la carpeta de trabajo")
    return path


def resolver_ruta(value):
    """Traduce referencias antiguas sin alterar sus bytes ni sus hashes.

    También admite rutas relativas al repositorio, independientemente del cwd.
    Las demás rutas se devuelven tal cual. No se recurre a copias antiguas si el
    destino externo falta: la comprobación de integridad debe fallar de forma
    visible en lugar de utilizar otra fuente.
    """
    path = Path(value)
    candidate = path if path.is_absolute() else REPO / path
    candidate = candidate.resolve()
    for before, after in TRASLADOS.items():
        old = REPO / before
        if candidate.is_relative_to(old):
            return ruta_trabajo(after) / candidate.relative_to(old)
    return path
