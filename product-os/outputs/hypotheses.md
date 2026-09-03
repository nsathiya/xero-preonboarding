# Hypothesis register (living)

Testable beliefs. Update the same card as new evidence arrives.
Source of truth: `beliefs/hypotheses.yaml`.

## The category bet is scoped objects + triggers, not agent UX

- **ID**: `hyp-001`
- **Status**: proposed
- **Confidence**: low-medium
- **Derived from**: `ins-001`, `ins-005`

Knowledge-work products still constrain work (objects, access, approvals, steps) rather than offering open-ended autonomy. They do not share one abstraction. Notion puts scoped objects + triggers on a named agent. Viktor puts a brief on one employee. Zapier puts AI inside a trigger-action Zap and makes Copilot fill that canvas. Same category, three units.

**Supporting evidence** (5 in corpus):
- `ev-agent-notion-001` — Notion: Collect customer feedback template (hands-on) (Notion Custom Agents)
- `ev-agent-notion-002` — Notion: Connect Slack as a trigger (hands-on) (Notion Custom Agents)
- `ev-agent-notion-003` — Notion: Custom feedback triage agent with email write + HITL (Notion Custom Agents)
- `ev-agent-viktor-001` — Viktor: Slack-first onboarding (hands-on) (Viktor)
- `ev-agent-zapier-001` — Zapier: first automation (Copilot + Zap, not Agents) (Zapier)

**Assumptions:**
- The first Zapier pass (a Zap, not an Agent) is the default path, not a detour
- Custom-build (Notion) still used the same trigger / instructions / tools model
- Viktor's Slack-proposed pipeline is the intended setup path, not a fallback

**What would strengthen:**
- (HubSpot skipped — no access)
- A Zapier Agent that is still a workflow graph underneath

**What would falsify:**
- A common path that is mostly open-ended web/API autonomy with little product-object or step scaffolding

## Slack "message posted" is not fire-on-every-message

- **ID**: `hyp-002`
- **Status**: proposed
- **Confidence**: low-medium
- **Derived from**: `ins-002`

Notion's Slack channel trigger does not fire on every public-channel post in practice. A plain post created no session; after Save, an @Notion AI mention produced a run, a database write, and a Read & Reply thread confirmation.

**Supporting evidence** (1 in corpus):
- `ev-agent-notion-002` — Notion: Connect Slack as a trigger (hands-on) (Notion Custom Agents)

**Assumptions:**
- The first miss was missing @mention and/or unsaved settings, not the 36-hour Slack sync toast

**What would strengthen:**
- After Save, another unmentioned public-channel post still does not fire
- Docs or UI that say Slack triggers require @Notion AI

**What would falsify:**
- After Save, a plain (no mention) public-channel post creates a session and a feedback row

## Accountability for writes is not a first-class builder surface

- **ID**: `hyp-003`
- **Status**: proposed
- **Confidence**: medium
- **Derived from**: `ins-003`

Notion governs writes at connect-time (OAuth + toggles + optional Require confirmation) and governs interpretation in instructions. Help promises activity logs, version history, and reversible runs; the researcher could not find activity logs on these agents. Viktor gates Notion writes in Slack (Approve / Always approve). Post-hoc accountability is not first-class on either pass. Notion workspace AI analytics and the documented audit log are Enterprise; Viktor Usage was not opened.

**Supporting evidence** (6 in corpus):
- `ev-agent-notion-001` — Notion: Collect customer feedback template (hands-on) (Notion Custom Agents)
- `ev-agent-notion-002` — Notion: Connect Slack as a trigger (hands-on) (Notion Custom Agents)
- `ev-agent-notion-003` — Notion: Custom feedback triage agent with email write + HITL (Notion Custom Agents)
- `ev-agent-notion-004` — Notion Help: Custom Agents are persistent workspace objects (Notion Help)
- `ev-agent-notion-005` — Notion: Help promises Activity logs; not visible on this workspace (Notion Custom Agents)
- `ev-agent-viktor-001` — Viktor: Slack-first onboarding (hands-on) (Viktor)

**Assumptions:**
- Activity logs are not merely renamed to Recent chats / session steps
- Viktor Always approve is a consent shortcut, not an audit log

**What would strengthen:**
- Version history also missing on the same agents
- (HubSpot skipped — no access)
- Zapier Zap history empty after publish; confirm whether live runs appear
- Viktor Usage shows credits but not a per-write audit

**What would falsify:**
- An Activity tab (or equivalent) that is a real per-run log plus unsend on this plan
- Viktor Usage (or Slack) exposing a reversible action log for Always-approved writes

## Messaging-first setup trades speed for inspectability

- **ID**: `hyp-004`
- **Status**: proposed
- **Confidence**: medium
- **Derived from**: `ins-004`

If the primary place to configure a workflow is Slack/Teams chat (plan + Approve), operators get a fast "employee" install but lose streaming, loading, config knobs, and a saved spec they can inspect. A later session still showed Tasks at 0. Viktor named Customer Feedback Weekly Digest as active in the backend and called the empty portal a display bug, then said the Monday 9 AM job will run anyway. Sign-out and Calendar view also empty. Slack / the employee is the system of record. The portal is optional and can lie. Vertical templates stay thin because chat is a bad surface for schema work.

**Supporting evidence** (2 in corpus):
- `ev-agent-viktor-001` — Viktor: Slack-first onboarding (hands-on) (Viktor)
- `ev-agent-viktor-003` — Viktor: Tasks portal empty; employee says backend task is live (Viktor)

**Assumptions:**
- The Slack proposal + Approve path is the intended custom-task setup, not a fallback
- Viktor's "display bug" claim is at least directionally right that something exists off-portal

**What would strengthen:**
- Monday 9 AM delivers (or does not). Either way the portal was not the truth. Sign-out and Calendar already failed.

**What would falsify:**
- Slack-created work reliably appears on Tasks with steps, scopes, test, retry
- Slack setup itself streams progress and exposes config knobs
- (Zapier already puts setup on a canvas; that strengthens the contrast, it does not falsify Viktor)

## XeroForce has to pick a point on define-vs-delegate, not a feature set

- **ID**: `hyp-005`
- **Status**: proposed
- **Confidence**: low-medium
- **Derived from**: `ins-005`

If XeroForce copies Zapier, users keep high workflow control and AI lives in selected steps. If it copies Notion, users configure a persistent agent without drawing the full graph. If it copies Viktor, users delegate the outcome and give up an explicit plan. Accounting work that is really a pipeline leans Zapier. Work that needs a named, scoped specialist leans Notion. Work that is "just get it done" leans Viktor and is the weakest to govern. The Zapier first pass published a Zap, not an Agent. The Viktor pass never showed a task editor.

**Supporting evidence** (7 in corpus):
- `ev-agent-notion-001` — Notion: Collect customer feedback template (hands-on) (Notion Custom Agents)
- `ev-agent-notion-003` — Notion: Custom feedback triage agent with email write + HITL (Notion Custom Agents)
- `ev-agent-notion-004` — Notion Help: Custom Agents are persistent workspace objects (Notion Help)
- `ev-agent-viktor-001` — Viktor: Slack-first onboarding (hands-on) (Viktor)
- `ev-agent-viktor-002` — Viktor docs: brief an employee, do not build a workflow (Viktor)
- `ev-agent-viktor-003` — Viktor: Tasks portal empty; employee says backend task is live (Viktor)
- `ev-agent-zapier-001` — Zapier: first automation (Copilot + Zap, not Agents) (Zapier)

**Assumptions:**
- The missing Viktor editor is not hiding a Notion-like Settings object
- Zapier's default path is Zap+Copilot, not the Agents product
- Accounting operators will want named ownership of high-risk workflows

**What would strengthen:**
- (HubSpot skipped — no access)
- A Zapier Agent that is still a Zap graph underneath
- A Xero workflow (e.g. invoice exception) that is unsafe to leave as "Viktor figures out the steps"

**What would falsify:**
- Tasks list showing the digest with a Settings-like editor
- A Zapier Agent that is a true persistent agent (not a Zap) and is the default create path
- A later product that is agent + employee + workflow with no real tradeoff

## Zapier will not replace the workflow graph with an agent

- **ID**: `hyp-006`
- **Status**: proposed
- **Confidence**: low-medium
- **Derived from**: `ins-005`

Zapier believes users still want an explicit workflow graph. AI should make selected parts of that graph adaptive or autonomous, not retire Trigger → Action. Copilot, AI by Zapier, Human in the Loop, and even the Agents tour all sit on top of steps, tests, and publish. If that bet is right, XeroForce should keep a visible pipeline and put models inside steps. If it is wrong, the graph becomes legacy chrome and the Agents product (or something like Viktor) eats the default path.

**Supporting evidence** (1 in corpus):
- `ev-agent-zapier-001` — Zapier: first automation (Copilot + Zap, not Agents) (Zapier)

**Assumptions:**
- The first published Zap is the intended default, not a fallback from a failed Agent create
- "AI teammates" marketing does not already mean the graph is being deprecated

**What would strengthen:**
- A Zapier Agent that is still a step graph underneath (trigger, AI step, actions, test, publish)
- HITL as another step in the same graph, not a different object
- Other products keeping canvas-plus-AI-step rather than employee-in-chat

**What would falsify:**
- Default create path is an Agent with no Trigger → Action canvas
- Copilot shipping a black-box employee that hides steps after publish

## Digits is the more dangerous competitor because it replaces the GL, not just the workflow

- **ID**: `hyp-007`
- **Status**: proposed
- **Confidence**: low-medium
- **Derived from**: `ins-006`

Karbon/Aider adds AI on top of Xero (or QBO). That is a workflow-layer threat: firms might do period close and advisory in Karbon, not Xero. But the GL stays. Digits replaces the GL entirely with an agentic system — if a firm migrates to Digits, Xero loses the system of record. An agentic GL that auto-books 95%+ of transactions makes the traditional categorize-then-reconcile GL feel manual. XeroForce defending the GL may matter more than XeroForce adding workflow features.

**Supporting evidence** (4 in corpus):
- `ev-comp-digits-001` — Digits: Agentic General Ledger, positioning, and AI-native accounting (Digits)
- `ev-comp-digits-002` — Digits whitepaper: LLMs vs AGL on transaction categorization (Digits)
- `ev-comp-digits-003` — Digits vs Xero page: continuous close as the differentiator (Digits)
- `ev-comp-aider-001` — Aider (Karbon): positioning, AI agents, period close automation (Karbon / Aider)

**What would strengthen:**
- Hands-on Digits trial confirms 95%+ auto-booking in practice
- SMB firms citing Digits as reason to leave Xero
- Digits for Firms growing adoption among Xero partner firms

**What would falsify:**
- Digits auto-booking accuracy much lower in practice than claimed
- SMBs unwilling to leave their GL (switching cost too high)
- Xero ships agentic categorization/reconciliation that matches Digits

## The competitor trust model is ahead of the agent-builder trust model

- **ID**: `hyp-008`
- **Status**: proposed
- **Confidence**: low
- **Derived from**: `ins-003`, `ins-006`, `ins-007`

Digits ships embedded verification (two AI layers in the same system of record) and manage-by-exception UX. Karbon ships approve/edit/reject with audit trail via Agent Management System. Both are more concrete than Notion's missing activity logs, Viktor's empty portal, or Zapier's optional HITL step. If XeroForce copies agent-builder trust patterns instead of competitor trust patterns, it will underdeliver on accountability for financial writes.

**Supporting evidence** (5 in corpus):
- `ev-comp-digits-001` — Digits: Agentic General Ledger, positioning, and AI-native accounting (Digits)
- `ev-comp-aider-001` — Aider (Karbon): positioning, AI agents, period close automation (Karbon / Aider)
- `ev-comp-aider-003` — Aider tutorial: period-close dashboard, firm template, Ask Client (Aider (Karbon) tutorial)
- `ev-agent-notion-005` — Notion: Help promises Activity logs; not visible on this workspace (Notion Custom Agents)
- `ev-agent-viktor-003` — Viktor: Tasks portal empty; employee says backend task is live (Viktor)

**What would strengthen:**
- Hands-on Digits exception inbox shows rich context for reviewer
- Karbon Agent Management System audit trail is detailed and usable

**What would falsify:**
- Digits verification layer is cosmetic — errors slip through at similar rates
- Karbon audit trail is shallow or hard to use in practice

## If XeroForce stays on agentic ledger workflows, Karbon takes the rest of the client lifecycle

- **ID**: `hyp-009`
- **Status**: proposed
- **Confidence**: low
- **Derived from**: `ins-006`, `ins-009`, `ins-010`

Karbon's role list is a scope claim — Bookkeeper (workpapers, reconcile, client follow-up), Tax Admin (returns, compliance, summaries), Fractional CFO (forecasts, what-ifs, client-ready reports), Onboarding Specialist (collect, validate, configure). Aider's acquisition list adds management reports and advisory dashboards. XeroForce focusing on agentic workflows inside the GL leaves reports, onboarding, tax ops, and billing as Karbon's default. Accounting being workflow-defined makes that land-grab cheaper for Karbon than it would be in an MSP-like industry.

**Supporting evidence** (2 in corpus):
- `ev-comp-aider-002` — Karbon: role-based agents, 40-hour claim, workflow-defined accounting (Karbon / Aider)
- `ev-comp-aider-001` — Aider (Karbon): positioning, AI agents, period close automation (Karbon / Aider)

**What would strengthen:**
- XeroForce brief that names ledger workflows and omits reports / onboarding / tax
- Firms using Karbon for reports and client ops while keeping Xero as GL

**What would falsify:**
- XeroForce scope already includes client reports and full-lifecycle ops
- Karbon Agents stay vaporware and firms do lifecycle work in Xero

## Role agents work in accounting because the jobs are shared; they would fail in MSP-like variance

- **ID**: `hyp-010`
- **Status**: proposed
- **Confidence**: low
- **Derived from**: `ins-005`, `ins-009`, `ins-010`

Aider can ship one Monthly Close - Accrual template onto 82 clients because close work is shared enough to teach as workflow-plus-tool. MSP training that only sells the tool, with high workflow variance, cannot do that. Whether Karbon can also ship Bookkeeper / Tax Admin / fCFO as named teammates is a separate, untested claim — we have not seen Agents. If the shared-job bet is right, XeroForce can be opinionated about close. If it is wrong, firms will reject templates the way MSPs reject one-size playbooks.

**Supporting evidence** (2 in corpus):
- `ev-comp-aider-002` — Karbon: role-based agents, 40-hour claim, workflow-defined accounting (Karbon / Aider)
- `ev-comp-aider-003` — Aider tutorial: period-close dashboard, firm template, Ask Client (Aider (Karbon) tutorial)

**What would strengthen:**
- Customer evidence that close / onboarding steps look the same across firms
- More templates beyond Monthly Close - Accrual applied at similar scale

**What would falsify:**
- Firms needing heavily custom close that a shared template cannot absorb
- Hands-on Karbon Agents (still unseen) that require each firm to specify the whole job

## Continuous close may create work the way more-frequent MSP scans do — verify with users

- **ID**: `hyp-011`
- **Status**: proposed
- **Confidence**: low
- **Derived from**: `ins-011`, `ins-006`

Digits now distinguishes fast month-end (automate the sprint; still a sprint) from continuous close (rebuild the GL; no backlog). They say bolt-on AI on Xero cannot do the second because of truth drift. Their own 'stay traditional if' list matches the MSP-scan cut: <5 clients, clients not asking for current reporting, monthly cadence still fits. Alternative still open: even for larger books, a mid-month exception drip can be more work than one automated close if nobody uses Tuesday-afternoon numbers. If that is right, XeroForce can ship a faster month-end on Xero and cover most of the market Digits concedes. If clients are asking for current numbers and week-one cleanup is the burnout, a smarter sprint will not be enough. Sharper framing than 'do they want it': continuous close is a *behaviour migration*, not a feature. The firm has to move from batch review to continuous exception handling, which changes staffing, scheduling, and what clients expect — which is why Digits had to rebuild the ledger, and also why a firm might decline even if the technology works. So the question is whether firms are willing to change behaviour, and whether adoption needs an explicit incentive to happen at all.

**Supporting evidence** (4 in corpus):
- `ev-comp-digits-004` — Digits blog: What is continuous close (Digits)
- `ev-comp-digits-003` — Digits vs Xero page: continuous close as the differentiator (Digits)
- `ev-comp-digits-002` — Digits whitepaper: LLMs vs AGL on transaction categorization (Digits)
- `ev-comp-digits-001` — Digits: Agentic General Ledger, positioning, and AI-native accounting (Digits)

**What would strengthen:**
- Accountants who ignore intra-month flags or say flags create extra review
- SMBs / firms who only need books at month-end, tax, or lender ask
- Firms with >5 clients who still prefer a batch close
- Firms who say the staffing/scheduling change is the blocker, not the technology

**What would falsify:**
- Firms citing always-current cash/P&L as why they left Xero
- Continuous inbox that is quieter than Xero's month-end queue
- Clients actually requesting treated numbers mid-period (the Stripe Tuesday story)
- Firms who migrated cadence without any incentive beyond the software

## Accounting adopts agents faster than engineering because the work is checkable — unless error cost dominates

- **ID**: `hyp-012`
- **Status**: proposed
- **Confidence**: low
- **Derived from**: `ins-014`, `ins-013`, `ins-006`

Verifiability, not absence of judgment, is what distinguishes accounting from engineering here. A categorisation can be graded against firm history, prior decisions, and a ledger that must balance; a software design decision cannot. That is why a verification layer is buildable in accounting and largely is not in engineering, and it predicts higher adoption. Against that, consequence severity raises the confidence threshold required before anyone lets an agent act: a bad commit is reverted in review, a bad posting may need a restatement and has statutory exposure. So the prediction is conditional — accounting adopts faster where errors are cheap to correct (coding, categorisation, reconciliation) and slower where they are not (anything filed, remitted, or reported externally), rather than faster or slower overall. Note this is not the same claim as 'accounting needs little judgment', which Digits' own 10.4% human-versus-human disagreement contradicts.

**Supporting evidence** (3 in corpus):
- `ev-comp-digits-002` — Digits whitepaper: LLMs vs AGL on transaction categorization (Digits)
- `ev-comp-digits-001` — Digits: Agentic General Ledger, positioning, and AI-native accounting (Digits)
- `ev-comp-aider-003` — Aider tutorial: period-close dashboard, firm template, Ask Client (Aider (Karbon) tutorial)

**Assumptions:**
- Digits' reported human disagreement rate is representative, not an artefact of their sample
- Firms distinguish reversible postings from filed/remitted outputs when deciding what to automate

**What would strengthen:**
- Accountants who accept automation on coding but not on anything filed
- Firms who say they trust an automated check more than a junior reviewer
- Adoption concentrated in reversible steps of the close

**What would falsify:**
- Blanket refusal to automate regardless of reversibility (then trust, not error cost, is the barrier)
- Firms automating filings readily (then consequence severity is not the brake)
- Accounting adoption no higher than engineering despite verifiability
