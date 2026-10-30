# Known Limitations ⟢

## Purpose
This will be used to record the known limitations and what CampusConnect will not include for the cycle, what work has been delayed and what still needs to be checked before the system is ready.

## Known Limitations

| ID | Feature | Reason |
| --- | --- | --- |
| DL-01 | Other University Systems | Connecting CampusConnect to other university systems is outside the scope.

## Deferred Defects

| ID | Limitations | Impact | Reason for Delay | Owner | Status
| --- | --- | --- | --- | --- | --- |
| N/A | None Confirmed | N/A | N/A | N/A | N/A |

## Release Readiness Concerns

| ID | Concern | Why It Matters | Next Step |
| --- | --- | --- | --- |
| RR-01 | Request Submission | Students should be able to submit requests and save info correctly | Verify Submission and tests
| RR-02 | Students must be able to see the correct status of their requests. | Test status updates and visibility. |
| RR-03 | Integration and Testing | Different parts of the system must work together without errors. | Reveiw integration tests and Github Cl results. |
| RR-04 | Important technical decisions must be confirmed and documented. | Review the latest approved architecture decisions. |

 ## Release Readiness Confirmations
 
 ★ The team must confirm that the features work right before considering everything to be ready.

 # Before release:
- [ ] Verify that all required features meet their acceptance criteria.
- [ ] Confirm that student and reviewer permissions work correctly.
- [ ] Review test results and integration checks.
- [ ] Document any unfinished work or known defects so the team understands what still needs to be completed. 

## Related Risks 

| Risk ID | Risk | Related Concern |
|---------|------|-----------------|
| R-03 | Unclear requirements | RR-04 |
| R-04 | Integration problems | RR-03 |
| R-05 | Git merge conflicts | RR-03 |
| R-08 | Technical bugs | RR-01, RR-02, RR-03 |
| R-10 | Outdated documentation | RR-04 |
| R-11 | Incomplete testing | RR-01, RR-02, RR-03 |
| R-14 | Schedule delays | RR-03 |
| R-15 | Requirements not met | RR-01, RR-02 |



