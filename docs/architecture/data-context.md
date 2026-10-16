# Data & Context Ownership

## Purpose
This document identified authoritative data, sensitive data, data owners, AI context sources, visibility limits, and logging expectations.

The goal is to ensure:
**Clear Data Custody:** Clear distinction between User-Owned Data, System Context, and Intellectual Property
**Context Integrity:** Unambiguous rules for how context is stored, cached, and shared.
**Privacy & Compliance:** Adherence to regulatory standards regarding data processing and retention.

## Ownership & Classification Matrix

| Data Class | Description | Primary Owner | Storage / Location | Retention Policy | Third-Party Exposure |
|---|---|---|---|---|---|
| Student Submissions & Requests | Raw support request text, descriptions, and inputs provided by students | TBD | PostgreSQL | Maintained per active request history and workflow requirements | None |
| Student-Visible Updates | Progress updates, public comments, and status changes visible to the student | TBD | PostgreSQL | Maintained per request history requirements | None |
| Internal Reviewer Notes | Confidential notes, triage, remarks, or administrative tags added by reviewers | TBD | PostgreSQL | Retained for audit and administrative traceability | Hidden from student access |
| System Context & Workflow Rules | Status transition matrices, role definitions and business logic routing rules | TBD | Git Repository | Persistent Version Controlled | Internal Only |
| Operational & Audit Logs | Application event logs, error traces, and access logs | TBD | Approved logging mechanism | Standard operational window | No Sensitive Data |

## Context Flow & Boundaries
**Session and In-Memory Context:** Incorporate active user authentication tokens, current request states, and transient API payload data. Isolation of multi-tenant and multi-user isolation must be enforced at the API gateway and backend controller layer. Session context must never bleed across user boundaries.

**Database Access and Persistence Boundaries:** Contains Layered Separation and Authorization Enforcement.
* Layered Separation: User interfaced have no direct access to the PostgreSQL database. All read and write operations must pass through API controllers, Application services, and Repository Layers.
* Authorization Enforcement: The backnd must explicitly validate user identity and role permissions before executing queries or returning data payloads.

**Separation of Student-Facing vs. Internal Data:** System must separate public interaction channels from confidential administrative spaces.

**AI & External Tool Data Boundaries:** AI must not have access to real student private data, credentials, and secrets must not be submitted to unapproved external AI tools or language models. AI can be used for approved documentation drafting, code suggestions, or debugging workflows. Make sure all output must be rigorously verified by humans. AI use must be logged in the ai-use-log.md
