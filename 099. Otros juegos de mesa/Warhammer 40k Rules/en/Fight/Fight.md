---
lang: en
type: concept
category: fight
canonical: true
source: core-rules
surface: article
owner-domain: fight
tags:
  - warhammer40k
  - fight
  - concept
aliases: []
related:
  - Fight System
  - Normal Fight
  - Overrun Fight
  - Pile-in Move
  - Consolidation Move
  - Eligible to Fight, But Unable to Fight
  - Fights First
  - Making Attacks
  - Attack System
  - Charge System
  - Movement System
  - Weapon System
---

# Fight

## Summary

Fight is the core melee-combat concept that orders which eligible units are selected, resolves Fights First combats before remaining combats, and routes each selected unit into the correct fight mode.

## Definition

Players alternate selecting eligible units to fight, resolving Fights First combats before remaining combats.

## Rules

A unit is eligible to fight if it has not already been selected to fight and it is engaged, was engaged at the start of the step, or made a charge move this turn.

When a unit is selected, it resolves the fight mode that applies to its current state through [[Normal Fight]] or [[Overrun Fight]].

Once a selected unit reaches the point of making melee attacks, it uses the shared attack procedure from [[Making Attacks]].

If new Fights First units become eligible while remaining combats are being resolved, the sequencing returns to Fights First combats before continuing.

## Interactions

- [[Normal Fight]] is the baseline branch for eligible engaged units.
- [[Overrun Fight]] is the special branch that adds another pile-in move before attacks when its permission applies.
- [[Fights First]] changes selection order inside this domain without replacing the melee attack pipeline.
- [[Pile-in Move]] and [[Consolidation Move]] are the fight-owned positional procedures that bracket melee attacks.
- [[Making Attacks]] and [[Attack System]] remain the shared downstream attack-resolution surfaces for hit, wound, save, and damage processing.
- [[Charge System]], [[Movement System]], and [[Weapon System]] provide upstream engagement state, movement context, and weapon data without becoming owned by this domain.

## Restrictions

- This concept does not redefine hit rolls, wound rolls, save rolls, inflict damage, or any other shared attack step.
- This concept does not own charge declaration, charge movement, or generic movement procedures outside the fight sequence.
- Weapon characteristics and weapon-side abilities remain owned by [[Weapon System]], even when they are used during melee attacks.

## Domain

Part of:
[[Fight System]]

## Navigation

- Return to [[Fight System]] for the authoritative Fight domain map.
- Read [[Normal Fight]] when the unit is already engaged and is following the standard melee branch.
- Read [[Overrun Fight]] when the fight involves the extra fight-only movement branch for an eligible unengaged unit.
- Read [[Pile-in Move]] or [[Consolidation Move]] when the question is about fight-specific positioning.
- Read [[Fights First]] when the issue is melee sequencing rather than attack resolution.
- Move to [[Making Attacks]] or [[Attack System]] when the question has moved into the shared attack pipeline.

## Related Concepts

- [[Fight System]]
- [[Normal Fight]]
- [[Overrun Fight]]
- [[Pile-in Move]]
- [[Consolidation Move]]
- [[Eligible to Fight, But Unable to Fight]]
- [[Fights First]]
- [[Making Attacks]]
- [[Attack System]]
- [[Charge System]]
- [[Movement System]]
- [[Weapon System]]

## See Also

- [[Fight System]]
- [[Normal Fight]]
- [[Overrun Fight]]
- [[Attack System]]
- [[Charge System]]

## References

- Warhammer 40,000 Core Rules extraction: Fight 12.04.
- Warhammer 40,000 Core Rules extraction: Normal Fight 12.05.
- Warhammer 40,000 Core Rules extraction: Overrun Fight 12.06.
- Warhammer 40,000 Core Rules extraction: Fights First 24.13.
- Warhammer 40,000 Core Rules extraction: Making Attacks 04.00.
