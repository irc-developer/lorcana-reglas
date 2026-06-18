---
lang: en
type: concept
category: keywords
canonical: true
source: core-rules
surface: article
owner-domain: keywords
tags:
  - warhammer40k
  - keywords
  - datasheets
aliases: []
related:
  - Units and Models
  - Mixed Keywords in Units
  - Keywords in Attached Units
---

# Keywords

## Summary

Keywords is the datasheet rule that defines how faction keywords and other keywords function for rules purposes and how keyword-qualified rules identify valid units.

## Definition

Datasheets list faction keywords and other keywords; for rules purposes both function as keywords unless a rule specifically refers to faction selection.

## Rules

Keywords appear in full capitals on datasheets.

When a rule names a keyword, that rule applies only to units that have that keyword.

The distinction between faction keywords and other keywords matters only when a rule specifically refers to faction selection or a faction-based requirement.

## Interactions

- [[Units and Models]] is the parent rules context where datasheets and their keyword lines are defined.
- [[Mixed Keywords in Units]] explains how a unit's keyword set works when its component models do not share the same keywords.
- [[Keywords in Attached Units]] is the attached-unit-specific branch that applies the same unit-level logic to attached units.
- Anti is a downstream consumer that checks whether the target unit has the named keyword.
- Core Abilities is the system surface where many keyword-qualified abilities rely on this rule as a prerequisite.

## Restrictions

- A keyword-qualified rule does not apply to a unit that lacks the named keyword.
- This article defines general keyword semantics and does not replace the more specific handling in [[Mixed Keywords in Units]] or [[Keywords in Attached Units]].

## Related Concepts

- [[Units and Models]]
- [[Mixed Keywords in Units]]
- [[Keywords in Attached Units]]

## Frequently Confused With

- [[Mixed Keywords in Units]], which governs how a unit aggregates keywords when its component models differ.
- [[Keywords in Attached Units]], which governs the attached-unit-specific keyword case.

## References

- Warhammer 40,000 Core Rules extraction: Keywords 02.05.
- Warhammer 40,000 Core Rules extraction: Mixed Keywords in Units.
- Warhammer 40,000 Core Rules extraction: Keywords in Attached Units 19.03.
- Warhammer 40,000 Core Rules extraction: Army Faction and Faction Keywords.
- Warhammer 40,000 Core Rules extraction: [ANTI] 24.03.