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

The team needs to select a database for CampusConnect that can 
reliably store and manage related application data, including users, 
support requests, request categories, assignments, comments, request history, 
and notifications. The database must support relationships between these records 
and the application's request workflow while being compatible with the Python backend.

The main constraints are that the database should be free to use, support relational data, 
provide reliable transactions and data integrity, integrate with the Python backend, 
and be practical to implement during Cycle 1. The team also wants a database that can 
support the application as CampusConnect grows.

## Decision

The team selected PostgreSQL as the primary database for CampusConnect.

Four of the six team members were in agreement with the decision. PostgreSQL will be used to store and manage 
the application's relational data, including users, support requests, assignments, comments, request history, 
and notifications.

PostgreSQL was selected because it is free and open source, supports relational data and reliable transactions, 
integrates with the project's Python backend, and provides the capabilities needed for the CampusConnect request workflow. 
The decision can be revisited if project requirements or technical constraints change.

## State the decision clearly enough that someone reviewing the repository later can understand what the team chose.

Kadeeja and Camille view this change.

## Alternatives Considered

### SQLite

SQLite was considered because it is free, lightweight, 
and easy to integrate with a Python application. 
However, PostgreSQL was preferred because CampusConnect 
is designed as a multi-user support workflow system with 
multiple related data entities and a need for reliable relational data management.

### PostgreSQL

PostgreSQL was selected because it is free and open source, 
supports relational data and transactions, integrates with Python, 
and provides room for CampusConnect to grow.

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

#Updates
- Last update. 10/05/2026; Dathal