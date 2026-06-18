---
lang: en
type: system
category: fight
canonical: true
source: core-rules
surface: system
owner-domain: fight
tags:
  - warhammer40k
  - fight
  - system
aliases: []
related:
  - Battle Sequence System
  - Charge System
  - Attack System
  - Ability System
  - Movement System
  - Objective Control System
  - Weapon System
---

# Fight System

## Overview

Fight System is the authoritative System Article for the Fight domain. It maps melee sequencing, eligibility, fight-only movement, and fight-order state while keeping the shared attack pipeline, charge procedures, generic movement, and weapon data in their owning domains.

## Scope

This domain covers the questions that arise once melee resolution begins: who can fight, when units fight, which fight mode applies, how pile-in and consolidation work, and how Fights First changes ordering.

Readers should expect published concept articles, fight-owned procedures, and glossary support for fight sequencing state.

This domain consumes upstream context from charge, movement, abilities, and the shared attack pipeline, but it does not republish those systems locally.

## Domain Ownership

- Owner domain: Fight.
- Domain role: publish and maintain the canonical melee-resolution surfaces that belong specifically to the Fight step.
- Publication role: provide the authoritative navigation hub for fight sequencing, permissions, and fight-specific movement.

## Domain Boundaries

- Fight owns who can fight, when units fight, Fights First ordering, pile-in, consolidation, and the fight-specific pass rule for eligible units that cannot currently reach an enemy.
- Fight does not own charge declaration or charge movement; those remain in [[Charge System]].
- Fight does not own generic movement procedures; those remain in [[Movement System]].
- Fight does not own hit rolls, wound rolls, save rolls, inflict damage, or the shared attack pipeline; those remain in [[Attack System]].
- Fight does not own weapon characteristics or weapon-side abilities; those remain in [[Weapon System]].
- Fight can point to [[Objective Control System]] when consolidation changes objective state, but it does not absorb objective ownership.

## Published Articles

- [[Fight]]
- [[Normal Fight]]
- [[Overrun Fight]]
- [[Pile-in Move]]
- [[Consolidation Move]]
- [[Eligible to Fight, But Unable to Fight]]
- [[Fights First]]
- [[Fights First unit]]

## Planned Articles

None.

## Related Systems

- [[Battle Sequence System]] provides the wider timing spine, while [[Fight Phase]] is the canonical phase article that contains melee resolution.
- [[Charge System]] creates the engagement opportunities and charge-derived state that feed into melee resolution.
- [[Movement System]] supplies the generic movement framework that Fight-specific movement must remain separate from.
- [[Attack System]] supplies the shared attack pipeline that melee attacks consume.
- [[Ability System]] remains the neighbouring system for broader ability classification, even when a fight-order state is used here.
- [[Weapon System]] supplies melee weapon data without transferring ownership of weapon characteristics into Fight.
- [[Objective Control System]] consumes positional outcomes created by consolidation without becoming part of Fight ownership.

## Navigation

- Start with [[Fight]] for the core melee sequencing rule.
- Continue to [[Normal Fight]] for the standard engaged melee branch.
- Continue to [[Overrun Fight]] when the selected unit uses the extra fight-only movement branch.
- Read [[Pile-in Move]] and [[Consolidation Move]] for the two fight-owned positional procedures.
- Read [[Eligible to Fight, But Unable to Fight]] when sequencing reaches a pass condition.
- Read [[Fights First]] and [[Fights First unit]] when ordering priority is the real question.
- Move to [[Fight Phase]] when the question is whether melee resolution is currently taking place in the turn.
- Move to [[Charge System]] when the question is about entering melee rather than resolving it.
- Move to [[Attack System]] when the question is about hit, wound, save, or damage mechanics shared with shooting.
- Move to [[Movement System]] when the issue is generic movement rather than fight-only positioning.
- Move to [[Weapon System]] when the issue is melee weapon data rather than fight sequencing.

## See Also

- [[Fight Phase]]
- [[Battle Sequence System]]
- [[Charge System]]
- [[Attack System]]
- [[Movement System]]
- [[Weapon System]]
- [[Objective Control System]]

## References

- Warhammer 40,000 Core Rules extraction: Fight Phase 12.00.
- Warhammer 40,000 Core Rules extraction: Fight 12.04.
- Warhammer 40,000 Core Rules extraction: Normal Fight 12.05.
- Warhammer 40,000 Core Rules extraction: Overrun Fight 12.06.
- Warhammer 40,000 Core Rules extraction: Pile-in Move 12.03.
- Warhammer 40,000 Core Rules extraction: Consolidation Move 12.08.
- Warhammer 40,000 Core Rules extraction: Eligible to Fight, But Unable to Fight.
- Warhammer 40,000 Core Rules extraction: Fights First 24.13.
