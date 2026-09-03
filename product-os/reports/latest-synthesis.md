# Synthesis report

Deterministic render of the living belief register plus corpus coverage.

## Evidence in corpus

- `ev-agent-notion-001` — Notion: Collect customer feedback template (hands-on) (Notion Custom Agents)
- `ev-agent-notion-002` — Notion: Connect Slack as a trigger (hands-on) (Notion Custom Agents)
- `ev-agent-notion-003` — Notion: Custom feedback triage agent with email write + HITL (Notion Custom Agents)
- `ev-agent-notion-004` — Notion Help: Custom Agents are persistent workspace objects (Notion Help)
- `ev-agent-notion-005` — Notion: Help promises Activity logs; not visible on this workspace (Notion Custom Agents)
- `ev-agent-viktor-001` — Viktor: Slack-first onboarding (hands-on) (Viktor)
- `ev-agent-viktor-002` — Viktor docs: brief an employee, do not build a workflow (Viktor)
- `ev-agent-viktor-003` — Viktor: Tasks portal empty; employee says backend task is live (Viktor)
- `ev-agent-zapier-001` — Zapier: first automation (Copilot + Zap, not Agents) (Zapier)
- `ev-comp-aider-001` — Aider (Karbon): positioning, AI agents, period close automation (Karbon / Aider)
- `ev-comp-aider-002` — Karbon: role-based agents, 40-hour claim, workflow-defined accounting (Karbon / Aider)
- `ev-comp-aider-003` — Aider tutorial: period-close dashboard, firm template, Ask Client (Aider (Karbon) tutorial)
- `ev-comp-digits-001` — Digits: Agentic General Ledger, positioning, and AI-native accounting (Digits)
- `ev-comp-digits-002` — Digits whitepaper: LLMs vs AGL on transaction categorization (Digits)
- `ev-comp-digits-003` — Digits vs Xero page: continuous close as the differentiator (Digits)
- `ev-comp-digits-004` — Digits blog: What is continuous close (Digits)

## Current insights

### These products ship automation, not free-form autonomy — but they disagree on where the agent lives

Notion, Viktor, and Zapier all sell configured automation, not an open-ended autonomous worker. They disagree on the home surface. Notion keeps a builder inside the host product. Viktor frames an AI employee whose workplace is Slack/Teams; the portal does not stay in sync. Zapier keeps a workflow canvas in-product (Copilot beside Trigger → Action). Agents marketing lives on a separate tour; the first published object was still a Zap on that canvas.

- Status: emerging · Confidence: medium
- Evidence: `ev-agent-notion-001`, `ev-agent-notion-002`, `ev-agent-notion-003`, `ev-agent-viktor-001`, `ev-agent-zapier-001`

### Connected is not the same as live

Connecting Slack (or Mail) and toggling a trigger does not mean the agent is watching. A plain Slack post did nothing while settings were unsaved; after Save plus an @Notion AI mention, the same feedback was captured, written to a database, and confirmed in-thread. Save is also a hard gate ("Agent won't run until you save").

- Status: emerging · Confidence: low-medium
- Evidence: `ev-agent-notion-001`, `ev-agent-notion-002`, `ev-agent-notion-003`

### Writes get HITL; interpretation gets a prompt; audit is thin

Notion puts quality rules in the instructions box (taxonomy, Guardrails) and write safety in product controls (OAuth, dropdowns, Require confirmation before email). Viktor also gates Notion writes with Slack Approve / Always approve. Help Center sells Custom Agents as "Safe & transparent" — activity logs, version history, reviewable and reversible runs — and puts workspace audit-log changes behind Enterprise. On this workspace the researcher looked for activity logs and they were not there. What exists is a current-run step trace, Recent chats, and an Analytics page that upsells Enterprise. No first-class send audit or unsend. Zapier treats HITL as an optional step after AI by Zapier ("review the output before your Zap continues") and has Zap history as a first-class page — empty immediately after publish. Viktor Usage was not opened.

- Status: emerging · Confidence: medium
- Evidence: `ev-agent-notion-001`, `ev-agent-notion-002`, `ev-agent-notion-003`, `ev-agent-notion-004`, `ev-agent-notion-005`, `ev-agent-viktor-001`, `ev-agent-zapier-001`

### Slack is a fast install surface and a weak workflow builder

Viktor's onboarding is Slack-first (signup, channel invite, "Now go to Slack," custom tasks via "Ask Viktor in Slack"). Templates are mostly generic productivity (briefings, meetings, email), not Notion-like verticals. A web checklist and Academy videos exist, but configuration of a real pipeline happened in Slack with Approve buttons and little streaming, loading, or config knobs. A later session still could not open a task editor. Tasks showed 0. Viktor said Customer Feedback Weekly Digest exists, is active in the backend, and called the empty portal a display bug, then said the Monday 9 AM digest will run anyway. Sign-out and Calendar view also failed. Two surfaces, no shared system of record. The employee is also the support desk.

- Status: emerging · Confidence: medium
- Evidence: `ev-agent-viktor-001`, `ev-agent-viktor-003`

### The split is how much of the execution plan the user defines vs delegates

The key difference across Zapier, Notion, and Viktor is how much of the execution plan the user defines versus delegates to the agent. Zapier is high-control / low-autonomy — the user owns an explicit workflow graph (steps, inputs/outputs, test, publish); AI or agentic steps run inside it. Viktor is high-autonomy / low-workflow-control — the user delegates an outcome; Viktor decides more of the path; the workflow is less visible and less configurable (this pass never produced an inspectable portal object). Notion sits in the middle — a persistent agent with instructions, context, tools, triggers, and permissions, but not a Zapier-style step graph. Primary abstractions, left to right: Workflow → Agent → AI employee. Feature checklists matter less than this. Hands-on: Zapier published Slack Feedback → AI Triage Analysis → Email v1 (AI by Zapier as a step); Notion published Customer Feedback Triage Agent; Viktor took a Slack brief and never showed a task editor.

- Status: emerging · Confidence: low-medium
- Evidence: `ev-agent-notion-001`, `ev-agent-notion-003`, `ev-agent-notion-004`, `ev-agent-notion-005`, `ev-agent-viktor-001`, `ev-agent-viktor-002`, `ev-agent-viktor-003`, `ev-agent-zapier-001`, `ev-comp-aider-002`

### Competitors split into GL-replacement vs practice-layer — XeroForce must know which fight it is in

Digits replaces the general ledger itself with an agentic system that auto-books 95%+ of transactions using custom-trained ML (not LLMs) on $875B in real SMB data. The user does not configure or name an agent; the ledger IS the agent. Karbon/Aider sits on top of existing GLs. Seen in an Aider tutorial: Period Close Dashboard (client × period, Pass/red counts), a firm template (Monthly Close - Accrual) on 82 clients, Built-in and Automatic-N-conditions checks, exception inbox, Ask Client batched end of day. Those are rules and a close workflow — not evidence of how Karbon AI Agents work. Agents (Bookkeeper, Tax Admin, fCFO, Onboarding) are marketed as roles and listed as early beta / 2026; no Agents tutorial or product pass yet. Different layers: Digits threatens Xero the product; Karbon threatens the portfolio-close and (if Agents ship) client-lifecycle layer.

- Status: emerging · Confidence: low-medium
- Evidence: `ev-comp-aider-001`, `ev-comp-aider-002`, `ev-comp-aider-003`, `ev-comp-digits-001`, `ev-comp-digits-002`, `ev-comp-digits-003`

### "Shipped vs marketed" is a reliable signal — the more specific the claim, the more likely it is real

Across both agent builders and competitors, there is a consistent gap between what is marketed and what has been observed. Notion markets activity logs (missing), Viktor markets a live task (portal empty). Karbon markets AI Agents and Kai; what we have seen is Aider period-close rules, which are not those agents. Digits markets 'Agentic GL' and has shipped auto-booking — its claims are specific (95%+, 97.8% accuracy, $875B training data) and closer to verifiable. Pattern: vague 'AI agent' framing with role metaphors (employee, coworker, teammate) is easy to over-read. Specific, quantified claims about what the software does tend to be closer to reality. Do not treat a rules/checklist product as proof of an agent model.

- Status: emerging · Confidence: low-medium
- Evidence: `ev-comp-aider-001`, `ev-comp-digits-001`, `ev-agent-notion-005`, `ev-agent-viktor-003`, `ev-agent-zapier-001`, `ev-comp-aider-002`, `ev-comp-aider-003`

### MCP-as-platform is an industry convergence — accounting data as tools for external AI

Zapier, Karbon, and Digits all ship or announce MCP servers. The pattern: expose accounting/practice data to Claude, ChatGPT, Cursor, and other AI clients. This means firms will expect to plug their accounting data into whatever AI tools they choose, not only the vendor's own AI. Zapier also positions as a tool layer for external agents (not just its own Agents/Zaps).

- Status: emerging · Confidence: low
- Evidence: `ev-comp-aider-001`, `ev-comp-digits-001`, `ev-agent-zapier-001`

### Karbon's Agents are marketed as roles; we have not seen the Agents product

Karbon's AI Agents article sells Viktor-like firm roles (Bookkeeper, Tax Admin, Fractional CFO, Onboarding Specialist) — capabilities mapped to jobs that already exist, split into Service Delivery vs Service Management. That is marketing copy only. The Aider tutorial we have is period close: portfolio dashboard, firm checklist, Built-in / Automatic-N-conditions checks, Ask Client. Those are rules. Rules are not agents, and that tutorial is not evidence of how Agents work. Do not conclude Agents are workflow-based, role-based, or anything else until there is an Agents tutorial or hands-on pass.

- Status: emerging · Confidence: low
- Evidence: `ev-comp-aider-001`, `ev-comp-aider-002`, `ev-comp-aider-003`, `ev-agent-viktor-001`, `ev-agent-viktor-002`, `ev-agent-zapier-001`

### Accounting work is workflow-defined; that is why role agents and tutorial-plus-tool content both fit

Aider's tutorial names a standard close problem (managers have no single view of client close; status lives in meetings and memory; same issue at 15 or 15,000 clients), then shows the tool: portfolio dashboard, one Monthly Close - Accrual template applied to 82 clients, Built-in/Automatic checks, exception inbox, Ask Client batched to end of day. Workflow and tool are taught together. That only works if the close is shared enough to template. Contrast with MSPs, where vendors sell tools and workflows vary — a known industry problem. The 40 hours/employee/month figure remains a Karbon CEO research claim, not a measured Aider outcome; 19.9 hrs/week is a separate Karbon PM number.

- Status: emerging · Confidence: low-medium
- Evidence: `ev-comp-aider-002`, `ev-comp-aider-003`

### Continuous close is Digits' cadence bet — not yet a verified customer want

Digits built a GL from the ground up. Architecture bet (whitepaper): specialized AGL beats LLM / LLM-harness on categorization accuracy, latency, and cost — on Digits' own data. Cadence bet (blog + vs-Xero page): categorize / rec / verify as txns arrive so month-end is review, not a cleanup sprint. Digits themselves split 'fast month-end' (Xero + AI; sprint shrinks, still exists) from 'continuous close' (rebuild the ledger; sprint gone). Stated user value: client sees treated numbers the day activity happens (Stripe Tuesday example); firm week-one becomes advisory; exceptions while context is fresh; capacity scales with judgment not volume; firm knowledge stays in models. They also say stay on month-end if <5 clients, clients are not asking for current reporting, or monthly cadence still fits. Unverified with customers. Researcher MSP parallel still stands. Benchmark numbers on the blog (17,792 txns, LLMs <73%) do not match the whitepaper on file (2,000 txns, top LLM 86.8%) — same paper title, different result.

- Status: emerging · Confidence: low
- Evidence: `ev-comp-digits-001`, `ev-comp-digits-002`, `ev-comp-digits-003`, `ev-comp-digits-004`

## Current hypotheses

### The category bet is scoped objects + triggers, not agent UX

Knowledge-work products still constrain work (objects, access, approvals, steps) rather than offering open-ended autonomy. They do not share one abstraction. Notion puts scoped objects + triggers on a named agent. Viktor puts a brief on one employee. Zapier puts AI inside a trigger-action Zap and makes Copilot fill that canvas. Same category, three units.

Would falsify:
- A common path that is mostly open-ended web/API autonomy with little product-object or step scaffolding

### Slack "message posted" is not fire-on-every-message

Notion's Slack channel trigger does not fire on every public-channel post in practice. A plain post created no session; after Save, an @Notion AI mention produced a run, a database write, and a Read & Reply thread confirmation.

Would falsify:
- After Save, a plain (no mention) public-channel post creates a session and a feedback row

### Accountability for writes is not a first-class builder surface

Notion governs writes at connect-time (OAuth + toggles + optional Require confirmation) and governs interpretation in instructions. Help promises activity logs, version history, and reversible runs; the researcher could not find activity logs on these agents. Viktor gates Notion writes in Slack (Approve / Always approve). Post-hoc accountability is not first-class on either pass. Notion workspace AI analytics and the documented audit log are Enterprise; Viktor Usage was not opened.

Would falsify:
- An Activity tab (or equivalent) that is a real per-run log plus unsend on this plan
- Viktor Usage (or Slack) exposing a reversible action log for Always-approved writes

### Messaging-first setup trades speed for inspectability

If the primary place to configure a workflow is Slack/Teams chat (plan + Approve), operators get a fast "employee" install but lose streaming, loading, config knobs, and a saved spec they can inspect. A later session still showed Tasks at 0. Viktor named Customer Feedback Weekly Digest as active in the backend and called the empty portal a display bug, then said the Monday 9 AM job will run anyway. Sign-out and Calendar view also empty. Slack / the employee is the system of record. The portal is optional and can lie. Vertical templates stay thin because chat is a bad surface for schema work.

Would falsify:
- Slack-created work reliably appears on Tasks with steps, scopes, test, retry
- Slack setup itself streams progress and exposes config knobs
- (Zapier already puts setup on a canvas; that strengthens the contrast, it does not falsify Viktor)

### XeroForce has to pick a point on define-vs-delegate, not a feature set

If XeroForce copies Zapier, users keep high workflow control and AI lives in selected steps. If it copies Notion, users configure a persistent agent without drawing the full graph. If it copies Viktor, users delegate the outcome and give up an explicit plan. Accounting work that is really a pipeline leans Zapier. Work that needs a named, scoped specialist leans Notion. Work that is "just get it done" leans Viktor and is the weakest to govern. The Zapier first pass published a Zap, not an Agent. The Viktor pass never showed a task editor.

Would falsify:
- Tasks list showing the digest with a Settings-like editor
- A Zapier Agent that is a true persistent agent (not a Zap) and is the default create path
- A later product that is agent + employee + workflow with no real tradeoff

### Zapier will not replace the workflow graph with an agent

Zapier believes users still want an explicit workflow graph. AI should make selected parts of that graph adaptive or autonomous, not retire Trigger → Action. Copilot, AI by Zapier, Human in the Loop, and even the Agents tour all sit on top of steps, tests, and publish. If that bet is right, XeroForce should keep a visible pipeline and put models inside steps. If it is wrong, the graph becomes legacy chrome and the Agents product (or something like Viktor) eats the default path.

Would falsify:
- Default create path is an Agent with no Trigger → Action canvas
- Copilot shipping a black-box employee that hides steps after publish

### Digits is the more dangerous competitor because it replaces the GL, not just the workflow

Karbon/Aider adds AI on top of Xero (or QBO). That is a workflow-layer threat: firms might do period close and advisory in Karbon, not Xero. But the GL stays. Digits replaces the GL entirely with an agentic system — if a firm migrates to Digits, Xero loses the system of record. An agentic GL that auto-books 95%+ of transactions makes the traditional categorize-then-reconcile GL feel manual. XeroForce defending the GL may matter more than XeroForce adding workflow features.

Would falsify:
- Digits auto-booking accuracy much lower in practice than claimed
- SMBs unwilling to leave their GL (switching cost too high)
- Xero ships agentic categorization/reconciliation that matches Digits

### The competitor trust model is ahead of the agent-builder trust model

Digits ships embedded verification (two AI layers in the same system of record) and manage-by-exception UX. Karbon ships approve/edit/reject with audit trail via Agent Management System. Both are more concrete than Notion's missing activity logs, Viktor's empty portal, or Zapier's optional HITL step. If XeroForce copies agent-builder trust patterns instead of competitor trust patterns, it will underdeliver on accountability for financial writes.

Would falsify:
- Digits verification layer is cosmetic — errors slip through at similar rates
- Karbon audit trail is shallow or hard to use in practice

### If XeroForce stays on agentic ledger workflows, Karbon takes the rest of the client lifecycle

Karbon's role list is a scope claim — Bookkeeper (workpapers, reconcile, client follow-up), Tax Admin (returns, compliance, summaries), Fractional CFO (forecasts, what-ifs, client-ready reports), Onboarding Specialist (collect, validate, configure). Aider's acquisition list adds management reports and advisory dashboards. XeroForce focusing on agentic workflows inside the GL leaves reports, onboarding, tax ops, and billing as Karbon's default. Accounting being workflow-defined makes that land-grab cheaper for Karbon than it would be in an MSP-like industry.

Would falsify:
- XeroForce scope already includes client reports and full-lifecycle ops
- Karbon Agents stay vaporware and firms do lifecycle work in Xero

### Role agents work in accounting because the jobs are shared; they would fail in MSP-like variance

Aider can ship one Monthly Close - Accrual template onto 82 clients because close work is shared enough to teach as workflow-plus-tool. MSP training that only sells the tool, with high workflow variance, cannot do that. Whether Karbon can also ship Bookkeeper / Tax Admin / fCFO as named teammates is a separate, untested claim — we have not seen Agents. If the shared-job bet is right, XeroForce can be opinionated about close. If it is wrong, firms will reject templates the way MSPs reject one-size playbooks.

Would falsify:
- Firms needing heavily custom close that a shared template cannot absorb
- Hands-on Karbon Agents (still unseen) that require each firm to specify the whole job

### Continuous close may create work the way more-frequent MSP scans do — verify with users

Digits now distinguishes fast month-end (automate the sprint; still a sprint) from continuous close (rebuild the GL; no backlog). They say bolt-on AI on Xero cannot do the second because of truth drift. Their own 'stay traditional if' list matches the MSP-scan cut: <5 clients, clients not asking for current reporting, monthly cadence still fits. Alternative still open: even for larger books, a mid-month exception drip can be more work than one automated close if nobody uses Tuesday-afternoon numbers. If that is right, XeroForce can ship a faster month-end on Xero and cover most of the market Digits concedes. If clients are asking for current numbers and week-one cleanup is the burnout, a smarter sprint will not be enough.

Would falsify:
- Firms citing always-current cash/P&L as why they left Xero
- Continuous inbox that is quieter than Xero's month-end queue
- Clients actually requesting treated numbers mid-period (the Stripe Tuesday story)

## Uncited evidence

All current evidence IDs are cited on at least one living card.

## Contradictions / uncertainty

- No counter-evidence IDs recorded on living insights yet.
