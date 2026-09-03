# Competitor landscape: Aider (Karbon) vs Digits

**Live scorecards (current read per competitor, updated in place):**

- `notes/competitors/scorecard/aider.md`
- `notes/competitors/scorecard/digits.md`
- Convention: `notes/competitors/scorecard/_scorecard-guide.md`

This file is the cross-competitor comparison. Scorecards hold the
per-competitor detail and the `VERIFIED` / `CLAIMED` / `UNSEEN`
status of each claim.

## The stack position matters more than the feature list

Aider/Karbon and Digits are both "AI for accounting" but they
compete at different layers:

| | Digits | Aider (Karbon) |
|---|---|---|
| **Layer** | General ledger (replaces QBO/Xero) | Practice management (sits on top of a GL) |
| **What the AI does** | IS the system of record — auto-books, reconciles, verifies | Intelligence layer on existing workflows — checklists, flags, client questions |
| **Agent abstraction** | The ledger itself is the agent. No user-configured agent. | Role-based agents (bookkeeper, fCFO) attached to practice workflows. Announced, not shipped. |
| **Shipped AI today** | Agentic GL (95%+ auto-booking), continuous close, automated schedules, Ask Digits | Period close automation, smart checklists, inline editing, client questions, AI doc validation |
| **Marketed but not shipped** | — | AI Agents, Kai (conversational coworker), agentic workflows |
| **Human oversight** | Manage by exception (inbox of low-confidence items), accountant approval on schedules | Approve/edit/reject agent outputs, audit trail via Agent Management System |
| **ML approach** | Custom-trained models on $875B real txns (not LLMs) | LLM-based conversational AI (Kai) + workflow automation |
| **MCP** | Yes (live) | Yes (announced June 2026) |
| **Xero relationship** | Migration destination (CSV import from Xero). Direct threat to Xero core. | GL-agnostic practice mgmt. Indirect threat — owns the workflow layer. |

## Connecting to the agent-builder define-vs-delegate axis

From `ins-005`:

```
More explicit workflow control ← Zapier — Notion — Viktor → More delegated agent autonomy
                                  Workflow → Agent → AI employee
```

Competitors extend this differently:

- **Karbon AI Agents (unseen)**: Article sells Viktor-like roles
  (Bookkeeper, Tax Admin, fCFO, Onboarding). No Agents tutorial or
  product pass yet. Do not place on this axis.
- **Aider period close (seen in tutorial)**: Not agents. Rules and
  a close workflow — Period Close Dashboard, firm template
  **Monthly Close - Accrual** on 82 clients (Built-in /
  Automatic-N-conditions), exception inbox, **Ask Client** batched
  to end of day.
- **Digits**: Off the axis entirely. Not "user builds agent" or "user
  delegates to employee." The **system is inherently agentic** — no
  configuration step, no agent object. Closer to "AI IS the product"
  than any of the agent builders.

## What this means for XeroForce

1. **Digits is the existential threat — and it is two bets, not
   one**: (a) rebuild the GL with specialized ML (`ev-comp-digits-002`);
   (b) change close **cadence** to continuous exceptions
   (`ev-comp-digits-003`). (a) does not prove users want (b).
   Automating month-end on Xero is a different product than a
   continuous inbox. Ask customers; MSP "more scans ≠ more value"
   is the check. Digits also lists Karbon as a partner — GL
   replacement and practice layer can stack.

2. **Karbon/Aider is the lifecycle threat, not just a workflow
   threat**: The role list covers workpapers, client follow-up,
   returns, forecasts, client-ready reports, onboarding, billing.
   If XeroForce stays on "agentic workflows" inside the ledger,
   Karbon is claiming the rest of the client lifecycle. Karbon
   Magazine (accounting articles + tutorial videos that teach
   workflow *and* tool) is a useful source because accounting
   work is unusually workflow-defined — unlike MSPs, where tools
   are sold and workflows vary.

3. **Both ship MCP**: The industry is converging on "accounting data
   as tools for AI." XeroForce should assume firms will want to plug
   Xero data into Claude/Cursor/ChatGPT, not just use Xero's own AI.

4. **Do not collapse close rules into Agents**: Aider period close
   is a real, seen product (rules, dashboard, Ask Client). Karbon
   AI Agents are a separate, unseen bet. Digits' AGL claims are
   specific and closer to a shipped engine. Weight observed
   products over role-metaphor marketing.

5. **Trust model comparison**:
   - Digits: embedded verification (two AI layers, same system of
     record). Accountant reviews exceptions.
   - Karbon: approve/edit/reject + audit trail (Agent Management
     System). Human signs off on everything.
   - Both are ahead of Notion (activity logs missing) and Viktor
     (portal disconnect, no inspectable object).
