ADR-001: DataBase Choice
Status: Proposed
Date: 2026-09-29
Decision Owners: Dathal

## Context
CampusConnect needs a database to store and manage
student support requests and related information. 
This includes users, request categories, assignments, 
comments request history, and notifications.

The database should support relationships between these records 
and the request workflow. The team also needs a database choice 
that can be integrated with the Python backend during Cycle 1.

## What engineering problem or decision requires resolution?

What constraints, requirements, risks, or forces influence the decision?

## Decision

4/6 were in agreement.

## State the decision clearly enough that someone reviewing the repository later can understand what the team chose.

Kadeeja and Camille view this change.
Alternatives Considered

SOLite 

Upon research it was leaning towards PostgresQL


## Consequences

None PostgresQL seems to be reliable

## Positive

is a free and open source, works well with python, 
supports relational data, provides reliable transactions
and scale as CampusConnect grows.

## Evidence

- The CampusConnect architecture requires a database for relational data such as users, support requests, assignments, comments, request history, and notifications.
- PostgreSQL supports relational databases and is compatible with the project’s proposed Python backend.
- PostgreSQL is free and open source, which supports the team’s requirement for a free database.
- The team can verify the choice through a working PostgreSQL connection/test during implementation.
- The architecture decision can be reviewed by the team lead and development team before being marked approved.

## Revisit Conditions

Reconsider the PostgreSQL decision if project requirements change, 
PostgreSQL cannot meet the team’s technical needs, the development or 
deployment environment does not support PostgreSQL, or the team identifies 
a free database solution that better fits the project.