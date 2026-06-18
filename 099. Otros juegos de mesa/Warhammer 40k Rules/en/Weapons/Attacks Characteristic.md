---
lang: en
type: concept
category: weapons
canonical: true
source: core-rules
surface: article
owner-domain: weapons
tags:
  - warhammer40k
  - weapons
  - concept
aliases: []
related:
  - Weapon System
  - Weapon Characteristics
  - Weapon Profile
  - Select Weapons
  - Resolve Attacks
  - Attack Sequence
  - Weapon Abilities
---

# Attacks Characteristic

## Summary

Attacks Characteristic is the weapon value that establishes how many attacks a selected weapon contributes before those attacks are resolved through the attack pipeline.

## Definition

The Attacks Characteristic is the A value on a weapon profile. It determines the number of attacks gathered for that weapon unless another rule changes that amount.

## Rules

The Attacks Characteristic is part of the weapon profile rather than a separate attack procedure.

When a weapon is selected, its A value establishes the weapon's starting attack count.

That value is then used when attacks are gathered for resolution.

Some weapon abilities change how many attack dice are gathered, but they do so by modifying the weapon's attacks rather than replacing the existence of the Attacks Characteristic itself.

## Interactions

- [[Weapon Characteristics]] places the Attacks Characteristic inside the wider weapon data model.
- [[Weapon Profile]] is the datasheet entry where the A value is recorded.
- [[Select Weapons]] determines which profile's A value will matter for the current attack declaration.
- [[Resolve Attacks]] is the downstream step that gathers attacks from the selected weapon.
- [[Attack Sequence]] resolves each gathered attack after the attack count has already been established.
- [[Weapon Abilities]] covers profile-based rules that can add attacks or otherwise modify attack gathering.

## Restrictions

- The Attacks Characteristic does not itself select a weapon or a target.
- The Attacks Characteristic does not define hit, wound, save, or damage handling.
- Extra attacks come only from rules that explicitly modify the weapon or its attacks.

## Domain

Part of:
[[Weapon System]]

## Navigation

- Return to [[Weapon System]] for the domain map.
- Read [[Weapon Characteristics]] for the full profile structure around the A value.
- Read [[Select Weapons]] when the issue is which weapon contributes attacks.
- Read [[Resolve Attacks]] when the issue is gathering those attacks for one target at a time.
- Read [[Weapon Abilities]] when the attack count changes because of a weapon rule.

## Related Concepts

- [[Weapon Characteristics]]
- [[Weapon Profile]]
- [[Select Weapons]]
- [[Resolve Attacks]]
- [[Attack Sequence]]
- [[Weapon Abilities]]

## Frequently Confused With

- [[Attack Sequence]], which resolves attacks after they have already been gathered.

## See Also

- [[Weapon System]]
- [[Resolve Attacks]]
- [[Weapon Abilities]]

## References

- Warhammer 40,000 Core Rules extraction: Weapons 02.04.
- Warhammer 40,000 Core Rules extraction: Resolve Attacks 04.03.
- Warhammer 40,000 Core Rules extraction: [BLAST] 24.05.
- Warhammer 40,000 Core Rules extraction: [CLEAVE] 24.06.
- Warhammer 40,000 Core Rules extraction: [RAPID FIRE] 24.30.