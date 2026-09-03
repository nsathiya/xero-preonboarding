---
id: ev-comp-digits-004
domain: competitor
source_type: docs
source_name: Digits
date: 2026-09-03
title: "Digits blog: What is continuous close"
confidence: indirect
url: https://digits.com/blog/what-is-continuous-close/
product_area: competitive_intelligence
tags:
  - digits
  - continuous-close
  - cadence
  - truth-drift
  - month-end
---

# Digits blog: What is continuous close

## Raw evidence

Article: [What Is Continuous Close? How AI Ends the Month-End
Cleanup Sprint](https://digits.com/blog/what-is-continuous-close/)
Team Digits, June 5, 2026.

This is Digits marketing / explainer. Claims are theirs.

### Definition they use

> Continuous close is an accounting workflow where the ledger
> categorizes, reconciles, and verifies transactions the moment
> they arrive. The books stay current throughout the month
> instead of being cleaned up at month-end.

Requires "an agentic ledger" that does that work **inside** the
ledger, not AI on top of a legacy close.

### Fast month-end vs continuous (their distinction)

> A fast month-end close is still a month-end close. Continuous
> close removes the catch-up process entirely.

Most "AI close" tools are fast-close tools: categorize faster,
find exceptions earlier, shrink the sprint from five days to
two. The sprint still exists because work still accumulates.

> AI can accelerate that process. It cannot fundamentally
> eliminate it unless the ledger itself is rebuilt for
> continuous accounting.

This is Digits' answer to "why not just automate month-end on
Xero": they say that is a different product (fast close), and
legacy ledgers (Xero, QuickBooks) were designed around periodic
catch-up.

### Stated benefits

**For the client (SaaS Stripe example):** payout hits the bank
Tuesday 2 pm. Traditional: cash movement is in the feed, correct
revenue treatment waits for the next close; "the reporting the
client would want to see today does not exist yet." Continuous:
treatment applied, reconciled, posted after verification;
"within minutes, the books are closer to current."

**For the firm:** multiply across thousands of txns / dozens of
clients. Traditional first week = catch-up. Continuous: recs
already ran, exceptions already surfaced, drafts waiting;
"first week of the month shifts from cleanup to advisory."

**Why they say it matters for firms:**

- Capacity scales with judgment/exceptions, not txn volume.
- Reporting closer to real time (not 5th–10th of the month).
- Cognitive load: exceptions when context is fresh, not a
  reconstruction sprint.
- Firm knowledge encoded in firm-level models instead of
  walking out with senior reviewers.

**95%** of transactions post without human intervention.
**97.8%** production accuracy (claimed). Trained on **$875B+**.

### When Digits says stay on month-end

Their own "Stay with the traditional month-end close if":

- Firm has **fewer than five clients**, and periodic catch-up
  is manageable.
- Clients are **not asking for current reporting**.
- Monthly reporting cadence still matches the client base.

"Choose continuous close if": growing / capacity bottleneck;
clients asking for current numbers; team burning out on the
sprint; want intelligence that compounds; evaluate on published
benchmarks.

### Truth drift (why bolt-on AI fails, in their telling)

When categorization/rec live in third-party tools via APIs, the
firm still has to check that the result synced, posted to the
right entity, and stayed consistent. That gap is **truth drift**.
Continuous close "only works when the intelligence lives inside
the system of record."

Digits "replaces the general ledger. It is not a categorization
plugin layered onto QuickBooks, and it is not a close-acceleration
tool running alongside an existing ledger."

### Architecture they describe

Tiered intelligence: client-level models, firm-level models,
global models, plus fallback agents that research vendors /
gather context on low-confidence items. Separate verification
layer before post.

### Benchmark numbers in this article (do not collapse with
`ev-comp-digits-002`)

This page: AGL **93.5%** on **17,792** transactions; every
frontier LLM tested (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash)
**below 73%**. Cites the same whitepaper title as
`ev-comp-digits-002`.

The June 9, 2026 whitepaper on file used **2,000** transactions
from **4** Digits businesses; top LLM harness reached **86.8%**.
Different dataset and model set. Same paper name. Do not treat
as one result.

## Notes

This is the clearest Digits statement of *why* continuous close,
not just *what*. Three claimed user values, all unverified:

1. **Freshness** — client sees treated numbers today (Stripe
   Tuesday example).
2. **Sprint removal** — firm week-one becomes review/advisory.
3. **Fresh context** — exceptions when the txn is still
   rememberable (this is their answer to "isn't a drip more
   work?").

They also concede the researcher's cut: if clients are not
asking for current reporting, or the book is tiny, stay on
month-end. That is the MSP-scan point in their own words.
Continuous close is for capacity + current-numbers demand, not
for every firm.

Their reply to "Xero can just automate month-end": yes, that
exists, they call it **fast close**, and they say it cannot
eliminate the backlog or truth drift without replacing the GL.
That is an architecture claim, not a user-want claim.

Follow-ups:

- Do clients actually ask for Tuesday-afternoon books, or is
  that a SaaS-founder story?
- Firms with >5 clients: is week-one cleanup the pain, or is
  a mid-month inbox the new pain?
- Reconcile the 17,792 / 73% numbers with the 2,000 / 86.8%
  whitepaper.
