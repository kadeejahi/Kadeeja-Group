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

