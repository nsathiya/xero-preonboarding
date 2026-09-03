---
id: note-agent-builders-matrix-notion-001
type: working_notes
effective_date: 2026-08-31
confidence: direct
product: notion
---

# Notion Custom Agents — observation matrix (notes)

Use this to capture quickly while researching/using Notion.

Reference guide for what each section means:
`notes/agent-builders/matrix/_dimension-guide.md`

For each entry:
- **What you saw** (as close to source as possible)
- **Where** (screen/page/url)
- **Evidence quality** (hands-on / docs / marketing)
- **Follow-ups** (what you need to verify)

Optional structure (paste under any heading):
- What I saw:
- Where:
- Evidence quality:
- Follow-ups:

## Getting started
- First page is notion doc, but 'New Chat' section on the side.
- 'New Chat' brings you to a AI chat screen. 
- 'Add Agent' on the left column. 
- Evidence: `ev-agent-notion-001` (screen recording)

What I saw:
- "Create a new agent" modal with categories and a template marketplace.
- You can start from a template (vs. create blank).
Where:
- `app.notion.com` agent creation flow (recording)
Evidence quality:
- hands-on
Follow-ups:
- Try "Create blank" and compare friction/controls vs template.

Also (`ev-agent-notion-003`): custom start by pasting a long schema/guardrail prompt into Create a new agent (not picking a template as the primary path). Agent created: Customer Feedback Triage Agent.

## Creation model

What I saw:
- Template appears to provision Notion databases/pages automatically (e.g. "Created database ...", "Updated database ...").
- Separate right-side "Settings" panel for triggers + instructions + tools/access.
Where:
- Customer Feedback Tracker run trace + Settings panel
Evidence quality:
- hands-on
Follow-ups:
- Can you edit the underlying workflow/steps, or only instructions + tool/page scope?

Also (`ev-agent-notion-003`): custom agent is still “one long instructions box” but with a required response format, severity taxonomy (S1–S4), single-theme rule, and ⚖️ Guardrails. Builder tells you to connect Mail in Settings after the workflow is drafted.

## Mental model

What I saw:
- The template describes the agent in terms of recurring capture + a recurring report (weekly trend report).
Where:
- Agent summary + trigger + report generation output
Evidence quality:
- hands-on
Follow-ups:
- Does the product treat this as “agent with tools” vs “workflow with chat UI”? (try a non-template build)

## Agent abstraction / delegation model

What I saw:
- The user creates a **named Custom Agent** (Customer Feedback Tracker; Customer Feedback Triage Agent). That object owns instructions, tools/access, triggers, model, chat, and (per docs) activity, version history, share permissions, and handoffs to other agents.
- For customer-feedback triage you design the **agent**, then new items invoke that same object.
- Middle of the define-vs-delegate line: persistent agent, not a Zapier step graph, not a Viktor employee brief.
- Help Center: "Custom Agents live inside Notion and run on your instructions"; "set them up once... they become a shared resource"; access is explicit per agent; Activity + Version history + Share.
Where:
- Hands-on agent Settings (`ev-agent-notion-001`, `003`); https://www.notion.com/help/custom-agents (`ev-agent-notion-004`)
Evidence quality:
- hands-on + first-party docs
Follow-ups:
- Activity logs not visible (`ev-agent-notion-005`). Version history / handoff still unopened.
- Place HubSpot on the same line.

## Context / knowledge

What I saw:
- A Notion tool scope lists specific pages/databases the agent can access (Customer Feedback, Customer Feedback Reports).
Where:
- Settings → Tools and access → Notion
Evidence quality:
- hands-on
Follow-ups:
- Are pages inherited by workspace/creator by default, or is explicit selection required?

## Tools / actions

What I saw:
- Tools include "Notion" plus optional "Web access" (toggle).
- Add connection catalog includes Slack plus many SaaS apps; Slack capability copy lists read/send/reply, emoji react, mention response, and Slack search.
- Mail connect (`ev-agent-notion-003`): Connect your email to Notion (Google / Outlook). After connect: `narensathiya92@gmail.com` with **Read, modify inbox, draft and send**. Toggles: Modify inbox, Draft, Send, **Require confirmation**.
Where:
- Settings → Tools and access; Add connection modal; Mail connect modal
Evidence quality:
- hands-on (`ev-agent-notion-001`, `ev-agent-notion-002`, `ev-agent-notion-003`)
Follow-ups:
- What can “Web access” do concretely (browse, fetch, summarize)? Does it obey "Trusted URLs"?
- Which Slack capabilities are actually gated by the Read / Read & Reply / None dropdown vs promised in the catalog copy?

## Permissions

What I saw:
- Notion pages listed show "Can edit content" (suggesting explicit write capability).
- Slack (tether-labs) uses a separate dropdown for "All public channels": Read & Reply / Read / None. Read & Reply is described as "Only replies in the thread where it was triggered."
- Channel-level add/select exists (+ Select channels / + Add channel).
- Slack OAuth consent lists workspace/channel/user content categories before Allow.
- Mail OAuth: “All permissions are required to connect your email” if the grant is incomplete. Copy: Notion does not train on email; only approved permissions are used.
Where:
- Settings → Tools and access; Slack OAuth modal; Mail connect modal
Evidence quality:
- hands-on (`ev-agent-notion-001`, `ev-agent-notion-002`, `ev-agent-notion-003`)
Follow-ups:
- When another user runs the agent, whose permissions apply (creator vs runner)?
- Do Slack private channels require extra consent beyond "All public channels"?

## Sharing

What I saw:
- Agent header shows "Private" (visibility signal).
Where:
- Agent top bar
Evidence quality:
- hands-on
Follow-ups:
- How does sharing work across teamspaces/org (copy vs shared instance)?

## MCP / extensibility

What I saw:
- Add connection catalog includes many first-party/SaaS connectors.
- Catalog footer shows **"+ Add custom MCP"**.
Where:
- Settings → Add connection modal
Evidence quality:
- hands-on (`ev-agent-notion-002`)
Follow-ups:
- What does custom MCP require (auth, schema, hosting)? Can it be used as a trigger or only as a tool?

## Triggers

What I saw:
- Native: new chat, mentioned in Notion, weekly schedule, manual Run agent.
- After Slack connect: **"Message posted in #new-channel"** can be toggled on.
- Slack catalog also advertises trigger "Emoji reaction added to a message" (not configured in this run).
- Slack-side: Notion AI joins the channel and appears under Agents & apps.
- Successful run used Slack messages that **@Notion AI** / `@notion_ai` tagged the bot, then created a Notion page and replied in the Slack thread.
- Custom triage agent (`ev-agent-notion-003`): trigger documented as `notion.agent.mentioned`; chat explains “mention on a Notion page.”
Where:
- Settings → Triggers; Slack #new-channel
Evidence quality:
- hands-on (`ev-agent-notion-001`, `ev-agent-notion-002`)
Follow-ups:
- Does “Message posted in #new-channel” fire on every message, or only @Notion AI mentions?
- What payload is passed (full message, thread, sender)?

## Human-in-loop

What I saw:
- “Agent won't run until you save” is a gating step.
- Mail **Require confirmation** + in-run prompt **“Do you want to send this email?”** with **Reject** / **Continue** (`ev-agent-notion-003`).
Where:
- Settings header; Mail permission menu; chat HITL prompt
Evidence quality:
- hands-on (`ev-agent-notion-001`, `ev-agent-notion-003`)
Follow-ups:
- Is Reject/Continue enforced by the Require confirmation toggle, or also prompt-only?

## Testing

What I saw:
- A "Test run without side effects" appears in the run trace, followed by "The safe test passed without making changes. Save the agent to activate it."
- Slack trigger test sequence (`ev-agent-notion-002`):
  - Plain-text post in #new-channel while “5 unsaved edits”: **no session** (4:40–4:43 PM CT).
  - Toast: “Agent saved successfully.”
  - Re-post tagging **@Notion AI**: new run started after 4:43 PM CT.
  - Success (3 steps): queried database → created page “Tickets update too infrequently; data is stale” → replied in Slack thread.
  - Customer Feedback DB row appeared (TL;DR + Verbatim Quote). User asked “where is my data”; agent said both DBs live under Welcome to Notion.
Where:
- Run trace + agent chat + Slack #new-channel + Customer Feedback DB
Evidence quality:
- hands-on (`ev-agent-notion-001`, `ev-agent-notion-002`)
Follow-ups:
- Isolate whether Save, @mention, or both are required.
- What qualifies as “side effects”? Is there a mode that simulates DB writes?

Also (`ev-agent-notion-003`): **Run agent** plus chat test chips — “Suggest a page for me to test on”, “Generate a realistic test message I can paste into a page”, “I’ll paste a Notion page link to test on”. Trigger named `notion.agent.mentioned`.

## Debugging

What I saw:
- Run trace shows step-by-step actions (creating DB, searching, updating permissions/instructions).
Where:
- Agent run trace
Evidence quality:
- hands-on
Follow-ups:
- Can you re-run from a step or inspect tool call inputs/outputs?

## Observability

What I saw:
- Agent home **Recent chats** list (run history), including Slack-sourced titles like “Agent run confirmation from Slack” and `@naren.sathiya: [@notion_ai]... #new-channel`.
- An **Insights** link on the agent home.
- You can ask the agent about its own runs (“did the agent run…”, “any updates?”); it searches/lists **agent sessions** and reports counts/time windows (e.g. zero sessions 4:40–4:43 PM CT).
- A successful Slack run shows a session pane: **Task triggered** (timestamp), Slack source message + “View in Slack”, then **Cooking** → **3 steps / Success** (Queried database → Created page → Replied in Slack thread).
- Slack-side confirmation: in-thread reply with the new Notion page link; Unsend / View message controls.
- **Credits** in the top bar (usage, not a full run log).
- Custom triage run (`ev-agent-notion-003`): current-chat steps (Thought → Loaded Notion Mail tools → Sent email). No first-class audit log of the outbound email (recipient/body/time) and no reverse/unsend of a sent mail observed.
- **Analytics** page exists: “Understand Notion and AI usage” — **Upgrade to the Enterprise plan** (AI adoption, AI activity, page-level insights, workspace adoption, etc.). Deeper analytics are plan-gated, not absent.
- Help Center promises **activity logs**, an **Activity** tab, version history, and reversible runs. Researcher verified **activity logs are not visible** on these agents (`ev-agent-notion-005`). Per-run step traces and Recent chats are not that log. Workspace audit log is documented as Enterprise-only.
Where:
- Agent home; session pane; Slack thread; Credits; Mail send step; Help Center
Evidence quality:
- hands-on (`ev-agent-notion-001`, `ev-agent-notion-002`, `ev-agent-notion-003`, `ev-agent-notion-005`) + docs (`ev-agent-notion-004`)
Follow-ups:
- Version history — missing too, or elsewhere?
- Is Activity gated by plan/role without being labeled?
- Open Credits and document what (if anything) exists beyond 15/300.

## Failure handling

What I saw:
- First Slack post (no mention, unsaved settings) produced zero sessions.
- After Save + @Notion AI mention, the run succeeded (create page + Slack thread reply).
- Toast after Slack connect: "Started syncing from Slack. This can take up to 36 hours." (did not block the later successful run)
Evidence: `ev-agent-notion-002`
Follow-ups:
- Intentionally break a config (remove a page permission) and observe error UX.
- Confirm whether unsaved config or missing @mention was the first-post failure.

## Iteration UX

## Discoverability

## Governance

What I saw:
- Slack security is two-step: Slack OAuth consent, then Notion-side channel permission dropdown + trigger toggle.
- Instructions include a rule not to re-collect from Slack/email/web during weekly reporting (policy-in-prompt, not a hard tool lock).
- Custom agent (`ev-agent-notion-003`): ⚖️ Guardrails in the instructions box; Mail write gated by OAuth + granular toggles + Require confirmation HITL.
- Docs: "Safe & transparent" + Enterprise audit log. Product: no Activity logs found (`ev-agent-notion-005`).
Where:
- Slack OAuth modal; Settings → Tools and access; Instructions; Mail permissions; Help Center
Evidence quality:
- hands-on (`ev-agent-notion-002`, `ev-agent-notion-003`, `ev-agent-notion-005`)
Follow-ups:
- Are instruction-level guardrails actually enforced, or only prompt guidance?

## Pricing

What I saw:
- “Credits” appears in top navigation (possible usage model indicator).
Where:
- Agent top bar
Evidence quality:
- hands-on
- Analytics / deeper AI usage visibility is **Enterprise-gated** (`ev-agent-notion-003`).
Follow-ups:
- How credits map to runs / model choice / web access.
- What an Enterprise Analytics view actually shows vs builder-level run traces.

## Delight / friction

What I saw:
- Delight: template creates DBs + report structure quickly; Slack Read & Reply is explicit; successful Slack mention produced a DB row + in-thread confirmation with a Notion link.
- Friction: first Slack post did nothing until Save + @mention; user still had to ask the agent “where is my data” to find the databases. Help promises activity logs; they are not visible (`ev-agent-notion-005`).
Evidence: `ev-agent-notion-001`, `ev-agent-notion-002`, `ev-agent-notion-005`

## Evidence quality (overall)

hands-on `ev-agent-notion-001`–`003`, `005`; docs `ev-agent-notion-004`.
