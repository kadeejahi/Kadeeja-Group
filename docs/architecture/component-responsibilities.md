## Component Responsibilities
## Purpose
Document the responsibilities, boundaries, and interactions of the major components within CampusConnect. This document establishes which components handle user interactions, application logic, authorization, request workflows, communication, notifications, and persistent data storage.
The purpose is to provide a shared engineering reference for implementation, integration, testing, and maintenance. Component responsibilities should remain consistent with the system architecture, API contracts, and approved architecture decisions.
## Component Responsibilities
1. Presentation Layer
Responsibility: Provide the interface through which Students and Support Reviewers interact with CampusConnect.
Engineering responsibilities:
* Display request submission forms and request information.
* Allow students to view their own requests and relevant updates.
* Provide authorized reviewers with request-management interfaces.
* Display validation errors and operation results.
* Send user actions to the backend through the defined application interfaces.
Boundary: The presentation layer must not directly access the database or serve as the sole enforcement point for authorization.
Related evidence: Architecture diagram; API contracts; request submission requirements.
2. API / Application Layer
Responsibility: Receive application requests, validate inputs, coordinate processing, and return responses.
Engineering responsibilities:
* Validate incoming request data.
* Coordinate authentication and authorization checks.
* Route operations to the appropriate service components.
* Return consistent success and error responses.
* Follow the interfaces documented in the API contracts.
Boundary: Business rules and access restrictions must not be bypassed when processing application requests.
Related evidence: API contracts; authentication and authorization requirements; API integration tests.
3. Authentication and Authorization
Responsibility: Verify user identity through the configured authentication mechanism and enforce role-based access restrictions.
Engineering responsibilities:
* Distinguish Students from Support Reviewers.
* Restrict students to their own requests and permitted information.
* Restrict reviewer operations to authorized users.
* Prevent unauthorized access to internal notes and protected information.
* Reject unauthorized operations at the backend.
Boundary: Authorization must not depend solely on user-interface restrictions or client-provided role information.
Related evidence: Requirements documentation; API contracts; authorization tests.
4. Request Management Service
Responsibility: Implement the core operations for creating, retrieving, and updating student support requests.
Engineering responsibilities:
* Create requests and associate them with their submitting students.
* Manage request details, categories, and assignments.
* Retrieve requests according to applicable access restrictions.
* Coordinate request updates with the workflow and data-access components.
* Enforce the agreed request-management rules.
Boundary: Request operations must preserve request ownership, permissions, and workflow restrictions.
Related evidence: Request submission requirements; request management requirements; API contracts; request service tests.
5. Request Workflow and Status
Responsibility: Enforce the permitted lifecycle and status transitions of support requests.
Engineering responsibilities:
* Define and validate permitted status transitions.
* Reject invalid workflow operations.
* Enforce the team’s rule that students cannot reopen old or closed requests.
* Coordinate relevant status changes with request-history recording.
* Ensure updates are persisted consistently.
Boundary: A user’s permission to manage a request does not automatically make every status transition valid.
Related evidence: Workflow requirements; architecture decision records; status-transition tests.
6. Communication and Comments
Responsibility: Manage comments and communication updates associated with support requests.
Engineering responsibilities:
* Associate comments with the relevant request and author.
* Record message timestamps.
* Retrieve communications for authorized users.
* Protect internal notes and restricted information.
* Validate required message content.
Boundary: Users must not access or modify communications belonging to requests they are not authorized to access.
Related evidence: Communication requirements; API contracts; comment and access-control tests.
7. Request History and Audit
Responsibility: Maintain a record of relevant events and changes to support requests.
Engineering responsibilities:
* Record request creation and relevant status or assignment changes.
* Associate history records with the affected request and, when available, the responsible actor.
* Record event timestamps and relevant details.
* Support authorized history retrieval.
* Maintain consistency between workflow changes and history records.
Boundary: History records must accurately represent events that occurred and must not replace the current request state.
Related evidence: Request-history requirements; workflow design; transaction and history tests.
8. Notification Component
Responsibility: Create and manage notifications for relevant request events according to the agreed requirements.
Engineering responsibilities:
* Identify events that require notifications.
* Determine the intended recipients.
* Record notification information and delivery status where required.
* Protect sensitive information in notification content.
* Coordinate with the request workflow and communication components.
Boundary: Creating a notification record does not necessarily mean a notification has been delivered. The delivery mechanism must be confirmed and tested.
Related evidence: Notification requirements; API contracts; notification tests, when implemented.
9. Data Access Layer
Responsibility: Provide controlled database access for application services.
Engineering responsibilities:
* Create, retrieve, update, and query application records.
* Support database transactions for related operations.
* Handle database errors appropriately.
* Use parameterized queries or an appropriate data-access library.
* Support schema migrations and database integration tests.
Boundary: Database access must not bypass application authorization or workflow validation.
Related evidence: Database architecture decision record; database schema; data-access implementation; integration tests.
10. PostgreSQL Database
Responsibility: Persist CampusConnect data and enforce database-level integrity.
Engineering responsibilities:
* Store users, support requests, categories, assignments, comments, history, and notifications.
* Maintain relationships through primary and foreign keys.
* Enforce applicable database constraints.
* Support transactions and persistent storage.
* Support appropriate backup and recovery procedures once configured.
Boundary: PostgreSQL provides data storage and integrity mechanisms; it does not independently implement the application’s full authorization or workflow rules.
Related evidence: PostgreSQL selection ADR; database schema; migration files; database integration tests.
## Cross-Component Rules
* Authorization for protected operations must be enforced by the backend.
* Students may access only their own requests and permitted associated information.
* Students cannot reopen old or closed requests, according to the team’s agreed rule.
* Request status changes and corresponding history records must remain consistent.
* Components must use agreed interfaces and must not bypass defined responsibility boundaries.
* Database constraints and transaction handling must protect data integrity.
* Documentation must be updated when component responsibilities or interfaces change.
Ownership and Maintenance
The Architecture Lead maintains this document and ensures consistency with the architecture diagram, API contracts, and architecture decision records.
Implementation ownership must be assigned through the team’s task tracker or other agreed ownership documentation. Component owners are responsible for reporting changes that affect the documented responsibilities or interfaces.
Open Questions
The team must confirm:
* The authentication mechanism and implementation approach.
* The frontend technology and application interface.
* The final request statuses and permitted transitions.
* The notification delivery mechanism required for Cycle 1.
* The database access library and schema migration approach.
* The implementation ownership of each component.
## Related Evidence
* Architecture overview: docs/architecture/architecture.md
* API contracts: docs/architecture/api-contracts.md
* PostgreSQL selection ADR: https://github.com/kadeejahi/Kadeeja-Group/pull/25
* Requirements and acceptance criteria: https://github.com/kadeejahi/Kadeeja-Group/blob/main/docs/requirements/requirements.md 
* https://github.com/kadeejahi/Kadeeja-Group/blob/main/docs/requirements/acceptance-criteria.md
* Architecture diagram: https://github.com/kadeejahi/Kadeeja-Group/pull/35
* Tests and implementation evidence: https://github.com/kadeejahi/Kadeeja-Group/pull/37
Evidence status: This document defines proposed component responsibilities. Implementation and testing evidence must be linked when available; proposed responsibilities do not establish that a component has already been implemented or verified.
