---
name: lorcana-card-verification
description: "Usar cuando un ruling, caso o explicación dependa del texto exacto de una carta concreta. Obliga a verificar nombre y texto exacto solo en la sección 02. Listado de Cartas, usando el archivo del set correspondiente, antes de razonar."
---

# Verificación exacta de cartas

- No cierres un ruling sobre una carta específica sin verificar antes su texto exacto en la sección `02. Listado de Cartas`, usando el archivo del set correspondiente.
- Confirma el nombre exacto y la versión correcta de la carta antes de razonar.
- Enlaza al lector la imagen de esa misma carta en Lorcast, usando la URL devuelta por su API o el mapa verificado `.github/planes/mapa-cartas-lorcast.json`. La ficha local sigue siendo evidencia de trabajo; no generes enlaces públicos al epígrafe del set.
- Lee el texto completo disponible y detecta palabras críticas como `instead`, `prevent`, `when`, `whenever`, `would take` o `would be dealt`.
- Basa la respuesta en ese texto exacto, no en una paráfrasis recordada.
- Si la carta o su texto no pueden verificarse dentro del alcance permitido, detente y pide al usuario el dato exacto o una ampliación explícita del alcance.
