---
id: ev-comp-digits-001
domain: competitor
source_type: desk_research
source_name: Digits
date: 2026-09-03
title: "Digits: Agentic General Ledger, positioning, and AI-native accounting"
confidence: indirect
product_area: competitive_intelligence
tags:
  - digits
  - agentic-general-ledger
  - bookkeeping
  - continuous-close
  - ai-native
---

# Digits: Agentic General Ledger, positioning, and AI-native accounting

## Raw evidence

### Company context

Digits bills itself as "the world's first Agentic General Ledger
(AGL)." Founded by serial entrepreneur Jeff Seibert. Backed by ~$100M
from Benchmark, SoftBank, GV, plus angel investors (Aaron Levie, Dick
Costolo, Kevin Weil, etc.). Customers include Particle News, Wispr,
Partiful, Replika, Pogo, Kino AI, and "thousands of others."

### What Digits does (shipped, live)

**Agentic General Ledger (AGL)**

- Custom-trained ML models (not general-purpose LLMs), trained on
  $875B+ in real SMB transactions.
- Auto-books 95%+ of transactions in real time as they arrive.
- Production accuracy: 97.8% (claimed).
- Vector similarity models that learn from each user's prior
  categorization decisions.
- Recurrence detection on the first occurrence of a transaction.
- Auto-flagging of anomalies, duplicates, items needing review.
- "Inbox" workflow for reviewing exceptions — manage by exception,
  not every transaction.

**Embedded verification**

- Separate AI layer checks every categorization against the firm's
  historical treatments and accounting standards before posting.
- "The AI executing the work and the AI verifying the work operate
  inside the same system of record" — no truth drift, no sync lag,
  no second ledger.

**Continuous / Agentic Close**

- Books stay current throughout the period (categorize, reconcile,
  verify, post continuously).
- Month-end becomes a review, not a sprint.
- Orchestrates reconciliations, variance detection, review workflows
  on top of the AGL.
- Close checklists surface what still needs human attention.

**Automated Schedules** (announced May 7, 2026, live on Firms plans)

- Fixed assets, prepaid expenses, accrual workflows.
- System detects schedule-worthy transactions automatically.
- Drafts depreciation/amortization entries with context.
- Posts recurring journal entries period after period.
- Subject to accountant approval.
- Revenue recognition and accrued expenses coming next.

**Other shipped features**

- Invoicing and bill pay (drag, drop, approve, pay).
- Live dashboards and financials (P&L, Balance Sheet, Cash Flow).
- Cash flow and runway tracking.
- AR/AP aging, dimensional accounting (department, location,
  project).
- Multi-entity accounting and inter-company transactions (Advanced).
- Ask Digits: natural-language financial analysis assistant.
- Receipt, contract, invoice upload and organization.
- Vendor and customer tracking with auto-enriched directory.

**Integrations**

- 12,000+ banks/cards via Plaid.
- Native: Mercury, Ramp, Gusto, BILL, Stripe, Arc.
- QuickBooks COA import; Xero / Puzzle / Excel CSV import.
- Digits Connect REST API.
- MCP server (live): Claude, ChatGPT, Cursor, other MCP clients.
- Tax partner network, one-click tax package handoff.

### Positioning / language

- "AI-powered accounting software that does the work for you."
- "The world's first Agentic General Ledger."
- "Books that keep themselves."
- "AI learns your business — no rules to manage."
- "Human in the loop — Managed accounting" (on homepage: sign up
  and invite your existing accountant, or find one through Digits'
  Accounting Firm Directory).
- "24/7 AI bookkeeping" / "real-time categorization."
- Not "AI agent" or "AI employee" — the agent is the ledger itself.
  The user does not configure or name an agent. The system is the
  agent.

### Pricing

- Essentials: $65/mo. Solopreneurs / early-stage. AI bookkeeping,
  invoicing, bill pay, dashboards, Ask Digits, 12K+ bank
  integrations.
- Core: $100/mo (most popular). Small business. Adds Stripe/Ramp/
  BILL integrations, AR/AP aging, custom dashboards, dimensional
  accounting.
- Advanced: custom pricing. Multi-entity, close automation, custom
  management reporting, inter-company transactions.
- Digits for Firms: separate plans (not captured in this pass).

### Sources

- https://digits.com/
- https://digits.com/product/bookkeeping/
- https://digits.com/accountants/
- https://digits.com/agl/
- https://digits.com/product/agentic-close/
- https://digits.com/blog/what-is-continuous-close/
- https://help.digits.com/business-getting-started/setup-methods
- https://softwareconnect.com/reviews/digits-accounting-software/
- https://www.bill.com/blog/digits-names-bill-an-api-partner

## Notes

### Key observations

1. **The agent IS the ledger**: Digits does not ask users to build,
   configure, or name an agent. The entire GL is agentic. This is a
   fundamentally different abstraction from Notion (configure an
   agent), Viktor (delegate to an employee), Zapier (build a
   workflow), or Karbon (attach agents to practice management). The
   AI is not a layer on top; it is the system of record.

2. **Custom ML, not LLMs**: Digits explicitly uses custom-trained
   models on $875B in real transactions, not general-purpose LLMs.
   This is a domain-specific bet that accounting patterns are
   learnable from data at scale — contrasts with Karbon/Kai using
   conversational AI and LLM-based agents.

3. **Manage by exception**: The UX model is "inbox of exceptions" —
   95%+ posts automatically, humans review the rest. This inverts
   the traditional bookkeeping workflow (human categorizes → system
   records) to (system categorizes → human reviews exceptions).

4. **Continuous close, not period-end sprint**: Because categorization
   and reconciliation happen as transactions arrive, month-end
   becomes a review checkpoint, not a backlog. This directly
   competes with Aider's period close automation (which still
   operates on a period cadence with checklists).

5. **Replaces the GL, not the practice**: Digits is a general ledger
   replacement (competes with QuickBooks/Xero). Karbon/Aider is
   practice management (sits on top of a GL). These are different
   layers of the stack. Both could be competitors to XeroForce but
   in different ways — Digits threatens Xero the product; Karbon
   threatens the workflow layer Xero doesn't own.

6. **Xero as import source**: Digits supports Xero COA import via
   CSV. Digits is explicitly positioning as a migration destination
   from Xero (and QuickBooks, Puzzle, Excel). This is a direct
   competitive threat to Xero's core product.

7. **MCP as platform strategy**: Like Karbon and Zapier, Digits ships
   an MCP server. The pattern is clear: accounting data as tools for
   external AI agents. This positions all three as both AI products
   and AI tool providers.

8. **Embedded verification**: The "two AI layers" claim (one executes,
   one verifies, same system of record) is a trust/audit story. More
   sophisticated than Karbon's "approve/edit/reject" or Notion's
   missing activity logs. Needs hands-on verification.

Follow-ups:

- Hands-on trial to verify the 95%+ auto-booking claim.
- Whitepaper and Digits-vs-Xero cadence question: see
  `ev-comp-digits-002`, `ev-comp-digits-003`.
- What does the exception inbox actually look like?
- Digits for Firms pricing and features.
