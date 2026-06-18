---
lang: en
type: concept
category: core-concepts
canonical: true
source: core-rules
surface: article
owner-domain: core-concepts
tags:
  - warhammer40k
  - core-concepts
  - units
aliases: []
related:
  - Units and Models
  - Attached unit
  - Destroyed
  - Revived
---

# Starting Strength and Half-strength

## Summary

Starting Strength and Half-strength is the core-concepts rule that fixes a unit's starting strength and defines when a unit is below starting strength, at half-strength, or below half-strength by comparing its current remaining models, or a single-model unit's remaining wounds, against that fixed reference.

## Definition

Starting strength is the number of models a unit contains at the start of the first battle round.

For a single-model unit, these strength-state checks use the model's remaining wounds against its W characteristic instead of model count.

## Rules

### Determining Starting Strength

A unit's starting strength is determined by the number of models it contains at the start of the first battle round.

For a single-model unit, starting strength is tracked using the model's remaining wounds against its W characteristic.

If a rule adds a new unit to your army during the battle, that unit's starting strength is determined when it is added to your army.

Apart from when its starting strength is determined, that unit uses the same starting-strength rules as other units.

For an [[Attached unit]], starting strength uses the total number of models in that attached unit at the start of the first battle round.

### Strength States

A unit is below starting strength if it has fewer remaining models than its starting strength.

A single-model unit is below starting strength if it has fewer remaining wounds than its W characteristic.

A unit is at half-strength if it has exactly half as many remaining models as its starting strength.

A single-model unit is at half-strength if it has exactly half as many remaining wounds as its W characteristic.

A unit is below half-strength if it has fewer than half as many remaining models as its starting strength.

A single-model unit is below half-strength if it has fewer than half as many remaining wounds as its W characteristic.

If the relevant value cannot be evenly halved, the unit or model cannot be at half-strength, but it can still be below half-strength.

### State Transitions And Rule Evaluation

Once determined, a unit's starting strength remains the reference point used for later strength-state checks.

A unit moves from starting strength to below starting strength as soon as it has fewer remaining models than that reference, or as soon as a single-model unit has fewer remaining wounds than its W characteristic.

A unit is at half-strength only while its current remaining models, or a single-model unit's remaining wounds, are exactly half of the relevant starting value.

A unit becomes below half-strength as soon as its current remaining models, or a single-model unit's remaining wounds, are fewer than half of that value.

Rules that evaluate these states compare the unit's current remaining models, or a single-model unit's current remaining wounds, against its fixed starting-strength reference.

When a rule returns destroyed models to a unit, the unit's current state is re-evaluated against the same starting-strength reference, and returned models cannot take the unit above that starting strength.

## Interactions

- [[Units and Models]] provides the unit/model distinction that these strength-state checks use.
- [[Destroyed]] defines when models or units have actually been destroyed; this article uses the remaining models or wounds after that destruction to evaluate strength states.
- [[Revived]] returns destroyed models to a unit, but the unit is still checked against the same fixed starting-strength reference.
- [[Attached unit]] changes how starting strength is counted only insofar as the attached unit's total model count is used at the start of the first battle round.
- Battle-shock Rolls uses whether a unit is at half-strength or below half-strength as an input condition, but the battle-shock procedure and its consequences belong to that separate rule.

## Restrictions

- This article defines strength states only and does not restate the Battle-shock Rolls procedure or its consequences.
- This article does not restate attached-unit formation, strategic reserves, movement procedures, or abilities.
- At half-strength exists only when the relevant starting value can be evenly halved.
- For single-model units, these checks use remaining wounds and the W characteristic, not model count.

## Domain Membership

- Owner domain: Core Concepts.

## Related Concepts

- [[Units and Models]]
- [[Attached unit]]
- [[Destroyed]]
- [[Revived]]

## Frequently Confused With

- Battle-shock Rolls, which uses half-strength as a trigger condition but is a separate rule.
- [[Revived]], which can return models to the unit but does not reset or replace the unit's original starting-strength reference.
- [[Attached unit]], which can change the counted model total at the start of the first battle round but does not redefine the strength-state thresholds.

## References

- Warhammer 40,000 Core Rules extraction: Starting Strength and Half-strength.
- Warhammer 40,000 Core Rules extraction: Adding a New Unit to Your Army.
- Warhammer 40,000 Core Rules extraction: Battle-shock Rolls 01.07.
- Warhammer 40,000 Core Rules extraction: Profiles 02.02.
- Warhammer 40,000 Core Rules extraction: Revived.