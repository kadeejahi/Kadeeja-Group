Workflow Review Traceability

1. Purpose
This document records the traceability of CampusConnect development work from requirements and GitHub Issues through implementation, code review, automated checks, testing, and final integration decisions.
The purpose is to provide verifiable evidence that development work is connected to project requirements, reviewed appropriately, and evaluated before integration. It also helps the team identify incomplete work, unresolved defects, and decisions requiring follow-up.
Incomplete items will be explicitly marked as pending and updated when the required work or supporting evidence becomes available. Evidence must reflect actual repository activity and must not be reported as complete without verification.

2. Project Information
Item	Details
Project Name	CampusConnect
Team Name	The Crazy 6
Repository	https://github.com/kadeejahi/Kadeeja-Group
Primary Owner	Dathal
Backup Owner	Pending team confirmation
Last Updated	2026-10-28
Current Release Focus	Cycle 1: Student support request submission, request management, status tracking, communication and updates, role-based access, and request history/visibility

3. Traceability Workflow
CampusConnect uses the following workflow to connect project requirements to implementation and integration evidence.
1. Requirement or Issue: Identify the requirement, task, defect, or engineering decision.
2. Branch and Commit: Record the branch and commits associated with the work.
3. Pull Request: Link the proposed change to the relevant issue or requirement.
4. Review: Record reviewer feedback, requested changes, and how review comments were resolved.
5. CI/CD and Testing: Link automated workflow results and relevant test evidence.
6. Integration Decision: Record whether the change was merged, closed without merging, or deferred.
7. Follow-up: Link unresolved problems to a GitHub Issue or documented action item.
Not every documentation-only change requires a separate issue. However, significant implementation work should be traceable to its purpose, relevant acceptance criteria, and review evidence.

4. Requirement and Issue Traceability
The following requirements represent the current Cycle 1 scope. Each requirement should be linked to its actual GitHub Issue, implementation, and verification evidence when available.
Requirement ID	Requirement	GitHub Issue	Implementation / PR	Verification Evidence
REQ-001	Students can submit support requests.	Pending — issue not yet linked	Pending — add branch, commit, and PR links	Pending — add relevant test results
REQ-002	Students can view their own requests and statuses, but not other students’ requests.	Pending — issue not yet linked	Pending — add branch, commit, and PR links	Pending — add authorization test results
REQ-003	Authorized support reviewers can access and manage submitted requests.	Pending — issue not yet linked	Pending — add branch, commit, and PR links	Pending — add role-access test results
REQ-004	Authorized reviewers can update request information and status.	Pending — issue not yet linked	Pending — add branch, commit, and PR links	Pending — add update and status-transition test results
REQ-005	Authorized reviewers can add progress updates and communicate with students.	Pending — issue not yet linked	Pending — add branch, commit, and PR links	Pending — add communication test results
REQ-006	Internal staff notes are not visible to students.	Pending — confirm or create issue	Pending — add branch, commit, and PR links	Pending — add visibility and authorization test results
REQ-007	Request history and progress information are available to authorized users.	Pending — confirm or create issue	Pending — add branch, commit, and PR links	Pending — add history and visibility test results
REQ-008	Students cannot reopen previously closed requests.	Pending — confirm or create issue	Pending — add branch, commit, and PR links	Pending — add request-state validation test results
Traceability note: Confirm that these requirements match the current requirements document and approved team decisions. Requirement IDs, issue links, implementation references, and test results must come from the actual repository. A pending entry does not indicate that a requirement has been implemented or verified.

## 5. Issue-to-Pull-Request Traceability
Each significant implementation change should have a clear relationship to its corresponding issue or requirement.

(Pending)
Field	Information to Record
Issue ID / Link	GitHub Issue associated with the work
Requirement ID	Related requirement, if applicable
Task Description	Brief description of the work
Branch Name	Branch containing the implementation
Commit Hash / Link	Commit or commits containing the change
Pull Request Link	Proposed change submitted for review
Review Status	Actual status, such as pending, changes requested, or approved
CI/CD Status	Actual status, such as pending, passed, failed, or not configured
Test Evidence	Relevant automated or manual test results
Final Decision	Merged, closed without merging, or deferred, as applicable
Follow-up	Remaining actions or related issues
Use the actual GitHub status and link for each field. If evidence is unavailable, mark the field as pending rather than assuming completion.

## 6. Pull Request Review Evidence
Pull requests provide evidence that proposed changes were reviewed before integration.
For each selected pull request, record:
* The purpose and scope of the change.
* The associated issue or requirement.
* Reviewer comments and requested changes.
* How significant review comments were addressed.
* Relevant automated checks and test results.
* The final merge or no-merge decision.
* Known limitations and follow-up work.
Reviewed Pull Request Record
Field	Evidence
Pull Request	Pending — add actual GitHub PR link
Related Issue	Pending — add issue link or document why no issue was required
Change Summary	Pending — describe the change
Reviewer(s)	Pending — record actual reviewers
Review Findings	Pending — summarize significant feedback
Corrective Actions	Pending — describe changes made in response
CI/CD Results	Pending — link actual workflow checks
Test Results	Pending — link actual test evidence
Final Decision	Pending — record the actual outcome
Remaining Risks	Pending — record unresolved risks or state that none were identified after review
At least one meaningful reviewed pull request should be linked as evidence for Assignment 4. Select an actual pull request that demonstrates review feedback, author responses or corrective changes where applicable, status checks, and a documented integration decision.
Approval and successful checks must apply to the version being merged. If significant code changes occur after approval, the relevant review and checks should be repeated before integration.

## 7. CI/CD and Testing Traceability
Automated checks and testing evidence should be connected to the pull request or commit they evaluate. Evidence should identify the workflow used, the checks executed, the results, and any corrective actions taken.
CI/CD Evidence Record
Evidence Item	Information to Record
Workflow File	Pending — link the actual workflow configuration, if one exists
Pull Request	Pull Request #41
Pull Request Files	View files changed in PR #41
Workflow Run	Pending — link the actual GitHub Actions run
Checks Executed	Pending — record the checks shown in the workflow run
Result	Pending — record the actual completed result
Failure Resolution	Pending — link corrective commits or follow-up issues, if applicable
Test Evidence	Pending — link actual test reports, test output, or relevant documentation
The files-changed page provides context about the proposed changes. The workflow configuration describes the automated process, while an individual workflow run records the checks performed during a particular execution. These serve different purposes and should not be treated as interchangeable.
A successful CI/CD run does not automatically demonstrate that every CampusConnect requirement works correctly. Relevant functional tests, authorization checks, and other requirement-specific verification should also be documented when available.
If automated checks have not run or a workflow is not configured, record that limitation explicitly rather than claiming successful validation.

## 8. Merge and No-Merge Decisions
Integration decisions should be supported by evidence rather than assumptions.
Merge Criteria
Before merging a pull request, verify that:
* The change addresses its stated purpose.
* Relevant review feedback has been resolved or appropriately dispositioned.
* Required CI/CD checks have passed.
* Relevant tests have been executed and evaluated.
* Known risks and limitations have been documented.
* The pull request meets the team’s applicable approval and branch-protection requirements.
No-Merge or Deferred Work
Pull Request	Decision	Reason	Follow-up Action
Pull Request #25	Reported as not merged; verify actual GitHub status	The ADR documentation did not sufficiently address the questions and decision rationale required for review. Additional detail was needed to explain the decision, supporting evidence, alternatives considered, and relevant consequences.	Revise the ADR to address review feedback, document the rationale and alternatives, and submit the updated work for review when ready.
The recorded decision must reflect the actual GitHub outcome. If the pull request was closed without merging, record that status rather than describing it as deferred unless the team explicitly deferred the work.
Update this record if the revised ADR is subsequently submitted, reviewed, or approved. Link the relevant follow-up pull request when available.

## 9. Known Risks and Follow-up Actions
The following are areas to evaluate, not confirmed defects. A risk should only be described as a confirmed problem when supported by implementation, review, or testing evidence.
Risk Area	Evidence to Check	Follow-up
Role-based access	Tests showing students cannot access other students’ requests	Pending — link the relevant issue or test evidence
Internal notes	Tests showing internal notes are hidden from students	Pending — link the relevant issue or test evidence
Request status transitions	Tests covering allowed and disallowed transitions	Pending — link the relevant issue or test evidence
Request history	Tests confirming updates and history remain consistent	Pending — link the relevant issue or test evidence
Notifications	Evidence that expected notifications are triggered and failures are handled	Pending — link the relevant issue or test evidence
Error handling	Logs, tests, or documented failure scenarios	Pending — link the relevant issue or test evidence
Incomplete integration	Open issues, failed checks, or missing test evidence	Pending — identify the follow-up action and owner
For each confirmed unresolved risk, record its impact, owner, status, supporting evidence, and follow-up issue where appropriate. Do not mark an issue resolved without supporting evidence.

## 10. Evidence Maintenance
The primary owner maintains this document and ensures that traceability links remain accurate as development progresses. The backup owner assists with collecting and verifying evidence.
Updates should be made when significant requirements, issues, implementation changes, reviews, CI/CD results, or integration decisions change.
Evidence should be linked to its authoritative location rather than copied unnecessarily into multiple documents. Related evidence may include:
* docs/reviews/assignment4-reviewpackage.md
* The project’s requirements and scope documentation.
* Architecture and API contract documentation.
* Component responsibilities and test plan documentation.
* GitHub Issues, commits, branches, and pull requests.
* CI/CD workflow configurations and actual workflow run results.
* Architecture review action items and deferred-work records.
Confirm all file paths before adding links because the repository’s actual directory structure is authoritative.
This document should be considered current only to the extent that its linked evidence has been verified. Pending items must remain clearly identified until the corresponding work or evidence is available.
