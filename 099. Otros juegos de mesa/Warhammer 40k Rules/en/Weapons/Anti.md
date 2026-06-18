---
lang: en
type: concept
category: weapons
canonical: true
source: core-rules
surface: article
owner-domain: weapons
tags:
  - warhammer40k
  - weapons
  - concept
aliases:
  - '[ANTI]'
related:
  - Weapon System
  - Weapon Abilities
  - Core Abilities
  - Attack System
  - Wound Rolls
  - Keywords
---

# Anti

## Summary

Anti is the weapon ability that turns an unmodified wound roll of the listed value into a critical wound against targets with the named keyword.

## Definition

Anti-X Y+ makes an unmodified wound roll of Y+ a critical wound against targets with keyword X.

## Rules

Anti applies when resolving [[Wound Rolls]].

It affects only targets with the named keyword.

When the listed wound-roll result is achieved against a matching target, that wound roll is a critical wound.

## Interactions

- [[Wound Rolls]] is the attack-sequence step that Anti modifies.
- [[Keywords]] determines whether the target has the named keyword required by the ability.
- [[Attack System]] is the shared attack pipeline that receives this modifier.
- [[Weapon Abilities]] places Anti inside the broader weapon-ability cluster.

## Restrictions

- Anti applies only against targets with the named keyword.
- Anti changes wound-roll outcome classification; it does not replace the wound-roll step.
- This article does not redefine what a keyword is or how wound rolls are otherwise resolved.

## Domain

Part of:
[[Weapon System]]

## Navigation

- Return to [[Weapon System]] for the weapon-data domain map.
- Read [[Wound Rolls]] when the question is about the underlying wound procedure.
- Read [[Keywords]] when the issue is whether the target qualifies.
- Move to [[Core Abilities]] for the wider attack-facing ability index.

## Related Concepts

- [[Weapon System]]
- [[Weapon Abilities]]
- [[Core Abilities]]
- [[Attack System]]
- [[Wound Rolls]]
- [[Keywords]]

## Frequently Confused With

- [[Lethal Hits]], which changes how a critical hit behaves rather than how a wound roll becomes critical.

## References

- Warhammer 40,000 Core Rules extraction: [ANTI] 24.03.
- Warhammer 40,000 Core Rules extraction: Wound Rolls 05.02.

*** Add File: c:\Users\plata\OneDrive\Documentos\Proyectos\warhammerwiki\Warhammer 40k Rules\Weapons\Blast.md
---
type: concept
category: weapons
canonical: true
source: core-rules
surface: article
owner-domain: weapons
tags:
  - warhammer40k
  - weapons
  - concept
aliases:
  - '[BLAST]'
related:
  - Weapon System
  - Weapon Abilities
  - Core Abilities
  - Attack System
  - Resolve Attacks
  - Close-quarters Shooting
---

# Blast

## Summary

Blast is the weapon ability that adds attack dice based on target-unit size when attack dice are gathered.

## Definition

Add attack dice for every five models in the target unit when gathering attack dice.

## Rules

Blast modifies attack gathering inside [[Resolve Attacks]].

For every five models in the target unit, add the listed extra attack dice.

If the ability is written as Blast X, add X attack dice for every five models in the target unit.

Blast cannot target units the attacker is engaged with in close-quarters contexts.

## Interactions

- [[Resolve Attacks]] is the attack-declaration procedure that Blast modifies.
- [[Close-quarters Shooting]] is the relevant close-range restriction context named by the rule.
- [[Attack System]] is the shared attack pipeline that receives the gathered attacks.
- [[Weapon Abilities]] places Blast inside the wider weapon-ability cluster.

## Restrictions

- Blast modifies attack-dice gathering only.
- Blast does not redefine target selection, hit rolls, or wound rolls.
- Blast cannot be used against units the attacker is engaged with in close-quarters contexts.

## Domain

Part of:
[[Weapon System]]

## Navigation

- Return to [[Weapon System]] for the weapon-data overview.
- Read [[Resolve Attacks]] when the issue is how attacks are gathered.
- Read [[Close-quarters Shooting]] when the issue is the engaged-target restriction.
- Move to [[Core Abilities]] for the wider attack-facing ability index.

## Related Concepts

- [[Weapon System]]
- [[Weapon Abilities]]
- [[Core Abilities]]
- [[Attack System]]
- [[Resolve Attacks]]
- [[Close-quarters Shooting]]

## Frequently Confused With

- [[Cleave]], which also scales with target-unit size but only if all attacks from the weapon target one unit.

## References

- Warhammer 40,000 Core Rules extraction: [BLAST] 24.05.
- Warhammer 40,000 Core Rules extraction: Resolve Attacks 04.03.

*** Add File: c:\Users\plata\OneDrive\Documentos\Proyectos\warhammerwiki\Warhammer 40k Rules\Weapons\Cleave.md
---
type: concept
category: weapons
canonical: true
source: core-rules
surface: article
owner-domain: weapons
tags:
  - warhammer40k
  - weapons
  - concept
aliases:
  - '[CLEAVE]'
related:
  - Weapon System
  - Weapon Abilities
  - Core Abilities
  - Attack System
  - Resolve Attacks
  - Blast
---

# Cleave

## Summary

Cleave is the weapon ability that adds attack dice against larger target units when all attacks from the weapon are directed at one unit.

## Definition

If all attacks from the weapon target one unit, add X attack dice for every five models in the target unit.

## Rules

Cleave modifies attack gathering inside [[Resolve Attacks]].

Its extra attack dice are gained only if all attacks from the weapon target one unit.

The extra attack dice scale with the size of the target unit.

## Interactions

- [[Resolve Attacks]] is the procedure that Cleave modifies.
- [[Attack System]] is the shared attack pipeline that consumes those gathered attacks.
- [[Blast]] is a neighbouring size-scaling weapon ability with a different condition.
- [[Weapon Abilities]] places Cleave inside the broader weapon-ability cluster.

## Restrictions

- Cleave applies only if all attacks from the weapon target one unit.
- Cleave changes attack gathering only.
- Cleave does not redefine target selection, hit rolls, or damage.

## Domain

Part of:
[[Weapon System]]

## Navigation

- Return to [[Weapon System]] for the weapon-data overview.
- Read [[Resolve Attacks]] when the issue is how attack dice are gathered.
- Compare with [[Blast]] when the question is about size-scaling attack-dice abilities.
- Move to [[Core Abilities]] for the wider attack-facing ability index.

## Related Concepts

- [[Weapon System]]
- [[Weapon Abilities]]
- [[Core Abilities]]
- [[Attack System]]
- [[Resolve Attacks]]
- [[Blast]]

## Frequently Confused With

- [[Blast]], which scales from target size without requiring all attacks from the weapon to go into one target unit.

## References

- Warhammer 40,000 Core Rules extraction: [CLEAVE] 24.06.
- Warhammer 40,000 Core Rules extraction: Resolve Attacks 04.03.

*** Add File: c:\Users\plata\OneDrive\Documentos\Proyectos\warhammerwiki\Warhammer 40k Rules\Weapons\Close-quarters.md
---
type: concept
category: weapons
canonical: true
source: core-rules
surface: article
owner-domain: weapons
tags:
  - warhammer40k
  - weapons
  - concept
aliases:
  - '[CLOSE-QUARTERS]'
related:
  - Weapon System
  - Weapon Abilities
  - Core Abilities
  - Shooting System
  - Close-quarters Shooting
  - Pistol
---

# Close-quarters

## Summary

Close-quarters is the weapon ability that allows eligible units with one or more qualifying weapons to use close-quarters shooting.

## Definition

Units with one or more Close-quarters weapons can use close-quarters shooting.

## Rules

Close-quarters grants access to [[Close-quarters Shooting]].

When using another shooting type, each non-MONSTER and non-VEHICLE model must choose either its Close-quarters weapons or its other ranged weapons, not both.

## Interactions

- [[Close-quarters Shooting]] is the shooting mode that this ability enables.
- [[Shooting System]] owns the phase-level procedure that consumes this ability.
- Pistol is an alias of this concept for all rules purposes.
- [[Weapon Abilities]] places Close-quarters inside the broader weapon-ability cluster.

## Restrictions

- Close-quarters does not redefine the shooting-mode procedure itself.
- When using another shooting type, each non-MONSTER and non-VEHICLE model must choose either its Close-quarters weapons or its other ranged weapons, not both.
- This page is distinct from [[Close-quarters Shooting]], which is the enabled shooting mode rather than the weapon ability.

## Domain

Part of:
[[Weapon System]]

## Navigation

- Return to [[Weapon System]] for the weapon-data overview.
- Read [[Close-quarters Shooting]] when the question is about the enabled shooting mode.
- Read Pistol when the lookup starts from the official alias.
- Move to [[Core Abilities]] for the wider attack-facing ability index.

## Related Concepts

- [[Weapon System]]
- [[Weapon Abilities]]
- [[Core Abilities]]
- [[Shooting System]]
- [[Close-quarters Shooting]]
- Pistol

## Frequently Confused With

- [[Close-quarters Shooting]], which is the shooting mode granted by this ability rather than the weapon ability itself.

## References

- Warhammer 40,000 Core Rules extraction: [CLOSE-QUARTERS] 24.07.
- Warhammer 40,000 Core Rules extraction: Close-quarters Shooting 10.06.