---
id: note-agent-builders-matrix-viktor-001
type: working_notes
effective_date: 2026-08-31
confidence: direct
product: viktor
---

# Viktor — observation matrix (notes)

Reference: `notes/agent-builders/matrix/_dimension-guide.md`
Evidence: `ev-agent-viktor-001` (onboarding only)

## Getting started

What I saw:
- Signup is Slack / Teams first ("Continue with Slack", "$100 credits included").
- Copy frames Viktor as an **AI employee / coworker** "right inside Slack."
- Web checklist "Get Viktor up to speed" (2/4): connect 5 integrations, teach skills.
- **Viktor Academy**: 7 short video lessons (getting started, integrations, model settings, scheduled tasks, skills).
- Channel invite step, then **"Now go to Slack!"** / Message Viktor.
Where:
- app.viktor.com getting-started + dashboard
Evidence quality: hands-on
Follow-ups: Complete remaining 2/4 onboarding tasks.

## Creation model

What I saw:
- **New task** from templates: "Viktor sets it up and runs it for you."
- Custom: **"Ask Viktor in Slack or Teams"** or **+ Create manually**.
- Tasks page: "Create a task above, or by talking to Viktor in chat."
- In Slack, a requested "customer feedback pipeline" is negotiated as a plan + Approve (Notion DB + Monday digest).
- Slack treated that pipeline as set up; web Tasks stayed empty ("No tasks to show").
- Later session (`ev-agent-viktor-003`): Tasks still **0**. Editor unreachable. Viktor said **Customer Feedback Weekly Digest** is active in the backend and blamed a portal display bug. Sign-out and Calendar view also empty.
Where:
- New task modal; Slack DM; Tasks page
Evidence quality: hands-on
Follow-ups: Monday 9 AM digest — does it actually arrive?

## Mental model

What I saw:
- Employee/coworker, not "an agent you configure in a builder."
- DM like a coworker; @Viktor in channels with thread as background.
- Joins channels quietly; only responds when @mentioned.
Where:
- Signup, complete step, Slack intro
Evidence quality: hands-on + marketing

## Agent abstraction / delegation model

What I saw:
- The persistent object is **Viktor**. What you create is a **task / brief** (goal, source, destination, output shape, boundary), not a named "Customer Feedback Agent."
- Hands-on: "a customer feedback pipeline I fully run" → Viktor proposed Notion DB + digest + monitor; user Approved. Tasks page stayed empty — no separate agent object appeared. Later, Viktor named the object **Customer Feedback Weekly Digest** and said it is live; the portal still showed 0, so the researcher could not open an editor.
- Docs: a good task "reads like a brief you would give a sharp new hire, not a search query." Recurring = "saved routine," not a new agent.
- Hire page: "No workflows to build. Just delegate. Agent builders hand you a canvas and a manual. With an AI employee you describe the outcome — Viktor figures out the steps, the tools, and the schedule."
- High-autonomy / low-workflow-control end of the define-vs-delegate line.
Where:
- Slack DM + Tasks (`ev-agent-viktor-001`); https://viktor.com/blog/how-to-write-tasks-for-your-ai-employee and https://viktor.com/hire-an-ai-employee (`ev-agent-viktor-002`)
Evidence quality: hands-on + first-party docs/marketing
Follow-ups: If the task ever appears on Tasks, open the editor and list fields vs Notion Settings. Until then the inspectable object is missing.

## Context / knowledge

What I saw:
- Integrations + Skills marketplace; "connect five integrations to unlock the full setup."
- Slack thread used as context when @mentioned.
- Proposed Notion DB as the store for a feedback pipeline.
Follow-ups: How context is scoped per task vs globally.

## Tools / actions

What I saw:
- Connect integrations from web (**Browse Integrations**) and from Slack buttons (Calendar, Gmail, Outlook).
- Skills = prebuilt workflows (Marketplace).
- URL on channel-invite step included `mcp_connected=true`.
- Slack-side Notion write: create database / create pages (approval gated).
Evidence quality: hands-on
Follow-ups: Open MCP connection details; list of available integrations.

## Permissions

What I saw:
- Channel join: invite to public channels or select channels; quiet join; @mention-only responses.
- Notion writes: per-action approval; "Always approve enabled by naren.sathiya: notion-create-database" / "notion-create-pages."
Evidence quality: hands-on
Follow-ups: Can Always approve be revoked per action type? Private channels?

## Sharing

Not observed beyond workspace Slack install.

## MCP / extensibility

What I saw:
- `mcp_connected=true` in getting-started URL. Not inspected.
Follow-ups: What MCP server was connected and what it can do.

## Triggers

What I saw:
- @mention in Slack; DM; scheduled tasks (Academy lesson + proposed Monday 9am Chicago digest).
- "Viktor only responds when someone @mentions him."
Evidence quality: hands-on

## Human-in-loop

What I saw:
- Slack **Approve** before Notion DB create.
- "Notion writes each need a click for now."
- Always-approve can be enabled per action family.
Evidence quality: hands-on

## Testing

What I saw:
- No Notion-style "safe test without side effects" or test-case chips on this pass.
- Onboarding uses academy videos + "message Viktor" rather than a sandbox run.
Follow-ups: Is there a dry-run for tasks?

## Debugging

What I saw:
- Onboarding: Slack status text ("Almost done"), no step canvas.
- Later: asked the employee why the portal was empty. Viktor diagnosed a display bug and offered to file a ticket / email support. Debugging the missing editor happens in Slack, not on a task page.
Evidence: `ev-agent-viktor-001`, `ev-agent-viktor-003`

## Observability

What I saw:
- Web: Tasks list empty after Slack reported setup; later still **0**. Usage not opened; Academy 0/7; checklist 2/4.
- Slack: prose status + Always approve. Viktor later claimed backend task **Customer Feedback Weekly Digest** is active; portal shows nothing.
- Two surfaces, no shared status. Operator cannot inspect the live job except by asking the employee.
Evidence quality: hands-on (`ev-agent-viktor-001`, `ev-agent-viktor-003`)
Follow-ups: Monday 9 AM delivery; Usage page.

## Failure handling

Not observed.

## Iteration UX

What I saw:
- Changing a Slack-proposed plan means more chat, not editing a saved spec.
Follow-ups: Editor still unreachable (`ev-agent-viktor-003`). Changing the plan is still more Slack.

## Discoverability

What I saw:
- Marketplace, Skills browse, template search, Recommended automations.
- Templates are generic (briefings, meetings, email) plus a few like Revenue Recovery / Deep Work Guardian — not Notion-like Sales/Support/Marketing verticals.

## Governance

What I saw:
- SOC2 / GDPR / CCPA on signup.
- Channel quiet-join + mention-only.
- Per-write Notion approvals.
Follow-ups: Admin controls, audit of Always-approve.

## Pricing

What I saw:
- "$100 credits included" on signup. Usage page not opened.
Evidence quality: marketing + signup UI

## Delight / friction

What I saw:
- Delight: fast Slack install; employee metaphor; Approve is explicit for Notion writes.
- Friction: portal dumps you into Slack for the real setup; Slack is a poor workflow-builder (no stream, no loading canvas, no config knobs). Slack / the employee can claim a live backend task while Tasks shows 0 — you cannot open the editor.
Evidence: `ev-agent-viktor-001`, `ev-agent-viktor-003`

## Evidence quality (overall)

hands-on onboarding + later portal check (`ev-agent-viktor-001`, `ev-agent-viktor-003`). Docs/marketing on tasks (`ev-agent-viktor-002`). No observed Monday digest run. Viktor's "display bug / pipeline not broken" is unverified.
