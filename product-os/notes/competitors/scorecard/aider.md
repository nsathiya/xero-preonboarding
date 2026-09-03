---
id: note-competitors-scorecard-aider-001
type: living_scorecard
effective_date: 2026-09-03
confidence: indirect
competitor: aider_karbon
---

# Aider (Karbon) — live scorecard

**Mutable. Overwrite in place.** Guide:
`notes/competitors/scorecard/_scorecard-guide.md`

**One-line read:** A practice-management host whose *seen* product is
an opinionated period-close rules engine across a client portfolio,
and whose *marketed* product is a set of role-based AI teammates we
have not observed at all. Keep those apart.

**Evidence on file:** `ev-comp-aider-001` (desk research: acquisition,
release notes, feature pages), `ev-comp-aider-002` (Agents article,
40-hour claim, workflow-defined observation), `ev-comp-aider-003`
(tutorial screenshots — period close, screenshots on file).
**Hands-on:** none. **Agents product: never seen.**

## Scorecard

| Dimension | Current read | Status | Evidence |
|---|---|---|---|
| Stack position | Practice management on top of someone else's GL. Aider inline edits push to QuickBooks. Karbon is the system of management for firms. | `VERIFIED` | `003`, `001` |
| What the AI is — **seen** | Period-close **rules**. Checks are labeled Built-in or "Automatic - N Conditions." Not an agent. | `VERIFIED` | `003` |
| What the AI is — **marketed** | Role-based teammates modeled on jobs that already exist in a firm, split into Service Delivery (bookkeeping, payroll, tax) and Service Management (billing, triage, onboarding). | `CLAIMED` | `002`, `001` |
| Unit the user creates | Seen: a **firm template** (`Monthly Close - Accrual`, Active, applied to 82 clients, with Publish Template). Marketed: a role. **Do not place Karbon Agents on the define-vs-delegate axis yet.** | `VERIFIED` / `CLAIMED` | `003`, `002` |
| Cadence | Period-end. Rows are client × period (FY 2024, Oct 2025, Nov 2025). Contrast with Digits' continuous claim. | `VERIFIED` | `003` |
| Autonomy vs control | Checks flag; humans resolve. Operator reclassifies inline, thumbs-up, Mark as Reviewed. Marketed Agents: approve/edit/reject, "nothing executes without your sign-off," which trains them over time. | `VERIFIED` / `CLAIMED` | `003`, `002` |
| Trust / audit | Marketed: AI Agent Management System — enable/disable agents and capabilities, control per-agent data access, complete audit trail of every agent decision. None of this observed. | `CLAIMED` | `001`, `002` |
| Human workflow | Portfolio dashboard → exception category → line items. Dashboard columns: Progress (bar or "In Review"), Alerts (green Pass or red counts: 78, 47, 82), then Bank, Data Quality, Invoices, Balance Sheet, P&L, Additional. Example screen: "8 Uncategorized Transactions" with inline Account dropdowns. | `VERIFIED` | `003` |
| Client interaction | **Ask Client** panel bound to a specific transaction. Question, client reply, and attached receipt all return to that line. Batched: footer reads "Sends end of day (5pm, Dec 2)." Client replies via Karbon for Clients portal. AI Document Validation compares uploads against what was requested. | `VERIFIED` | `003`, `001` |
| Model approach | Unclear. Seen automation is rule/condition-based. Kai is conversational LLM-style. No published benchmark, no accuracy number, no training-data claim. Sharp contrast with Digits. | `UNSEEN` | — |
| Benchmarks / metrics | No product accuracy benchmark found. What exists is time-savings marketing: CEO Delaney, "firms using AI at an advanced level are saving up to 40 hours per employee each month" (Karbon's own research, about advanced AI users generally — **not** a measured Aider outcome). Separate number, same page: 19.9 hrs/week saved on Karbon PM. Third-party coverage of the State of AI report suggests ~18 hrs/month average. **Do not collapse these three.** | `CLAIMED` | `002` |
| Xero relationship | GL-agnostic practice management. QuickBooks write-back confirmed in the tutorial; Xero integration likely given Aider's NZ origins but **not** confirmed in these passes. Threatens the workflow layer, not the ledger. | `DISPUTED` | `003`, `001` |
| Ecosystem / MCP | Public MCP server announced June 2026. 80+ native integrations claimed. Gusto payroll integration. Digits lists Karbon as a partner. | `CLAIMED` | `001` |
| Pricing | Not captured. Period Close is live for all US customers; AI Agents are early beta with select firms; Kai is early access. | `UNSEEN` | `001` |
| Scope claimed | Wide. Roles cover workpapers, reconciliation, client follow-up, returns, compliance, client summaries, forecasts, what-if models, client-ready reports, entity validation, workflow configuration. Aider adds management reports and advisory dashboards. Effectively the full client lifecycle. | `CLAIMED` | `002`, `001` |
| Threat to XeroForce | Lifecycle land-grab. If XeroForce stays on agentic workflows inside the ledger, Karbon's claimed scope covers reports, onboarding, tax ops, and billing by default. | — | `002` |
| Biggest unknown | **What is a Karbon AI Agent, concretely?** Brief a Bookkeeper? Edit a graph? Fill a template? Everything about the agent model is currently marketing. | `UNSEEN` | — |

## Shipped vs marketed (the discipline for this competitor)

Seen in the tutorial, in order — this is how they teach it:

1. Name the manager's problem: no single view of client close;
   "status lives in weekly meetings and memory"; relevant at 15 or
   15,000 clients; capacity issues surface only after costing time.
2. Portfolio dashboard with exception counts per check category.
3. One firm template pushed to 82 clients.
4. Line-item work: reclassify, Ask Client, batched end-of-day send.

Workflow **and** tool, taught together. That only works because the
close is standardized enough to template — the contrast with MSPs,
where vendors sell tools and workflows vary widely (`ins-010`).

Not seen anywhere: Bookkeeper, Tax Admin, Fractional CFO, Onboarding
Specialist, Kai, Agent Management System, audit trail.

## Next evidence to get

- **Karbon AI Agents tutorial or early beta.** Highest value. Nothing
  else resolves the agent-model question.
- Does "Automatic - N Conditions" open a real rule editor?
- Confirm Xero vs QuickBooks write-back from the exception inbox.
- Karbon pricing tiers; what is add-on vs included.
- The State of AI in Accounting report behind the 40-hour claim.
- More Karbon Magazine — flagged as a genuinely good accounting source.

## Changelog

- **2026-09-03** — Corrected the agent-model row. Earlier read placed
  Karbon near Zapier by inferring from the host product; the Agents
  article actually sells Viktor-like roles. Then narrowed further:
  the tutorial is period-close **rules**, which is not evidence about
  Agents either. Agents now `UNSEEN` rather than characterized.
- **2026-09-03** — Added tutorial rows (dashboard, template, Ask
  Client) as `VERIFIED` from `ev-comp-aider-003`.
- **2026-09-03** — Created. Seeded from `ev-comp-aider-001`,
  `ev-comp-aider-002`, `ev-comp-aider-003`. Separated the three
  time-savings numbers.
