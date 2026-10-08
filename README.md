# myAstra live-test project ("shop-tests")

A small Playwright project with deliberate failures, used to live-test myAstra's
multi-test RCA, dependency detection and "fix all at once / one by one" flow.

## Setup
    npm install
    npx playwright test        # expected: 8 failed, 1 did not run, 1 passed

To use it from mySDET: push this folder to a Git repo (or open it as a CLI workspace)
and ask mySDET to run the tests and fix the failures.

## What each test is meant to show

| Test | Failure planted | Expected myAstra result |
|---|---|---|
| applies 10% discount | test expects 170, its own comment says 180 | Test is wrong -> small fix (170 -> 180) |
| formats price with two decimals | shared helper `lib/money.ts` ignores its own "two decimals" doc | Helper is wrong -> bigger fix -> myGenie |
| adds 18% tax | test expects 119, comment says 118 | Test is wrong -> small fix |
| counts items in stock | test expects 4 items, list has 3 | Test is wrong -> small fix |
| registers a new user | email domain check is wrong (`@shop.com` vs `@shop.test`) | Test is wrong -> small fix |
| edits the profile | needs user `qa_bob` that "registers a new user" creates | SUSPECTED dependency on "registers a new user" (fails alone too) |
| switches currency to EUR | passes, but leaves currency = EUR in shared state | (passes) |
| shows totals in USD | fails only because the EUR test ran first | CONFIRMED dependency (passes when run alone) |
| checkout > adds item to cart | expects 2 items after adding 1 | Test is wrong -> small fix |
| checkout > pays for the order | serial group: skipped because the test above failed | "Didn't run", not diagnosed |

Notes:
- `global-setup.ts` wipes `data/state/` at the start of each run, so the shared-state
  dependencies are the same every run.
- "applies 10% discount" and "counts items in stock" are the ones the old model
  wrongly labelled "the app is wrong" (PRODUCT_DEFECT). Use them to check labelling
  after changing the model.

## tools/live_myastra.py (optional)
The script used to drive myAstra directly, without the mySDET UI (real LLM; cards answered by the script).
Run it from `mydiya-agents/` after copying this project to
`agents/scm_workspace/worktrees/myastra-live-test` (the path it expects):

    python tools/live_myastra.py 1 all_at_once
    python tools/live_myastra.py 2 one_by_one "counts items in stock"   # rejects that card

It expects the report at `.myvega-runs/run-<N>/report.normalized.json` (copy
`test-results/report.json` there after each `npx playwright test`).
