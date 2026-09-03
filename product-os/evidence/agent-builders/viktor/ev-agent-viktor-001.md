---
id: ev-agent-viktor-001
domain: agent_builder
source_type: hands_on
source_name: Viktor
date: 2026-08-31
title: Viktor: Slack-first onboarding (hands-on)
confidence: direct
artifact_path: artifacts/agent-builders/viktor/ev-agent-viktor-001/viktor-onboarding.mov
product_area: getting_started
tags:
  - slack
  - onboarding
  - templates
  - employee
---

# Viktor: Slack-first onboarding (hands-on)

## Raw evidence

This evidence is based on a hands-on onboarding flow recorded in:
`artifacts/agent-builders/viktor/ev-agent-viktor-001/viktor-onboarding.mov`

Additional artifacts:

- `artifacts/agent-builders/viktor/ev-agent-viktor-001/signup-slack-first.png`
- `artifacts/agent-builders/viktor/ev-agent-viktor-001/get-up-to-speed.png`
- `artifacts/agent-builders/viktor/ev-agent-viktor-001/viktor-academy.png`
- `artifacts/agent-builders/viktor/ev-agent-viktor-001/recommended-automations.png`
- `artifacts/agent-builders/viktor/ev-agent-viktor-001/new-task-templates.png`
- `artifacts/agent-builders/viktor/ev-agent-viktor-001/new-task-templates-2.png`
- `artifacts/agent-builders/viktor/ev-agent-viktor-001/slack-approve-notion-db.png`

Derived frames: `derived/artifacts/ev-agent-viktor-001/frames_15s/`

### Signup / positioning

Signup page: **"Try Viktor for free. $100 credits included."**

Primary CTAs:

- **Continue with Slack**
- **Continue with Microsoft Teams**
- **Book a demo**

Copy: "No credit card required • SOC2 Type I compliant"

Left-rail marketing:

- Testimonial: "An AI employee connected to all our systems, right inside
  Slack."
- "Add Viktor to Slack and Teams - no card, live in minutes"
- "Viktor connects your tools and onboards itself"
- "Then your AI employee gets it done"

Compliance badges: GDPR Aligned, CCPA Compliant, SOC 2 Type 1 Audited.

### Onboarding checklist (web)

Page **"Get Viktor up to speed"**: "Complete the core setup steps so
Viktor is fully ready for your workspace." Progress **2 / 4 tasks**.

Visible tasks:

- **Connect 5 integrations** — "2 / 5 integrations." "Give Viktor
  enough access to work across your stack." Button: **Browse
  Integrations.**
- **Teach Viktor new skills** — "Skills are prebuilt workflows — from
  drafting emails to pulling reports. Browse the Marketplace and
  install what fits." Button: **Browse Skills.**

### Viktor Academy

**"Viktor Academy — Master Viktor in 7 short lessons."**

Visible lessons:

- Lesson 1 Getting started (4:58)
- Lesson 2 Integrations / "Connect Your Tools" (6:28)
- Lesson 3 Model settings (2:47)
- Lesson 4 Scheduled tasks (4:33)
- Lesson 5 Skills

Sidebar later shows **Academy (0/7)**.

### Invite to Slack channels

URL includes `app.viktor.com/getting-started?step=select-channels` and
`mcp_connected=true`.

Page: **"Invite Viktor to Slack channels"**

- Channel chip **#social**; "Viktor was added to #social by
  naren.sathiya"
- Button: **"Invite Viktor to public channels (4)"**
- Link: "Select channels"
- Disclaimers:
  - "Viktor joins quietly, it won't post anything in these channels."
  - "Viktor only responds when someone @mentions him."

### Onboarding complete → Slack

`app.viktor.com/getting-started?step=complete`

Headline: **"Now go to Slack!"**

- "Find Viktor under 'Apps' or mention @Viktor in any channel in
  tether-labs."
- Button: **"Message Viktor"**
- Link: "Add more integrations"

Mock Slack DM: "I am Viktor, your new AI coworker." Ways to work:

- DM like a coworker
- @Viktor in any channel — "I'll jump in with the full thread as
  background."

### Web portal still exists

Dashboard sidebar includes: Browse, Chat, Dashboard, Integrations,
Skills, Teach Viktor, Spaces, Pages, Tasks, Team, Usage, Settings.

Persistent: **"Open Viktor in Slack"**, Academy, Marketplace, Rewards.

Tasks page (`app.viktor.com/settings/tasks`): "Create a task above, or
by talking to Viktor in chat." Empty state: "No tasks to show."
Buttons: Calendar, **+ New task**.

### Task templates (not vertical-specific)

**New task** modal: "Start from a template — Viktor sets it up and
runs it for you."

Search: "Search templates..."

Templates visible (generic productivity / team, Slack on nearly every
card):

- Daily morning briefing (Slack, Calendar, Outlook, Gmail, +)
- Meeting Prep (Calendar, Slack, Drive, Notion)
- Email Assistant (Gmail, Slack)
- Meeting prep agent
- Weekly Team Digest / Weekly Team Summary
- End of day summary / Workday Wrap-up
- Revenue Recovery — "Scan Stripe disputes every three days and
  stage evidence drafts" (Stripe, Slack)
- Deep Work Guardian — auto-decline meeting spam
- Email Triage

Footer: **"Need something custom? Ask Viktor in Slack or Teams."**
Button: **+ Create manually**

**Recommended automations:** Meeting Prep, Weekly Team Digest, Daily
morning briefing — Slack icon on each.

### Slack as the setup surface

In Slack DM, user: "how about A customer feedback pipeline I fully
run"

Viktor proposes a Notion database **"Customer Feedback (Viktor)"**
with fields: Feedback, Verbatim, Customer, Source, Theme, Severity,
Status, Affected feature, Mentions, Slack link, Date received.

Plan:

1. Log existing feedback: "tickets update too infrequently"
2. Weekly Monday digest (top themes, urgent items, vs prior week)
3. Monitor mentions / @mentions; capture, tag, dedupe

Status: **"Always approve enabled by naren.sathiya:
notion-create-database"**

Later thread: "Almost done — just one more approval (Notion writes
each need a click for now)." Database created in private section.
Weekly digest Mondays 9:00 AM Chicago. "Always approve enabled ...
notion-create-pages."

Also in Slack: Connect Google Calendar / Gmail / Outlook Calendar /
Outlook Mail buttons; "reply with done" when icons show green.

### Slack vs portal (disconnected)

Slack status treated the pipeline as set up / nearly set up (Always
approve, Notion DB created, Monday digest scheduled). The web
portal did not echo that work:

- Tasks page still **"No tasks to show."**
- Onboarding checklist still **2 / 4**
- Academy still **0 / 7**

Researcher: Slack messages said setup was complete; no matching
updates appeared on the portal.

## Notes

Researcher takeaways (not raw evidence):

- Positioning is explicitly **AI employee / coworker inside Slack or
  Teams**. Signup and the last onboarding step both push messaging
  first.
- Templates are mostly generic work-about-work (briefings, meetings,
  email), not org-vertical like Notion's Sales/Support/Marketing
  agent templates. One exception visible: Revenue Recovery (Stripe).
- A web portal exists (integrations, tasks, academy) but custom task
  setup and the "go live" moment are in Slack. Slack has no streaming
  build UI, no loading of a workflow canvas, few knobs — setup feels
  isolating compared with Notion's settings panel.
- Slack and the portal are not one system of record. Slack can say
  you are set up while Tasks / checklist / Academy stay unchanged.
  Two-surface experience feels disconnected.
- Onboarding sequence is handholding: connect Slack → academy videos
  → connect N integrations / skills.

Follow-ups:

- Later check: Tasks still empty; Viktor claimed a live backend
  task. See `ev-agent-viktor-003`.
- Finish a full Slack-configured pipeline and compare observability
  (run log, failures) to Notion's step trace.
- Whether "Always approve" can be scoped per tool / per action.
- Usage page contents (credits vs activity).
- Custom MCP (`mcp_connected=true` in the URL) — what was connected.
