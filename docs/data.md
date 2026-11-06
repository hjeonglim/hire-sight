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

### Micron: 10/01/2025 - 10/30/2026 Monthly

| Month   | All | HBM (core) | HBM share |
| ------- | --- | ---------- | --------- |
| 2025-11 | 181 | 20         | 11.0%     |
| 2025-12 | 277 | 17         | 6.1%      |
| 2026-01 | 385 | 29         | 7.5%      |
| 2026-02 | 321 | 32         | 10.0%     |
| 2026-03 | 510 | 73         | 14.3%     |
| 2026-04 | 441 | 77         | 17.5%     |
| 2026-05 | 417 | 59         | 14.1%     |
| 2026-06 | 362 | 49         | 13.5%     |
| 2026-07 | 430 | 59         | 13.7%     |
| 2026-08 | 669 | 99         | 14.8%     |
| 2026-09 | 707 | 125        | 17.7%     |
| 2026-10 | 739 | 113        | 15.3%     |
