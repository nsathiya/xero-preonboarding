# Current insights (living)

Beliefs that span runs (and later, products). Evidence IDs are citations, not chapters.
Source of truth: `beliefs/insights.yaml`. Re-run `refresh` after editing that file.

## These products ship automation, not free-form autonomy — but they disagree on where the agent lives

- **ID**: `ins-001`
- **Status**: emerging
- **Confidence**: medium
- **Products**: notion, viktor, zapier

Notion, Viktor, and Zapier all sell configured automation, not an open-ended autonomous worker. They disagree on the home surface. Notion keeps a builder inside the host product. Viktor frames an AI employee whose workplace is Slack/Teams; the portal does not stay in sync. Zapier keeps a workflow canvas in-product (Copilot beside Trigger → Action). Agents marketing lives on a separate tour; the first published object was still a Zap on that canvas.

**Why it might matter:** XeroForce has to pick a home — in-product builder vs messaging coworker vs workflow canvas. That choice drives setup visibility, who can configure, and whether accounting objects stay first-class.

**Supporting evidence** (5 in corpus):
- `ev-agent-notion-001` — Notion: Collect customer feedback template (hands-on) (Notion Custom Agents)
- `ev-agent-notion-002` — Notion: Connect Slack as a trigger (hands-on) (Notion Custom Agents)
- `ev-agent-notion-003` — Notion: Custom feedback triage agent with email write + HITL (Notion Custom Agents)
- `ev-agent-viktor-001` — Viktor: Slack-first onboarding (hands-on) (Viktor)
- `ev-agent-zapier-001` — Zapier: first automation (Copilot + Zap, not Agents) (Zapier)

**Counter-evidence:** none yet

**Next evidence to seek:**
- Whether a Zapier Agent (not a Zap) still lives on a canvas
- (HubSpot skipped — no access)
- Creator vs runner permission inheritance (Notion)

## Connected is not the same as live

- **ID**: `ins-002`
- **Status**: emerging
- **Confidence**: low-medium
- **Products**: notion

Connecting Slack (or Mail) and toggling a trigger does not mean the agent is watching. A plain Slack post did nothing while settings were unsaved; after Save plus an @Notion AI mention, the same feedback was captured, written to a database, and confirmed in-thread. Save is also a hard gate ("Agent won't run until you save").

**Why it might matter:** Accounting agents will need the same split — consent vs action scope vs trigger activation — plus a clear "this run happened / this row was written" signal. Users will otherwise assume connected equals live.

**Supporting evidence** (3 in corpus):
- `ev-agent-notion-001` — Notion: Collect customer feedback template (hands-on) (Notion Custom Agents)
- `ev-agent-notion-002` — Notion: Connect Slack as a trigger (hands-on) (Notion Custom Agents)
- `ev-agent-notion-003` — Notion: Custom feedback triage agent with email write + HITL (Notion Custom Agents)

**Counter-evidence:** none yet

**Next evidence to seek:**
- Isolate Save vs @mention on Slack (plain post after Save)
- Compare Slack vs Calendar/GitHub trigger activation
- Whether Mail send also requires Save before HITL appears
- Viktor "Always approve" vs Notion Save / @mention as two "not live yet" patterns

## Writes get HITL; interpretation gets a prompt; audit is thin

- **ID**: `ins-003`
- **Status**: emerging
- **Confidence**: medium
- **Products**: notion, viktor, zapier

Notion puts quality rules in the instructions box (taxonomy, Guardrails) and write safety in product controls (OAuth, dropdowns, Require confirmation before email). Viktor also gates Notion writes with Slack Approve / Always approve. Help Center sells Custom Agents as "Safe & transparent" — activity logs, version history, reviewable and reversible runs — and puts workspace audit-log changes behind Enterprise. On this workspace the researcher looked for activity logs and they were not there. What exists is a current-run step trace, Recent chats, and an Analytics page that upsells Enterprise. No first-class send audit or unsend. Zapier treats HITL as an optional step after AI by Zapier ("review the output before your Zap continues") and has Zap history as a first-class page — empty immediately after publish. Viktor Usage was not opened.

**Why it might matter:** For XeroForce, HITL before an outbound or financial write is the right pattern. Prompt guardrails are not enough. Do not copy Notion's help copy. If activity logs are advertised and missing, operators will think they have an audit trail they do not. Gating real visibility behind Enterprise is worse when the action touches money or customers.

**Supporting evidence** (7 in corpus):
- `ev-agent-notion-001` — Notion: Collect customer feedback template (hands-on) (Notion Custom Agents)
- `ev-agent-notion-002` — Notion: Connect Slack as a trigger (hands-on) (Notion Custom Agents)
- `ev-agent-notion-003` — Notion: Custom feedback triage agent with email write + HITL (Notion Custom Agents)
- `ev-agent-notion-004` — Notion Help: Custom Agents are persistent workspace objects (Notion Help)
- `ev-agent-notion-005` — Notion: Help promises Activity logs; not visible on this workspace (Notion Custom Agents)
- `ev-agent-viktor-001` — Viktor: Slack-first onboarding (hands-on) (Viktor)
- `ev-agent-zapier-001` — Zapier: first automation (Copilot + Zap, not Agents) (Zapier)

**Counter-evidence:** none yet

**Next evidence to seek:**
- Reject the HITL email and confirm it does not send
- Version history — also missing, or elsewhere?
- Zapier audit and undo models (HubSpot skipped)
- Viktor Usage page and whether Slack Always-approve is auditable
- Zapier Human in the Loop step — does it actually pause a send?
- Zap history after a live Slack trigger (empty right after publish)

## Slack is a fast install surface and a weak workflow builder

- **ID**: `ins-004`
- **Status**: emerging
- **Confidence**: medium
- **Products**: viktor

Viktor's onboarding is Slack-first (signup, channel invite, "Now go to Slack," custom tasks via "Ask Viktor in Slack"). Templates are mostly generic productivity (briefings, meetings, email), not Notion-like verticals. A web checklist and Academy videos exist, but configuration of a real pipeline happened in Slack with Approve buttons and little streaming, loading, or config knobs. A later session still could not open a task editor. Tasks showed 0. Viktor said Customer Feedback Weekly Digest exists, is active in the backend, and called the empty portal a display bug, then said the Monday 9 AM digest will run anyway. Sign-out and Calendar view also failed. Two surfaces, no shared system of record. The employee is also the support desk.

**Why it might matter:** Messaging-first can get an "employee" live in minutes, but accounting workflows need inspectable setup (steps, scopes, test) on the same surface operators will return to. If Slack can claim a live backend job while the portal stays empty, operators cannot tell what is actually live and cannot edit it except by chatting.

**Supporting evidence** (2 in corpus):
- `ev-agent-viktor-001` — Viktor: Slack-first onboarding (hands-on) (Viktor)
- `ev-agent-viktor-003` — Viktor: Tasks portal empty; employee says backend task is live (Viktor)

**Counter-evidence:** none yet

**Next evidence to seek:**
- Does the Monday 9 AM digest actually arrive?
- After a real Slack push, does Zapier Zap history show the run?

## The split is how much of the execution plan the user defines vs delegates

- **ID**: `ins-005`
- **Status**: emerging
- **Confidence**: low-medium
- **Products**: notion, viktor, zapier

The key difference across Zapier, Notion, and Viktor is how much of the execution plan the user defines versus delegates to the agent. Zapier is high-control / low-autonomy — the user owns an explicit workflow graph (steps, inputs/outputs, test, publish); AI or agentic steps run inside it. Viktor is high-autonomy / low-workflow-control — the user delegates an outcome; Viktor decides more of the path; the workflow is less visible and less configurable (this pass never produced an inspectable portal object). Notion sits in the middle — a persistent agent with instructions, context, tools, triggers, and permissions, but not a Zapier-style step graph. Primary abstractions, left to right: Workflow → Agent → AI employee. Feature checklists matter less than this. Hands-on: Zapier published Slack Feedback → AI Triage Analysis → Email v1 (AI by Zapier as a step); Notion published Customer Feedback Triage Agent; Viktor took a Slack brief and never showed a task editor.

**Why it might matter:** XeroForce is picking a point on this line, not a model vendor. High workflow control is inspectable and closer to existing automation. High autonomy is faster to start and harder to govern. The middle (named agent, no full graph) is a real third product, not a compromise UI. Karbon's Agents article sits with Viktor (firm roles) — that is marketing only; the Agents product has not been seen. HubSpot skipped.

**Supporting evidence** (9 in corpus):
- `ev-agent-notion-001` — Notion: Collect customer feedback template (hands-on) (Notion Custom Agents)
- `ev-agent-notion-003` — Notion: Custom feedback triage agent with email write + HITL (Notion Custom Agents)
- `ev-agent-notion-004` — Notion Help: Custom Agents are persistent workspace objects (Notion Help)
- `ev-agent-notion-005` — Notion: Help promises Activity logs; not visible on this workspace (Notion Custom Agents)
- `ev-agent-viktor-001` — Viktor: Slack-first onboarding (hands-on) (Viktor)
- `ev-agent-viktor-002` — Viktor docs: brief an employee, do not build a workflow (Viktor)
- `ev-agent-viktor-003` — Viktor: Tasks portal empty; employee says backend task is live (Viktor)
- `ev-agent-zapier-001` — Zapier: first automation (Copilot + Zap, not Agents) (Zapier)
- `ev-comp-aider-002` — Karbon: role-based agents, 40-hour claim, workflow-defined accounting (Karbon / Aider)

**Counter-evidence:** none yet

**Next evidence to seek:**
- Create a Zapier Agent (not a Zap) — still a graph, or a new object?
- Notion Version history / handoff (Activity logs already missing)
- Zap history after a real Slack-triggered run
- Hands-on Karbon Agents — still a role, or a hidden workflow graph?
- (HubSpot skipped — no access)

## Competitors split into GL-replacement vs practice-layer — XeroForce must know which fight it is in

- **ID**: `ins-006`
- **Status**: emerging
- **Confidence**: low-medium

Digits replaces the general ledger itself with an agentic system that auto-books 95%+ of transactions using custom-trained ML (not LLMs) on $875B in real SMB data. The user does not configure or name an agent; the ledger IS the agent. Karbon/Aider sits on top of existing GLs. Seen in an Aider tutorial: Period Close Dashboard (client × period, Pass/red counts), a firm template (Monthly Close - Accrual) on 82 clients, Built-in and Automatic-N-conditions checks, exception inbox, Ask Client batched end of day. Those are rules and a close workflow — not evidence of how Karbon AI Agents work. Agents (Bookkeeper, Tax Admin, fCFO, Onboarding) are marketed as roles and listed as early beta / 2026; no Agents tutorial or product pass yet. Different layers: Digits threatens Xero the product; Karbon threatens the portfolio-close and (if Agents ship) client-lifecycle layer.

**Why it might matter:** XeroForce has to answer whether it is defending the GL (against Digits) or covering the full client lifecycle Karbon is claiming (reports, onboarding, tax, advisory, billing) — or both. Staying on 'agentic workflows' only concedes the rest of the firm to Karbon.

**Supporting evidence** (6 in corpus):
- `ev-comp-aider-001` — Aider (Karbon): positioning, AI agents, period close automation (Karbon / Aider)
- `ev-comp-aider-002` — Karbon: role-based agents, 40-hour claim, workflow-defined accounting (Karbon / Aider)
- `ev-comp-aider-003` — Aider tutorial: period-close dashboard, firm template, Ask Client (Aider (Karbon) tutorial)
- `ev-comp-digits-001` — Digits: Agentic General Ledger, positioning, and AI-native accounting (Digits)
- `ev-comp-digits-002` — Digits whitepaper: LLMs vs AGL on transaction categorization (Digits)
- `ev-comp-digits-003` — Digits vs Xero page: continuous close as the differentiator (Digits)

**Counter-evidence:** none yet

**Next evidence to seek:**
- Hands-on Digits trial (verify 95%+ auto-booking claim)
- Confirm Aider write-back target (Xero vs QBO) from the inbox
- Confirm Aider/Karbon Xero integration status
- Digits for Firms pricing and what close automation includes
- What XeroForce's brief includes vs Karbon's four roles
- Karbon AI Agents tutorial or early-beta — still unseen
- Customer view on continuous close vs automated month-end (`ins-011`)

## "Shipped vs marketed" is a reliable signal — the more specific the claim, the more likely it is real

- **ID**: `ins-007`
- **Status**: emerging
- **Confidence**: low-medium

Across both agent builders and competitors, there is a consistent gap between what is marketed and what has been observed. Notion markets activity logs (missing), Viktor markets a live task (portal empty). Karbon markets AI Agents and Kai; what we have seen is Aider period-close rules, which are not those agents. Digits markets 'Agentic GL' and has shipped auto-booking — its claims are specific (95%+, 97.8% accuracy, $875B training data) and closer to verifiable. Pattern: vague 'AI agent' framing with role metaphors (employee, coworker, teammate) is easy to over-read. Specific, quantified claims about what the software does tend to be closer to reality. Do not treat a rules/checklist product as proof of an agent model.

**Why it might matter:** For XeroForce, this means do not copy competitor marketing language into product requirements. Ground every claim in shipped, observable behavior. And when evaluating threats, weight shipped capability over announced roadmap.

**Supporting evidence** (7 in corpus):
- `ev-comp-aider-001` — Aider (Karbon): positioning, AI agents, period close automation (Karbon / Aider)
- `ev-comp-digits-001` — Digits: Agentic General Ledger, positioning, and AI-native accounting (Digits)
- `ev-agent-notion-005` — Notion: Help promises Activity logs; not visible on this workspace (Notion Custom Agents)
- `ev-agent-viktor-003` — Viktor: Tasks portal empty; employee says backend task is live (Viktor)
- `ev-agent-zapier-001` — Zapier: first automation (Copilot + Zap, not Agents) (Zapier)
- `ev-comp-aider-002` — Karbon: role-based agents, 40-hour claim, workflow-defined accounting (Karbon / Aider)
- `ev-comp-aider-003` — Aider tutorial: period-close dashboard, firm template, Ask Client (Aider (Karbon) tutorial)

**Counter-evidence:** none yet

**Next evidence to seek:**
- Hands-on verification of Digits shipped features
- Track which announced features (Kai, Karbon Agents) actually ship in 2026

## MCP-as-platform is an industry convergence — accounting data as tools for external AI

- **ID**: `ins-008`
- **Status**: emerging
- **Confidence**: low

Zapier, Karbon, and Digits all ship or announce MCP servers. The pattern: expose accounting/practice data to Claude, ChatGPT, Cursor, and other AI clients. This means firms will expect to plug their accounting data into whatever AI tools they choose, not only the vendor's own AI. Zapier also positions as a tool layer for external agents (not just its own Agents/Zaps).

**Why it might matter:** If XeroForce does not ship an MCP server (or equivalent open tool layer), firms will route Xero data through competitors that do. The value shifts from 'our AI is best' to 'our data is accessible to any AI.'

**Supporting evidence** (3 in corpus):
- `ev-comp-aider-001` — Aider (Karbon): positioning, AI agents, period close automation (Karbon / Aider)
- `ev-comp-digits-001` — Digits: Agentic General Ledger, positioning, and AI-native accounting (Digits)
- `ev-agent-zapier-001` — Zapier: first automation (Copilot + Zap, not Agents) (Zapier)

**Counter-evidence:** none yet

**Next evidence to seek:**
- Test Digits MCP server with Claude/Cursor
- Karbon MCP server — what data is exposed?
- Does Xero already have an MCP server or equivalent?

## Karbon's Agents are marketed as roles; we have not seen the Agents product

- **ID**: `ins-009`
- **Status**: emerging
- **Confidence**: low
- **Products**: viktor, zapier

Karbon's AI Agents article sells Viktor-like firm roles (Bookkeeper, Tax Admin, Fractional CFO, Onboarding Specialist) — capabilities mapped to jobs that already exist, split into Service Delivery vs Service Management. That is marketing copy only. The Aider tutorial we have is period close: portfolio dashboard, firm checklist, Built-in / Automatic-N-conditions checks, Ask Client. Those are rules. Rules are not agents, and that tutorial is not evidence of how Agents work. Do not conclude Agents are workflow-based, role-based, or anything else until there is an Agents tutorial or hands-on pass.

**Why it might matter:** Mixing Aider's close rules with Karbon's Agents marketing will make XeroForce copy the wrong object. Period close is a real, opinionated product. Agents are a separate, unseen bet. Place them on the define-vs-delegate line only after seeing them.

**Supporting evidence** (6 in corpus):
- `ev-comp-aider-001` — Aider (Karbon): positioning, AI agents, period close automation (Karbon / Aider)
- `ev-comp-aider-002` — Karbon: role-based agents, 40-hour claim, workflow-defined accounting (Karbon / Aider)
- `ev-comp-aider-003` — Aider tutorial: period-close dashboard, firm template, Ask Client (Aider (Karbon) tutorial)
- `ev-agent-viktor-001` — Viktor: Slack-first onboarding (hands-on) (Viktor)
- `ev-agent-viktor-002` — Viktor docs: brief an employee, do not build a workflow (Viktor)
- `ev-agent-zapier-001` — Zapier: first automation (Copilot + Zap, not Agents) (Zapier)

**Counter-evidence:** none yet

**Next evidence to seek:**
- Karbon AI Agents tutorial or early-beta (not period close)
- Does the user brief a Bookkeeper, edit a graph, or something else?
- Does Kai appear in the Agents product, or only in marketing?

## Accounting work is workflow-defined; that is why role agents and tutorial-plus-tool content both fit

- **ID**: `ins-010`
- **Status**: emerging
- **Confidence**: low-medium

Aider's tutorial names a standard close problem (managers have no single view of client close; status lives in meetings and memory; same issue at 15 or 15,000 clients), then shows the tool: portfolio dashboard, one Monthly Close - Accrual template applied to 82 clients, Built-in/Automatic checks, exception inbox, Ask Client batched to end of day. Workflow and tool are taught together. That only works if the close is shared enough to template. Contrast with MSPs, where vendors sell tools and workflows vary — a known industry problem. The 40 hours/employee/month figure remains a Karbon CEO research claim, not a measured Aider outcome; 19.9 hrs/week is a separate Karbon PM number.

**Why it might matter:** XeroForce can assume more shared close workflow than an MSP product can — that is why one accrual template can sit on 82 clients. That does not decide the Agents model. It does mean opinionated close checklists are viable here. Client reports and full-lifecycle ops are a separate scope question, not proven by this tutorial.

**Supporting evidence** (2 in corpus):
- `ev-comp-aider-002` — Karbon: role-based agents, 40-hour claim, workflow-defined accounting (Karbon / Aider)
- `ev-comp-aider-003` — Aider tutorial: period-close dashboard, firm template, Ask Client (Aider (Karbon) tutorial)

**Counter-evidence:** none yet

**Next evidence to seek:**
- Customer evidence that firms actually share close/onboarding steps
- {'Counter-evidence': 'firms with highly custom close processes'}
- Source report behind the 40-hour claim

## Continuous close is Digits' cadence bet — not yet a verified customer want

- **ID**: `ins-011`
- **Status**: emerging
- **Confidence**: low

Digits built a GL from the ground up. Architecture bet (whitepaper): specialized AGL beats LLM / LLM-harness on categorization accuracy, latency, and cost — on Digits' own data. Cadence bet (blog + vs-Xero page): categorize / rec / verify as txns arrive so month-end is review, not a cleanup sprint. Digits themselves split 'fast month-end' (Xero + AI; sprint shrinks, still exists) from 'continuous close' (rebuild the ledger; sprint gone). Stated user value: client sees treated numbers the day activity happens (Stripe Tuesday example); firm week-one becomes advisory; exceptions while context is fresh; capacity scales with judgment not volume; firm knowledge stays in models. They also say stay on month-end if <5 clients, clients are not asking for current reporting, or monthly cadence still fits. Unverified with customers. Researcher MSP parallel still stands. Benchmark numbers on the blog (17,792 txns, LLMs <73%) do not match the whitepaper on file (2,000 txns, top LLM 86.8%) — same paper title, different result.

**Why it might matter:** XeroForce can ship a faster month-end on Xero without accepting Digits' cadence. Digits says that is a different, inferior product (truth drift, leftover sprint). That is their architecture claim. Whether users want Tuesday-afternoon books — or would find a mid-month inbox more work — is still a customer question. Digits' own 'stay traditional if' list is the cut to test.

**Supporting evidence** (4 in corpus):
- `ev-comp-digits-001` — Digits: Agentic General Ledger, positioning, and AI-native accounting (Digits)
- `ev-comp-digits-002` — Digits whitepaper: LLMs vs AGL on transaction categorization (Digits)
- `ev-comp-digits-003` — Digits vs Xero page: continuous close as the differentiator (Digits)
- `ev-comp-digits-004` — Digits blog: What is continuous close (Digits)

**Counter-evidence:** none yet

**Next evidence to seek:**
- {"Customer interviews against Digits' own cut": 'asking for current numbers vs not'}
- Do clients want Tuesday-afternoon treated books, or is that a SaaS story?
- Hands-on inbox volume vs Xero rec queue
- Reconcile 17,792 / <73% vs 2,000 / 86.8% whitepaper numbers
