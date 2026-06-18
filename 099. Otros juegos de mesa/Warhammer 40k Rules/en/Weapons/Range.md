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
  - Select Targets
  - Resolve Attacks
---

# Range

## Summary

Range is the weapon characteristic that tells you whether a weapon is ranged or melee and, for ranged weapons, the distance band within which that weapon can be used.

## Definition

Range is the R value on a weapon profile. Ranged weapons have a distance value, while melee weapons have R shown as Melee.

## Rules

Range is part of the weapon profile and is read before attacks are resolved.

For a ranged weapon, the Range value supplies the distance reference used when deciding whether that weapon can affect a target.

For a melee weapon, the profile does not have a numeric range value; it is identified by the Melee label instead.

Some weapon abilities and downstream attack rules check whether a target is within half range, so the Range value can remain relevant after target selection has already been made.

## Interactions

- [[Weapon Characteristics]] is the umbrella article that places Range inside the wider weapon data model.
- [[Weapon Profile]] is the profile entry where Range appears alongside the weapon's other fields.
- [[Select Weapons]] uses weapon profile data when an attacking model decides which weapons it will use.
- [[Select Targets]] is the attack-declaration step most directly constrained by whether a target is in range.
- [[Resolve Attacks]] remains a downstream consumer when a rule checks range again, such as half-range conditions tied to a weapon ability.

## Restrictions

- Range does not determine visibility, cover, or any other targeting condition outside the weapon's own distance requirement.
- Range does not grant permission to attack.
- The Melee label is not a numeric distance value.
- This article does not replace the target-selection procedure that applies range to a specific attack declaration.

## Domain

Part of:
[[Weapon System]]

## Navigation

- Return to [[Weapon System]] for the domain map.
- Read [[Weapon Characteristics]] for the full weapon data model.
- Read [[Select Targets]] when the question is about applying range to a declared target.
- Read [[Resolve Attacks]] when the issue is a rule that checks half range after target selection.

## Related Concepts

- [[Weapon Characteristics]]
- [[Weapon Profile]]
- [[Select Weapons]]
- [[Select Targets]]
- [[Resolve Attacks]]

## Frequently Confused With

- [[Select Targets]], which applies Range during attack declaration instead of defining what Range is.

## See Also

- [[Weapon System]]
- [[Weapon Characteristics]]
- [[Select Targets]]

## References

- Warhammer 40,000 Core Rules extraction: Weapons 02.04.
- Warhammer 40,000 Core Rules extraction: Select Targets 04.02.
- Warhammer 40,000 Core Rules extraction: Core Abilities 24.00.
- Warhammer 40,000 Core Rules extraction: [MELTA] 24.25.
- Warhammer 40,000 Core Rules extraction: [RAPID FIRE] 24.30.