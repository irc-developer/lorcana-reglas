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
  - Weapon Profile
  - Weapon Characteristic
  - Range
  - Attacks Characteristic
  - Strength Characteristic
  - Armour Penetration
  - Damage Characteristic
  - Weapon Abilities
  - Select Weapons
  - Attack Sequence
---

# Weapon Characteristics

## Summary

Weapon Characteristics is the umbrella concept for the data fields printed in a weapon profile and later consumed by the rules that declare and resolve attacks.

## Definition

A weapon profile defines the characteristics and labels that describe how that weapon functions, including Range, Attacks, BS or WS, Strength, Armour Penetration, Damage, and any weapon abilities listed on the profile.

## Rules

Weapon characteristics belong to the weapon profile carried by a datasheet rather than to the attack procedure itself.

These values establish what data an attacking model brings into the attack system before any hit, wound, save, or damage step is resolved.

Range distinguishes ranged profiles from melee profiles, where the R value is Melee instead of a distance.

Attacks sets how many attacks that weapon contributes when its attacks are gathered.

Strength, Armour Penetration, and Damage remain part of the same profile and are consumed later by different parts of the attack pipeline.

Weapon abilities are also read from the weapon profile and can change how that weapon is selected or how its attacks are resolved.

## Interactions

- [[Weapon Profile]] is the glossary surface for the complete datasheet entry that carries these values together.
- [[Weapon Characteristic]] is the glossary surface for an individual value inside that profile.
- [[Select Weapons]] is the attack-declaration step that first turns weapon profile data into selected attacks.
- [[Attack Sequence]] is the downstream pipeline that consumes characteristic data once attacks begin resolving.
- [[Range]], [[Attacks Characteristic]], [[Strength Characteristic]], [[Armour Penetration]], and [[Damage Characteristic]] split the main profile fields into separate published concepts.
- [[Weapon Abilities]] explains the profile-based abilities that can modify weapon selection or later attack handling.

## Restrictions

- Weapon Characteristics does not grant permission to shoot or fight.
- Weapon Characteristics does not replace [[Making Attacks]], [[Select Weapons]], or [[Attack Sequence]].
- This article is the umbrella for the weapon data model, not a restatement of the attack procedure that consumes that data.
- BS and WS remain part of the weapon profile even though they are not expanded into standalone published surfaces in this slice.

## Domain

Part of:
[[Weapon System]]

## Navigation

- Return to [[Weapon System]] for the domain map.
- Read [[Weapon Profile]] when the question is about the whole datasheet entry rather than one field.
- Continue to [[Range]], [[Attacks Characteristic]], [[Strength Characteristic]], [[Armour Penetration]], or [[Damage Characteristic]] for the specific fields that feed later attack handling.
- Read [[Weapon Abilities]] for the profile-based rules text that modifies how weapons behave.
- Move to [[Select Weapons]] or [[Attack Sequence]] when the question becomes procedural instead of structural.

## Related Concepts

- [[Weapon Profile]]
- [[Weapon Characteristic]]
- [[Range]]
- [[Attacks Characteristic]]
- [[Strength Characteristic]]
- [[Armour Penetration]]
- [[Damage Characteristic]]
- [[Weapon Abilities]]
- [[Select Weapons]]
- [[Attack Sequence]]

## Frequently Confused With

- [[Weapon Profile]], which is the complete datasheet entry that carries the characteristics together.
- [[Attack Sequence]], which resolves attacks using weapon data but does not define the weapon data model.

## See Also

- [[Weapon System]]
- [[Weapon Profile]]
- [[Weapon Abilities]]

## References

- Warhammer 40,000 Core Rules extraction: Weapons 02.04.
- Warhammer 40,000 Core Rules extraction: Making Attacks 04.00.
- Warhammer 40,000 Core Rules extraction: Attack Sequence 05.00.
- Warhammer 40,000 Core Rules extraction: Core Abilities 24.00.