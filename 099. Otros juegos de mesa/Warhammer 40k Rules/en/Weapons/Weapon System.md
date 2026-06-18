---
lang: en
type: system
category: weapons
canonical: true
source: core-rules
surface: system
owner-domain: weapons
tags:
  - warhammer40k
  - weapons
  - system
aliases: []
related:
  - Datasheet System
  - Ability System
  - Core Abilities
  - Attack System
  - Keywords
---

# Weapon System

## Overview

Weapon System is the authoritative System Article for the Weapons domain. It maps the published weapon data surfaces that live on datasheets, the profile concepts that describe weapon characteristics, the glossary vocabulary for weapon profiles, and the boundary between weapon modelling and attack execution.

## Scope

This domain covers the published weapon profile concepts, characteristic fields, and glossary support that describe weapon data before the attack sequence starts resolving.

It helps answer questions about what a weapon profile contains, how each characteristic should be read, and which neighbouring systems consume weapon data without owning it.

## Domain Ownership

- Owner domain: Weapons.
- Publication role: maintain the canonical weapon data articles and glossary support that define weapon profiles and their characteristics.
- Domain system role: provide the authoritative entry point and navigation surface for the published Weapons-domain footprint.

## Domain Boundaries

Weapons owns:

- [[Weapon Characteristics]], [[Range]], [[Attacks Characteristic]], [[Strength Characteristic]], [[Armour Penetration]], [[Damage Characteristic]], and [[Weapon Abilities]] as the published weapon-data surfaces.
- [[Anti]], [[Assault]], [[Blast]], [[Cleave]], [[Close-quarters]], [[Devastating Wounds]], [[Extra Attacks]], [[Hazardous]], [[Heavy]], [[Ignores Cover]], [[Indirect Fire]], [[Lance]], [[Lethal Hits]], [[Melta]], [[One Shot]], [[Precision]], [[Psychic]], [[Rapid Fire]], [[Sustained Hits]], [[Torrent]], and [[Twin-linked]] as published weapon-side ability articles.
- [[Pistol]] as the published alias entry that routes to [[Close-quarters]].
- [[Weapon Profile]] and [[Weapon Characteristic]] as glossary support for reading weapon information.

Weapons does not own:

- [[Datasheet System]] ownership of the broader unit-data model that carries weapons.
- [[Attack System]] ownership of the attack sequence that consumes weapon statistics.
- [[Ability System]] ownership of generic ability-classification rules beyond weapon-specific ability presentation.
- [[Keyword System]] ownership of generic keyword semantics even when weapon rules interact with keyword-qualified targeting.

## Published Articles

- [[Weapon Characteristics]]
- [[Range]]
- [[Attacks Characteristic]]
- [[Strength Characteristic]]
- [[Armour Penetration]]
- [[Damage Characteristic]]
- [[Weapon Abilities]]
- [[Anti]]
- [[Assault]]
- [[Blast]]
- [[Cleave]]
- [[Close-quarters]]
- [[Devastating Wounds]]
- [[Extra Attacks]]
- [[Hazardous]]
- [[Heavy]]
- [[Ignores Cover]]
- [[Indirect Fire]]
- [[Lance]]
- [[Lethal Hits]]
- [[Melta]]
- [[One Shot]]
- [[Precision]]
- [[Psychic]]
- [[Rapid Fire]]
- [[Sustained Hits]]
- [[Torrent]]
- [[Twin-linked]]
- [[Pistol]]
- [[Weapon Profile]]
- [[Weapon Characteristic]]

## Planned Articles

None.

## Related Systems

- [[Datasheet System]] supplies the unit-data structure that carries weapon profiles without taking ownership of weapon semantics.
- [[Attack System]] consumes weapon statistics and weapon abilities during attack declaration and resolution.
- [[Ability System]] governs how weapon abilities sit beside other ability families without absorbing the Weapons-domain data model.
- [[Core Abilities]] is the published system map that indexes the attack-facing ability cluster across domains.
- [[Keyword System]] provides the neighbouring keyword framework that some weapon rules depend on.

## Navigation

- Start here when the question is about what a weapon profile contains before attacks are resolved.
- Read [[Weapon Characteristics]] first for the full weapon data model.
- Use [[Weapon Profile]] and [[Weapon Characteristic]] when the question is terminological or glossary-level.
- Follow [[Range]], [[Attacks Characteristic]], [[Strength Characteristic]], [[Armour Penetration]], or [[Damage Characteristic]] when the issue is a specific profile field.
- Read [[Weapon Abilities]] when the issue is a rule listed in the weapon profile rather than in the datasheet Abilities section.
- Read [[Anti]], [[Assault]], [[Blast]], [[Cleave]], [[Close-quarters]], [[Devastating Wounds]], [[Extra Attacks]], [[Hazardous]], [[Heavy]], [[Ignores Cover]], [[Indirect Fire]], [[Lance]], [[Lethal Hits]], [[Melta]], [[One Shot]], [[Precision]], [[Psychic]], [[Rapid Fire]], [[Sustained Hits]], [[Torrent]], or [[Twin-linked]] when the lookup is already narrowed to a specific weapon ability.
- Read [[Pistol]] when the lookup starts from the alias rather than the canonical target.
- Move to [[Attack System]] when the lookup becomes about the sequence that consumes those characteristics.
- Move to [[Core Abilities]] or [[Ability System]] when the lookup becomes about classifying abilities rather than reading weapon data.
- Move to [[Keyword System]] when the lookup depends on keyword-qualified targeting or other generic keyword semantics.
- Move to [[Datasheet System]] when the lookup starts from the unit's printed data model.

## See Also

- [[Weapon Characteristics]]
- [[Range]]
- [[Attacks Characteristic]]
- [[Strength Characteristic]]
- [[Armour Penetration]]
- [[Damage Characteristic]]
- [[Weapon Abilities]]
- [[Anti]]
- [[Assault]]
- [[Blast]]
- [[Cleave]]
- [[Close-quarters]]
- [[Devastating Wounds]]
- [[Extra Attacks]]
- [[Hazardous]]
- [[Heavy]]
- [[Ignores Cover]]
- [[Indirect Fire]]
- [[Lance]]
- [[Lethal Hits]]
- [[Melta]]
- [[One Shot]]
- [[Precision]]
- [[Psychic]]
- [[Rapid Fire]]
- [[Sustained Hits]]
- [[Torrent]]
- [[Twin-linked]]
- [[Pistol]]
- [[Weapon Profile]]
- [[Weapon Characteristic]]
- [[Datasheet System]]
- [[Ability System]]
- [[Core Abilities]]
- [[Attack System]]
- [[Keyword System]]

## References

- Warhammer 40,000 Core Rules extraction: Datasheets 02.00.
- Warhammer 40,000 Core Rules extraction: Profiles 02.02.
- Warhammer 40,000 Core Rules extraction: Weapons 02.04.
- Warhammer 40,000 Core Rules extraction: Making Attacks 04.00.
- Warhammer 40,000 Core Rules extraction: Attack Sequence 05.00.
- Warhammer 40,000 Core Rules extraction: Core Abilities 24.00.
- Warhammer 40,000 Core Rules extraction: Abilities 24.01.