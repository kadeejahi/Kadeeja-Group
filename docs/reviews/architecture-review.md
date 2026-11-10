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
| ARCH-01 | A3-A4 | PostgreSQL decision: reviewers requested clearer reasoning, alternatives, and tradeoffs. | Verify PostgreSQL selection in the ADR, document alternatives and tradeoffs, and obtain approval from the authorized reviewer. | Dathal - confirmation needed | Open | [PR #25](https://github.com/kadeejahi/Kadeeja-Group/pull/25) |
| ARCH-02 | A4 | Clear reference to architectural goals needed. | Document relevant architectural goals and connect them to design decisions and the AI verification checklist. | Edgar - confirmation needed | Open | [PR #42](https://github.com/kadeejahi/Kadeeja-Group/pull/42) |

All action items should remain in this table, including resolved and deferred items. Update the status and evidence as progress is made.

### Additional Notes & Evidence 
Use this section only when an action item requires additional explanation beyond what fits in the tracker. Reference the action item's ID (ARCH-01, ARCH-02, etc.) in both sections to keep the information connected.

#### (Template) ARCH-XX — [Brief Title]
- **Original Concern:** [What was questioned during review?]
- **Decision & Rationale:** [What was the reasoning for the change?]
- **Alternatives & Tradeoffs:** [What other options were considered, and what were their advantages or disadvantages?]
- **Decision Authority:** [Who has the authority to approve this architectural decision, and where is that authority documented?]
- **Approval Status & Date: ** [Has the decision been approved, is approval pending, and when was it approved?]
- **Outcome:** [What changed, what decision was made, or why the concern was deferred.]
- **Verification / Evidence:** [How was the outcome verified? Include links.]
- **Remaining Follow-Up (if any):** [Next steps, or "None."]

## ARCH-01 — PostgreSQL Database Decision

- **Original Concern:** Reviewers requested clearer reasoning behind the PostgreSQL database decision, including alternatives, tradeoffs, and final approval.
- **Decision & Rationale:** PostgreSQL is the database technology under review for CampusConnect. The team's final selection and reasoning must be confirmed against the updated Architecture Decision Record.
- **Alternatives & Tradeoffs:** The team must verify which alternative database technologies were considered and document their advantages and disadvantages compared with PostgreSQL.
- **Decision Authority:** The authorized architectural decision-maker has not yet been confirmed. The team must identify the approving individual or role and reference where that authority is documented.
- **Approval Status & Date:** Pending verification. No final approval date has been established in this review record.
- **Outcome:** The PostgreSQL decision remains open in this tracker until its rationale, alternatives, tradeoffs, and approval evidence are verified.
- **Verification / Evidence:**  PR #25. The PR must be reviewed to confirm its contents and whether an authorized approval was recorded.
- **Remaining Follow-Up:** Confirm the decision authority, review the ADR, document the selected outcome, and record an inspectable approval reference.

## ARCH-02 — Architectural Goals Documentation

- **Original Concern:** Reviewers identified that CampusConnect's architectural goals were not clearly referenced or connected to the project's design and verification documentation.
- **Decision & Rationale:** The team needs to identify and document the architectural goals guiding CampusConnect's design. These goals will provide a reference for evaluating architectural decisions and verifying their alignment with project requirements.
- **Alternatives & Tradeoffs:** Not yet established. If competing architectural goals or design approaches are identified, the team should document the relevant tradeoffs.
- **Decison Authority:** The authorized reviewer responsible for approving the architectural goals has not yet been confirmed.
- **Approval Status & Date:** Pending verification. No final approval date has been established in this review record.
- **Outcome:** Open. The architectural goals and their supporting approval evidence still require verification.
- **Verification / Evidence:** PR #42. Review the PR and related architecture documentation to confirm the goals and their connection to the AI verification checklist.
- **Remaining Follow-Up:** Identify the relevant architectural goals, document their connection to CampusConnect's design decisions, and confirm the authorized reviewer's approval.

---

## Review History 
| Date | Assignment/Cycle | Team Member | Update |
|---|---|---|---|
| 10-28-2026 | A4 | Camille | Established the architecture review tracker. |
| 10-28-2026 | A4 | Camille | Documented ARCH-01 and ARCH-02 |
| 11-09-2026 | A5 | Dean | Updated template for additional notes & evidence including ARCH_01 and ARCH-02 | 


