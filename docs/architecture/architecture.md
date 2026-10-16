## Architecture

## Project Information
Item	Team Response
Project name	CampusConnect
Team number/team name	The Crazy 6
Repository URL	https://github.com/kadeejahi/Kadeeja-Group
Architecture owner	Dathal
Backup owner	Kadeeja
Last updated	2026-10-15
Cycle 1 / current release focus	Student support request submission, request management, status tracking, communication and updates, role-based access, and request history/visibility

## System Overview
CampusConnect is a Python-based student support request and workflow management system designed to centralize how student support needs are submitted, managed, tracked, and resolved. Students can submit support requests, view their own requests and current statuses, and receive progress updates. Authorized support reviewers can access submitted requests, assign work, update statuses, communicate progress, add internal notes, and record resolutions. The system replaces fragmented communication through emails, shared documents, and verbal follow-ups with a structured workflow.
For Cycle 1, the architecture focuses on the core request-management workflow, role-based access control, communication, and request history. The system uses a layered architecture to separate presentation, application services, business/workflow logic, and data persistence. PostgreSQL is the proposed database and remains subject to the team’s documented architecture decision and approval process.
The architecture is intended to make component responsibilities, interfaces, security boundaries, dependencies, and validation requirements clear before implementation expands.
3. Users, Roles, and Permissions
User / Role	Primary Goals	Allowed Actions	Limitations / Approvals
Student	Submit and track support requests	Create and submit requests; view their own requests and statuses; add permitted comments or clarifications; view student-visible progress updates	Cannot view other students’ requests, perform reviewer actions, approve or close their own requests, or reopen old requests
Support Reviewer	Review, manage, and resolve requests	Access authorized requests; update request information and status; assign requests; add student-visible updates; add internal notes; record resolutions	Must follow assigned permissions; internal notes must remain hidden from students; reopening permissions must follow the team’s confirmed workflow policy
Development Team	Build, test, and maintain CampusConnect	Implement approved requirements; review code; maintain documentation; test architecture and security boundaries	Must follow repository workflow, review requirements, and applicable AI-use disclosure rules
Team Lead / Authorized Approver	Coordinate decisions and engineering governance	Review significant decisions, approve changes where required, and coordinate phase-gate readiness	Approval authority must follow the team’s agreed responsibilities and course requirements

## Authorization Rules
* Users must be authenticated before accessing protected application functionality.
* Students may access only requests associated with their own accounts.
* Support reviewers may access and manage requests only within their authorized permissions.
* Student-facing responses must not expose internal reviewer notes.
* The backend must enforce authorization and workflow rules; the user interface alone is not a security boundary.
* Students cannot reopen resolved requests.
* Reviewer reopening permissions and any additional approval requirements must be confirmed and documented before implementation.

## Architecture Diagram
The CampusConnect architecture separates user interfaces, API/controllers, application services, business/workflow logic, data access, and persistent storage. Authentication, authorization, validation, logging, configuration, and error handling apply across the relevant components.
The primary request flow is:
Student or Support Reviewer → User Interface → API / Controllers → Application Services → Business / Workflow Logic → Repositories / Data Access → Database
Responses return through the application layers to the appropriate user interface.
The architecture diagram should identify the major components, their responsibilities, communication paths, database dependency, authorization boundaries, and relevant logging or audit evidence.
Diagram location: /docs/architecture/architecture-diagram.png
If the diagram is stored elsewhere, update the path to match the actual repository location.

## Component Responsibility Map
Component	Owns / Responsible For	Must Not Own	Inputs / Outputs	Evidence
Student UI	Collecting request information and displaying student-visible requests, statuses, and updates	Backend authorization decisions or business rules	Form data; request and status views	Link to relevant issue, PR, or test
Reviewer UI	Displaying authorized requests and providing reviewer-management actions	Direct database writes or bypassing backend permissions	Reviewer actions; request details and updates	Link to relevant issue, PR, or test
API / Controllers	Receiving API requests, validating input format, checking access through authorization services, and routing operations	Persistent data ownership or bypassing workflow rules	API requests; application responses	Link to relevant issue, PR, or test
Authentication / Authorization	Verifying identity and enforcing role, request-ownership, and permission checks	Owning request-state transition rules	User identity and requested action; authorization result	Link to security tests or review
Application Services	Coordinating request submission, assignments, status updates, comments, and resolution workflows	Direct UI rendering or bypassing business rules	Validated actions; operation results	Link to relevant issue, PR, or test
Business / Workflow Logic	Enforcing request-management rules, permitted status transitions, and workflow restrictions	UI rendering or direct database connection management	Requested workflow action; permitted state change or validation error	Link to workflow tests
Repositories / Data Access	Providing interfaces for reading and writing application records	Owning user-facing authorization policy or presentation behavior	Data queries; stored or retrieved records	Link to relevant issue, PR, or test
PostgreSQL	Persisting application records and supporting relational data operations	Replacing application-level authorization and workflow enforcement	Database queries and records	Link to ADR-001 and database tests
Logging / Error Handling	Recording relevant application events and errors while avoiding unnecessary sensitive data	Storing secrets or exposing private request contents through logs	Operational events and error information	Link to logging requirements and tests
Evidence links must be added when the corresponding issues, pull requests, tests, or reviews exist. Planned evidence must not be represented as completed evidence.

## Interfaces, APIs, and Tool Boundaries
CampusConnect components communicate through defined interfaces. The presentation layer sends user actions to the API/controllers. Application services coordinate the requested operations, business/workflow logic enforces permitted behavior, and repositories provide access to persistent data.
Detailed API contracts should be maintained separately in /docs/architecture/api-contracts.md.
Interface / Dependency	Producer	Consumer	Contract / Behavior	Failure / Security Notes
Request submission API	Student UI	API / Application Services	Accepts required request details and initiates request creation	Reject invalid input; verify authentication and student identity
Request retrieval API	Student or Reviewer UI	API / Application Services	Returns requests the authenticated user is permitted to access	Deny unauthorized access; students must not retrieve other students’ requests
Request management API	Reviewer UI	API / Application Services	Supports authorized updates, assignments, status changes, and resolution	Enforce reviewer permissions and workflow rules
Request status interface	Application Services	Student UI / Reviewer UI	Returns the current status of an authorized request	Verify request ownership or reviewer authorization
Comments / Updates interface	Student or Reviewer UI	API / Application Services	Creates and retrieves permitted comments and progress updates	Enforce comment permissions and visibility rules
Internal Notes interface	Reviewer UI	API / Application Services	Creates and retrieves internal reviewer notes	Restrict access to authorized reviewers; never expose notes in student-facing responses
Data persistence interface	Application / Repository Layer	PostgreSQL	Stores and retrieves users, requests, assignments, comments, notes, notifications, and history	Validate data, protect credentials, and handle database failures
Authentication / Authorization	Authentication and authorization component	Protected application services	Determines whether a user may perform a requested operation	Deny unauthorized actions by default
Logging / Observability	Application components	Authorized development or operational reviewers	Records relevant events, failures, and diagnostic information	Avoid sensitive data exposure; restrict log access

## Dependency Boundaries
* User interfaces communicate with the backend through defined application interfaces.
* Application services coordinate use cases and call the appropriate workflow and data-access components.
* Business/workflow rules determine whether a requested operation is valid.
* Repository interfaces isolate application logic from database-specific operations.
* The database must not be accessed directly by user-interface components.
* Authorization checks must be enforced on protected backend operations.
* External integrations must be documented and approved before they are introduced into the system.

## Failure Behavior
* Invalid request data must be rejected with an appropriate response.
* Unauthorized operations must be denied.
* Database or service failures must not be reported as successful operations.
* Errors returned to users must not disclose secrets or unnecessary internal details.
* Relevant operational failures should be logged without exposing sensitive student information.
* Retry and recovery behavior must be defined for operations where failure could create duplicate records or inconsistent workflow state.
Data and Context Ownership
CampusConnect uses a centralized persistence layer. Application data is accessed through the application and data-access layers rather than through direct database access from the user interface.
Data / Context	Authoritative Source	Used By	Purpose	Access / Protection
User information	Application database	Authentication, Authorization, Application Services	Identifies students and support reviewers	Restrict access to authorized components and users
Support requests	Application database	Student UI, Reviewer UI, Application Services	Stores request details and current state	Students can access only their own requests; authorized reviewers access permitted requests
Assignment information	Application database	Reviewer UI, Workflow Logic	Tracks reviewer assignments	Restricted to authorized reviewers and relevant services
Student-visible comments and updates	Application database	Student UI, Reviewer UI, Application Services	Communicates progress and clarifications	Apply request ownership, role, and visibility rules
Internal reviewer notes	Application database	Reviewer UI, Workflow Logic	Records information for internal reviewer use	Hidden from students and restricted to authorized reviewers
Request history / status changes	Application database	Workflow Logic, Reviewer UI	Supports traceability of request activity	Protect records and restrict access by role
Notification records	Application database, if implemented	Application Services, Notification Component	Tracks notifications associated with request activity	Apply appropriate access and data-protection controls
Request status	Application database, governed by Workflow Logic	Student UI, Reviewer UI	Represents the current stage of a request	Status changes must follow authorized workflow rules
AI prompts and outputs, if applicable	Approved AI-use records or other explicitly designated source	Development Team or approved AI-assisted workflow	Supports documented AI-assisted engineering or approved runtime functionality	Do not submit real student private data or secrets to unapproved tools
Operational logs	Approved logging mechanism	Authorized development or operational reviewers	Supports debugging, monitoring, and incident investigation	Minimize sensitive data and restrict access

## Data Protection Principles
* Use only the data necessary for the operation being performed.
* Do not use real student records in AI prompts or sample data unless explicitly authorized under applicable requirements.
* Separate student-visible updates from internal reviewer notes.
* Ensure database credentials and other secrets are not committed to the repository.
* Define appropriate retention and deletion requirements as the system’s governance requirements become clearer.
* Record important workflow changes where required for request history and engineering traceability.

## AI / Tool Boundary and Governance Model
AI-assisted development must remain reviewable and accountable. AI-generated code, documentation, tests, and architecture suggestions do not replace human responsibility for engineering decisions.
CampusConnect does not assume a runtime AI feature unless one is explicitly approved and documented.
Boundary	Team Position	Human Approval / Validation	Evidence Location
Read	AI tools may be used with appropriate development context, but real student private data, credentials, and secrets must not be supplied to unapproved tools	The team member verifies the input is appropriate before submitting it	/docs/ai/ai-use-log.md
Infer	AI may assist with drafting, code suggestions, test ideas, or design analysis when permitted	A team member verifies the output against requirements, constraints, and system behavior	AI-use log and relevant PR review
Change	AI-generated suggestions do not automatically approve or merge code or authorize application-state changes	Code changes follow the team’s review, testing, and approval process; runtime operations follow backend authorization rules	GitHub PR and test evidence
Log	Record AI assistance and verification according to the course’s disclosure requirements	Team members ensure disclosures are accurate and sufficiently detailed	/docs/ai/ai-use-log.md
Recover	If an AI development tool is unavailable, development can continue manually where practical. Runtime AI recovery is not applicable unless a runtime AI feature is approved	The team documents and reviews fallback behavior when a tool becomes an operational dependency	Relevant architecture or operations documentation

## AI Accountability Requirements
* Identify material AI assistance in accordance with course and team requirements.
* Review AI-generated code and documentation before accepting them.
* Validate generated code through relevant tests and human review.
* Do not treat AI-generated explanations or recommendations as proof that a design is correct.
* Do not allow an AI suggestion to bypass authorization, workflow validation, or the team’s approval process.
* Document any approved runtime AI feature, including its inputs, permitted outputs, human oversight, failure behavior, and security boundaries.

## Testing and Review Implications
Architecture claims must be supported by appropriate validation evidence. Test cases, pull requests, review records, and other evidence should be linked as they become available.
Architecture Claim	What Must Be Tested or Reviewed	Owner	Evidence Link
Students can submit support requests	Valid submissions succeed; missing or invalid required fields are rejected	Backend / Testing owner	[Add issue, PR, or test link]
Students can view their own requests	Authorized students can retrieve their requests and statuses	Backend / Testing owner	[Add issue, PR, or test link]
Students cannot view other students’ requests	Cross-user access attempts are denied	Security / Backend owner	[Add security test link]
Students cannot perform reviewer actions	Student attempts to use reviewer-only operations are denied	Backend / Testing owner	[Add test link]
Internal notes remain private	Student-facing responses cannot retrieve internal reviewer notes	Security / Backend owner	[Add test link]
Workflow state changes are controlled	Invalid or unauthorized status transitions are rejected	Workflow / Testing owner	[Add workflow test link]
Students cannot reopen resolved requests	Student attempts to reopen old requests are denied	Workflow / Testing owner	[Add test link]
Reviewer permissions are enforced	Reviewers can perform permitted actions but cannot exceed their authorization	Backend / Testing owner	[Add test link]
Comments and updates respect permissions	Users can only create and view comments they are authorized to access	Backend / Testing owner	[Add test link]
Request history supports traceability	Required status changes and relevant activity are recorded and retrievable	Backend / Testing owner	[Add test link]
Database persistence works correctly	Records are stored and retrieved consistently; database failures are handled appropriately	Data / Testing owner	[Add integration-test link]
AI-assisted engineering remains accountable	Material AI-assisted work is disclosed and relevant changes are reviewed and tested	Contributors / Reviewers	[Add AI-use log and PR link]
Operational failures are diagnosable	Relevant errors can be investigated without exposing unnecessary sensitive data	Backend / Testing owner	[Add test or review link]
Testing owners should be assigned to actual teammates. A test should be marked complete only after the required behavior has been verified and evidence is available.

## Architecture Decision Record (ADR) Index
Significant decisions affecting system structure, persistence, workflow, security, governance, and operational behavior should be documented in individual ADR files.
ADR ID	Decision Title	Status	Owner	File / Evidence Link
ADR-001	Database / Persistence Approach	Proposed until team approval is confirmed	Dathal / Decision owners	/docs/architecture/adr/ADR-001-database-selection.md
ADR-002	AI Integration Approach	Proposed if an AI integration is under consideration	[Assign owner]	/docs/architecture/adr/ADR-002-ai-integration-approach.md
ADR-003	Request Workflow and Reopening Policy	Draft / Proposed until reviewed	[Assign owner]	/docs/architecture/adr/ADR-003-request-workflow-policy.md

## ADR Requirements
Each ADR should record:
* The decision context and problem being addressed.
* The proposed or approved decision.
* Alternatives considered.
* Reasons for selecting the chosen approach.
* Benefits, drawbacks, and tradeoffs.
* Consequences for implementation, testing, security, and maintenance.
* Risks, deferred work, and unresolved questions.
* Decision owners, date, status, and relevant review or approval evidence.
The architecture overview summarizes decisions and links to their ADRs. Detailed decision reasoning belongs in the individual ADR files.

## Known Architecture Risks and Open Questions
The following are proposed risks and open questions that require team review. Update them as decisions are made and evidence becomes available.
ID	Risk / Question	Impact	Owner	Next Action
AR-001	PostgreSQL approval status may not be finalized	Medium	Architecture owner	Confirm team approval and update ADR-001
AR-002	Incomplete authorization could expose student request information	High	Backend / Security owner	Define authorization rules and validate them with tests
AR-003	Internal reviewer notes could be exposed through student-facing responses	High	Backend owner	Enforce visibility boundaries and add tests
AR-004	Request history requirements may expand during implementation	Medium	Architecture owner	Define the Cycle 1 history requirements and record deferred work
AR-005	API contracts may not fully define validation and failure responses	Medium	API owner	Complete and review /docs/architecture/api-contracts.md
AR-006	Reviewer reopening permissions have not been confirmed in this document	Medium	Team lead / Architecture owner	Confirm the policy and update the workflow rules, ADR, and tests
AR-007	Notification behavior and delivery requirements may be incomplete	Medium	Assigned feature owner	Confirm Cycle 1 scope and document delivery and failure behavior
AR-008	AI-assisted engineering evidence may be incomplete	Medium	Contributors / Architecture owner	Maintain the AI-use log and verify relevant human review
AR-009	Database connection or service failures may interrupt request processing	Medium	Backend owner	Define error handling and test failure scenarios
AR-010	Architecture documentation may become inconsistent with implementation	Medium	Architecture owner / Contributors	Review documentation during relevant pull requests and architecture reviews

## Forecast Problems

This section identifies potential technical, security, workflow, and operational problems that CampusConnect may encounter during development and use. These problems are forecasts rather than confirmed defects. The team will use these forecasts to guide architecture decisions, implementation priorities, and testing.

ID | Forecast Problem | Potential Impact | Prevention / Mitigation | 
FP-001	Unauthorized access to student support requests | Exposure of private student information | Enforce authentication, request ownership checks, and role-based authorization on the backend. |
FP-002	Students attempt to reopen resolved requests | Violations of the agreed request workflow	Prevent students from reopening resolved requests through server-side workflow rules. |
FP-003	Duplicate support requests are submitted | Duplicate records and additional reviewer workload | Validate submissions and implement appropriate duplicate-processing protections. | 
FP-004	Invalid or incomplete request information is submitted | Inaccurate records and processing errors | Validate required fields and input formats on both the client and server.|
FP-005	Database or network failures | interrupt request processing |	Requests may fail to save or retrieve correctly | Implement error handling, transaction management, appropriate backups, and safe recovery procedures. |
FP-006	Concurrent reviewer updates overwrite newer information | Lost updates and inconsistent request history | Evaluate transaction handling or optimistic locking and test concurrent updates. |
FP-007	Internal reviewer notes become visible to students	 | Exposure of confidential internal information	Separate internal notes from student-visible comments and enforce server-side access controls.|
FP-008	Request lists and dashboards become slow as data grows	Reduced usability and delayed request processing | Evaluate database indexing, pagination, and performance testing. |
FP-009	Invalid status transitions occur | Requests enter incorrect or unauthorized workflow states | Define permitted state transitions and enforce them in backend business logic. |
FP-010	Errors are not logged or communicated appropriately | Difficult troubleshooting and confusion for users | Log relevant failures safely and return clear error responses without exposing sensitive information. |

- Validation and Review - 

The development team should validate these forecasts through code reviews, automated tests, integration tests, and performance testing where appropriate. Mitigations must be verified before they are considered complete.

The architecture owner will coordinate updates to this section as requirements, architecture decisions, and implementation evidence evolve. Forecasts should be revised when risks are addressed, new problems are identified, or the team’s understanding changes.

## Deferred Work and Operational Constraints
* Detailed database schema and migration strategy must be documented as implementation progresses.
* API contracts must be updated when interfaces or expected behaviors change.
* Deployment configuration, secret management, backup and recovery, and monitoring details should be documented as required by the actual deployment scope.
* External services must not become dependencies without appropriate review and documentation.
* Risks must be revisited when requirements, architecture boundaries, or implementation evidence change.

## Maintenance and Ownership
The architecture owner is responsible for coordinating updates to this document as decisions are approved and the implementation evolves. Contributors should update relevant architecture evidence when changes affect component responsibilities, interfaces, dependencies, workflows, data handling, security assumptions, AI/tool boundaries, or operational behavior.
Architecture documentation must describe the actual agreed design. Proposed decisions, unresolved questions, and incomplete validation must remain clearly identified until the appropriate review or approval takes place.
