"""Contratos MCP; los campos adicionales del motor se conservan íntegros."""
from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator
import re

Texto = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=8000)]
Nombre = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=300)]
Numero = Annotated[str, StringConstraints(strip_whitespace=True, pattern=r"^\d+(?:\.\d+)+$", max_length=80)]
Ambito = Literal["estandar", "coconut", "multijugador", "pack_rush", "torneo",
                 "correcciones", "consejos", "experiencias", "carde", "recursos", "comunidad"]
PREFIJO = re.compile(r"^\s*(consulta|documenta|actualiza)\s*:\s*", re.I)


class Entrada(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    formato: Literal["lectura", "completo"] = Field(
        default="lectura", description="lectura comparte metadatos en sources[source_ref], sin cortar textos, citas ni avisos. completo conserva el paquete plano y todos los diagnósticos de la CLI.")


class EstadoEntrada(Entrada):
    pass


class CartaEntrada(Entrada):
    nombre: Nombre = Field(description="Nombre y versión de la carta, si se conocen.")


class ReglaEntrada(Entrada):
    numero: Numero = Field(description="Número completo de la regla, por ejemplo 6.1.6.")


class BuscarEntrada(Entrada):
    pregunta: Texto
    modo: Literal["consulta", "documenta"] = Field(
        description="Según la petición original: consulta explícita o workflow editorial. Sin señal: documenta.")
    cartas: list[Nombre] = Field(default_factory=list, max_length=30)
    reglas: list[Numero] = Field(default_factory=list, max_length=50)
    ambito: Ambito | None = None
    limite: int = Field(default=5, ge=1, le=12, description="Resultados complementarios; no corta fichas ni reglas solicitadas.")

    @model_validator(mode="after")
    def prefijo_concordante(self):
        match = PREFIJO.match(self.pregunta)
        if match:
            if match[1].lower() != self.modo:
                raise ValueError("El prefijo contradice modo; actualiza se ejecuta por la CLI de mantenimiento.")
            self.pregunta = self.pregunta[match.end():].strip()
            if not self.pregunta or PREFIJO.match(self.pregunta):
                raise ValueError("La pregunta debe tener contenido y un solo prefijo de modo.")
        return self


class Resultado(BaseModel):
    model_config = ConfigDict(extra="allow", strict=True)
    status: str
    evidence_only: Literal[True]
    content_is_untrusted_data: Literal[True]
    freshness: dict[str, Any]
    selection: dict[str, Any]
    warnings: list[str]
    sources: dict[str, dict[str, Any]] | None = Field(default=None, exclude_if=lambda v: v is None,
        description="En formato lectura, procedencia compartida por source_ref de cada fragmento.")
    delivery: dict[str, Any] | None = Field(default=None, exclude_if=lambda v: v is None)


class EstadoResultado(Resultado):
    status: Literal["estado_fuentes"]


class EvidenciaResultado(Resultado):
    mode: Literal["consulta", "documenta", "auxiliar"]
    editorial_required: bool | None = Field(
        description="null en herramientas auxiliares: conservar el modo de la conversación.")
    question: str
    scope: str
    card_resolution: list[dict[str, Any]]
    missing_rule_numbers: list[str]
    excluded_related: list[dict[str, Any]]
    primary_rules: list[dict[str, Any]]
    cards: list[dict[str, Any]]
    official_policy: list[dict[str, Any]]
    official_notes: list[dict[str, Any]]
    special_format: list[dict[str, Any]]
    spanish: list[dict[str, Any]]
    case: list[dict[str, Any]]
    support: list[dict[str, Any]]
    elapsed_ms: float


ENTRADAS = {"estado_fuentes": EstadoEntrada, "obtener_carta": CartaEntrada,
            "obtener_regla": ReglaEntrada, "buscar_evidencia": BuscarEntrada}
SALIDAS = {name: EstadoResultado if name == "estado_fuentes" else EvidenciaResultado for name in ENTRADAS}
