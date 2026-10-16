ADR-001: Select PostgreSQL as the Primary Database

Status

Accepted — selected by the team, with 6 of 6 team members in agreement. Confirm any additional approval requirements under the team’s decision-making process.

Date

* Initial discussion: 2026-10-05
* Last updated: 2026-10-15
* Decision owner: Dathal
* Project: CampusConnect
* Related documentation: docs/architecture/architecture.md

## Context

CampusConnect is a Python-based student support request management system. The application allows students to submit support requests and track their status while authorized Support Reviewers manage requests, communicate updates, and maintain request history.

The system requires persistent storage for several related types of application data, including:

* Users: Student and Support Reviewer accounts, identities, and role information.
* Support requests: Request descriptions, categories, submission dates, current statuses, and ownership.
* Request categories: The types of student support services available through the application.
* Assignments: The relationship between support requests and the reviewers responsible for handling them.
* Comments and updates: Messages associated with a request, including the author and creation timestamp.
* Request history: Records of significant request events, such as status changes and assignment updates.
* Notifications: Information used to track relevant updates and notify users about changes to their requests.

These records are related. For example, a support request belongs to the student who submitted it, may be assigned to a reviewer, may contain multiple comments, and may have multiple historical status changes. The database must preserve these relationships and help prevent invalid or inconsistent data.

CampusConnect also requires data integrity during operations that modify multiple related records. For example, changing a request’s status and recording the corresponding history entry should be handled consistently so that the request and its history do not disagree.

The database must integrate with the project’s Python backend and be practical to configure, develop, and test during Cycle 1. The team also needs a solution that is free to use, supports relational data, and can accommodate future growth without requiring an unnecessary change in database technology.
The team therefore needs to select a database that balances implementation effort, reliability, maintainability, and the application’s expected data-management requirements.

## Engineering Problem

The team must select a primary database for CampusConnect that can reliably store, retrieve, and update related application records while supporting the request-management workflow.
The selected database must satisfy the following requirements:

1. Relational data support: Represent relationships among users, requests, categories, assignments, comments, history records, and notifications.
2. Data integrity: Support primary keys, foreign keys, uniqueness constraints, and other appropriate validation constraints.
3. Transactional consistency: Allow related database operations to succeed or fail together when necessary.
4. Python compatibility: Integrate with the project’s Python backend through an appropriate database driver or data-access library.
5. Cost: Be free to use and avoid requiring a paid database license.
6. Cycle 1 feasibility: Be practical for team members to configure, develop against, and test within the current development cycle.
7. Maintainability: Support understandable schema design, controlled database changes, and reliable testing.
8. Multi-user operation: Support concurrent application access and database operations without relying on a single-user workflow.
9. Future growth: Provide a reasonable path for expanding the application’s data and usage requirements.

The engineering decision is whether PostgreSQL, SQLite, or another suitable database provides the best balance of these requirements.

## Decision

The team selected PostgreSQL as the primary relational database for CampusConnect. PostgreSQL will serve as the persistent data store for users, 
support requests, request categories, assignments, comments, request history, and notifications.
The decision is based on PostgreSQL’s relational data capabilities, transactional support, data integrity features, compatibility with Python applications, 
and suitability for an application with multiple related entities and concurrent users.
PostgreSQL is free and open source, satisfying the team’s database licensing requirement. Its support for relational constraints and transactions will help 
the development team maintain consistent data as the request workflow is implemented.
The team will use the database through the Python backend rather than allowing application users to access the database directly. Database operations will 
be performed through the application’s approved data-access mechanisms, with authorization enforced by the backend.
During implementation, the team must define the database schema, configure the Python database connection, manage schema changes, and verify that the application can create, 
retrieve, and update records correctly.
Six of the six team members agreed with this selection. The documented agreement reflects the current decision and does not imply unanimous agreement.
The decision may be revisited if implementation evidence identifies a significant technical limitation, the deployment environment cannot support PostgreSQL, or project requirements change materially.

## Alternatives Considered

4.1 PostgreSQL — Selected

PostgreSQL is an open-source relational database management system that supports structured data, relationships, constraints, and transactions.

Advantages:

* Supports relational tables and relationships through primary keys and foreign keys.
* Supports transactions to keep related database operations consistent.
* Provides constraints that help prevent invalid or inconsistent records.
* Supports concurrent access by multiple application users.
* Integrates with Python through database drivers and compatible data-access libraries.
* Supports schema migrations and automated database testing.
* Provides a practical foundation for future expansion of CampusConnect.
* Has no database software licensing fee.

Disadvantages and trade-offs:

* Requires database configuration and a running database service in development and deployment environments.
* Requires connection configuration and secure handling of database credentials.
* Introduces setup and maintenance work, including schema migrations, backups, and deployment configuration.
* May require more initial setup than a lightweight, file-based database.
* The team must configure and test the database environment consistently across development and deployment.

Assessment:

PostgreSQL best fits the team’s requirements for relational integrity, transactions, concurrent access, and long-term maintainability. The additional setup effort is considered acceptable for the application’s intended workflow.

4.2 SQLite — Considered but Not Selected

SQLite is a free, embedded relational database that stores data in a local file and can be accessed from Python without running a separate database server.

Advantages:

* Free to use and easy to integrate with Python.
* Requires minimal setup for local development and basic testing.
* Supports relational tables, constraints, and transactions.
* Can be useful for prototypes, small applications, and automated tests.

Disadvantages and trade-offs:

* Database writes are more constrained by its locking and concurrency model than PostgreSQL’s.
* A file-based database may be less convenient when the application requires a shared database service across multiple application instances or deployment environments.
* Differences between SQLite and PostgreSQL can affect schema behavior, SQL features, and testing results.
* Using SQLite during development and PostgreSQL in production would require additional compatibility testing.

Assessment:

SQLite is technically capable of supporting many of CampusConnect’s basic data requirements. It was not selected because PostgreSQL 
provides a better fit for the team’s intended multi-user application architecture and reduces the need to switch database systems as the project evolves.
SQLite could be reconsidered if the scope changes to a small, single-instance application with minimal concurrent write activity.

4.3 Other Database Solutions

Other relational database systems could potentially satisfy the application’s data-management requirements. 
However, the team prioritized a free, relational solution with strong Python compatibility and manageable Cycle 1 implementation effort.

No additional database was selected for this decision. The team may evaluate other options if PostgreSQL fails to meet a documented requirement 
or a material technical constraint emerges.

## Consequences

Selecting PostgreSQL establishes the database technology that the CampusConnect backend and architecture documentation will target.

## Positive Consequences

* Relational integrity: Foreign keys and other constraints can help prevent invalid references between related records.
* Transactional consistency: Related operations can be grouped into transactions to avoid partial updates.
* Concurrent access: PostgreSQL supports multiple users and application operations accessing shared data.
* Python integration: The backend can connect through an appropriate PostgreSQL driver or data-access library.
* Maintainability: The team can use a defined relational schema and controlled schema migrations.
* Testing: Database integration tests can verify persistence, relationships, constraints, and transaction behavior.
* Future flexibility: The database provides capabilities suitable for expanding the application’s workflow and data requirements.
* Licensing: PostgreSQL avoids a paid database software license.

5.2 Negative Consequences and Costs

* Configuration effort: Team members must configure a database instance and its connection settings.
* Environment management: Development and deployment environments must use compatible database configurations.
* Security responsibilities: Credentials must be protected, database access restricted, and appropriate permissions configured.
* Operational maintenance: Deployment planning must address backups, restoration, database availability, and schema changes.
* Migration management: Changes to the schema must be coordinated with application code and existing data.
* Testing effort: The team must verify actual database behavior rather than relying only on mocked database operations.

5.3 Neutral Consequences

* The architecture and API contracts must describe database-backed behavior consistently.
* The team must agree on how tables, relationships, and database changes will be managed.
* Database access should be kept behind the backend’s data-access layer or equivalent approved component.
* The database choice does not itself implement application authorization, request workflow rules, notification delivery, or history tracking. Those behaviors must be designed and implemented separately.

## Implementation Implications

The following implementation work is required to make this decision effective:

1. Define the relational schema for users, requests, categories, assignments, comments, history, and notifications.
2. Establish primary keys, foreign keys, and appropriate constraints for related records.
3. Configure the Python backend to connect to PostgreSQL using an appropriate driver or data-access library.
4. Store connection credentials in suitable configuration or environment variables rather than committing secrets to the repository.
5. Define a repeatable process for creating and updating the database schema.
6. Implement transaction handling for operations that modify multiple related records.
7. Define and test how request-history records are created when relevant workflow events occur.
8. Configure appropriate database permissions and ensure that application-level authorization is enforced by the backend.
9. Create integration tests for database connectivity, record persistence, relationship integrity, and invalid operations.
10. Document the local development setup so team members can reproduce the environment.

These are implementation requirements resulting from the decision; they should not be marked complete until the corresponding work and evidence exist.

## Evidence and Verification

The decision is supported by the following architectural requirements and can be verified through implementation evidence.

Existing architectural rationale

* CampusConnect requires persistent storage for multiple related application entities.
* The request-management workflow requires consistent relationships between requests, users, assignments, comments, and history.
* The project uses a Python backend and requires a database compatible with it.
* The team requires a database that is free to use and practical to implement during Cycle 1.

Evidence to collect during implementation

* [ ]	A successful connection from the Python backend to PostgreSQL.
* [ ]	A database schema containing the required entities and relationships.
* [ ]	Tests demonstrating successful creation and retrieval of support requests.
* [ ]	Tests demonstrating that foreign-key constraints prevent invalid relationships.
* [ ]	Tests demonstrating transaction rollback when a related operation fails.
* [ ]	Tests verifying that relevant request changes are recorded in request history.
* [ ]	Tests verifying that unauthorized users cannot perform restricted operations through the application.
* [ ]	Documentation for database setup and schema changes.
* [ ]	A code review confirming that database access follows the agreed architecture.

Evidence status: The architectural rationale is documented. [ Implementation evidence must be linked here as the relevant code, tests, and configuration become available. (Not avalible now)]

Related evidence:

* Architecture: docs/architecture/architecture.md
* API contracts: docs/architecture/api-contracts.md
* Database implementation: Link the actual schema or database module when available.
* Integration tests: Link the actual test files when available.
* Related ADRs: Add links to decisions that depend on the database selection.

## Revisit Conditions

The team should reconsider this decision if any of the following conditions occur:

* PostgreSQL cannot be supported by the required development or deployment environment.
* Measured performance or resource requirements cannot be met with a reasonable PostgreSQL configuration.
* The application scope changes substantially, making a different storage model more appropriate.
* A documented technical limitation prevents PostgreSQL from supporting a required workflow.
* The team’s cost, operational, or hosting constraints change materially.
* Implementation or testing evidence demonstrates that another suitable database better satisfies the requirements.

A future review should compare the alternatives against the same requirements, document the evidence, and record any replacement decision in a new or superseding ADR.

## Decision Ownership and Review

Dathal is responsible for maintaining this ADR and ensuring that related architecture documentation remains consistent with the decision.
The development team is responsible for providing implementation feedback and evidence. Changes to the selected database should be discussed with the team and documented before the architecture is changed.
The decision should be reviewed when the database implementation is first integrated, when deployment constraints become clear, or when one of the revisit conditions is met.

## Update History

* 2026-10-05: Initial database decision discussion and documentation.
* 2026-10-15: Expanded the decision rationale, alternatives, consequences, implementation implications, evidence requirements, and revisit conditions. Updated by Dathal.