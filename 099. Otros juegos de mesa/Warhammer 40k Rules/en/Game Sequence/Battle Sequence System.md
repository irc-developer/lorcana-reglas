---
lang: en
type: system
category: game-sequence
canonical: true
source: core-rules
surface: system
owner-domain: game-sequence
tags:
  - warhammer40k
  - game-sequence
  - system
aliases: []
related:
  - Core Concepts System
  - Datasheet System
  - Ability System
  - Keyword System
  - Pre-battle and Deployment System
---

# Battle Sequence System

## Overview

Battle Sequence System is the authoritative System Article for the Game Sequence domain. It maps the battle-round loop, the turn-level sequence, and the published phase-level timing articles that own the repository's main play-order spine.

## Scope

This domain covers the outer battle loop, the turn-level sequence, and the phase-level timing containers that structure the rest of the ruleset without absorbing the canonical rules that belong to downstream gameplay domains.

It helps answer questions about when rules happen, how the battle-round and turn sequence frame phase play, and which adjacent systems a reader should enter when the lookup stops being about timing and becomes about a specific mechanic.

## Domain Ownership

- Owner domain: Game Sequence.
- Publication role: publish and maintain the canonical timing-spine articles for battle rounds, turn structure, and named phases.
- Domain system role: provide the authoritative entry point and navigation surface for the published timing spine and its adjacent systems.

## Domain Boundaries

Game Sequence owns:

- the timing-spine relationship surface represented by Battle Sequence System;
- [[Battle Round]] and [[Turn Structure]] as the published parent timing concepts of live play;
- [[Command Phase]], [[Movement Phase]], [[Shooting Phase]], [[Charge Phase]], and [[Fight Phase]] as the published phase timing surfaces;
- unresolved timing nodes such as Start of Battle Round, Gain Core CP, and Command Abilities as non-published structural or placeholder nodes until a source-backed publication surface is justified.

Game Sequence does not own:

- [[Core Concepts System]] concepts such as units, measurement, or state terminology.
- [[Pre-battle and Deployment System]] ownership of the pre-battle sequence that precedes the first battle round.
- phase-domain rule meaning owned by adjacent published systems such as movement, shooting, charge, fight, abilities, or keywords.
- datasheet modelling or keyword classification merely because those systems depend on timing windows.

## Published Articles

- [[Battle Round]]
- [[Turn Structure]]
- [[Command Phase]]
- [[Movement Phase]]
- [[Shooting Phase]]
- [[Charge Phase]]
- [[Fight Phase]]

## Planned Articles

None.

## Related Systems

- [[Core Concepts System]] provides the baseline concepts that every phase and timing surface consumes.
- [[Pre-battle and Deployment System]] connects the pre-battle sequence to the first battle round without transferring ownership of the battle loop.
- [[Movement System]], [[Shooting System]], [[Charge System]], [[Fight System]], and [[Battle-shock System]] consume the phase timing spine while keeping their own mechanics in their home domains.
- [[Datasheet System]], [[Ability System]], [[Keyword System]], and [[Stratagem System]] depend on timing windows defined here while remaining responsible for their own domain content.

## Navigation

- Start here when the question is about when a rule happens rather than how a specific mechanic resolves.
- Read [[Battle Round]] first when the question is about the outer loop of play, round count, or first-turn structure.
- Read [[Turn Structure]] when the question is about how a player turn is ordered.
- Read [[Command Phase]] when the lookup is about CP gain, command-level timing, or when command-phase subrules apply.
- Read [[Movement Phase]] when the issue is whether a movement-domain procedure is currently available.
- Read [[Shooting Phase]] when the question is where ranged attacks sit in the turn.
- Read [[Charge Phase]] when the issue is when charge procedures are available.
- Read [[Fight Phase]] when the question is where melee resolution sits in the turn.
- Move to [[Core Concepts System]] when the lookup depends on baseline unit, measurement, or state terminology.
- Move to [[Pre-battle and Deployment System]] when the lookup is still before the first battle round.
- Move outward to [[Movement System]], [[Shooting System]], [[Charge System]], [[Fight System]], or [[Battle-shock System]] once the lookup stops being about timing and becomes about a domain-owned mechanic.

## See Also

- [[Battle Round]]
- [[Turn Structure]]
- [[Command Phase]]
- [[Movement Phase]]
- [[Shooting Phase]]
- [[Charge Phase]]
- [[Fight Phase]]
- [[Core Concepts System]]
- [[Movement System]]
- [[Shooting System]]
- [[Charge System]]
- [[Fight System]]
- [[Battle-shock System]]
- [[Stratagem System]]
- [[Datasheet System]]
- [[Ability System]]
- [[Keyword System]]
- [[Pre-battle and Deployment System]]