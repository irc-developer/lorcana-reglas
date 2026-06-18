---
lang: en
type: procedure
category: attack-resolution
canonical: true
source: core-rules
surface: article
owner-domain: attack-resolution
tags:
  - warhammer40k
  - attack-resolution
  - procedure
aliases: []
related:
  - Attack System
  - Attack Sequence
  - Resolve Attacks
  - Wound Rolls
---

# Hit Rolls

## Summary

Hit Rolls is the first live resolution step in the attack sequence, determining whether each attack dice becomes a hit.

## Definition

Roll one D6 for each attack dice.

## Rules

Hit Rolls is the first child step of [[Attack Sequence]].

An unmodified roll of 1 always fails.

An unmodified roll of 6 is a critical hit.

Any other result that is equal to or greater than the relevant BS or WS is a hit.

Successful hits continue to [[Wound Rolls]].

## Interactions

- [[Attack Sequence]] places hit rolls at the start of the shared attack pipeline.
- [[Dice]] provides the shared D6 notation that this roll uses.
- [[Resolve Attacks]] is the procedure that gathers attack dice before they reach this step.
- [[Wound Rolls]] is the immediate downstream step for successful hits.
- Critical hits remain hits even when another rule cares about the critical result.

## Restrictions

- A hit roll of 1 does not become a hit.
- This step determines only whether the attack hits; it does not resolve damage.
- Any rule that changes hit-roll handling must say so explicitly.

## Domain

Part of:
[[Attack System]]

## Navigation

- Return to [[Attack System]] for the domain overview.
- Read [[Attack Sequence]] for the full order of downstream steps.
- Read [[Resolve Attacks]] if the issue is really about batching attacks before rolling.
- Continue to [[Wound Rolls]] for the next step after successful hits.

## Related Concepts

- [[Attack System]]
- [[Dice]]
- [[Attack Sequence]]
- [[Resolve Attacks]]
- [[Wound Rolls]]

## See Also

- [[Attack System]]
- [[Attack Sequence]]
- [[Wound Rolls]]

## References

- Warhammer 40,000 Core Rules extraction: Hit Rolls 05.01.
- Warhammer 40,000 Core Rules extraction: Attack Sequence 05.00.
