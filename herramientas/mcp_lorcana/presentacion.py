"""Vista de lectura: textos íntegros y metadatos de fuente compartidos.

No decide relevancia ni resume evidencia. La vista completa sigue disponible.
"""
from copy import deepcopy
import json

GROUPS = ("primary_rules", "cards", "official_policy", "official_notes",
          "special_format", "spanish", "case", "support")
SOURCE_FIELDS = frozenset((
    "source_id", "path", "absolute_path", "kind", "scope", "authority",
    "source_hash", "version", "effective_date", "source_limitations",
    "documented_urls", "maintenance_observation", "official_url",
    "official_url_verified_on", "raw_text_preserved_in_index",
))


def lectura(data):
    """Compartir procedencia sin perder campos de los fragmentos ni sus textos."""
    result = deepcopy(data)
    sources, identities = {}, {}
    for group in GROUPS:
        for packet in result.get(group, []):
            metadata = {k: packet[k] for k in packet if k in SOURCE_FIELDS}
            identity = json.dumps(metadata, ensure_ascii=False, sort_keys=True)
            if identity not in identities:
                ref = f"S{len(sources) + 1}"
                identities[identity] = ref
                sources[ref] = metadata
            for k in metadata:
                del packet[k]
            packet["source_ref"] = identities[identity]
    # La lista global de exclusiones es diagnóstico del corpus. Las exclusiones
    # relacionadas con la pregunta, cambios y advertencias permanecen completas.
    selection = result["freshness"].get("selection", {})
    excluded = selection.pop("excluded", None)
    if excluded is not None:
        selection["excluded_count"] = len(excluded)
    result["sources"] = sources
    result["delivery"] = {"format": "lectura", "complete_texts": True,
                          "source_metadata": "sources[source_ref]",
                          "full_diagnostics": "Repetir con formato=completo solo si se necesitan."}
    return result


def expandir_fuentes(data):
    """Reconstruir cada fragmento; útil para clientes que requieren campos planos."""
    result = deepcopy(data)
    for group in GROUPS:
        for packet in result.get(group, []):
            ref = packet.pop("source_ref", None)
            if ref is not None:
                packet.update(result["sources"][ref])
    return result
