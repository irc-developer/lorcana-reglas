---
lang: en
type: system
category: datasheets-and-unit-data
canonical: true
source: core-rules
surface: system
owner-domain: datasheets-and-unit-data
tags:
  - warhammer40k
  - datasheets-and-unit-data
  - system
aliases: []
related:
  - Core Concepts System
  - Ability System
  - Keyword System
  - Keywords
  - Mixed Keywords in Units
---

# Datasheet System

## Overview

Datasheet System is the domain MOC for the unit data model used throughout the rules. It maps the parent datasheet concept, the structural child articles that describe what a datasheet contains, and the neighbouring systems that consume profiles, weapons, keywords, abilities, and unit composition data.

## Scope

This domain covers the datasheet as the unit data model and the planned structural child surfaces that explain what information a datasheet contains before other systems tell the reader how that information behaves in play.

It helps answer questions about where rules data lives on a unit, which parts of that data model are separate publishable concepts, and which neighbouring systems consume those fields.

## Domain Ownership

- Owner domain: Datasheets and Unit Data.
- Publication role: maintain the datasheet-structure surfaces that explain how unit data is organised before gameplay systems consume it.
- Domain system role: provide the authoritative entry point and navigation surface for the Datasheets and Unit Data domain.

## Domain Boundaries

Datasheets and Unit Data owns:

- [[Profiles]] as the published datasheet-structure article currently available in this domain.
- the planned datasheet-structure surfaces Datasheets, Datasheet Name, Weapons, Unit Composition and Other Rules, and Wargear Options.

Datasheets and Unit Data does not own:

- [[Core Concepts System]] ownership of the baseline meaning of units and models that datasheets describe.
- [[Ability System]] ownership of ability classification and propagation.
- [[Keyword System]] ownership of keyword semantics and mixed-keyword interpretation.
- [[Weapon System]] ownership of weapon-data semantics even when weapons originate from the datasheet structure.
- phase-domain systems that consume datasheet values during play.

## Published Articles

- [[Datasheets]]
- [[Datasheet Name]]
- [[Profiles]]
- [[Weapons]]
- [[Unit Composition and Other Rules]]
- [[Wargear Options]]

## Planned Articles

- None.

## Related Systems

- [[Core Concepts System]] provides the upstream unit and model baseline that datasheets describe.
- [[Ability System]] consumes datasheet ability fields without taking ownership of the data model.
- [[Keyword System]] consumes datasheet keyword fields and owns their semantics.
- [[Weapon System]] consumes weapon-profile data that originates from the datasheet structure.

## Navigation

- Start here when the question is about what information a datasheet carries before asking how that information behaves in play.
- Read [[Profiles]] when the question is about the model characteristics printed on a datasheet before another domain consumes those values.
- Move to [[Ability System]] when the lookup becomes about ability classes, propagation, or special rules text.
- Move to [[Keyword System]] when the lookup becomes about keyword matching, inheritance, or mixed-keyword behaviour.
- Move to [[Weapon System]] when the lookup is specifically about weapon profiles or weapon characteristics rather than the broader datasheet structure.
- Move to [[Core Concepts System]] when the lookup depends on the baseline meaning of units, models, or shared state.

## See Also

- [[Core Concepts System]]
- [[Ability System]]
- [[Keyword System]]
- [[Weapon System]]
- [[Profiles]]
- [[Keywords]]
- [[Mixed Keywords in Units]]

## References

- Warhammer 40,000 Core Rules extraction: Datasheets 02.00.
- Warhammer 40,000 Core Rules extraction: Datasheet Name 02.01.
- Warhammer 40,000 Core Rules extraction: Profiles 02.02.
- Warhammer 40,000 Core Rules extraction: Weapons 02.04.
- Warhammer 40,000 Core Rules extraction: Unit Composition and Other Rules 02.06.
- Warhammer 40,000 Core Rules extraction: Wargear Options 02.07.