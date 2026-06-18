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
  - Hit Rolls
  - Save Rolls
  - Mortal Wounds
---

# Wound Rolls

## Summary

Wound Rolls is the attack-sequence step that tests each successful hit against the target's Toughness to determine whether it becomes a successful wound.

## Definition

Roll one D6 for each hit.

## Rules

Wound Rolls happens after [[Hit Rolls]] inside [[Attack Sequence]].

An unmodified roll of 1 always fails.

An unmodified roll of 6 is a critical wound.

For any other result, compare the attack's Strength to the target's Toughness.

If Strength is at least double Toughness, the roll succeeds on 2+.

If Strength is greater than Toughness, the roll succeeds on 3+.

If Strength equals Toughness, the roll succeeds on 4+.

If Strength is lower than Toughness, the roll succeeds on 5+.

If Strength is half or less than Toughness, the roll succeeds on 6+.

Successful wounds proceed to [[Save Rolls]].

## Interactions

- [[Hit Rolls]] supplies the hits that become wound-roll attempts.
- [[Save Rolls]] is the immediate downstream step for successful wounds.
- [[Attack Sequence]] places wound rolls between hit determination and defensive saving.
- Critical wounds remain wounds even when another rule cares about the critical result.
- [[Mortal Wounds]] becomes relevant when another rule converts or adds direct wounds after a critical wound or successful attack.

## Restrictions

- A wound roll of 1 does not become a wound.
- The required result depends on the Strength and Toughness comparison for that attack and target.
- This step determines whether a wound is scored; it does not itself resolve saving or damage.

## Domain

Part of:
[[Attack System]]

## Navigation

- Return to [[Attack System]] for the domain map.
- Read [[Attack Sequence]] for the full order of attack resolution.
- Read [[Hit Rolls]] for the prior step that generated the current wound attempts.
- Continue to [[Save Rolls]] after a successful wound.
- Read [[Mortal Wounds]] when another rule turns the attack into direct wound loss outside the normal save branch.

## Related Concepts

- [[Attack System]]
- [[Attack Sequence]]
- [[Hit Rolls]]
- [[Save Rolls]]
- [[Mortal Wounds]]

## See Also

- [[Attack System]]
- [[Hit Rolls]]
- [[Save Rolls]]

## References

- Warhammer 40,000 Core Rules extraction: Wound Rolls 05.02.
- Warhammer 40,000 Core Rules extraction: Attack Sequence 05.00.
