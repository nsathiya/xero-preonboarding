---
id: ev-agent-notion-003
domain: agent_builder
source_type: hands_on
source_name: Notion Custom Agents
date: 2026-08-31
title: Notion: Custom feedback triage agent with email write + HITL
confidence: direct
artifact_path: artifacts/agent-builders/notion/ev-agent-notion-003/custom-triage-agent-email-write.mov
product_area: creation_model
tags:
  - custom-agent
  - email
  - write
  - permissions
  - guardrails
  - human-in-loop
  - testing
---

# Notion: Custom feedback triage agent with email write + HITL

## Raw evidence

This evidence is based on a hands-on flow recorded in:
`artifacts/agent-builders/notion/ev-agent-notion-003/custom-triage-agent-email-write.mov`

Additional artifacts:

- `artifacts/agent-builders/notion/ev-agent-notion-003/guardrails.png`
- `artifacts/agent-builders/notion/ev-agent-notion-003/mail-permissions.png`
- `artifacts/agent-builders/notion/ev-agent-notion-003/test-run-chat.png`
- `artifacts/agent-builders/notion/ev-agent-notion-003/hitl-email-approval.png`
- `artifacts/agent-builders/notion/ev-agent-notion-003/enterprise-ai-analytics.png`

Derived frames: `derived/artifacts/ev-agent-notion-003/frames_15s/`

### Custom start (not a template pick)

**Create a new agent** modal is used with a long pasted instruction
rather than selecting an existing template as the primary path.

The prompt specifies a structured output schema with fields:

- Feedback summary
- Product area
- Underlying problem
- Sentiment
- Severity
- Theme
- Recommended action
- Reasoning

Sidebar already lists both **Customer Feedback Triage Agent** and
**Customer Feedback Tracker**.

Agent description (after create):
"Turns LedgerFlow customer feedback into structured product intelligence
and emails each completed triage."

### Instructions / guardrails

Instructions section prompt:
"What should the agent do every time it runs? Here are a few best
practices."

A **⚖️ Guardrails** block lists:

- "Do not invent customer facts, frequency, account tier, revenue
  impact, workaround availability, affected users, or technical causes."
- "If information is ambiguous, explicitly say what is unclear and
  select the best-supported classification."
- "Separate emotional tone from operational impact when choosing
  sentiment and severity."
- "Do not silently infer urgency from capitalization, profanity, or
  repetition alone."

Severity scale visible in Settings instructions:

- S1 – Critical: Widespread failure, security risk
- S2 – High: Core workflow blocked, no practical workaround
- S3 – Medium: Meaningful friction, workaround exists
- S4 – Low: Minor inconvenience or cosmetic issue

Also: "Choose exactly one theme" (example theme: Reconciliation
confidence).

Required response format fields visible include:
Feedback summary, Product area, Underlying problem, Sentiment.

Overview text:
"Analyze each incoming piece of customer feedback for LedgerFlow and
convert it into consistent, structured product intelligence. After
processing, email the completed triage to narensathiya92@gmail.com."

User-authored constraints also include:
"Do not invent customer facts that are not present in the feedback."
"If information is ambiguous, explicitly say so."
"Send an email to narensathiya92@gmail.com on the feedback after
processing it."

### Connect Mail (write to another service)

Agent setup copy tells the user to finish email delivery:

1. Settings → Tools and access → Feedback Email → Connect to Mail
2. Sign in with the mailbox the agent should send from
3. Reply once connected so sending can be enabled

**Connect your email to Notion** modal:

- "Let Notion AI use email context when managing your workspace."
- "Permissions will be opened in a new tab. Accept permissions to
  continue."
- "Your data, secured: Notion does not train models on your email
  data."
- "You stay in control: Only approved permissions are used."
- Buttons: **Continue with Google**, **Continue with Outlook**

Error shown on one attempt:
"All permissions are required to connect your email. Please try again
and grant all requested permissions."

After connect, Mail shows `narensathiya92@gmail.com` with summary
**"Read, modify inbox, draft and send"**.

Open permission menu (all toggles ON):

- **Modify inbox** — "Archive, trash, label, set reminders, block, and
  unsubscribe."
- **Draft**
- **Send**
- **Require confirmation**
- **Remove address**

Web access toggle is OFF. Notion pages "shared with everyone" shown as
**None** in a later settings view.

### Test / run workflow

Settings includes a **Run agent** control and the note
**"Agent won't run until you save."**

Chat onboarding / test screen:

- Title: Customer Feedback Triage Agent
- Pill: "Help me run Customer Feedback Triage Agent."
- Copy: "The agent is set up to run when it’s mentioned on a Notion
  page (trigger: `notion.agent.mentioned`)."
- Example: “@Customer Feedback Triage Agent please triage this”
- Suggested actions:
  - "Suggest a page for me to test on"
  - "Generate a realistic test message I can paste into a page"
  - "I’ll paste a Notion page link to test on"

A toast appears later: **"Agent saved successfully."**

A test prompt used LedgerFlow / Chase bank-reconciliation feedback and
`@Customer Feedback Triage Agent please triage the feedback above.`

### Structured triage output + HITL before send

Agent output includes structured fields, e.g.:

- Product area: Bank Reconciliation
- Sentiment: Very Negative
- Severity: S2 – High
- Theme: Reconciliation confidence
- Recommended action: Escalate immediately

**Reasoning:** block (example bullets):

- "Bank reconciliation data appears inaccurate (duplicates + wrong
  dates), undermining trust in cleared totals and account balances."
- "Impact is a blocked core workflow (month-end close) with no
  effective workaround identified; re-sync did not resolve."
- "Clear fit for Reconciliation confidence theme..."
- "Urgency is supported by the reported close-blocking impact..."

HITL prompt under the reasoning:

- **"Do you want to send this email?"**
- Buttons: **Reject**, **Continue**

A run trace later shows steps including:

- Thought
- Loaded Notion Mail tools
- Thought
- **Sent email**

### Analytics (plan-gated)

An **Analytics** page titled "See workspace activity and feature usage"
shows an Enterprise upsell card:

- Heading: **"Understand Notion and AI usage"**
- Copy: "Upgrade to the Enterprise plan to gain visibility into
  workspace-level engagement, adoption trends, and AI usage."
- Button: **"Upgrade now"**
- Listed features:
  - AI adoption at a glance
  - AI activity across the workspace
  - Page-level insights
  - Workspace adoption metrics
  - Content engagement trends
  - Search behavior insights
  - "...and more"
- Preview graph: "Active AI members" (sample/empty state)

So deeper AI analytics **exist as a product surface**, but are
**Enterprise-gated** on this workspace.

### What was not visible in this session

In the captured UI, there is:

- A **Credits** control in the top bar (basic usage; see ev-001)
- Session/step traces (Thought / Loaded tools / Sent email)
- A settings-level **Show changes** / **Undo** on instruction edits
- An Analytics page that requires **Enterprise** to unlock AI usage
  visibility

Not observed on this plan:

- An audit trail of outbound actions (what email was sent, to whom,
  when, with what body) as a first-class log
- A way to reverse/unsend an already-sent email from the agent UI
- Non-Enterprise deeper credit/AI-usage analytics

## Notes

Researcher takeaways (not raw evidence):

- Custom start is instruction-schema-first: you paste a richer
  taxonomy (severity scale, themes, required fields, guardrails) into
  the same long instructions box.
- Write actions to Mail are gated by OAuth + granular toggles
  (modify/draft/send) plus an explicit **Require confirmation** HITL
  prompt before send.
- Test UX is strong: Run agent + chat chips that generate a page,
  generate a realistic message, or accept a page link; trigger is
  named as `notion.agent.mentioned`.
- Observability is step-level for the current chat, not an audit log
  of irreversible writes. Deeper AI analytics exist but are
  Enterprise-plan gated.

Follow-ups:

- Confirm whether Reject vs Continue is enforced by the Mail
  "Require confirmation" toggle (vs prompt-only).
- After send: is there any message-level unsend, or only Gmail’s own
  undo?
- Compare this custom agent’s schema vs the template Customer
  Feedback Tracker (ev-001/002).
