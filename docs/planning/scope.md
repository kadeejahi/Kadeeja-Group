
# CampusConnect - Project Scope


## Overview: The System will allow students to submit support requests and allow support reviewrs to manage, track, and resolve those request.

## In Scope

- Students request submission
- Request management
- Request status tracking
- Communication and updates
- Resolution tracking
- Role based access
- Request history and visibility



## Decision

The team will focus Cycle 1 on the core student support-request workflow:

* Students can create and submit support requests.
* Students can view the status of their requests.
* Reviewers can view submitted requests.
* Reviewers can update request information and status.
* Reviewers can add updates to requests.
* Reviewers can record how a request was resolved.
* The system will maintain a history of request updates and status changes.
* Students and reviewers will have different access permissions.

Additional features will not be considered part of the initial Cycle 1 scope unless they are necessary to support this workflow.

## Reason

The team needs a manageable vertical slice that demonstrates meaningful end-to-end functionality without committing to features that may exceed the team's available time or implementation capacity.

Focusing on the core workflow gives the team a shared target for Cycle 1 while allowing implementation experience to inform future requirements and prioritization.

This approach also reduces the risk of spending Cycle 1 designing features that may change once the team better understands the technical and user requirements.

## Alternatives Considered

### 1. Implement the full feature set upfront

The team could have attempted to define and implement a more comprehensive system, including additional features such as notifications, file attachments, reporting, dashboards, and integrations.

**Why not chosen:** This would increase the initial scope and make it more difficult to determine whether the team could complete the core workflow within the Cycle 1 timeframe.

### 2. Define requirements only as implementation begins

The team could have avoided establishing detailed requirements and allowed requirements to evolve entirely during development.

**Why not chosen:** This could lead to inconsistent assumptions between team members and make it more difficult to establish a shared understanding of the intended system behavior.

### 3. Focus only on individual technical components

The team could have divided Cycle 1 into isolated technical tasks such as database design, API development, or UI development.

**Why not chosen:** This would provide less evidence that the system works as a complete solution. A vertical slice allows the team to validate the interaction between major parts of the system.

## Consequences

### Positive

* Provides a clear and achievable Cycle 1 target.
* Gives the team a shared understanding of the initial system behavior.
* Allows the team to validate the end-to-end workflow early.
* Leaves room to adjust requirements based on implementation findings.

### Negative

* Some potentially useful features will be deferred.
* Requirements may need to be revisited after the team gains implementation experience.
* The initial system may have limited functionality outside the core support-request workflow.

## Follow-Up

The team will revisit the requirements as Cycle 1 progresses. Changes should be based on implementation findings, effort estimates, technical constraints, or newly identified requirements.
