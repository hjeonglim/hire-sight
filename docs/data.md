## Ensure HBM data only

no_filter: id, location (US)
CORE_FILTERS = ["HBM", "high bandwidth memory"]

### All tests: **Micron** (company ID), US, last 30 days.

| #   | Test                                                | Count | Result                    |
| --- | --------------------------------------------------- | ----- | ------------------------- |
| 1   | No filter                                           | 821   |                           |
| 2a  | Core filter (v1)                                    | 130   |                           |
| 2b  | Core + adjacent filter (v0)                         | 162   | +32 vs core               |
| 3   | Precision: read 20 core matches                     | 130   | 20/20 broad, 12/20 strict |
| 4   | Misses: 20 from memory pool, excluding core matches | 680   | 0/20 mention HBM          |

- Broad: HBM in the job's duties or requirements
- Strict: HBM is the job's main focus (HBM in the job title or the main duties)

HBM share (2a ÷ 1): 130 / 821 = 15.8%
Decision (keep or change filter, why): Keep core filter v1. Precision 20/20 (broad), and 0/20 misses in the memory pool, so adjacent terms add noise without catching real HBM jobs.

### All tests: **Samsung** (company ID), US, last 30 days.

| #   | Test             | Count | Result |
| --- | ---------------- | ----- | ------ |
| 1   | No filter        | 176   |        |
| 2a  | Core filter (v1) | 13    |        |

### All tests: **SK Hynix** (company ID), US, last 30 days.

| #   | Test             | Count | Result |
| --- | ---------------- | ----- | ------ |
| 1   | No filter        | 22    |        |
| 2a  | Core filter (v1) | 2     |        |

**Caveat:** This study only covers US. Samsung and SK Hynix hiring is not covered by TheirStack; US counts reflect US subsidiaries only.
