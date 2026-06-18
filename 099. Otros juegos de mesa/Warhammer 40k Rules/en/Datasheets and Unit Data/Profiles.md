---
lang: en
type: concept
category: datasheets-and-unit-data
canonical: true
source: core-rules
surface: article
owner-domain: datasheets-and-unit-data
tags:
  - warhammer40k
  - datasheets-and-unit-data
  - concept
aliases: []
related:
  - Datasheet System
  - Starting Strength and Half-strength
  - Battle-shock Rolls
  - Level of Control
  - Making Attacks
  - Weapon System
---

# Profiles

## Summary

Profiles is the datasheet-structure article that defines the model characteristics printed on a datasheet before other domains consume those values for movement, durability, attacks, battle-shock, and objectives.

## Definition

Profiles contain model characteristics: M, T, Sv, InSv, W, Ld, and OC.

## Rules

M '-' means the model can be set up but cannot otherwise be moved.

W reduced to 0 or fewer destroys the model.

OC '-' means the model cannot control objectives.

This article defines the profile data surface that other rules consume; it does not redefine the downstream mechanics that use those values.

## Interactions

- [[Making Attacks]] consumes profile data when attacks compare model values and weapon data during combat resolution.
- [[Starting Strength and Half-strength]] consumes profile-backed wounds data when tracking single-model units.
- [[Battle-shock Rolls]] consumes profile-backed Leadership values through the roll family it applies.
- [[Level of Control]] consumes profile-backed Objective Control values when calculating control of an objective.
- [[Weapon System]] remains the neighbouring domain for weapon profiles and weapon characteristics rather than the model profile defined here.

## Restrictions

- This article owns the datasheet profile and its listed characteristics, not the downstream procedures that use those characteristics.
- This article does not replace weapon profiles, weapon characteristics, or ability text.
- This article does not redefine attack resolution, battle-shock application, or objective control calculations.

## Domain Membership

- Owner domain: Datasheets and Unit Data.

## Related Concepts

- [[Datasheet System]]
- [[Making Attacks]]
- [[Starting Strength and Half-strength]]
- [[Battle-shock Rolls]]
- [[Level of Control]]
- [[Weapon System]]

## Frequently Confused With

- [[Weapon System]], which owns weapon profiles and weapon characteristics rather than the model profile on a datasheet.
- [[Starting Strength and Half-strength]], which consumes wounds data from profiles but does not define the profile itself.
- [[Level of Control]], which consumes OC values from profiles but does not define the data field.

## References

- Warhammer 40,000 Core Rules extraction: Profiles 02.02.
- Warhammer 40,000 Core Rules extraction: Making Attacks 04.00.
- Warhammer 40,000 Core Rules extraction: Starting Strength and Half-strength.
- Warhammer 40,000 Core Rules extraction: Battle-shock Rolls 01.07.
- Warhammer 40,000 Core Rules extraction: Level of Control 14.02.