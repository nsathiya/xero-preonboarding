---
id: ev-comp-digits-002
domain: competitor
source_type: docs
source_name: Digits
date: 2026-09-03
title: "Digits whitepaper: LLMs vs AGL on transaction categorization"
confidence: indirect
artifact_path: artifacts/competitors/digits/ev-comp-digits-002/beyond-the-hype-evaluating-llms-vs-digits-agl.pdf
product_area: competitive_intelligence
tags:
  - digits
  - agl
  - llm
  - categorization
  - whitepaper
---

# Digits whitepaper: LLMs vs AGL on transaction categorization

## Raw evidence

Paper: *Beyond the AI Hype: Evaluating LLMs vs. Digits AGL® for
Accounting Tasks.* Jo Pu, Hannes Hapke, Cole Howard, Siva
Manivannan, Chris Hassell. `ml@digits.com`. Digits Financial,
Inc. June 9, 2026. Fourth revision of the study.

Artifact:
`artifacts/competitors/digits/ev-comp-digits-002/beyond-the-hype-evaluating-llms-vs-digits-agl.pdf`

This is Digits-authored research. Treat numbers as their claims
on their dataset, not independent replication.

### What they measured

Task: predict the correct category from a business-specific Chart
of Accounts for a given transaction.

Dataset: 2,000 transactions from **4 randomly selected small
businesses that use Digits**. 88% / 12% debit / credit. CoA size
15–128 categories. US GAAP accountants reviewed expected
categories.

Human baseline: 12 outsourced accountants (June 2025), 4 teams of
3, majority vote, **same information as the LLMs** (no extra firm
history). Aggregate accuracy **79.1%**. 10.4% of transactions had
in-group disagreement. ~34 seconds per transaction.

14 frontier LLMs (one-shot JSON classification, then top models
in a 4-turn agent harness with `google_search` and
`get_historical_transactions`).

Hallucination defined as: suggested category not in the business
CoA.

### Headline numbers (Digits')

- No general-purpose LLM > **81%** one-shot; none > **87%** in
  the agent harness.
- 6 LLMs beat the 79.1% human baseline with zero hallucinations
  in the harness-era results. Top LLM beats human by 1.6%
  (Claude Opus 4.8 medium, one-shot).
- Agent harness: +4.5 to +9.1 pp accuracy vs one-shot; latency
  **5×–22×**; tokens **8×–29×**. Zero hallucinations in harness.
- Digits AGL® vs top LLM: **+17.1 pp** one-shot categorization,
  **+11 pp** in multi-turn agentic tasks, **1,634×** lower
  latency, **311×** lower token cost.
- AGL: **40 ms** per task, average **64 tokens**.
- Claude Opus 4.8 high (harness): **86.8%** accuracy, **65.38 s**,
  ~19.9k tokens — still **11 pp** behind AGL.

Digits AGL® "employs a combination of purpose-built machine
learning models and frontier LLMs, with the proprietary
components trained and hosted entirely in-house."

### Digits' interpretation (their words)

Accounting classification is subjective and firm-specific.
General-purpose world knowledge, even with retrieval, hits a
ceiling. The limiting factor is "absence of deeply embedded
domain context," not reasoning capacity. Raising reasoning
effort does not reliably improve accuracy and costs more.

They do **not** argue continuous close vs month-end close in
this paper. The paper is about **categorization architecture**
(specialized ML vs LLM / agent harness).

## Notes

This paper is the technical case for **building the GL from the
ground up** with in-house models, not wrapping Xero/QBO in an
LLM agent. Latency and cost at volume are the production
argument (40 ms vs tens of seconds). Accuracy is the quality
argument (AGL vs 87% LLM ceiling).

Caveats that matter:

- Dataset is 4 **Digits customers**. AGL has home-field data;
  LLMs do not get Digits' training corpus.
- Humans and one-shot LLMs were denied historical firm context;
  the harness and AGL were not equivalently constrained.
- Digits wrote and published the benchmark.
- 10.4% human disagreement shows the task is genuinely
  ambiguous — "accuracy" has a ceiling set by judgment, not
  just model quality.

Follow-ups:

- Independent or customer-side check of the 95%+ / 97.8%
  production claims vs this 2,000-row lab set.
- Does XeroForce need a specialized categorizer, or is an LLM
  harness "good enough" at month-end volumes?
