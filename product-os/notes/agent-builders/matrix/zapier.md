---
id: note-agent-builders-matrix-zapier-001
type: working_notes
effective_date: 2026-09-01
confidence: direct
product: zapier
---

# Zapier AI Agents — observation matrix (notes)

Reference: `notes/agent-builders/matrix/_dimension-guide.md`
Evidence: `ev-agent-zapier-001` (first automation; Zap not Agents)

## Getting started

What I saw:
- Entered via `zapier.com/agents`. Job-level onboarding, then Home with Copilot + five primitives (Zap / Agent / Chatbot / MCP / Form).
- Agents tour (`agents.zapier.com/first-bot`): "AI teammates", Activity mock, Chrome extension, **Create your first agent**.
- First published object was a **Zap**, built with Copilot, not an Agent.
Where: Home, Agents tour, Zap editor
Evidence quality: hands-on
Follow-ups: Finish the Agents create path on a second pass.

## Creation model

What I saw:
- Copilot: "Describe your workflow" then clarifying questions (Zap vs analyze-now; source; output; Slack trigger shape; sample messages; model).
- Canvas stays Trigger → Action while Copilot talks. Copilot then inserts Slack / AI by Zapier / Gmail steps.
- Copilot could not fully write the AI step: "needs manual configuration… paste into the AI step."
Where: Zap editor + Copilot sidebar
Evidence quality: hands-on

## Mental model

What I saw:
- Marketing: teammates / Agents / 9,000 apps.
- Working model: describe an automation, Copilot structures a Zap, AI is a **step** ("AI by Zapier") inside trigger → action.
- Home literally lists Agent as one primitive next to Zap.
- Product bet on this pass: keep the explicit workflow graph; make selected steps adaptive. Do not replace the graph with an employee.
Evidence quality: hands-on + marketing

## Agent abstraction / delegation model

What I saw:
- The user created a **workflow (Zap)** named Slack Feedback → AI Triage Analysis → Email, version **v1**.
- The word "agent" appears as a role inside the AI-step prompt ("Product Feedback Triage Agent for LedgerFlow"), not as a workspace object with its own share/activity page.
- Zapier is not replacing the workflow abstraction. AI is inserted into it (adaptive/autonomous **parts** of a graph the user still owns). High-control / low-autonomy on the define-vs-delegate line.
- More human-specified than Viktor (steps, fields, prompt pasted). Less of a named persistent agent than Notion (middle of the line).
Where: published Zap; Agents tour not completed
Evidence quality: hands-on
Follow-ups: Independent Zapier Agent object vs this Zap.

## Context / knowledge

What I saw:
- Prompt + mapped Slack message field `{{…message__raw_text}}`.
- Tools and Knowledge on AI step; web browse gated ("Advanced or Premium tier") and off.
Follow-ups: What "company knowledge" on the Agents product actually attaches.

## Tools / actions

What I saw:
- 9,000+ apps in copy. Connections happened **late**: Sign in Slack / Gmail when steps needed them, not an upfront integration checklist.
- MCP: connect Claude / ChatGPT / Cursor / etc. to Zapier apps.
- AI step tools: none configured; add-tool gated.
Evidence quality: hands-on

## Permissions

What I saw:
- Slack OAuth on tether-labs (content about you / channels / workspace).
- Slack trigger access: **Anyone in my workspace.**
- Gmail Sign in for Send Email.
Follow-ups: Whose credentials at runtime; admin app/action allowlists.

## Sharing

Not observed beyond "Anyone in my workspace" on the Slack trigger. Zap share/permissions not opened.

## MCP / extensibility

What I saw:
- First-class **MCP servers** in sidebar (New). New MCP server: pick an external AI agent, add apps, ask it to act.
Follow-ups: Stand up Claude or Cursor MCP and see what Zapier exposes.

## Triggers

What I saw:
- Slack **New Pushed Message**; Copilot framed keyword "feedback" / DM to bot.
- Publish copy: Zap runs when that Slack event occurs.
Follow-ups: Does a Slack DM to the Zapier app fire this Zap, or only "pushed message"? User DMed feedback; no reply in-frame.

## Human-in-loop

What I saw:
- After AI by Zapier: recommend **Human in the Loop** step because AI output varies. Not added.
- Copilot asked confirmation before testing Gmail send (**Test step** / Skip test).
Evidence quality: hands-on
Follow-ups: Add HITL and confirm it actually pauses.

## Testing

What I saw:
- Each step: Setup → Configure → **Test**. AI modal **Preview**. Copilot "Test step."
- Preview on placeholder then on the bank-rec sample (S2+ / Reconciliation confidence).
- Strong, familiar Zapier testing — not a new agent-debug model.
Evidence quality: hands-on

## Debugging

What I saw:
- Copilot auth errors (SlackCLIAPI / GoogleMailV2CLIAPI) then Connect Account.
- AI step red alert while Gmail still configuring.
- Copilot told the user to paste prompt/schema rather than applying it.
Follow-ups: Failed live run UX.

## Observability

What I saw:
- Agents marketing puts **Activity** front and center (status, apps used, needs action). Not used — no Agent was created.
- Zap: Publish v1; **Zap history** exists (Zap runs / Task usage / Autoreplay) but **No results found** and 0 / 1,000 right after publish.
Evidence quality: hands-on
Follow-ups: History after a real trigger; Agents Activity on a real Agent.

## Failure handling

What I saw:
- Blank white page on an agents onboarding URL; recovered via Home.
- Autoreplay toggle on Zap history (off). Not exercised.

## Iteration UX

What I saw:
- Copilot chat continues after publish ("Ask Copilot"). Undo in editor. Version labeled v1.
Follow-ups: Version history / diff of prompt changes.

## Discoverability

What I saw:
- Copilot-first, not a vertical agent template picker. Recommended **Zaps** (Drive, Calendar, Notion), not agent templates like Notion Sales/Support.
- Agents tour is a separate site (`agents.zapier.com`).

## Governance

Not observed (admin restrictions, audit of config). Zap history is the advertised run log.

## Pricing

What I saw:
- Pro trial, 14 days, 0 / 1,000 tasks. AI by Zapier Premium. Multi-step + premium apps called out at publish. Standard (Auto) = 1 task. 75 tasks per run limit on AI step. Tools need Advanced/Premium.
Evidence quality: hands-on

## Delight / friction

What I saw:
- Delight: Copilot names the Zap and lays out steps; Preview on the real sample; Publish is explicit ("Zap is live… v1").
- Friction: clarifying Qs before anything exists on the canvas; paste-the-prompt seam; auth dialogs; Zap history empty after go-live; Agents marketing vs Zap you actually ship.
Evidence: `ev-agent-zapier-001`

## Evidence quality (overall)

hands-on first Zap (`ev-agent-zapier-001`). Agents product only as tour/marketing. Sharing, admin, live Slack trigger, HITL step, MCP runtime not done. Treat as low-to-medium confidence until that second pass.
