# Api Contracts

## Purpose

This document defines the contracts across CampusConnect's component boundaries for the Cycle 1 student-support request workflow. A contract specifies the producer and consumer, required input, expected output, permissions, failure behavior, side effects, and evidence needed to verify it.
The architecture describes a Python-based layered system:


Student/Reviewer UI → API/Controllers → Application Services → Business/Workflow Logic → Repositories/Data Access → Database
Authentication, authorization, validation, logging, and error handling apply across the relevant boundaries. 

These contracts are logical interfaces, not a commitment to HTTP endpoints or a specific Python web framework. If the team selects HTTP, it must add approved routes, methods, response schemas, and status codes. PostgreSQL is proposed, not yet approved.

## Common contract rules

1. Protected operations require an authenticated user; backend authorization must be enforced independently of the UI.

2. Students may access only their own requests. Reviewers may access only requests within their authorized permissions.

3. Internal reviewer notes must never appear in student-facing responses.

4. Invalid inputs and disallowed workflow transitions must not modify stored records.

5. A failed persistence operation must not be reported as successful. Errors must not disclose secrets or unnecessary student information.

6. Changes affecting request status, assignment, resolution, or history should be recorded where required by the agreed history policy.

7. Exact field names, status codes, size limits, retention periods, and retry limits are pending implementation decisions unless explicitly defined below. Examples are illustrative rather than approved schemas.

8. Evidence links below are planned; do not mark a test, PR, or review as completed until it exists.


## 2. Interface Contract Summary

| ID | Interface | Producer -> Consumer | Authorized boundary | 
| --- | --- | --- | --- |
| C-01| Request submission | Student UI -> API | Authenticated student; create own request |
| C-02 | Request Retrieval | Student UI -> API | Student ownership or reviewer authorization |
| C-03 | Request Management | Reviewer UI -> API | Authorized reviewer; permitted updates, assignment, resolution | 
| C-04 | Request Status | Application Services -> Student/Reviewer UI | Status visibility and permitted transitions | 
| C-05 | Comments / Updates | Student/Reviewer -> API | Role-, request-, and visibility-based permissions |
| C-06 | Internal Notes | Reviewer UI -> API | Authorized reviewers only | 
| C-07 | Data Persistence | Application / Repository Layer -> Database | Repository-controlled reads and writes |
| C-08 | Authentication | Authentication component -> Protected services | Verify identity and allow/deny action | 
| C-09 | Logging / Observability | Application components -> Approved logs | Authorized operational access only |

## 3. Security and Action Boundaries

-[] Students can access only their own requests and permitted updates.

-[] Reviewers can manage only requests they are authorized to access.

-[] Internal reviewer notes must never appear in student-facing responses.

-[] Backend services enforce authorization and workflow rules.

-[] User interfaces cannot directly modify the database.

-[] Invalid requests must not change application data.

-[] Successful changes must be stored consistently and recorded in request history where required.

-[] Errors must not expose passwords, credentials, or private student information.

## 4. Tool and External Service Boundaries 

Database: Application services access persistent data through repository interfaces. PostgreSQL is proposed but requires final approval.

External services: No additional external service may be introduced without team review and documentation. Tool access must be limited to approved operations and permissions.

AI tools: CampusConnect does not currently include an approved runtime AI integration. AI-assisted development requires human review, testing, and disclosure in docs/ai/ai-use-log.md. AI tools cannot independently approve or merge code or receive unapproved private student data.

## 5. Verification and Evidence

| Contract Area | Required Verification | 
| --- | --- | 
| Request submission | Valid submission succeed any missing fields are rejected |
| Request retrieval | Students cannot access other students' requests |
| Request management | Unauthorized reviewer actions are denied |
| Status tracking | Invalid or unauthorized status changes are rejected|
| Comments and internal notes | Student-visible content remains separate from internal notes |
| Data persistence | Records save correctly; database failures are handled |
| Authentication and authorization | Protected operations reject unauthorized users |
| Logging | Relevant events are recorded without exposing sensitive information | 

Evidence should be linked to the relevant GitHub Issues, pull requests, or tests once available. Planned tests are not considered completed evidence.

## 6. Open Decisions

The team must confirm the following before finalizing affected contracts:

-[] Approval of PostgreSQL as the database.

-[] Reviewer permissions for reopening resolved requests.

-[] Which request-history information students may view.

-[] Whether notifications are included in Cycle 1.

[] Final API operation names and request/response formats once the implementation approach is confirmed.

Review Status: Pending team approval.

Related Document: docs/architecture/architecture.md


