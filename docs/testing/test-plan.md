# Test Plan

## Purpose

This document defines the testing approach for CampusConnect. It establishes the scope of testing, test levels and types, test environment, responsibilities, entry and exit criteria, and evidence required to verify that the application meets its requirements.

The test plan supports consistent verification of functional behavior, data integrity, access control, request workflow rules, and integration between application components.

This document must remain consistent with the requirements, architecture, API contracts, and implemented functionality. Test results must reflect actual execution and must not be reported as passing until supported by evidence.

## Scope

In Scope -

Testing will cover the following CampusConnect functionality:

1. Student Support Request Submission

* Verify that students can submit valid support requests.
* Verify that required fields are validated.
* Verify that invalid or incomplete submissions are rejected appropriately.
* Verify that successfully submitted requests are associated with the correct student.

2. Request Retrieval and Visibility

* Verify that students can view their own requests.
* Verify that students cannot access another student’s restricted request information.
* Verify that authorized Support Reviewers can access requests permitted by their role.
* Verify that unauthorized access attempts are rejected.

3. Request Management and Workflow

* Verify that authorized reviewers can perform permitted request-management operations.
* Verify that valid status transitions succeed.
* Verify that invalid status transitions are rejected.
* Verify that students cannot reopen old or closed requests.
* Verify that request status remains consistent after successful and unsuccessful operations.

4. Comments and Communication

* Verify that authorized users can create and retrieve permitted comments.
* Verify that comments are associated with the correct request and author.
* Verify that internal notes are not exposed to unauthorized users, if internal notes are implemented.
* Verify that invalid comment submissions are handled appropriately.

5. Request History

* Verify that required workflow events are recorded.
* Verify that history entries identify the relevant request and event details.
* Verify that failed operations do not create misleading history records.
* Verify that history information is available only to authorized users.

6. Notifications

* Verify notification creation and recipient selection for supported events.
* Verify notification status tracking where required.
* Verify that notification content does not expose restricted information.
* Verify delivery behavior if an external delivery mechanism is implemented.

7. Database and Data Integrity

* Verify Python backend connectivity to PostgreSQL.
* Verify persistence and retrieval of application records.
* Verify relationships between users, requests, assignments, comments, history, and notifications.
* Verify applicable primary-key, foreign-key, and other database constraints.
* Verify transaction behavior when related operations succeed or fail.

8. API and Error Handling

* Verify API inputs, outputs, validation, and documented error responses.
* Verify authentication and authorization behavior for protected operations.
* Verify that unexpected failures do not expose sensitive implementation details.
* Verify consistency between the API implementation and the API contracts.

Out of Scope -

The following activities are excluded unless explicitly required by the assignment or approved by the team:

* Production-scale performance and load testing beyond the project’s stated requirements.
* Formal third-party penetration testing.
* Testing external notification providers that have not been integrated.
* Testing functionality that has not been included in the approved project scope.
* Production backup and disaster-recovery certification before the relevant infrastructure exists.

Excluded items may be added if project requirements or deployment constraints change.

## Test Levels and Types

1. Unit Testing

Purpose: Verify individual functions, methods, and components independently.

Planned coverage:

* Input validation and required fields.
* Request status-transition rules.
* Request ownership and permission-checking logic.
* Comment validation.
* Notification recipient-selection logic.
* Error handling in individual services.

Evidence: Unit-test files, test execution results, and recorded failures or defects.

2. Integration Testing

Purpose: Verify that related components interact correctly.

Planned coverage:

* Python backend connection to PostgreSQL.
* Service-to-data-access interactions.
* Request creation and retrieval through the application interface.
* Database transaction handling.
* Request updates and corresponding history records.
* API authentication and authorization integration.
* Notification creation following supported events.

Evidence: Integration-test files, database test results, and relevant execution logs.

3. System Testing

Purpose: Verify complete user workflows across the integrated application.

Planned scenarios:

* A student submits a valid request and views the submitted request.
* A student attempts to access another student’s request.
* A Support Reviewer retrieves and manages an authorized request.
* A reviewer performs a permitted status transition.
* A student attempts to reopen an old or closed request.
* A request update is recorded in the request history.
* A user submits invalid information and receives an appropriate response.

Evidence: Test-case results, reproducible execution steps, and relevant screenshots or logs where appropriate.

4. Regression Testing

Purpose: Verify that changes do not break previously working functionality.

Regression testing should cover the affected functionality whenever changes are made to:

* Authentication or authorization.
* Request ownership and visibility.
* Request status transitions.
* Database schemas or migrations.
* API contracts.
* Comments, history, or notifications.

Evidence: Regression-test results associated with the relevant code changes or pull requests.

5. Security Testing

Purpose: Verify that access restrictions and sensitive data protections are enforced.

Planned coverage:

* Students cannot access other students’ restricted requests.
* Unauthorized users cannot perform reviewer-only operations.
* Invalid or manipulated requests cannot bypass backend authorization.
* Internal notes and restricted data are not exposed to unauthorized users.
* Database credentials and other secrets are not committed to the repository.
* Invalid inputs are handled safely.

Evidence: Authorization test results, security-related test cases, and documented defects or resolutions.

6. Data Integrity Testing

Purpose: Verify that persisted data remains valid and consistent.

Planned coverage:

* Required values cannot be omitted where prohibited.
* Foreign keys prevent invalid references.
* Related records remain consistent after successful operations.
* Failed multi-step operations roll back where required.
* Request history reflects completed workflow events accurately.

Evidence: Database integration tests and relevant transaction or constraint test results.

## Test Environment

Application Environment

* Programming language: Python.
* Application interface: The API or application interface defined by the team.
* Database: PostgreSQL, as selected in the database ADR.
* Test framework: Python testing framework selected by the development team, such as pytest.
* Version control: CampusConnect GitHub repository.
* Test data: Controlled test accounts, requests, categories, assignments, comments, and history records.

The exact framework, database version, dependency versions, and configuration must be documented once confirmed by the team.

## Environment Requirements

* The required Python runtime and project dependencies are installed.
* PostgreSQL is available and configured for the test environment.
* Database credentials are provided through appropriate configuration or environment variables.
* Test data is isolated from any real student information.
* Automated tests can be executed repeatedly using documented instructions.
* Test execution results can be associated with the relevant code version.

Tests that modify data must use an appropriate test database or isolated test fixtures to avoid unintended changes to development or production data.

## Responsibilities

Architecture Lead — Dathal

* Maintain the test plan’s alignment with the documented architecture and API contracts.
* Identify architecture-level risks that require verification.
* Ensure critical boundaries, including authorization and request workflow restrictions, are covered.
* Link relevant test evidence to the architecture documentation.
* Coordinate clarification of unresolved architecture and testing questions.

Development Team - Dathal , Kadeeja

* Implement unit and integration tests for the components they develop.
* Verify that implementation behavior matches the agreed requirements and API contracts.
* Correct defects identified during testing.
* Maintain tests when application behavior changes.
* Provide evidence of test execution and relevant fixes.

## Test Ownership

The team must agree on who coordinates overall test execution, who reviews test results, and who verifies defect fixes. Individual test ownership should be recorded in the team’s task tracker or pull requests.

All team members are responsible for reporting defects and avoiding unsupported claims that functionality has been verified.

## Entry Criteria

Testing may begin when the applicable conditions are met:

* Relevant requirements and acceptance criteria are documented.
* The functionality under test has been implemented or a testable interface has been provided.
* Required application dependencies and test tools are available.
* The appropriate test environment is configured.
* Required database schema and test data are available for database-related tests.
* Test cases or verification steps are defined.
* The expected behavior is sufficiently clear to determine pass or fail.

If a prerequisite is unavailable, the affected test must be identified as blocked or not yet executable rather than recorded as passed.

## Exit Criteria

A test cycle may be considered complete when:

* All planned tests for the applicable scope have been executed or explicitly accounted for.
* Results are recorded as passed, failed, blocked, or not run.
* Critical functional requirements have been verified against their acceptance criteria.
* Authorization and request ownership restrictions have been tested.
* The rule preventing students from reopening old or closed requests has been verified.
* Relevant database integrity and transaction tests have been completed where applicable.
* No unresolved critical defects remain for the release scope, or any exceptions have been explicitly reviewed and accepted by the authorized team.
* Failed tests have associated defect records or documented explanations.
* Test evidence is linked from the repository or relevant project documentation.

A passing test cycle does not automatically establish that the entire application is production-ready. Release readiness must also consider deployment, security, and operational requirements.

Test Evidence

Test evidence must demonstrate what was tested, how it was executed, and what result was observed.

## Required Evidence

For each applicable test or test group, record:

* Test identifier and description.
* Related requirement or acceptance criterion.
* Preconditions and test data.
* Execution steps or automated test command.
* Expected result.
* Actual result.
* Outcome: passed, failed, blocked, or not run.
* Date of execution and relevant code version or commit.
* Link to the test implementation, execution report, defect, or pull request.

## Evidence Sources

Relevant evidence may include:

* Automated unit-test results.
* Database and API integration-test results.
* System workflow test results.
* Authorization and access-control tests.
* Regression-test results.
* Pull request checks and code-review records.
* Defect reports and verification results after fixes.

Evidence must be linked to actual repository files, reports, or recorded execution results. Planned tests must not be represented as completed tests.

## Evidence Status

Test evidence will be added as implementation and verification progress. Until test results are available, the corresponding items remain planned or unverified.

## Related Evidence

* Architecture documentation: docs/architecture/architecture.md
* API contracts: docs/architecture/api-contracts.md
* PostgreSQL database ADR: Link to the actual ADR file.
* Component responsibilities: Link to the actual component responsibilities document.
* Requirements and acceptance criteria: Link to the team’s requirements document.
* Automated tests: Link to the actual test directory once confirmed.
* Pull requests and CI results: Link to the relevant GitHub records.

## Maintenance

The Architecture Lead and designated test coordinator should review this document when requirements, architecture, API contracts, or testing practices change.

Developers must update test cases when affected functionality changes. New or modified behavior should be accompanied by appropriate verification evidence before being considered complete.

The test plan must reflect the current implementation and known limitations of CampusConnect.