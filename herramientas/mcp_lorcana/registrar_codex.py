"""Preparar/registrar configuración del proyecto y sincronizar la skill revisada."""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
from pathlib import Path
import re
import tomllib

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ORIGINAL_SKILL_SHA = "cbf84eaa95f692bd6bf4a57dda840fcdedd40b2441ab923df44b708f8daf394a"
PREVIOUS_MCP_SKILL_SHA = "a9d0d12a89ae2d5f1bc382546a2d145f2badbb62ff834946846ed208077e33d0"


def preparar():
    config = ROOT / ".codex/config.toml"
    python = HERE / (".venv/Scripts/python.exe" if sys.platform == "win32" else ".venv/bin/python")
    if not python.is_file():
        raise ValueError("Instala antes el entorno .venv según README.md")
    names = ["estado_fuentes", "obtener_carta", "obtener_regla", "buscar_evidencia"]
    settings = {"command": python.as_posix(), "args": ["-B", "-X", "utf8", (HERE / "servidor.py").as_posix(), "--root", ROOT.as_posix()],
                "cwd": ROOT.as_posix(), "enabled": True, "startup_timeout_sec": 20, "tool_timeout_sec": 120,
                "enabled_tools": names, "env": {"PYTHONDONTWRITEBYTECODE": "1", "PYTHONUTF8": "1"}}
    # Preservar literalmente el resto de la configuración; no alterar el perfil global.
    prior = config.read_text(encoding="utf-8-sig") if config.exists() else ""
    parsed = tomllib.loads(prior)
    existing = parsed.get("mcp_servers", {}).get("lorcana")
    previous_generation = dict(settings, tools={name: {"output_token_limit": 100000} for name in names})
    if existing is not None and existing not in (settings, previous_generation):
        raise ValueError("Ya existe una configuración distinta de lorcana; revisar sin sobrescribirla.")
    if parsed.get("tool_output_token_limit", 100000) != 100000:
        raise ValueError("El proyecto ya tiene otro presupuesto de salida; revisar antes de cambiarlo.")
    block = "# MCP local de evidencia; rutas de este PC. Generado por registrar_codex.py.\n[mcp_servers.lorcana]\n"
    for k, v in settings.items():
        if isinstance(v, dict):
            continue
        block += f"{k} = {json.dumps(v, ensure_ascii=False)}\n"
    block += '\n[mcp_servers.lorcana.env]\nPYTHONDONTWRITEBYTECODE = "1"\nPYTHONUTF8 = "1"\n'
    if existing == previous_generation:
        # Migrar únicamente el bloque generado aquí; 0.147.0 rechaza el ajuste por herramienta.
        prior = re.sub(r"(?ms)^\[mcp_servers\.lorcana(?:\.[^\]]+)?\]\r?\n.*?(?=^\[|\Z)", "", prior)
    target_text = prior if existing == settings else prior.rstrip() + ("\n\n" if prior else "") + block
    if "tool_output_token_limit" not in parsed:
        target_text = "# Presupuesto de salida compatible con Codex 0.147.0; aplica a herramientas de este proyecto.\ntool_output_token_limit = 100000\n\n" + target_text
    assert tomllib.loads(target_text)["mcp_servers"]["lorcana"] == settings
    source = ROOT / "herramientas/consulta_lorcana/skill/SKILL.md"
    active = ROOT / ".agents/skills/lorcana-consulta-rapida/SKILL.md"
    desired = source.read_bytes()
    if active.exists():
        digest = hashlib.sha256(active.read_bytes()).hexdigest()
        if digest not in (ORIGINAL_SKILL_SHA, PREVIOUS_MCP_SKILL_SHA, hashlib.sha256(desired).hexdigest()):
            raise ValueError("La skill activa tiene otros cambios; integrar antes de sincronizar.")
    return config, target_text, active, desired


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--aplicar", action="store_true", help="Escribe solo configuración de proyecto y skill activa.")
    args = parser.parse_args()
    config, content, active, skill = preparar()
    if args.aplicar:
        config.parent.mkdir(parents=True, exist_ok=True)
        if not config.exists() or config.read_text(encoding="utf-8-sig") != content:
            config.write_text(content, encoding="utf-8")
        active.parent.mkdir(parents=True, exist_ok=True)
        if not active.exists() or active.read_bytes() != skill:
            active.write_bytes(skill)
        print("Registrado MCP del proyecto; skill activa sincronizada. Configuración global conservada.")
    else:
        print(content)
        print("Skill a sincronizar:", active)
        print("SHA-256 revisado:", hashlib.sha256(skill).hexdigest())
