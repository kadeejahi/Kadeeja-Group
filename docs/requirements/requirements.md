# Initial Requirements

## REQ-001 — Student Support Request Submission

**Requirement:**
Students can create and submit support requests.

**Acceptance Criteria:**

* A student can provide the required information for a support request.
* The system validates required information before submission.
* A valid support request can be submitted successfully.
* A submitted request is associated with the student who created it.

---

## REQ-002 — Student Request Status

**Requirement:**
Students can view the status of their submitted support requests.

**Acceptance Criteria:**

* A student can view requests they have submitted.
* Each request displays its current status.
* Students cannot view requests belonging to other students.

---

## REQ-003 — Reviewer Request Access

**Requirement:**
Reviewers can view submitted support requests.

**Acceptance Criteria:**

* An authorized reviewer can access submitted support requests.
* Reviewers can view the information associated with a request.
* Reviewer access is restricted to authorized users.

---

## REQ-004 — Reviewer Request Management

**Requirement:**
Reviewers can update request information and status.

**Acceptance Criteria:**

* An authorized reviewer can update request information.
* An authorized reviewer can change the status of a request.
* The system saves the updated information.
* Status changes are associated with the request.

---

## REQ-005 — Reviewer Request Updates

**Requirement:**
Reviewers can add updates to support requests.

**Acceptance Criteria:**

* An authorized reviewer can add an update to a request.
* The update is associated with the appropriate request.
* The update is retained after submission.

---

## REQ-006 — Resolution Recording

**Requirement:**
Reviewers can record how a support request was resolved.

**Acceptance Criteria:**

* An authorized reviewer can record resolution information.
* Resolution information is associated with the appropriate request.
* The recorded resolution can be viewed as part of the request history.

---

## REQ-007 — Request History

**Requirement:**
The system maintains a history of request updates and status changes.

**Acceptance Criteria:**

* The system records relevant request updates.
* The system records status changes.
* Historical information remains associated with the request.
* Authorized users can view the relevant request history.

---

## REQ-008 — Role-Based Access

**Requirement:**
Students and reviewers have different access permissions.

**Acceptance Criteria:**

* The system identifies whether a user is a student or reviewer.
* Students can access student-authorized functionality.
* Reviewers can access reviewer-authorized functionality.
* Users cannot perform actions outside their assigned permissions.

# Assumptions

The following assumptions are being made to guide the initial design and development of the system:

1. **Users have defined roles.**
   The system will support at least two user roles: **students** and **reviewers**. Each role will have different permissions.

2. **Students can only access their own requests.**
   Students will be able to create, submit, view, and track their own support requests but will not be able to view requests submitted by other students.

3. **Reviewers can access submitted requests.**
   Reviewers will have permission to view and manage support requests submitted by students.

4. **Requests have a defined lifecycle.**
   A support request will progress through statuses such as submitted, under review, in progress, resolved, or closed.

5. **Request history must be preserved.**
   Changes to request information and status will be recorded rather than overwriting the complete history of the request.

6. **Updates are associated with specific requests.**
   Reviewers can add notes or updates to a request, and those updates will remain associated with the request for future reference.

7. **The system will track resolution information.**
   When a request is resolved, the system will store information describing how the issue was addressed.

8. **Authentication is required.**
   Users will need to authenticate before accessing functionality that requires a specific role or account.

9. **Authorization will be enforced by the application.**
   The system will prevent users from accessing functionality or information outside of their assigned permissions.

10. **The initial system is focused on core support-request functionality.**
    Features such as notifications, file attachments, analytics, integrations, and automated routing are considered outside the initial scope unless later requirements identify them as necessary.

11. **A request contains enough information for a reviewer to understand the issue.**
    At minimum, a request will include information such as the submitting student, a description of the issue, its status, and relevant timestamps.

12. **The system will maintain an auditable history.**
    Important actions, including status changes and request updates, will include information about when the action occurred and which user performed it.

# Open Questions

The following questions should be answered before or during implementation because they could affect the system's architecture, database design, or user experience.

### User Accounts and Roles

1. What information is required when creating a student or reviewer account?
2. Who creates reviewer accounts?
3. Can a user have more than one role?
4. How will users authenticate—email/password, university credentials, or another authentication provider?
5. Should users be able to reset forgotten passwords?

### Support Requests

6. What fields are required when a student submits a support request?
7. Should students select a category for their request?
8. Should requests have a priority level?
9. Can students edit a request after submitting it?
10. Can students withdraw or delete a request?
11. Can reviewers reassign a request to another reviewer?

### Status and Workflow

12. What statuses should a request support?
13. Who is allowed to change a request's status?
14. Should certain status changes require additional information?
15. Can a resolved or closed request be reopened?
16. What is the difference between **resolved** and **closed**, if both statuses are needed?

### Updates and History

17. What information should be stored for each request update?
18. Can students respond to reviewer updates, or are updates reviewer-only?
19. Should users be able to edit or delete previously submitted updates?
20. Which actions must be recorded in the request history?
21. How long should request history be retained?

### Resolution

22. What information must a reviewer provide when resolving a request?
23. Should the system require a resolution description before allowing a request to be marked resolved?
24. Can a reviewer mark a request as resolved without the student's confirmation?

