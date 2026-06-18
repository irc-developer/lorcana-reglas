---
lang: en
type: concept
category: attack-resolution
canonical: true
source: core-rules
surface: article
owner-domain: attack-resolution
tags:
  - warhammer40k
  - attack-resolution
  - concept
aliases: []
related:
  - Attack System
  - Select Weapons
  - Select Targets
  - Resolve Attacks
  - Attack Sequence
  - Mortal Wounds
  - Shooting System
  - Fight System
---

# Making Attacks

## Summary

Making Attacks is the parent attack procedure that turns a unit's decision to shoot or fight into an ordered sequence of weapon selection, target selection, and attack resolution.

## Definition

When a unit shoots or fights, it resolves Select Weapons, Select Targets, and Resolve Attacks in that order.

## Rules

Making Attacks is the shared entry point for both ranged and melee attack resolution.

During this procedure, each attacking model first determines which weapons it will use through [[Select Weapons]].

After weapon selection, each selected weapon is assigned to a legal enemy target through [[Select Targets]].

Once weapons and targets are fixed, the attacks are processed through [[Resolve Attacks]], which applies the downstream attack pipeline one target at a time.

While shooting, a model can select one or more ranged weapons.

While fighting, a model selects one melee weapon unless another rule changes that default.

Different weapons from the same attacking unit can be assigned to different enemy units.

## Interactions

- [[Select Weapons]] determines which weapons contribute attacks to the current attack declaration.
- [[Select Targets]] fixes the enemy unit or units each selected weapon is attacking.
- [[Resolve Attacks]] applies the declared attacks against one enemy unit at a time.
- [[Attack Sequence]] is the downstream sub-pipeline used once attacks begin resolving.
- [[Shooting System]] and [[Fight System]] are phase-level consumers of this shared attack procedure.
- [[Mortal Wounds]] sits adjacent to the main save-based pipeline because some attack effects convert or add direct wounds outside normal saves.

## Restrictions

- Making Attacks does not itself grant permission to shoot or fight; that timing and permission come from other published systems or from rule text that authorizes the attack.
- The procedure does not remove weapon-specific or attack-type restrictions on what can be selected or targeted.
- Weapon abilities that alter weapon selection, target selection, or later attack resolution modify this procedure only where their own rules say they do.

## Domain

Part of:
[[Attack System]]

## Navigation

- Return to [[Attack System]] for the domain map and the full published attack-resolution cluster.
- Read [[Select Weapons]] first when the question is about what an attacking model can use.
- Read [[Select Targets]] when the issue is target legality or split targeting.
- Read [[Resolve Attacks]] and then [[Attack Sequence]] when the attacks have already been declared and must now be processed.
- Move to [[Shooting System]] or [[Fight System]] when the real question is phase-specific attack permission rather than the common resolution procedure.

## Related Concepts

- [[Attack System]]
- [[Select Weapons]]
- [[Select Targets]]
- [[Resolve Attacks]]
- [[Attack Sequence]]
- [[Mortal Wounds]]
- [[Shooting System]]
- [[Fight System]]

## See Also

- [[Attack System]]
- [[Select Weapons]]
- [[Attack Sequence]]

## References

- Warhammer 40,000 Core Rules extraction: Making Attacks 04.00.
- Warhammer 40,000 Core Rules extraction: Select Weapons 04.01.
- Warhammer 40,000 Core Rules extraction: Select Targets 04.02.
- Warhammer 40,000 Core Rules extraction: Resolve Attacks 04.03.
