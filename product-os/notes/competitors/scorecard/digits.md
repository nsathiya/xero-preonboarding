---
id: note-competitors-scorecard-digits-001
type: living_scorecard
effective_date: 2026-09-03
confidence: indirect
competitor: digits
---

# Digits — live scorecard

**Mutable. Overwrite in place.** Guide:
`notes/competitors/scorecard/_scorecard-guide.md`

**One-line read:** An AI-native general ledger that replaces Xero
rather than extending it, betting on two things at once — a
specialized categorization engine, and a continuous close cadence
that we have not yet validated anyone wants.

**Evidence on file:** `ev-comp-digits-001` (desk research),
`ev-comp-digits-002` (whitepaper, PDF on file),
`ev-comp-digits-003` (vs-Xero page), `ev-comp-digits-004`
(continuous close blog).
**Hands-on:** none yet.

## Scorecard

| Dimension | Current read | Status | Evidence |
|---|---|---|---|
| Stack position | Replaces the GL. Explicitly not a plugin on QuickBooks and not a close-accelerator beside a ledger. | `DOCS` | `002`, `004` |
| What the AI is | The ledger itself is agentic. No named assistant sitting on top. | `DOCS` | `001`, `004` |
| Unit the user creates | **Nothing.** No agent to configure, name, or share. You connect banks and work exceptions. Off the define-vs-delegate axis entirely. | `DOCS` | `001`, `004` |
| Cadence | Continuous — categorize, reconcile, verify, post as transactions arrive. They distinguish this from "fast month-end close," which they call a shrunken sprint. | `CLAIMED` | `004`, `003` |
| Autonomy vs control | 95% of transactions post without human intervention. Low-confidence items route to an exception queue. Automated Schedules draft depreciation/amortization entries subject to accountant approval. | `CLAIMED` | `001`, `004` |
| Trust / audit | Separate AI verification layer checks each categorization against firm history and standards **before** posting. Claimed benefit: no truth drift, because execution and verification share one system of record. Exception flags named: Missing, Date mismatch, Duplicate, Overmatched, plus an audit trail. | `CLAIMED` | `004`, `003` |
| Human workflow | Manage by exception. Inbox of low-confidence items, not review-every-transaction. Month-end becomes review and sign-off. | `CLAIMED` | `001`, `004` |
| Client interaction | Invite your existing accountant, or find one via their Accounting Firm Directory. Built-in comments across transactions/reports plus an Inbox. No per-transaction client Q&A observed (contrast Aider's Ask Client). | `DOCS` | `001`, `003` |
| Model approach | Custom-trained ML, explicitly not general-purpose LLMs, plus "some frontier LLMs" in the mix. Tiered: client-level → firm-level → global models, with fallback agents that research novel vendors. Vector similarity learns from prior decisions. | `DOCS` | `002`, `004` |
| Benchmarks / metrics | **Do not collapse these.** Whitepaper on file: 2,000 txns from 4 Digits businesses; AGL beats top LLM by 17.1pp one-shot / 11pp in harness; 40ms and ~64 tokens per task vs 1,634× latency and 311× tokens for Claude Opus 4.8 high; human baseline 79.1% with 10.4% in-group disagreement. Blog cites a *different* set: 93.5% on 17,792 txns, all frontier LLMs below 73%. Production claim: 97.8%. Same paper title, different numbers. | `DISPUTED` | `002`, `004` |
| Xero relationship | Direct GL competitor and migration destination — Xero CoA import via CSV. Comparison page frames Digits Core $100/mo vs Xero Established $90/mo, and characterizes Xero as "AI assistance added on top of traditional workflows." | `DOCS` | `001`, `003` |
| Ecosystem / MCP | MCP server live (Claude, ChatGPT, Cursor). Digits Connect REST API. Native: Mercury, Ramp, Gusto, BILL, Stripe, Arc. 12,000+ banks via Plaid. **Partners with Karbon** (also Ignition, Reach Reporting). | `DOCS` | `001`, `003` |
| Pricing | Essentials $65/mo, Core $100/mo, Advanced custom (multi-entity, close automation, inter-company). Unlimited users, billed per business/client rather than per seat. Digits for Firms plans not captured. | `DOCS` | `001`, `003` |
| Scope claimed | GL, bookkeeping, reconciliation, close, automated schedules, bill pay, invoicing, dashboards, financial reporting, Ask Digits. All-in-one so firms need fewer add-ons. | `DOCS` | `001`, `003` |
| Threat to XeroForce | **Existential, not adjacent.** If a firm migrates, Xero loses the system of record — XeroForce would have nothing underneath it. | — | `001`, `003` |
| Biggest unknown | Does anyone want continuous cadence? Digits' own "stay traditional if" list concedes: <5 clients, clients not asking for current reporting, monthly cadence still fits. | `UNSEEN` | `004` |

## The two bets (keep separate)

1. **Architecture** — specialized ML beats LLM-on-a-legacy-ledger for
   categorization. Accuracy, latency, cost. `ev-comp-digits-002`.
2. **Cadence** — work exceptions all month instead of batching at
   close. `ev-comp-digits-003`, `ev-comp-digits-004`.

(1) does not prove (2). A better categorizer could run as a month-end
job. XeroForce could take (1) without (2).

Digits' stated benefits for (2): client sees treated numbers same-day
(their Stripe-payout-Tuesday example); firm's week one shifts from
cleanup to advisory; exceptions surface while context is fresh;
capacity scales with judgment not volume; firm standards persist in
firm-level models instead of leaving with senior reviewers.

Open counter (`hyp-011`): a mid-month exception drip may be more work
than one contained close, especially for thin-staffed firms — the MSP
scan-frequency parallel. Digits partially concedes this.

## Caveats on their numbers

- Whitepaper dataset is 4 **Digits customers** — AGL has home-field
  training data; the LLMs do not.
- Humans and one-shot LLMs were denied historical firm context. AGL
  and the harness were not equivalently constrained.
- Digits authored and published the benchmark.
- 10.4% human-vs-human disagreement means the task has a judgment
  ceiling; "accuracy" is not a clean target.

## Next evidence to get

- Hands-on trial: verify 95% auto-post and what the exception inbox
  actually shows a reviewer.
- Customer interviews against Digits' own cut — are clients asking
  for current numbers, or is week-one cleanup the real pain?
- Reconcile the 17,792 / <73% figures against the 2,000 / 86.8%
  whitepaper.
- Digits for Firms pricing and what close automation includes.
- MCP server with Claude/Cursor in practice.

## Changelog

- **2026-09-03** — Created. Seeded from `ev-comp-digits-001`,
  `ev-comp-digits-002`, `ev-comp-digits-003`, `ev-comp-digits-004`.
  Split architecture from cadence. Marked benchmarks `DISPUTED`
  (blog and whitepaper cite different datasets under one title).
  Noted Karbon partnership, which softens a pure Digits-vs-Karbon
  framing.
