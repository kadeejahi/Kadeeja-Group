# Test Evidence Tracker
## Purpose

This document tracks testing and verification evidence for CampusConnect throughout development.

It connects tests to project requirements, acceptance criteria, review findings, edge cases, and failure paths. The goal is to show what was tested, what results were observed, and where the supporting evidence can be found.

For the team's overall testing approach, see [Test Plan](../docs/testing/test-plan.md).

## Expectations & Instructions

- Record evidence for tests and verification activities as they are completed.
- Connect each test to a documented requirement, API contract, or review finding.
- Include both successful behavior and relevant failure or edge cases.
- Link to actual test files, GitHub Actions runs, PRs, logs, or other verification results.
- Record the execution date and relevant commit or PR when results are available.
- Do not mark a test as passed without supporting execution evidence.
- Update existing entries as work progresses rather than duplicating them.
- If testing is blocked or deferred, document why and identify the necessary follow-up.

### Status Definitions

- **Not Verified:** A test is planned or identified, but execution evidence has not been confirmed.
- **Passed:** The test was executed and produced the expected result.
- **Failed:** The test was executed and did not produce the expected result.
- **Blocked:** The test could not be executed because a prerequisite was unavailable.
- **Deferred:** Testing has been postponed with a documented reason and follow-up.

---
## Requirements-to-Test Coverage
These entries identify the testing evidence needed. They do not represent completed test results, and are based on the project's documented requirements and acceptance criteria.

| ID | Requirement | Test Scenario | Expected Result | Status |
|---|---|---|---|---|
| TEST-01 | REQ-001 | Submit a request with all required information | Request is created and associated with the submitting student | Not Verified |
| TEST-02 | REQ-001 | Submit a request with missing required information | Submission is rejected with appropriate validation feedback | Not Verified |
| TEST-03 | REQ-002 | Student retrieves their own submitted requests | Student can view their requests and current statuses | Not Verified |
| TEST-04 | REQ-002 | Student attempts to retrieve another student's request | Access is denied and restricted information is not exposed | Not Verified |
| TEST-05 | REQ-003 | Authorized reviewer retrieves submitted requests | Reviewer can access requests permitted by their role | Not Verified |
| TEST-06 | REQ-003 | Unauthorized user attempts reviewer-level access | Access is denied | Not Verified |
| TEST-07 | REQ-004 | Authorized reviewer updates request information or status | Changes are saved and associated with the correct request | Not Verified |
| TEST-08 | REQ-004 | Unauthorized or invalid request update is attempted | Update is rejected without making unintended changes | Not Verified |
| TEST-09 | REQ-005 | Authorized reviewer adds an update to a request | Update is saved and associated with the correct request | Not Verified |
| TEST-10 | REQ-005 | Reviewer attempts to submit an invalid update | Invalid input is handled according to the approved validation rules | Not Verified |
| TEST-11 | REQ-006 | Authorized reviewer records a request resolution | Resolution information is saved and associated with the request | Not Verified |
| TEST-12 | REQ-006 | Resolution information is retrieved through request history | Recorded resolution is available in the appropriate request history | Not Verified |
| TEST-13 | REQ-007 | Request information or status is changed | Required events are recorded in the correct request history | Not Verified |
| TEST-14 | REQ-007 | Unauthorized user attempts to view restricted history | Restricted history is not exposed | Not Verified |
| TEST-15 | REQ-008 | Student accesses permitted student functionality | Authorized action succeeds | Not Verified |
| TEST-16 | REQ-008 | Student attempts reviewer-only functionality | Action is rejected by backend authorization | Not Verified |

**Requirements Source:** [Requirements Document](../docs/requirements/requirements.md)

**API Contracts Source:** [API Contracts](../docs/architecture/api-contracts.md)

Additional scenarios should be added as implementation progresses or new testing needs are identified.

---
## Code Review and CI Findings

This section tracks verification activities resulting from technical reviews or identified testing concerns.

| ID | Source / Finding | Verification Required | Status | Evidence / Follow-Up |
|---|---|---|---|---|
| TEST-CI-01 | PR #41 — CI may succeed without executing tests | Verify that CI discovers and executes tests, reports results, and handles missing tests appropriately | Not Verified | [PR #41](https://github.com/kadeejahi/Kadeeja-Group/pull/41); see `docs/testing/ci-evidence.md` |

Review findings should remain open until the required verification evidence has been reviewed.

---

## Test Execution Records

Use this section to document completed test execution. A single entry may represent one test or a related group of automated tests.

### Execution Record Template

**Test ID(s):** TEST-XX
- **Related Requirement / Finding:** REQ-XXX or PR reference
- **Test File / Location:** [Link]
- **Execution Date:** [Date]
- **Commit / PR:** [Link or SHA]
- **Environment / Preconditions:** [Relevant setup and test data]
- **Command / Steps:** [Exact execution command or reproducible steps]
- **Expected Result:** [What should happen]
- **Actual Result:** [What happened]
- **Outcome:** Passed / Failed / Blocked
- **Supporting Evidence:** [CI run, logs, report, or other evidence]
- **Follow-Up:** [Required action, or None]
---

## Review History

| Date | Assignment / Cycle | Team Member | Update |
|---|---|---|---|
| 2026-10-29 | A4 / Cycle 1 | Camille | Established requirements-to-test coverage and initial CI review finding. |
