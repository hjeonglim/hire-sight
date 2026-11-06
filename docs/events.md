## Pre-registered tests: Micron, US, Nov 2025 - Oct 2026

Written before viewing keyword-level data. The overall monthly HBM share was already seen.

### Tests

| #   | Date       | Event                             | Source                 | Keywords                                    | Check window        | Expected  |
| --- | ---------- | --------------------------------- | ---------------------- | ------------------------------------------- | ------------------- | --------- |
| 1   | 2026-01-16 | NY (Clay) fab groundbreaking      | Press release          | `HBM` in NY postings                        | Nov 2025 - Feb 2026 | No signal |
| 2   | 2026-03-16 | HBM4 12H shipping, 16H samples    | Press release          | `16-high`, `16H`, `HBM4`                    | Dec 2025 - Mar 2026 | Signal    |
| 3   | 2026-05-22 | HBM4E on 1-gamma, TSMC logic dies | J.P. Morgan conference | `base die`, `logic die`, `1-gamma`, `HBM4E` | Feb - Jun 2026      | Signal    |

### Rules

Baseline = the 3 months before the check window. The baseline decides which rule a keyword gets:

- **0 postings in the baseline → Emergence.** 3+ postings a month, 2+ months in a row.
- **Some postings in the baseline → Rise.** The share is 1.5× or more of the previous 3 months' average, with 3+ postings, 2+ months in a row. Share = keyword postings ÷ HBM postings (test 1: ÷ NY postings).
- **Pass:** any keyword meets its rule inside the check window.

### Caveats

- Description matching is noisy. Results are "consistent with" an event, never "caused by" it.
- Test 1 is a negative control. If a rule fires, read the postings: boilerplate = false positive (method problem); real HBM roles = wrong assumption. If it fires, the rules are too loose.
- `HBM4` also matches `HBM4E`. Count them separately.
