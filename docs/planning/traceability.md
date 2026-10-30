# Requirement Traceability

| Requirement | Task IDs | Github Issue | Pull Request | Verification | Status | 
| --- | --- | --- | --- | --- | --- | 
| Student Request Submission | T-01 - T-05 | Pending | Pending | Test creating a request | Not Started |
| Request Management | T-06 - T-09 |  Pending | Pending | Test viewing and updating requests | Not Started |
| Request Status Tracking | T-10 - T-14 | Pending | Pending | Test changing request statuses | Not Started |
| Communication and Updates | T-15 - T-18 | Pending | Pending | Test adding and viewing updates | Not Started |
| Resolution Tracking | T-19 - T-23 | Pending | Pending | Test resolving a request | Not Started |
| Role-Based Access | T-24 - T-28 | Pending | Pending | Test access for each role | Not Started |
| Request History and Visibility | T-29 - T-32 | Pending | Pending | Verify previous actions are displayed | Not Started |
| Integration and Verification | T-33 - T-37 |  Pending | Pending | End-to-end workflow testing | Not Started |


## Engineering Evidence

### Purpose

This section documents engineering activities and supporting evidence throughout the CampusConnect development process.

It provides traceability between project tasks, implementation, testing, CI/CD execution, and issue tracking.

### Engineering Evidence Tracking

| Engineering Activity | Related Task / Requirement | Evidence | Verification | Status |
|---|---|---|---|---|
| CI Workflow Configuration | Development Infrastructure | [PR #41](https://github.com/kadeejahi/Kadeeja-Group/pull/41) | CI workflow configured and executed | Completed |
| CI Workflow Execution | Development Infrastructure | [GitHub Actions Run](https://github.com/kadeejahi/Kadeeja-Group/actions/runs/40593556940) | GitHub Actions workflow completed successfully | Passed |
| CI Results Documentation | Testing and Verification | `docs/testing/ci-evidence.md` | CI execution results and limitations documented | Documented |
| Issue and Defect Tracking | Engineering Process | GitHub Issues (links pending) | Issues documented and tracked as created | Ongoing |
| Application Implementation | T-01 – T-32 | Pending implementation PRs | Implementation evidence pending | Not Started |
| Automated Application Testing | T-09, T-14, T-18, T-23, T-28, T-32 | `tests/` | Automated test execution not yet confirmed | Pending |
| Integration Testing | T-33 – T-34 | Pending | End-to-end workflow verification | Not Started |
| Requirements Verification | T-35 | `docs/planning/traceability.md` | Requirements reviewed against implementation and tests | Pending |
| Final Project Review | T-37 | Pending | Final review and acceptance evidence | Not Started |

### Known Limitations

- CampusConnect application development is ongoing.
- The current CI workflow can pass without executing automated application tests.
- Successful CI execution does not necessarily demonstrate application correctness.
- Implementation and verification evidence will be updated as development progresses.
- GitHub Issues and pull requests will be linked as work is completed.

### Evidence Maintenance

Engineering evidence will be updated throughout development to maintain traceability between project requirements, tasks, implementation, and verification.

Each completed activity should include supporting evidence such as a GitHub Issue, pull request, test result, or CI execution record.



