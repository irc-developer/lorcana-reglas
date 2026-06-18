---
lang: en
type: concept
category: charge
canonical: true
source: core-rules
surface: article
owner-domain: charge
tags:
  - warhammer40k
  - charge
  - concept
aliases: []
related:
  - Charge System
  - Charge Move
  - Charge target
  - Battle Sequence System
  - Movement System
  - Fight System
  - Fights First
  - Attack System
---

# Charge

## Summary

Charge is the core Charge-domain concept for declaring a charge, making the charge roll that sets maximum distance, and determining whether the unit can convert that declaration into a Charge Move.

## Definition

An eligible unit declares one or more charge targets, makes a 2D6 charge roll, and if possible may make a [[Charge Move]].

## Rules

The charge declaration identifies the enemy units that the charging unit is trying to reach through its later charge move.

The charge roll is 2D6 and sets the maximum distance available for that move.

If a valid [[Charge Move]] is possible, the unit may make that move up to the distance shown by the charge roll.

If a valid charge move is impossible, or if the player declines to make it, the unit does not move. This is the failed-charge outcome inside this domain.

An unmodified roll of 2 is never sufficient for a charge because a unit cannot begin the procedure already within engagement range.

A successful charge is the charge outcome that leads to a valid [[Charge Move]], creating the position that downstream melee systems later consume.

## Interactions

- [[Charge Move]] is the procedure that executes the successful movement outcome of a charge.
- [[Charge target]] is the glossary support for the enemy units declared during the charge procedure.
- [[Movement System]] provides the generic movement framework that Charge uses without taking ownership of normal, advance, or fall-back movement.
- [[Fight System]] consumes the engagement opportunities created by a successful charge, but it does not own declaration or charge resolution.
- [[Fights First]] is a downstream fight-order state that can be created by a successful charge move without transferring ownership of that state out of Fight.
- [[Attack System]] remains downstream of this domain because charging creates melee opportunities but does not resolve hit, wound, save, or damage steps.

## Restrictions

- This concept does not define generic movement modes such as normal, advance, or fall-back movement.
- This concept does not define engagement range, fight eligibility, fight order, pile-in move, or consolidation move.
- This concept does not define hit rolls, wound rolls, save rolls, inflict damage, or weapon characteristics.
- Upstream rules can make a unit unable to declare a charge, but those lockouts remain owned by their own domains and are not republished here.

## Domain

Part of:
[[Charge System]]

## Navigation

- Return to [[Charge System]] for the authoritative Charge domain map.
- Read [[Charge Move]] when the question is about how the successful movement procedure is executed.
- Read [[Charge target]] when the issue is which enemy units were declared as the destination of the charge.
- Move to [[Movement System]] when the real question is about generic movement rules rather than charge-specific resolution.
- Move to [[Fight System]] when the question has moved from entering melee into resolving it.
- Move to [[Attack System]] when the question is really about melee attack execution rather than charge resolution.

## Related Concepts

- [[Charge System]]
- [[Charge Move]]
- [[Charge target]]
- [[Battle Sequence System]]
- [[Movement System]]
- [[Fight System]]
- [[Fights First]]
- [[Attack System]]

## See Also

- [[Charge System]]
- [[Charge Move]]
- [[Movement System]]
- [[Fight System]]
- [[Attack System]]

## References

- Warhammer 40,000 Core Rules extraction: Charge 11.02.
- Warhammer 40,000 Core Rules extraction: Charge Move 11.04.
