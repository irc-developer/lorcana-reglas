---
lang: en
type: system
category: charge
canonical: true
source: core-rules
surface: system
owner-domain: charge
tags:
  - warhammer40k
  - charge
  - system
aliases: []
related:
  - Battle Sequence System
  - Movement System
  - Terrain Visibility System
  - Fight System
---

# Charge System

## Overview

Charge System is the authoritative System Article for the Charge domain. It maps the declaration, roll, target selection, and move procedure that transition a unit from generic battlefield positioning into melee engagement opportunities.

## Scope

This domain covers the rules questions that arise once a unit commits to charging: what a charge is, how charge targets are declared, how the charge roll gates the outcome, and how a successful charge becomes a charge move.

Readers should expect one canonical concept article, one charge-owned movement procedure, and glossary support for target declaration.

This domain sits between [[Movement System]] and [[Fight System]]. It consumes generic movement context and passes downstream engagement opportunities into melee resolution without absorbing either neighbouring domain.

## Domain Ownership

- Owner domain: Charge.
- Domain role: publish and maintain the canonical surfaces for charge declaration, charge-roll outcome, charge targets, and the charge-owned move procedure.
- Publication role: provide the authoritative navigation hub for the transition from positioning into melee engagement.

## Domain Boundaries

- Charge owns declaration, charge targets, charge-roll handling, failed-charge handling, and [[Charge Move]] as the phase-specific movement procedure inseparable from charging.
- Charge owns the transition into melee engagement, but it does not own the engagement concept itself.
- Charge does not own generic movement procedures such as normal, advance, or fall-back movement; those remain in [[Movement System]].
- Charge does not own fight eligibility, fight order, pile-in move, consolidation move, or melee resolution; those remain in [[Fight System]].
- Charge does not own hit rolls, wound rolls, save rolls, inflict damage, or weapon data; those remain in [[Attack System]].
- Charge can create downstream state such as [[Fights First]], but the state itself remains owned by the Fight domain.

## Published Articles

- [[Charge]]
- [[Charge Move]]
- [[Charge target]]

## Planned Articles

None.

## Related Systems

- [[Battle Sequence System]] provides the wider timing spine, while [[Charge Phase]] is the canonical phase article that contains charge resolution.
- [[Movement System]] provides the generic movement framework that Charge reuses without owning normal, advance, or fall-back movement.
- [[Fight System]] consumes the engagement opportunities and charge-derived state created here, but it does not own declaration or charge movement.
- [[Attack System]] remains downstream of this domain because charging sets up later melee attacks without resolving them.

## Navigation

- Start with [[Charge]] for the core procedure that covers declaration, charge rolls, and failed-charge outcomes.
- Continue to [[Charge Move]] when the question is about the successful movement procedure and its end-position requirements.
- Read [[Charge target]] when the issue is which enemy units constrain the declaration and the finished move.
- Move to [[Charge Phase]] when the real issue is whether the timing window for charging is open.
- Move to [[Battle Sequence System]] when the real issue is the wider timing spine rather than the Charge phase specifically.
- Move to [[Movement System]] when the real issue is generic movement rather than charge-specific movement.
- Move to [[Fight System]] when the question has moved from entering melee into resolving it.
- Move to [[Attack System]] when the question is about the later melee attack pipeline rather than the charge transition.

## See Also

- [[Charge Phase]]
- [[Battle Sequence System]]
- [[Movement System]]
- [[Fight System]]
- [[Attack System]]

## References

- Warhammer 40,000 Core Rules extraction: Charge Phase 11.00.
- Warhammer 40,000 Core Rules extraction: Charge.
- Warhammer 40,000 Core Rules extraction: Charge Move 11.04.
- Warhammer 40,000 Core Rules extraction: Charge target.