# Analista, revisora y profesora de Lorcana

Auxiliares locales para conservar posiciones, planes, elecciones y revisiones
trazables. El método está en las skills y en el
[contrato de integración](../../../lorcana-trabajo/analisis/profesora-lorcana/INTEGRACION-AGENTES.md).
Las comprobaciones de identidad, orden y presupuesto declarado requieren además
revisión del contenido estratégico y de sus fuentes.

## Flujo de una posición nueva

1. Infraestructura/coordinación entrega una `lorcana-position-v1` con estado previo,
   perspectiva y composición histórica; conserva fuera de las evaluadoras el mapa
   original y la elección. Reutiliza el proyector de `herramientas/duels_analisis/`.
2. Analista y revisora guardan sus planes por separado para la misma posición.
   Las skills son `lorcana-analista-jugadas` y `lorcana-revisora-jugadas`.
3. Coordinación verifica ambos registros y sella sus referencias antes de exportar
   la elección limitada. `coordinar_piloto.release` implementa esta frontera para
   el formato de mapa del piloto. Un intento fallido se conserva y necesita otro
   destino para una entrega posterior válida.
4. Analista guarda elección y diagnóstico. Revisora recibe ese diagnóstico exacto
   y entrega su revisión, preservando diferencias y condiciones.
5. `profesora-lorcana` recibe los cinco originales: posición, elección, diagnóstico,
   plan revisor y revisión. Si hay sucesores, recibe también sus antecesores.
   `profesora.seguimiento.check_files` comprueba referencias/identidad; la profesora
   conserva categoría, certeza, desacuerdos y límites al enseñar.

Las entradas de activación están en `.agents/skills/` y las instrucciones mantenidas
en `.github/skills/`. No crear otras agentes o chats desde estas skills. El registro
documenta orden de artefactos y exposición declarada, sin imponer permisos entre
chats ni demostrar su conocimiento interno.

## Código y comprobaciones

- `contratos.py`: JSON estricto, SHA-256 canónico y referencias `{schema, sha256}`;
  los recibos de bytes se conservan por separado.
- `analista/registro.py`: registro de etapas y presupuesto declarado por línea.
- `revisora/registro.py`: línea previa, revelación, revisión y sucesores enlazados.
- `profesora/seguimiento.py`: pares verificados, denominadores de práctica y
  propagación de correcciones a conclusiones derivadas.
- `preparar_piloto.py`: prepara la muestra histórica concreta de esta fase. Su
  selección y dependencias están fijadas en el código; las partidas futuras
  requieren otra entrega explícita de posiciones.
- `coordinar_piloto.py`: sellado dual y proyecciones limitadas de elecciones.
  La selección iniciada pendiente de Guardaespaldas se distingue de resolución.

Una cadena titular se comprueba desde la raíz del repositorio con:

```powershell
python -B -m herramientas.profesora_lorcana.analista.registro verify --session RUTA_PRIVADA_DE_SESION
```

Pruebas de los auxiliares, desde la raíz:

```powershell
python -B -m unittest herramientas.profesora_lorcana.test_contratos herramientas.profesora_lorcana.test_coordinar_piloto herramientas.profesora_lorcana.analista.test_registro herramientas.profesora_lorcana.profesora.test_seguimiento -q
python -B -m unittest discover -s herramientas/profesora_lorcana/revisora -q
```

## Privacidad, correcciones y alcance

Las posiciones, partidas, memorias y ejemplos personales se guardan en
`../lorcana-trabajo/analisis/profesora-lorcana/desarrollo/`, excluido de Git. El cliente de Duels
mantiene sus credenciales en `.env` ignorado. Estos auxiliares operan sobre archivos
locales; la adquisición corresponde al cliente existente de `herramientas/duels/`.

Un juicio `corregir` suspende su explicación afectada hasta diagnóstico sucesor
y nueva revisión. Se preservan originales, `revision_of` y derivados sustituidos.
Una discrepancia se enseña como tal; una valoración indeterminada conserva lo que
falta. No convertir ausencia de respuesta en fallo ni ejemplos en práctica medida.

El estado de aceptación, pruebas ejecutadas y límites del piloto están en
[COORDINACION.md](../../../lorcana-trabajo/analisis/profesora-lorcana/COORDINACION.md). El seguimiento
de desarrollo tiene su propio cierre: estas herramientas no programan por sí
solas revisiones de partidas futuras. Las dudas normativas siguen la capa `.github/`.
