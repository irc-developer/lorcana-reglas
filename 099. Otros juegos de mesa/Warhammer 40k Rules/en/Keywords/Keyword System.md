---
lang: en
type: system
category: keywords
canonical: true
source: core-rules
surface: system
owner-domain: keywords
tags:
  - warhammer40k
  - keywords
  - system
aliases: []
related:
  - Keywords
  - Mixed Keywords in Units
  - Datasheet System
  - Ability System
  - Attached Unit System
---

# Keyword System

## Overview

Keyword System is the governance and navigation surface for the keyword domain. It connects the existing canonical keyword articles to the datasheet model they depend on, marks the still-missing glossary layer, and distinguishes general keyword handling from the separate attached-unit keyword branch.

## Scope

This domain covers generic keyword semantics, mixed-keyword interpretation within a unit, and the planned glossary support needed to keep keyword vocabulary stable and navigable.

It helps answer questions about what keywords mean, how mixed-keyword units are interpreted, and when a reader should move into datasheet structure, ability classification, or attached-unit-specific handling instead of staying in the generic keyword domain.

## Domain Ownership

- Owner domain: Keywords.
- Publication role: organise keyword semantics, keyword-qualified matching, and mixed-keyword interpretation at the domain level.
- Domain system role: provide the authoritative entry point and navigation surface for published and planned keyword-domain content.

## Domain Boundaries

Keywords owns:

- [[Keywords]] and [[Mixed Keywords in Units]] as the published canonical keyword articles.
- the planned glossary support surfaces Keyword, Faction keyword, Unit keyword, and Model keyword.

Keywords does not own:

- [[Datasheet System]] ownership of the data model that carries keywords on a unit.
- [[Ability System]] ownership of ability classification even when abilities refer to keywords.
- [[Attached Unit System]] ownership of keyword handling that is specific to combined-unit behaviour.

## Published Articles

- [[Keywords]]
- [[Mixed Keywords in Units]]

## Planned Articles

- Keyword
- Faction keyword
- Unit keyword
- Model keyword

## Related Systems

- [[Core Concepts System]] provides the baseline unit and model terminology used by keyword interpretation.
- [[Datasheet System]] provides the upstream data model that carries keywords.
- [[Ability System]] remains distinct because ability classes and keyword semantics are separate concept families.
- [[Attached Unit System]] consumes keyword behaviour in a constrained attached-unit context without taking ownership of the generic keyword domain.

## Navigation

- Start here when the question is about what keywords mean, how they are stored, or how mixed-keyword units are interpreted.
- Move to [[Keywords]] for the general canonical rules surface.
- Move to [[Mixed Keywords in Units]] for the mixed-model branch inside a single unit.
- Move to [[Datasheet System]] when the lookup is about where keywords live in the unit data model.
- Move to [[Ability System]] when the lookup becomes about ability classes rather than keyword semantics.
- Move to [[Attached Unit System]] when the lookup is specific to combined units instead of generic unit-level keyword behaviour.

## See Also

- [[Core Concepts System]]
- [[Keywords]]
- [[Mixed Keywords in Units]]
- [[Datasheet System]]
- [[Ability System]]
- [[Attached Unit System]]

## References

- Warhammer 40,000 Core Rules extraction: Keywords 02.05.
- Warhammer 40,000 Core Rules extraction: Mixed Keywords in Units.
- Warhammer 40,000 Core Rules extraction: Army Faction and Faction Keywords.