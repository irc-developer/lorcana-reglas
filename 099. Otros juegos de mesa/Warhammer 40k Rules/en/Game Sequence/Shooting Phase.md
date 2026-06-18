---
lang: en
type: concept
category: game-sequence
canonical: true
source: core-rules
surface: article
owner-domain: game-sequence
tags:
  - warhammer40k
  - game-sequence
  - concept
aliases: []
related:
  - Battle Sequence System
  - Turn Structure
  - Shooting System
  - Shoot
  - Attack System
  - Terrain Visibility System
  - Fire Overwatch
  - Actions
---

# Shooting Phase

## Summary

Shooting Phase is the turn-phase timing container for resolving ranged attacks one unit at a time through an eligible shooting procedure.

## Definition

Shooting Phase is the phase in which units resolve ranged attacks through one eligible shooting type.

## Rules

Shooting Phase resolves in this order:

1. Start of Shooting Phase.
2. [[Shoot]].
3. End of Shooting Phase.

Units shoot one at a time using one eligible shooting type.

A unit selected to shoot is no longer eligible to start an [[Actions|action]] until end of phase.

## Interactions

- [[Turn Structure]] is the parent timing article that places this phase inside each player turn.
- [[Shoot]] is the published shooting-owned procedure that this phase contains.
- [[Shooting System]] owns shooting permissions, modes, and targeting exceptions used in this phase.
- [[Attack System]] owns the shared attack pipeline consumed after shooting becomes legal.
- [[Terrain Visibility System]] owns visibility and cover states that constrain or modify shooting in this phase.
- [[Fire Overwatch]] is a downstream permission that allows shooting outside the normal sequence of this phase.
- [[Actions]] consumes the phase timing because shooting can block a unit from starting an action until end of phase.

## Restrictions

- This article owns the phase timing, not the shooting modes or attack-resolution mechanics used within it.
- It does not redefine target legality, visibility, attack steps, or weapon data.
- Exceptions that permit shooting outside the normal sequence remain owned by their own domains.

## Domain

Part of:
[[Battle Sequence System]]

## Navigation

- Return to [[Battle Sequence System]] for the authoritative Game Sequence domain map.
- Read [[Turn Structure]] for the full turn order.
- Read [[Shoot]] when the question is the unit-selection procedure used in this phase.
- Move to [[Shooting System]] when the issue is a shooting mode, targeting exception, or special shooting procedure.
- Move to [[Attack System]] when the question has moved into the shared combat pipeline.
- Move to [[Terrain Visibility System]] when line of sight or cover states are deciding the outcome.

## Related Concepts

- [[Battle Sequence System]]
- [[Turn Structure]]
- [[Shooting System]]
- [[Shoot]]
- [[Attack System]]
- [[Terrain Visibility System]]
- [[Fire Overwatch]]
- [[Actions]]

## See Also

- [[Battle Sequence System]]
- [[Turn Structure]]
- [[Shooting System]]
- [[Shoot]]
- [[Attack System]]
- [[Terrain Visibility System]]

## References

- Warhammer 40,000 Core Rules extraction: Shooting Phase 10.00.
- Warhammer 40,000 Core Rules extraction: Shoot 10.02.
