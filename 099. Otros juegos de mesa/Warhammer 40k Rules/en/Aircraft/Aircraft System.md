---
lang: en
type: system
category: aircraft
canonical: true
source: core-rules
surface: system
owner-domain: aircraft
tags:
  - warhammer40k
  - aircraft
  - system
aliases: []
related:
  - Pre-battle and Deployment System
  - Strategic Reserves System
  - Movement System
  - Transport System
---

# Aircraft System

## Overview

Aircraft System is the primary entry point for the Aircraft domain. It maps the aircraft article and its deployment placeholder dependency, and it routes readers toward the pre-battle, reserves, and movement systems that constrain how aircraft enter and move through the battle.

## Scope

This domain covers the narrow aircraft-specific rules surface and its planned deployment dependency, without expanding beyond the source-backed support currently available.

It helps answer questions about where aircraft-specific coverage belongs and when a reader should move into pre-battle, reserves, movement, or transport systems for adjacent mechanics.

## Domain Ownership

- Owner domain: Aircraft.
- Publication role: organise the narrow aircraft-specific rules surface and its setup dependency chain.
- Domain system role: provide the authoritative entry point and navigation surface for planned aircraft-domain content.

## Domain Boundaries

Aircraft owns:

- the planned aircraft concept Aircraft.
- the planned placeholder procedure Aircraft Deployment.

Aircraft does not own:

- [[Pre-battle and Deployment System]] ownership of the broader before-battle sequence around aircraft setup.
- [[Strategic Reserves System]] ownership of reserve placement and reserve arrival state.
- [[Movement System]] ownership of generic movement procedures and movement-phase branching.
- [[Transport System]] ownership of embarked occupancy and transport handling.

## Published Articles

- [[Aircraft]]
- [[Aircraft Deployment]]
- [[Aircraft Movement]]
- [[Aircraft Shooting]]
- [[Aircraft Charging and Fighting]]

## Planned Articles

- None.

## Related Systems

- [[Pre-battle and Deployment System]] provides the before-battle setup context that aircraft deployment depends on.
- [[Strategic Reserves System]] provides the adjacent reserve-state and arrival context used by aircraft.
- [[Movement System]] provides the generic movement framework that aircraft-specific rules modify or constrain.
- [[Transport System]] remains a separate vehicle-positioning domain that can intersect with aircraft handling without becoming part of Aircraft ownership.

## Navigation

- Start here when the question is specifically about aircraft as a system rather than generic reserve entry or movement.
- Move to [[Pre-battle and Deployment System]] when the issue is primarily about before-battle declarations and setup order.
- Move to [[Strategic Reserves System]] when the lookup is about arriving from reserves.
- Move to [[Movement System]] when the question is about how aircraft movement overrides or restricts general movement.

## See Also

- [[Pre-battle and Deployment System]]
- [[Strategic Reserves System]]
- [[Movement System]]
- [[Transport System]]

## References

- Warhammer 40,000 Core Rules extraction: Aircraft 23.02.
- Warhammer 40,000 Core Rules extraction: Aircraft Deployment 23.01.
- Warhammer 40,000 Core Rules extraction: Transports 18.00.