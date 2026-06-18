---
lang: en
type: system
category: attack-resolution
canonical: true
source: core-rules
surface: system
owner-domain: attack-resolution
tags:
  - warhammer40k
  - attack-resolution
  - system
aliases: []
related:
  - Datasheet System
  - Ability System
  - Core Abilities
  - Attached Unit System
  - Terrain Visibility System
  - Weapon System
---

# Attack System

## Overview

Attack System is the authoritative System Article for the Attack Resolution domain. It maps the published attack-declaration procedures, the hit-to-damage pipeline, direct-damage support rules, and the neighbouring systems that supply weapon data, visibility constraints, ability modifiers, and attached-unit interactions.

## Scope

This domain covers the shared attack pipeline used by combat systems, including attack declaration, live hit-to-damage resolution, and the published support rules that sit alongside that sequence.

It helps answer questions about how attacks are declared and resolved, where direct-damage branches fit into that process, and which neighbouring systems provide required inputs or consume attack outputs.

## Domain Ownership

- Owner domain: Attack Resolution.
- Publication role: maintain the canonical attack-declaration and attack-sequence articles that define the shared resolution pipeline used by combat systems.
- Domain system role: provide the authoritative entry point and navigation surface for the published Attack Resolution domain.

## Domain Boundaries

Attack Resolution owns:

- [[Making Attacks]] and [[Attack Sequence]] as the shared parent surfaces for attack declaration and attack resolution.
- [[Select Weapons]], [[Select Targets]], and [[Resolve Attacks]] as the published attack-declaration procedures.
- [[Hit Rolls]], [[Wound Rolls]], [[Save Rolls]], and [[Inflict Damage]] as the published live attack-sequence procedures.
- [[Mortal Wounds]] and [[Hazard Rolls]] as published direct-damage support rules in this domain.

Attack Resolution does not own:

- [[Weapon System]] ownership of weapon statistics and weapon abilities.
- [[Terrain Visibility System]] ownership of visibility, cover, and terrain-state rules used during targeting.
- [[Shooting System]] and [[Fight System]] phase-specific permissions to attack.
- [[Attached Unit System]] ownership of attached-unit-specific targeting, allocation, and save interactions.
- [[Core Concepts System]] ownership of foundational unit and model concepts such as [[Units and Models]].

## Published Articles

- [[Making Attacks]]
- [[Attack Sequence]]
- [[Mortal Wounds]]
- [[Select Weapons]]
- [[Select Targets]]
- [[Resolve Attacks]]
- [[Hit Rolls]]
- [[Wound Rolls]]
- [[Save Rolls]]
- [[Inflict Damage]]
- [[Hazard Rolls]]

## Planned Articles

None.

## Related Systems

- [[Core Concepts System]] provides the unit and model baseline that the attack pipeline consumes.
- [[Datasheet System]], [[Profiles]], and [[Weapon System]] provide the printed data surfaces that attacks use.
- [[Ability System]] provides the broader taxonomy for rules that can modify or constrain attack resolution.
- [[Core Abilities]] provides the published index for the attack-facing ability cluster that feeds into this domain.
- [[Terrain Visibility System]] provides the visibility and cover context used during target selection and resolution.
- [[Attached Unit System]] provides the neighbouring combined-unit interaction branch for targeting and saving.
- [[Shooting System]] and [[Fight System]] consume this shared attack pipeline in their phase-specific contexts.

## Navigation

- Start here when the question is about the common attack pipeline rather than a phase-specific permission to attack.
- Read [[Making Attacks]] for the parent declaration procedure that every attack begins with.
- Follow [[Select Weapons]], [[Select Targets]], and [[Resolve Attacks]] in order when the issue is about declaring or batching attacks.
- Follow [[Attack Sequence]], [[Hit Rolls]], [[Wound Rolls]], [[Save Rolls]], and [[Inflict Damage]] when the issue is about the live resolution pipeline.
- Read [[Mortal Wounds]] or [[Hazard Rolls]] when damage is being applied outside the normal save sequence.
- Move to [[Weapon System]] when the lookup is about weapon data or weapon abilities before the attack sequence starts resolving.
- Move to [[Core Abilities]] when the lookup has narrowed to a published attack-facing ability such as [[Anti]], [[Blast]], [[Precision]], [[Devastating Wounds]], or [[Torrent]].
- Read [[Fire Overwatch]] or [[Epic Challenge]] when the question is about a downstream stratagem that consumes or grants an attack-facing rule from this domain.
- Move to [[Profiles]] when the question is about model characteristics on the datasheet rather than the attack procedure itself.
- Move to [[Terrain Visibility System]] when target selection depends on visibility or cover-state interactions.
- Move to [[Attached Unit System]] when save allocation or targeting interacts with an attached unit.
- Move to [[Shooting System]] or [[Fight System]] when the real question is phase-specific permission to attack rather than the shared attack procedure.

## See Also

- [[Making Attacks]]
- [[Attack Sequence]]
- [[Mortal Wounds]]
- [[Select Weapons]]
- [[Select Targets]]
- [[Resolve Attacks]]
- [[Hit Rolls]]
- [[Wound Rolls]]
- [[Save Rolls]]
- [[Inflict Damage]]
- [[Hazard Rolls]]
- [[Core Concepts System]]
- [[Datasheet System]]
- [[Profiles]]
- [[Weapon System]]
- [[Terrain Visibility System]]
- [[Ability System]]
- [[Core Abilities]]
- [[Fire Overwatch]]
- [[Epic Challenge]]
- [[Attached Unit System]]
- [[Shooting System]]
- [[Fight System]]