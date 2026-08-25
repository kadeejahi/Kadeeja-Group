# Team Roles, Identities, and Evidence Ownership

Every student is a **Developer** and also holds at least one specialized engineering role. Each specialized role must have a primary owner and a different backup owner.

The purpose of this file is to provide one authoritative, reviewable record of:

- team membership and GitHub identities;
- specialized engineering-role ownership;
- Project Launch (A1) deliverable ownership;
- role changes during the project; and
- each student's acknowledgement of their responsibilities.

Keep this file current throughout A1-A6. Use the same student names consistently in every table.

## Team Members and GitHub Identities

Replace the sample student entries below with the members of your team. Leave the instructor entry in place.

| Student Name | GitHub Login | Git Author Alias(es) | Member Type |
|---|---|---|---|
| Jordan Smith | jsmith-luc | Jordan Smith; J. Smith | Student |
| Taylor Nguyen | tnguyen22 | Taylor Nguyen | Student |
| Morgan Lee | mlee-luc | Morgan Lee | Student |
| Casey Patel | cpatel-luc | Casey Patel | Student |
| Riley Chen | rchen-luc | Riley Chen | Student |
| William O'Connell | woconnell1 |  | Instructor / Observer |

### Instructions

- List every student on the team.
- Leave the instructor entry in the table.
- Enter the exact GitHub login shown on the repository collaborator list.
- In **Git Author Alias(es)**, list any names that appear for the student in Git commit history. Separate multiple aliases with semicolons.
- Leave **Git Author Alias(es)** blank when no alias is needed or no commits exist yet.
- Private email addresses are not required.
- The instructor is not a team member, does not receive a student role, and is excluded from team contribution and role-fulfillment metrics.
- If a GitHub or Git identity cannot be confidently mapped to a student, update this table so the relationship is explicit.

## Specialized Engineering Role Ownership

Every student has the base role **Developer**. In addition, the team must assign primary and backup ownership for all five specialized engineering roles.

| Specialized Role | Primary Owner(s) | Backup Owner | Effective Gates | Notes |
|---|---|---|---|---|
| Team Lead | Jordan Smith | Taylor Nguyen | A1-A6 | |
| Planning & Process Lead | Taylor Nguyen | Jordan Smith | A1-A6 | |
| Architecture & Development Lead | Morgan Lee | Casey Patel | A1-A6 | |
| Quality & Review Lead | Casey Patel | Morgan Lee | A1-A6 | |
| Operations & Evidence Lead | Riley Chen | Jordan Smith | A1-A6 | |

### Instructions

- Use the **Student Name** values from the Team Members and GitHub Identities table.
- Assign at least one primary owner for every specialized role.
- The backup owner must be different from every primary owner listed for that role.
- A student may hold more than one primary specialized role only when the team has fewer than five students.
- A student may back up more than one role, but the team should avoid concentrating most backup responsibilities in one person.
- Unless a change is documented below, role assignments remain effective through A6.
- Use the **Notes** column to explain shared ownership, small-team role concentration, temporary coverage, or other relevant circumstances.

## Project Launch (A1) Deliverable Ownership

The following ownership assignments apply to the Project Launch (A1) deliverables. Team members may contribute to or update any artifact, but the named primary owner is accountable for ensuring that it is current, correct, internally consistent, and ready for phase-gate review. The backup owner must understand the artifact well enough to review it and assume responsibility when necessary.

| Deliverable | Primary Owner | Backup Owner | Evidence Location |
|---|---|---|---|
| Repository README | Jordan Smith | Taylor Nguyen | `/README.md` |
| Team Charter | Taylor Nguyen | Jordan Smith | `/docs/team/team-charter.md` |
| Role Matrix | Jordan Smith | Casey Patel | `/docs/team/roles.md` |
| Working Agreements | Taylor Nguyen | Riley Chen | `/docs/team/working-agreements.md` |
| AI-Use Policy | Riley Chen | Casey Patel | `/docs/ai/ai-policy.md` |
| AI-Use Log | Riley Chen | Casey Patel | `/docs/ai/ai-use-log.md` |
| Initial Requirements | Morgan Lee | Taylor Nguyen | `/docs/requirements/` |
| Planning and Risk | Taylor Nguyen | Jordan Smith | `/docs/planning/` |
| Initial Decision Record | Morgan Lee | Casey Patel | `/docs/decisions/` |

### Instructions

- Replace the sample names with declared students from the Team Members and GitHub Identities table.
- Every deliverable must have a primary owner and a different backup owner.
- The **Evidence Location** should point to the authoritative repository location for the deliverable.
- Ownership does not mean that one person must perform all work. It identifies who is accountable for readiness at the A1 phase gate.
- Later assignments may rely on the specialized role assignments above. Add a new ownership table only when assignment instructions explicitly require different artifact ownership.

## Role Changes

Document role changes before the gate at which they become effective. Do not overwrite the original assignment without recording the change.

| Effective Gate | Role | Previous Primary | New Primary | Backup | Reason |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Instructions

- Use an assignment gate such as `A2`, `A3`, `A4`, `A5`, or `A6`.
- Record changes to primary ownership, backup ownership, or shared ownership.
- Explain why the change was made.
- Keep prior entries so the role history remains reviewable.

## Team Member Acknowledgement

Each student must confirm that they understand:

- their base Developer role;
- their primary specialized role or roles;
- their backup responsibilities;
- the A1 deliverables they own or back up; and
- the expectation that they will help keep repository evidence current and reviewable.

The **Evidence** column should reference a repository-visible confirmation made by that student using their own GitHub identity. Appropriate evidence includes an issue comment, pull-request review, pull-request comment, or commit that explicitly confirms the assignment. This provides stronger evidence than one person entering `Yes` for the entire team.

| Student Name | Acknowledged | Evidence |
|---|---|---|
| Jordan Smith | Yes | Issue #2 comment |
| Taylor Nguyen | Yes | PR #3 review |
| Morgan Lee | Pending |  |
| Casey Patel | Pending |  |
| Riley Chen | Pending |  |

### Instructions

- Include one row for every declared student.
- Use `Yes` only after the student has personally confirmed the assignment.
- In **Evidence**, link or reference the student's own repository-visible confirmation, such as `Issue #2 comment`, `PR #3 review`, or `Commit abc1234`.
- Do not use meeting notes or another student's statement as the only acknowledgement evidence.
- If acknowledgement evidence is not yet available, use `Pending` and leave the Evidence field blank until the student confirms.
- The instructor does not complete an acknowledgement row.
