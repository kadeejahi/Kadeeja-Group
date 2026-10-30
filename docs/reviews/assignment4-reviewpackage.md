Assignment 4 Evidence Review Package

## 1. Purpose

This document serves as the central index for Assignment 4 engineering evidence for CampusConnect. It identifies the documentation, repository artifacts, workflow records, peer reviews, automated checks, and testing evidence used to demonstrate construction readiness, integration progress, quality assurance, and responsible engineering practices.

The purpose of this package is to make the team’s engineering process transparent, traceable, and verifiable. Each evidence item should link to its authoritative location within the GitHub repository or associated GitHub workflow records.

Evidence must accurately reflect the current state of the project. Completed work should be supported by verifiable evidence, while missing documentation, unresolved findings, and incomplete activities should be clearly identified.

## 2. Project Information

Item	Details
Project Name	CampusConnect
Team Name	The Crazy 6
Repository	https://github.com/kadeejahi/Kadeeja-Group
Assignment	Assignment 4
Primary Owner	Dathal
Backup Owner	Camille
Last Updated	2026-10-28

## 3. Evidence Index

# 3.1 Construction and Architecture Evidence

Evidence	Purpose	Location	Status
Project Scope	Defines the features, requirements, and boundaries of Cycle 1.	docs/planning/scope.md	Verified
Architecture Documentation	Describes the system structure, architectural design, components, and responsibilities.	docs/architecture/architecture.md	Verified
API Contracts	Documents expected communication, request formats, and responsibilities between system components.	docs/architecture/api-contracts.md	Verified
Component Responsibilities	Defines component ownership, boundaries, and assigned responsibilities.	docs/architecture/component-responsibilities.md	Verified
Architecture Review Action Items	Records architecture review findings, corrective actions, deferred items, and closure evidence.	docs/reviews/architecture-review.md	Verified

# 3.2 Change and Workflow Traceability

Evidence	Purpose	Location	Status
Changed-File Index	Identifies files added, modified, or unchanged since Assignment 3.	https://github.com/kadeejahi/Kadeeja-Group/pull/54	In Progress
GitHub Issues	Records requirements, implementation tasks, defects, and decisions requiring follow-up.	https://github.com/kadeejahi/Kadeeja-Group/issues/50	Verified
Branches and Commits	Provides a record of development history and implementation changes.	https://github.com/kadeejahi/Kadeeja-Group	Verified
Pull Requests	Documents proposed changes, implementation discussions, and integration decisions.	Pending – Issue Not Yet Linked	Pending
Reviewed Pull Request	Demonstrates meaningful peer review, reviewer feedback, and a merge/no-merge decision.	https://github.com/kadeejahi/Kadeeja-Group/pull/51	Verified
Workflow Review Traceability	Connects issues, branches, commits, pull requests, reviews, CI checks, and final integration decisions.	https://github.com/kadeejahi/Kadeeja-Group/pull/53/files	In Progress

# 3.3 CI/CD and Testing Evidence

Evidence	Purpose	Location	Status
CI/CD Workflow	Defines the automated build, validation, and testing processes.	.github/workflows/ci.yml	Verified
CI/CD Results	Demonstrates whether automated checks passed, failed, or required corrective action.	Pending – Issue Not Yet Linked	Pending
Test Plan	Defines testing scope, test levels, environment, responsibilities, and entry/exit criteria.	docs/testing/test-plan.md	Verified
Test Evidence	Records executed tests, results, and supporting validation documentation.	Pending – Issue Not Yet Linked	Pending
Runtime / Logging Evidence	Documents runtime behavior, error handling, logging, and troubleshooting evidence.	docs/observability/runtime-evidence.md	Verified
Code Review Evidence	Records reviewer feedback, requested changes, and evidence of resolution.	Pending – Issue Not Yet Linked	Pending

# 3.4 AI-Assisted Engineering Evidence

Evidence	Purpose	Location	Status
AI Assistance Disclosure	Identifies where AI assistance was used and explains how generated suggestions or outputs were evaluated.	docs/ai/ai-use-log.md	Verified
Human Review and Validation	Demonstrates that AI-assisted changes were independently reviewed, tested, and validated by team members.	Pending – Issue Not Yet Linked	Pending

## 4. Workflow Traceability

The team should be able to demonstrate how significant engineering changes move through the development and integration process.

The expected workflow is:

Requirement or Issue → Task → Branch → Commit → Pull Request → Review → CI Checks → Merge or No-Merge Decision

For each significant change, the available evidence should identify:

* The related requirement, issue, or implementation task.
* The branch used for development.
* The commit containing the change.
* The pull request submitted for review.
* The review outcome and any requested corrections.
* The results of relevant automated checks.
* The final integration decision.

Not every documentation update requires a separate GitHub issue. However, significant implementation work should be traceable to its purpose, requirements, and acceptance criteria.

Traceability Record Template

Item	Reference / Evidence
Requirement or Issue	Add GitHub issue link or identifier.
Task	Add task description or reference.
Branch	Add branch name or link.
Commit	Add commit link or hash.
Pull Request	Add pull request link.
Review Outcome	Record approval, requested changes, or other review outcome.
CI/CD Result	Link to relevant workflow run or automated checks.
Final Decision	Record whether the change was merged, not merged, or deferred.
Evidence Notes	Summarize the outcome, validation performed, and remaining limitations.

## 5. Pull Request Review Expectations

Pull requests should provide sufficient information for reviewers to understand, evaluate, and verify proposed changes.

A meaningful pull request should include:

* A clear explanation of the proposed change and its purpose.
* Links to related GitHub issues, requirements, or implementation tasks where applicable.
* Relevant implementation or documentation changes.
* Tests performed and their results.
* Known risks, limitations, or deferred work.
* Disclosure of AI assistance when required by course or team guidelines.
* Reviewer feedback and evidence that requested changes were addressed.
* A documented merge or no-merge decision.

Approval and successful automated checks should apply to the version that is ultimately merged. If significant changes are made after approval, the relevant review and automated checks should be repeated before integration.

## 6. CI/CD and Test Validation

Automated checks should provide visible evidence that submitted changes were evaluated against the project’s validation requirements.

The team should document:

* The workflow or automated process executed.
* The checks and tests performed.
* The results of each relevant check.
* Any failures, warnings, or corrective actions.
* Whether the final changes passed validation.

Testing documentation should distinguish between:

1. Planned Tests: Tests identified in the test plan but not yet executed.
2. Executed Tests: Tests that have been performed, regardless of outcome.
3. Passed Tests: Tests that completed successfully and met their expected results.
4. Failed Tests: Tests that identified an error, defect, or unmet expectation.

Where automated checks or runtime evidence are unavailable, the limitation must be documented rather than represented as successful validation.

## 7. Architecture Review and Deferred Work

Architecture and implementation findings should be documented with enough information to explain the original concern, the action taken, and the final disposition.

Finding or Decision	Action Taken	Supporting Evidence	Status
Database	Document the selected approach, rationale, alternatives, and any implementation changes.	Pending – Issue Not Yet Linked	Pending

For each additional finding or decision, record:

* The issue or architectural concern.
* The action taken or proposed resolution.
* The supporting pull request, commit, issue, or decision record.
* The current status.
* Any remaining risks or dependencies.

Deferred items must include the reason for deferral, potential impact, and any follow-up issue or condition required for reconsideration.

## 8. Known Limitations and Risks

The review package should identify known limitations and potential risks affecting the reliability, security, usability, and maintainability of CampusConnect.

The following areas should be evaluated:

* Role-Based Access Control: Verify that students cannot access requests belonging to other students and that staff access is appropriately restricted.
* Input Validation: Verify that submitted request information is validated before being processed or stored.
* Request Status and History: Confirm that status changes are recorded consistently and that request history accurately reflects updates.
* Internal Staff Notes: Verify that internal notes are restricted to authorized staff members and are not exposed to students.
* Error Handling and Logging: Evaluate how the application handles failures during request submission, updates, and other operations.
* Notification Delivery: Review notification delivery, failure handling, and communication reliability.
* Automated Testing: Identify incomplete test coverage, missing integration tests, or unavailable automated validation.

These items represent areas requiring evaluation and are not claims that defects currently exist.

Only confirmed defects should be recorded as actual findings. Each confirmed issue should be linked to its corresponding GitHub issue, pull request, or supporting evidence.

Unverified concerns should remain documented as risks or pending review items until sufficient evidence is available.

## 9. Evidence Completion Checklist

The following checklist identifies the remaining activities required to prepare the evidence package for submission.

* [ ]	Verify that repository links and document paths are accurate.
* [ ]	Confirm that architecture and API contract documentation reflect the current implementation.
* [ ]	Complete or link the Changed-File Index.
* [ ]	Link relevant GitHub issues, branches, commits, and pull requests.
* [ ]	Identify at least one meaningful reviewed pull request.
* [ ]	Record reviewer feedback and the final merge or no-merge decision.
* [ ]	Link the CI/CD workflow and actual execution results.
* [ ]	Link the test plan and available test results.
* [ ]	Add runtime, logging, or troubleshooting evidence where available.
* [ ]	Document AI assistance and human validation where required.
* [ ]	Record unresolved risks, deferred work, and architecture review actions.
* [ ]	Verify that every completion claim is supported by authoritative evidence.
* [ ]	Update this document to reflect the final state of the project before submission.

## 10. Review and Maintenance

The primary owner is responsible for maintaining this evidence package and ensuring that repository references, documentation paths, and supporting evidence remain accurate.

The backup owner assists with evidence collection, documentation review, and verification of repository links.

This document should be updated whenever significant implementation changes, review decisions, automated checks, or testing results affect the available engineering evidence.

The final submission must clearly distinguish between:

* Completed Evidence: Documentation or records that exist and have been verified.
* In-Progress Evidence: Work that has started but is not yet complete.
* Pending Evidence: Evidence that has not yet been provided or linked.
* Deferred Work: Activities intentionally postponed with a documented reason.
* Unresolved Findings: Issues or risks that still require investigation or corrective action.

The evidence package should provide an accurate and verifiable representation of CampusConnect’s engineering progress and demonstrate that the team’s construction, integration, testing, and review activities are supported by documented evidence.