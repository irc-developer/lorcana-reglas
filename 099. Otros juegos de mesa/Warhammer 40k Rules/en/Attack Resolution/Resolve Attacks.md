---
lang: en
type: procedure
category: attack-resolution
canonical: true
source: core-rules
surface: article
owner-domain: attack-resolution
tags:
  - warhammer40k
  - attack-resolution
  - procedure
aliases: []
related:
  - Attack System
  - Making Attacks
  - Select Targets
  - Attack Sequence
  - Hit Rolls
  - Wound Rolls
  - Save Rolls
  - Inflict Damage
---

# Resolve Attacks

## Summary

Resolve Attacks is the procedure that processes declared attacks one enemy unit at a time by gathering compatible attack dice and sending them through the attack sequence.

## Definition

Resolve attacks against one enemy unit at a time, gathering attack dice for one selected weapon and any identical attacks that can be resolved together.

## Rules

Resolve Attacks happens after [[Select Weapons]] and [[Select Targets]] have already fixed the weapons and targets involved.

Choose one enemy unit that has been declared as a target.

Gather the attack dice for one selected weapon and any other identical attacks that can be resolved together against that same unit.

Identical attacks must share the same BS or WS, Strength, Armour Penetration, Damage, and the same applicable abilities and rules.

Resolve all gathered attack dice through [[Attack Sequence]].

Continue until every declared attack against every declared target unit has been resolved.

## Interactions

- [[Making Attacks]] is the parent procedure that leads into this step after weapons and targets are declared.
- [[Select Targets]] fixes the target assignments that this procedure now processes.
- [[Attack Sequence]] is the immediate downstream pipeline used for each gathered attack.
- [[Hit Rolls]], [[Wound Rolls]], [[Save Rolls]], and [[Inflict Damage]] are the child procedures used once the attack dice are being resolved.

## Restrictions

- Attacks can only be batched together when they are identical in the ways the rule requires.
- This procedure resolves attacks one enemy unit at a time, not every declared target simultaneously.
- Declared weapon and target choices are not reopened during this step.

## Domain

Part of:
[[Attack System]]

## Navigation

- Return to [[Attack System]] for the full domain map.
- Read [[Making Attacks]] if the issue is still about attack declaration rather than attack resolution.
- Read [[Attack Sequence]] when the question turns to the internal hit-to-damage order.
- Follow [[Hit Rolls]], [[Wound Rolls]], [[Save Rolls]], and [[Inflict Damage]] for the downstream steps.

## Related Concepts

- [[Attack System]]
- [[Making Attacks]]
- [[Select Targets]]
- [[Attack Sequence]]
- [[Hit Rolls]]
- [[Wound Rolls]]
- [[Save Rolls]]
- [[Inflict Damage]]

## See Also

- [[Attack System]]
- [[Attack Sequence]]
- [[Hit Rolls]]

## References

- Warhammer 40,000 Core Rules extraction: Resolve Attacks 04.03.
- Warhammer 40,000 Core Rules extraction: Attack Sequence 05.00.
