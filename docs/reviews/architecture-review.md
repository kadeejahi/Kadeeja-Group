# Architecture Review

## Purpose
This document tracks architectural concerns, decisions, and necessary follow-up actions identified during our team's design reviews. It records what was reviewed, what concerns were raised, what changes were made, what remains unresolved, and what evidence supports each decision.

This document will be continuously updated throughout the project as team members review and make changes to the system's architecture, and as upcoming action items are addressed. 

## Expectations & Instructions
- Document architectural concerns or questions raised during design reviews, PR discussions, team meetings, or feedback from previous assignments.
- Each item should identify the concern, the action needed, the responsible team member, and its current status.
- Include links to relevant PRs, commits, or other documentation whenever possible.
- Document the outcome of each concern, including any changes made or decisions to leave the design unchanged.
- Do not mark an item as resolved until there is evidence showing it has been addressed.
- When deferring an item, document the reason for postponement and the expected follow-up.
- Keep the document updated as architectural decisions and changes are made. Record significant updates in the Review History table.

## Status Definitions
- **Open:** Concern has been identified but work has not started.
- **In Progress:** A team member is actively working on the item.
- **Resolved:** The concern has been addressed, verified, and supported by evidence.
- **Deferred:** The team has decided to address the concern in a future assignment or development cycle. (Reasoning and expected follow-up timeline must be documented). 
- **Accepted:** The concern was reviewed, and the team determined that no architectural change is necessary. (Reasoning must be documented).

---

## Architecture Review Action Item Tracker
This table provides an overview of architectural concerns and their current status. 

| ID | Assignment/Cycle | Concern/Source | Action or Decision | Owner | Status | Evidence/Follow-Up |
|---|---|---|---|---|---|---|
| ARCH-01 | A3-A4 | PostgreSQL decision: reviewers requested clearer reasoning, alternatives, and tradeoffs. | Review the updated ADR and confirm final approval before committing. | Dathal - confirmation needed | Open | [PR #25](https://github.com/kadeejahi/Kadeeja-Group/pull/25) |
| ARCH-02 | A4 | Clear reference to architectural goals needed. | Identify the relevant architecture goals, reference within AI verification checklist. | Edgar - confirmation needed | Open | [PR #42](https://github.com/kadeejahi/Kadeeja-Group/pull/42) |

All action items should remain in this table, including resolved and deferred items. Update the status and evidence as progress is made.

### Additional Notes & Evidence 
Use this section only when an action item requires additional explanation beyond what fits in the tracker. Reference the action item's ID (ARCH-01, ARCH-02, etc.) in both sections to keep the information connected.

#### (Template) ARCH-XX — [Brief Title]
- **Original Concern:** [What was questioned during review?]
- **Outcome:** [What changed, what decision was made, or why the concern was deferred.]
- **Verification / Evidence:** [How was the outcome verified? Include links.]
- **Remaining Follow-Up (if any):** [Next steps, or "None."]

---

## Review History 
| Date | Assignment/Cycle | Team Member | Update |
|---|---|---|---|
| 10-28-2026 | A4 | Camille | Established the architecture review tracker. |
| 10-28-2026 | A4 | Camille | Documented ARCH-01 and ARCH-02 |
