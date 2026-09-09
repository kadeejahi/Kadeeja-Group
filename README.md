# COMP 330/474 — Fall 2026 Repository Starter Kit

Official course-specific repository starter kit for COMP 330/474 Software Engineering at Loyola University Chicago.

This course starter kit is distinct from the general ETIS Engineering Platform Starter Kit; it is specifically designed to establish the team repository used for COMP 330/474 course work.

This repository establishes the engineering workspace and evidence structure your team will use throughout the semester.

Your team GitHub repository becomes the authoritative engineering record for the project, including planning, requirements, architecture, implementation, testing, AI use and verification, reviews, release readiness, operations, and continuous improvement.

---

## Student Team Setup — Required

After establishing your team repository from this starter kit, **update this README to describe your project and team**.

At a minimum:

1. Replace the project title and description below with your team's project information.
2. **Delete the sample team-member row** and add one row for each member of your team.
3. Update the project status as the project progresses.
4. Maintain the build, run, and test instructions as the system evolves.
5. Keep this README current throughout the semester.

The README is the **entry point to your engineering record**. It should help another engineer quickly understand the project and locate its evidence. It does not replace the authoritative engineering artifacts stored elsewhere in the repository.

---

# CampusConnect

**Project Brief**

CampusConnect is a student support request and workflow management system designed to provide a structured and transparent process for handling student support needs. In lieu of numerous emails, shared documents, or verbal follow-ups - the system presents a centralized workflow that allows requests to be submitted. reviewed, updated, tracked, and resolved.

**Problem Statement**

Often times, student support requests are often handled through informal and disconnected communication channels. Students may submit requests via email, verbally, or rely on shared documents in order to track their needs. As mentioned in the project brief, these methods can make it difficult to determine whether a request was received, who is responsible for addressing it, what actions have been taken, and whether the issue has been resolved.

**Intended Users and Stakeholders**

CampusConnect's primary users are students as they can utilize the system in order to assist with their requests. They can use CampusConnect to:

- Submit support requests.
- Provide relevant information about their needs.
- View the status of submitted requests.
- Review updates and resolution information.
- Track their requests without relying on repeated email or verbal follow-up.

Secondary users include support reviewers whom are responsible for evaluating and managing submitted requests. They can use the system to:

- View incoming student requests.
- Review request details.
- Update request status.
- Add notes or relevant information.
- Track requests through the resolution process.
- Document how requests were handled.

**Purpose**
The primary purpose of CampusConnect is to **centralize and standardize the student support request communication cycle**. The system is intended to improve transparency, accountability, consistency, and communication without adding any unnecessary complexity to the process.

**Scope**

1. Student Request Submission

Students can create and submit support requests containing relevant information about their needs. Each request becomes a trackable record within the system.

2. Request Management

Support reviewers can access submitted requests and manage them through the support workflow. Reviewers can examine request details, make updates, and record relevant actions.

3. Request Status Tracking

Requests progress through defined workflow states, allowing students and reviewers to understand where a request currently stands. Example statuses may include:

- Submitted
- Under Review
- In Progress
- Resolved
- Closed

4. Communication and Updates

The system provides a centralized location for recording updates associated with a request. This reduces the need for students and reviewers to rely on separate email conversations or verbal communication to determine what has occurred.

5. Resolution Tracking

Support reviewers can document the outcome of a request, providing a clear record of how the request was addressed and when it was resolved.

6. Role-Based Access

The system distinguishes between student and support-reviewer responsibilities. Students should have access to their own requests, while reviewers should have appropriate access to requests they are responsible for managing.

7. Request History and Visibility

The system maintains an inspectable record of requests and their workflow progression. This provides greater accountability and makes it easier to understand the history of a support request.

---

## Project Status

Update this section throughout the semester to reflect the current lifecycle stage and release cycle.

**Initial status:**

> Cycle 1 — Project Launch

---

## Team

The authoritative team roster, GitHub identities, specialized role
ownership, backup responsibilities, and team acknowledgements are
maintained in:

[`docs/team/roles.md`](docs/team/roles.md)

Keep that record current throughout the semester.

---

## Engineering Evidence

This repository is the **authoritative engineering record** for the project.

Engineering evidence is maintained throughout the repository, including:

- **Requirements** → `docs/requirements/`
- **Architecture** → `docs/architecture/`
- **Planning and engineering decisions** → `docs/planning/`
- **Testing and verification** → `docs/testing/`
- **Security** → `docs/security/`
- **Release evidence** → `docs/release/`
- **Operations and observability** → `docs/operations/`
- **Team evidence** → `docs/team/`
- **Reviews** → `docs/reviews/`

Do not duplicate detailed engineering evidence in this README. Use this page to orient reviewers and point them to the authoritative artifacts.

---

## Repository Structure

The repository is organized to preserve both the software system and the engineering evidence supporting it.

Major areas include:

- `src/` — application source code
- `tests/` — automated tests
- `docs/` — lifecycle engineering evidence and documentation
- `.github/` — GitHub workflows, templates, and repository automation

As the project evolves, update this section if additional top-level directories become important to understanding the system.

---

## Build, Run, and Test

**Update this section as implementation progresses.**

A new engineer should eventually be able to use the instructions here to:

1. clone the repository;
2. install or configure required dependencies;
3. configure the development environment;
4. build the system;
5. run the system; and
6. execute the automated tests.

### Prerequisites

Document required software, runtimes, tools, services, and versions here.

### Build

Document the build procedure here.

### Run

Document how to start and use the system here.

### Test

Document how to execute the project's automated tests here.

---

## Engineering Practices

This project uses repository-centered engineering practices, including:

- lifecycle-based engineering evidence;
- issue and pull-request workflows;
- documented engineering decisions;
- requirements and evidence traceability;
- automated testing and verification;
- peer review;
- responsible AI-assisted engineering;
- explicit AI disclosure and verification;
- release-readiness evidence; and
- continuous improvement.

Engineering evidence should be created and maintained **as the work occurs**, not reconstructed only when an assignment is due.

---

## Engineering Operating Model

COMP 330/474 uses three complementary environments:

- **Sakai** — the authoritative source for required readings, assignments, due dates, naming, grading, and submission expectations.
- **ETIS** — the professional engineering reference ecosystem, including the ETIS Framework, books and publications, Engineering Platform, and supporting guidance.
- **GitHub** — the authoritative engineering record for your team's project, decisions, implementation, reviews, testing, and evidence.

**Sakai defines what the course requires.**  
**ETIS provides the broader engineering discipline and professional reference model.**  
**GitHub preserves the evidence of what your team actually engineered.**

---

## Professional Engineering Expectations

A reviewer examining this repository should be able to determine:

- what the team intends to build;
- what problem the system addresses;
- who owns and contributes to the work;
- what engineering decisions were made and why;
- how requirements connect to architecture and implementation;
- what was reviewed and tested;
- how AI-assisted work was disclosed and verified;
- what risks, defects, and limitations remain;
- whether the system is ready to release and operate; and
- how the project improved over time.

A working system is necessary, but it is not sufficient.

Professional engineering also requires evidence that the system can be understood, reviewed, governed, changed, verified, operated, and defended.

---

## Course and Professional Context

This repository was established from the **COMP 330/474 Fall 2026 Repository Starter Kit**.

The broader ETIS professional engineering ecosystem is available at:

https://etisframework.org/

Use ETIS as professional guidance and reference material. **Sakai remains authoritative for COMP 330/474 course requirements.**
