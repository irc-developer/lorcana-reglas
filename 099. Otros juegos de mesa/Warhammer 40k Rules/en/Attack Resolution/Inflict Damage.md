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
  - Save Rolls
  - Mortal Wounds
  - Destroyed
  - Attached Unit System
---

# Inflict Damage

## Summary

Inflict Damage is the terminal attack-sequence step that resolves save results, applies wound loss to the selected model, and ends attacks that fail or finish dealing damage.

## Definition

Resolve save results from lowest to highest, select a model in the current allocation group, and determine whether each attack inflicts damage.

## Rules

Inflict Damage happens after [[Save Rolls]] inside [[Attack Sequence]].

Resolve the save results from lowest to highest.

For each result, select a model in the current allocation group.

If the current group has an Invulnerable Save characteristic and the unmodified save result meets it, the attack fails.

Otherwise, apply Armour Penetration to the save result and compare the modified result against the Save characteristic.

If the modified result meets or exceeds the Save characteristic, the attack fails.

Otherwise, the attack inflicts damage and the selected model loses wounds equal to the weapon's Damage characteristic.

Once the target unit has been destroyed, any excess attacks are lost.

## Interactions

- [[Save Rolls]] provides the save results and allocation order that this procedure resolves.
- [[Mortal Wounds]] is adjacent because some attack effects add direct wounds after normal damage has already been resolved.
- [[Destroyed]] becomes relevant when damage reduces a model to 0 wounds.
- [[Attached Unit System]] remains relevant when allocation groups and model structure affect how attacks finish resolving.

## Restrictions

- Save results are resolved from lowest to highest.
- The current allocation group controls which model is selected for the attack being resolved.
- Excess attacks do not spill into another unit once the current target unit has been destroyed.

## Domain

Part of:
[[Attack System]]

## Navigation

- Return to [[Attack System]] for the full attack-resolution map.
- Read [[Save Rolls]] for the upstream defensive step that produced the current save results.
- Read [[Mortal Wounds]] when the effect adds direct wounds outside the normal save branch.
- Read [[Destroyed]] when the question turns from damage application to destruction state.

## Related Concepts

- [[Attack System]]
- [[Attack Sequence]]
- [[Save Rolls]]
- [[Mortal Wounds]]
- [[Destroyed]]
- [[Attached Unit System]]

## See Also

- [[Attack System]]
- [[Save Rolls]]
- [[Mortal Wounds]]

## References

- Warhammer 40,000 Core Rules extraction: Inflict Damage 05.04.
- Warhammer 40,000 Core Rules extraction: Save Rolls 05.03.
- Warhammer 40,000 Core Rules extraction: Mortal Wounds 06.02.
