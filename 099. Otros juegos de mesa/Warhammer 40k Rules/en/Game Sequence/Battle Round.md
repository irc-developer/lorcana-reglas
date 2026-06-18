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
  - Command Phase
  - Pre-battle and Deployment System
  - Strategic Reserves System
---

# Battle Round

## Summary

Battle Round is the outer live-play loop that orders each round of the battle into a start step, the player-turn sequence, and an end step.

## Definition

A battle round is the outer turn loop of the game.

## Rules

Each battle round resolves in this order:

1. Start of Battle Round.
2. Player Turns, published canonically in this repository as [[Turn Structure]].
3. End of Battle Round.

The mission determines which player takes the first turn in each battle round.

The mission also determines how many battle rounds are played.

## Interactions

- [[Turn Structure]] is the per-player sequence nested inside each battle round.
- [[Command Phase]] is the first named phase inside the turn structure that each battle round contains through its player turns.
- [[Pre-battle and Deployment System]] owns the setup sequence that happens before the first battle round begins.
- [[Strategic Reserves System]] consumes battle-round numbering for default reserve-arrival and destruction timing.

## Restrictions

- This concept does not define the pre-battle sequence that happens before live play starts.
- This concept does not define the mechanics executed inside the phases of a player's turn.
- Mission-specific end-of-round scoring remains mission-owned rather than Game Sequence-owned.

## Domain

Part of:
[[Battle Sequence System]]

## Navigation

- Return to [[Battle Sequence System]] for the authoritative Game Sequence domain map.
- Read [[Turn Structure]] for the per-player sequence nested inside the battle round.
- Read [[Command Phase]] when the lookup has moved from round framing to the first phase of the turn.
- Move to [[Pre-battle and Deployment System]] when the question is still about setup before the first battle round.
- Move to [[Strategic Reserves System]] when the issue is reserve timing that depends on battle-round number.

## Related Concepts

- [[Battle Sequence System]]
- [[Turn Structure]]
- [[Command Phase]]
- [[Pre-battle and Deployment System]]
- [[Strategic Reserves System]]

## See Also

- [[Battle Sequence System]]
- [[Turn Structure]]
- [[Pre-battle and Deployment System]]
- [[Strategic Reserves System]]

## References

- Warhammer 40,000 Core Rules extraction: Battle Round 07.00.