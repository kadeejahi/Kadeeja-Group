# CampusConnect Architecture

**Team:** TheCrazy6

## Overview

This directory contains the architectural documentation and supporting evidence for the CampusConnect project. It establishes the system's high-level structure, defines the responsibilities and interactions of its components, and documents the interfaces and data models required to implement the project's functionality.

The architecture package is intended to provide a shared reference for developers, reviewers, and other stakeholders. It connects the project's functional requirements to concrete design decisions and implementation responsibilities.

During Cycle 1, the architecture focuses on the support request workflow: enabling students or clients to submit support requests and allowing authorized administrators or reviewers to review requests, update their status, and maintain a history of changes.

## Start here

| Resource | Purpose |
|---|---|
| [Architecture diagram](architecture-diagram.png) | Shows the presentation layer, backend layers, authentication/authorization, and database boundary. |
| [architecture.md](architecture.md)| Explains system purpose, major
components, responsibilities, dependency direction, and how the design
supports the Cycle 1 vertical slice. | 
| [Component Responsibility Map](component-responsibilities.md) | Mapping of components to their responsibilities and key boundaries and evidence tied to that responsibility. | 
| [api-contracts.md](api-contracts.md) | Defines inputs, outputs, permissions, action/evidence contracts, and error responses for the API endpoints. |
| [Data and Context Ownership](data-context.md) | Identifies authoritative data, sensitive data, data owners, AI context sources,
visibility limits, and logging expectations|
| [Architecture Decision Records (ADRs)](data-context.md) | Records important architecture decisions, alternatives considered, consequences,
risks, and owners. |
| [Architecture Review Evidence](architecture-review.md) | Summarizes peer review findings, author response, accepted/deferred/rejected feedback, and acion items. |
| [Review Workflow Evidence](data-context.md) | Records important architecture decisions, alternatives considered, consequences,
risks, and owners. |
| [Updated Planning Evidence](/docs/planning/) | Updates scope, task plan, risks, estimates, schedule, and team commitments |
| [Test/Review Evidence Plan](/docs/testing/test-strategy.md) | Maps key architecture risks, contracts, and workflows to planned tests or review evidence |
| [AI-Use Log Updates](/docs/ai/ai-use-log.md) | Discloses AI assistance used for architecture, diagrams, contracts, decisio records, risk analysis, etc. |
| [Architecture Review Action Tracking](Pending Link) | Tracks accepted, defered, and rejected rfindings; assigns owners and due dates; and links closure evidence |


## 1. Cycle 1 boundary and highest-risk flow

### Selected vertical slice

Cycle 1 focuses on the core student support-request workflow:

1. A student submits a support request.
2. The student can view the status and student-visible progress updates for their requests.
3. A support reviewer can view submitted requests, update request information and status, add updates, and record resolution.
4. The system retains a history of request updates and status changes.
5. Student and reviewer permissions differ. Internal staff notes must remain restricted to authorized staff.

External university-system integrations, advanced analytics/reporting, AI-based assignment, and a separate mobile application are out of scope for the initial release.

### Boundary and data flow

```text
Student UI
   │ Submit request (authenticated student + request fields)
   ▼
Application / API layer
   │ Validate payload; authenticate identity; enforce access policy
   ▼
Business / workflow layer
   │ Create request and unique ID; initialize status; record history
   ▼
Data access layer
   │ Persist request and history records
   ▼
Database
   │
   └── Result returns through the layers to the Student UI
```

### Core Architectural Workflow

The Cycle 1 architecture centers on the support request lifecycle.

- Request submission: A student or client submits a support request through the frontend.

- Request processing: The backend validates the request, verifies the user's identity and permissions, and processes the submission.

- Data persistence: The backend stores the support request and its associated information in the database.

- Status updates: Authorized users update request statuses as the request progresses through its lifecycle.

- History and accountability: The system preserves a record of relevant status changes so that request progress can be reviewed.

The frontend is responsible for presenting information and collecting user input. The backend is responsible for enforcing business rules and authorization. The database provides persistent storage for requests and their associated history.

### Architectural Principles

The architecture follows these principles:

- Separation of concerns: The frontend, backend, and database have distinct responsibilities.

- Security by default: Authorization is enforced by the backend rather than relying exclusively on frontend restrictions.

- Explicit interfaces: API contracts define how components exchange information.

- Data integrity: Validation and persistence rules protect the consistency of support requests and their histories.

- Traceability: Architectural decisions and design evidence should be traceable to project requirements.

- Incremental delivery: Cycle 1 prioritizes a complete, testable vertical slice before expanding the system's functionality.

### Architecture Evidence and Validation

Each architecture document should provide evidence that the proposed design is sufficiently detailed to guide implementation.

The evidence should demonstrate that:

- The primary workflow has clearly defined component boundaries.

- API contracts specify expected inputs, outputs, and failure behavior.

- Component responsibilities are explicit and do not create unnecessary coupling.

- The data model supports the required workflow and relationships.

- Authorization rules identify which roles may perform specific actions.

- Architectural decisions document their rationale and relevant trade-offs.

- The design can be validated through implementation, integration tests, or other appropriate verification methods.

### Scope and Maintenance

This package focuses on the architecture required to implement and evaluate the CampusConnect project, with particular emphasis on the Cycle 1 support request workflow.

The documentation will evolve alongside the implementation. When a significant architectural decision changes, the relevant diagrams, contracts, and decision records will be updated to remain consistent with the codebase.

This README serves as the central index for the package. New architecture documents should be added to the index as they are created, and obsolete links should be removed or replaced.

### Related Project Documentation

Architecture documentation should be read alongside the project's requirements, development plan, and implementation documentation. These materials describe what the system must accomplish, how its architecture supports those requirements, and how the design is realized in code.


