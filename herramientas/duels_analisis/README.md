# Vistas previas de decisiones de Duels

Herramienta local, solo biblioteca estándar de Python. No usa credenciales, red, motor del juego ni publicación. El método y el piloto privados están en `../lorcana-trabajo/analisis/profesora-lorcana/analisis-rotor/` (excluido de Git).

```powershell
python -m unittest discover -s herramientas/duels_analisis -p 'test_*.py' -v
python herramientas/duels_analisis/vista_decision.py RUTA/partida-01 --before-seq 2 --out RUTA_PRIVADA/vista.json
python herramientas/duels_analisis/vista_decision.py RUTA/partida-02 --before-seq 2 --previous-prefix RUTA/partida-01 --out RUTA_PRIVADA/vista-p2.json
```

Para prefijo `p` requiere `p-acciones.json`, `p-eventos.json`, `p-estados.jsonl.gz` y `p-resumen.json`, con el contrato del extractor local validado por datos. No acepta directamente un replay API distinto sin adaptar y validar ese contrato. El registro de datos no se imprime como vista.

`build_view(prefix, n)` selecciona exclusivamente el snapshot n−1 y eventos con índice menor que `acciones[n−1].logsFromInclusive`. Rechaza secuencias discontinuas, fronteras inmediatas incoherentes, perspectiva contraria y decisiones posteriores a GAME_END/GAME_CONCEDED. Un conjunto explícito de campos limita cada objeto proyectado. No transmite la elección `actionType`, el estado posterior, orden de mazo, mano rival, resultados, marcador ni logs libres. La lista propia se copia por cantidades desde el resumen específico de esa partida, acreditado por el lote de datos.

`--previous-prefix` admite observaciones públicas de una partida anterior del mismo encuentro, sin resultados. No reconstruye una mano rival exacta; una revelación puede haber dejado de estar en mano. `player` en observaciones es **actor del evento**, no propietario de todas las cartas referenciadas; un desafío/retorno puede citar cartas de ambos jugadores. Rechaza memoria de partidas duplicadas o con cambio de asiento: adaptar roles antes de incorporar ese caso.

La selección de primer jugador solo se copia tras CHOOSE_STARTING_PLAYER previa; en su ausencia se deriva del primer TURN_START ya ocurrido. Antes se marca `firstPlayerNotProvenInPrefix`, aunque el resumen final lo diga. Esto evita usar una selección futura presente anticipadamente en el snapshot base.

La salida conserva hashes de entradas, frontera e identidad. Para un uso auditable verificar el lote entregado por datos y comparar esos hashes con sus recursos antes de aceptar conclusiones. Es una proyección de evidencia, **no un motor de reglas ni un certificado de completitud de UI**.

Los efectos/contadores se identifican como registros del motor; verificar textos y reglas antes de concluir legalidad o cálculos. No se proyecta la bolsa completa ni zonas privadas de mirar cartas. Prompts propios desconocidos o con campos nuevos activan `pendingPromptIncomplete`; no evaluar una elección afectada hasta completar el adaptador con pruebas. Las habilidades estáticas requieren corpus de cartas verificado.

Las pruebas incluyen valores señuelo en información oculta, cambios de futuro sin cambio de contenido de vista, frontera n−1 y exclusión de eventos actuales, prompts de otra perspectiva y contexto BO3 no anterior. No equivalen a validar el motor o todas las variantes de su formato.

Para evaluaciones nuevas abrir una única posición, registrar alternativas, después mostrar la elección y finalmente avanzar. Abrir posiciones posteriores puede revelar futuros de posiciones anteriores incluso cuando cada JSON por separado está correctamente filtrado. Declarar cualquier exposición ya ocurrida.

## Lotes históricos

```powershell
python -B herramientas/duels_analisis/historico.py RUTA_LOTE --out RUTA_PRIVADA/resumen.json
python -B herramientas/duels_analisis/reconstruir_lote.py RUTA_LOTE --out RUTA_PRIVADA
python -B herramientas/duels_analisis/preparar_vistas.py RUTA_PRIVADA/reconstruccion.json RUTA_LOTE --out RUTA_PRIVADA/vistas
```

Ejecutar primero el `verify` del contrato de datos. `historico.py` consume solo filas `safe`, conserva tamaño real de lista, separa partida/BO3 y colores/arquetipo. Los resultados son descriptivos; las huellas representan listas declaradas y deben acompañarse de conflictos API/replay encontrados después. La selección segura por objeto no verifica nombres históricos.

`reconstruir_lote.py` procesa secuencialmente archivos locales, verifica hashes y usa las operaciones del extractor existente de `herramientas/duels_analisis/extraer_replays.py`. Adapta la salida para BO1 sin `matchView` y listas de tamaño distinto de 60. No repara discrepancias de listas o fronteras no monótonas: las registra. No modifica lote/originales. El directorio de salida completo contiene información futura y debe permanecer privado. **No volver a ejecutar sobre una auditoría compartida que deba conservarse**; usar otra ruta para una nueva versión.

Desde v2 precomprueba el array completo de fronteras y distingue `decreasing_count` de `outside_array`, con seq/contadores/longitud. Los parches y validaciones finales escriben en staging temporal y solo promueven el directorio al éxito; una excepción no publica estados parciales. Rechaza destinos/auditorías existentes. El esquema nuevo es `duels-reconstruction-audit-v2`; no sustituye auditorías v1. Los timestamps pueden revelar incompatibilidades adicionales, pero no sustituyen fronteras ni autorizan ordenar eventos, recortar o aplicar offsets.

`preparar_vistas.py` genera un mulligan, primera tinta y primera tinta con etiqueta Duels ≥6 cuando existan, solo para reconstrucciones completas. Conserva ausencias y memoria BO3 incompleta. Nombra exclusivamente los IDs de la lista propia ya registrada con el mapa observado de `normalizacion.json` y guarda su hash; nunca exporta el mapa global ni nombres de cartas ajenas por esa vía. El mapa observado aporta identidad, no reglas. El proyector simple puede mostrar algún nombre de lista no localizado; el preparador de lote resuelve ese caso con la evidencia de datos.

Las pruebas están separadas en proyección, medidas históricas, reconstrucción y enriquecimiento de nombres propios. La preparación de una vista no equivale a su revisión estratégica. Mantener separados catálogo de vistas, selección intencional y elecciones reveladas.
