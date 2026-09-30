# CampusConnect - Project Task Plan

## Purpose

This task plan breaks the overall CAmpusConnect Project into a brief and trackable taskes based on projects requirements.

Each task identifies its requirement, owner, dependecies, current status, and the evidence needed for completion.

The task plan will be updated throughout developement as task are completed, changed, added, or re-estimated. 


## 1. Student Request Submission

| ID | Task | Owner | Dependencies | Status | Completion Evidence |
|---|---|---|---|---|---|
| T-01 | Create student request submission form/input | TBD | None | Not Started | Request submission interface is implemented and available for testing |
| T-02 | Add required request information fields | TBD | T-01 | Not Started | All required fields are displayed correctly |
| T-03 | Validate required request information | TBD | T-01, T-02 | Not Started | Invalid or incomplete requests are rejected during testing |
| T-04 | Store submitted requests | TBD | T-02, T-03 | Not Started | A successfully submitted request can be retrieved |
| T-05 | Confirm successful request submission | TBD | T-04 | Not Started | Student receives confirmation after a valid submission |


## 2. Request Management

| ID | Task | Owner | Dependencies | Status | Completion Evidence |
|---|---|---|---|---|---|
| T-06 | Create reviewer view for submitted requests | TBD | T-04 | Not Started | Reviewer can view submitted requests |
| T-07 | Display individual request details to reviewer | TBD | T-06 | Not Started | Reviewer can open and inspect a selected request |
| T-08 | Allow reviewer to update permitted request information | TBD | T-07 | Not Started | Changes can be saved and retrieved |
| T-09 | Test reviewer request-management workflow | TBD | T-06–T-08 | Not Started | Request-management tests pass |


## 3. Request Status Tracking

| ID | Task | Owner | Dependencies | Status | Completion Evidence |
|---|---|---|---|---|---|
| T-10 | Define supported request statuses | TBD | None | Not Started | Supported statuses are documented and implemented |
| T-11 | Assign initial status when request is submitted | TBD | T-04, T-10 | Not Started | New request receives the expected initial status |
| T-12 | Allow authorized reviewer to update request status | TBD | T-07, T-10 | Not Started | Reviewer can successfully change status |
| T-13 | Display current request status to student | TBD | T-11 | Not Started | Student can view the correct current status |
| T-14 | Test status transitions and display | TBD | T-11–T-13 | Not Started | Status tests pass |


## 4. Communication and Updates

| ID | Task | Owner | Dependencies | Status | Completion Evidence |
|---|---|---|---|---|---|
| T-15 | Allow reviewer to add an update or note to a request | TBD | T-07 | Not Started | Reviewer can save an update to a request |
| T-16 | Store request updates with the correct request | TBD | T-15 | Not Started | Saved update can be retrieved with its request |
| T-17 | Display applicable updates to the student | TBD | T-16 | Not Started | Student can view updates associated with their request |
| T-18 | Test request communication workflow | TBD | T-15–T-17 | Not Started | Communication tests pass |


## 5. Resolution Tracking

| ID | Task | Owner | Dependencies | Status | Completion Evidence |
|---|---|---|---|---|---|
| T-19 | Allow reviewer to record request resolution | TBD | T-07 | Not Started | Resolution can be entered and saved |
| T-20 | Associate resolution information with the correct request | TBD | T-19 | Not Started | Resolution is retrieved with the correct request |
| T-21 | Update request status when appropriate after resolution | TBD | T-12, T-19 | Not Started | Resolved request displays the expected status |
| T-22 | Display resolution information to the student | TBD | T-20 | Not Started | Student can view the recorded resolution |
| T-23 | Test resolution workflow | TBD | T-19–T-22 | Not Started | Resolution tests pass |


## 6. Role-Based Access

| ID | Task | Owner | Dependencies | Status | Completion Evidence |
|---|---|---|---|---|---|
| T-24 | Define student and reviewer permissions | TBD | Requirements | Not Started | Role permissions are documented |
| T-25 | Implement student access restrictions | TBD | T-24 | Not Started | Student can access only permitted functionality |
| T-26 | Implement reviewer access permissions | TBD | T-24 | Not Started | Reviewer can access authorized management functionality |
| T-27 | Prevent unauthorized access to restricted functionality | TBD | T-25, T-26 | Not Started | Unauthorized access attempts are rejected |
| T-28 | Test role-based access | TBD | T-25–T-27 | Not Started | Role-access tests pass |


## 7. Request History

| ID | Task | Owner | Dependencies | Status | Completion Evidence |
|---|---|---|---|---|---|
| T-29 | Store relevant request history information | TBD | T-04 | Not Started | Request history information is retained |
| T-30 | Display student's submitted requests | TBD | T-29 | Not Started | Student can view previously submitted requests |
| T-31 | Display previous status changes and updates when applicable | TBD | T-14, T-18, T-29 | Not Started | Request history displays applicable changes |
| T-32 | Test request-history functionality | TBD | T-29–T-31 | Not Started | Request-history tests pass |


## 8. Integration and Project Verification

| ID | Task | Owner | Dependencies | Status | Completion Evidence |
|---|---|---|---|---|---|
| T-33 | Integrate completed project components | TBD | Applicable feature tasks | Not Started | Components operate together successfully |
| T-34 | Perform end-to-end workflow testing | TBD | T-33 | Not Started | Major user workflows pass testing |
| T-35 | Review implementation against project requirements | TBD | T-34 | Not Started | Requirements and acceptance criteria have been verified |
| T-36 | Resolve identified integration defects | TBD | T-34, T-35 | Not Started | Identified blocking defects are resolved |
| T-37 | Complete final project review | TBD | T-35, T-36 | Not Started | Team confirms planned project requirements are satisfied |
