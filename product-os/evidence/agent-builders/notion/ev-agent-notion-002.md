---
id: ev-agent-notion-002
domain: agent_builder
source_type: hands_on
source_name: Notion Custom Agents
date: 2026-08-31
title: Notion: Connect Slack as a trigger (hands-on)
confidence: direct
artifact_path: artifacts/agent-builders/notion/ev-agent-notion-002/Connect-slack-for-trigger.mov
product_area: triggers
tags:
  - slack
  - triggers
  - permissions
  - governance
---

# Notion: Connect Slack as a trigger (hands-on)

## Raw evidence

This evidence is based on a hands-on flow recorded in:
`artifacts/agent-builders/notion/ev-agent-notion-002/Connect-slack-for-trigger.mov`

Derived frames (every ~15s):
`derived/artifacts/ev-agent-notion-002/frames_15s/`

### Add connection catalog

From the existing **Customer Feedback Tracker** agent Settings panel, an
**Add connection** modal opens.

Left-side integration list includes (visible across frames):
Calendar, Mail, Slack, Amplitude, Attio, Box, Buildkite, ClickHouse,
Figma, GitHub, Grafana, Intercom, Linear, Mercury, Miro, Mixpanel, n8n,
PostHog, Ramp, Sentry, Stripe, Wiz.

At the bottom of the catalog: **"+ Add custom MCP"**.

### Slack connection capability copy (before connect)

Selecting Slack shows:

- Description: "Connect your agent to Slack so it can read, respond to,
  and take action on messages across your team's channels."
- Capabilities listed with checkmarks:
  - "Read, send, and reply to messages"
  - "React to messages with emoji"
  - "Respond to direct mentions"
  - "Search information in Slack"
- Triggers listed:
  - "Message posted to Slack channel"
  - "Emoji reaction added to a message"
- A **Connect** button

Calendar (also opened in this session) lists capabilities such as
"Read, create, and update events" and triggers "Event created",
"Event updated", "Event canceled".

### Slack OAuth consent

A Slack modal titled **"Allow the 'Notion AI' app to access Slack |
tether-labs Slack"** appears.

Visible UI:

- "App is approved by Slack"
- Workspace selector set to **tether-labs**
- Heading **"Review app permissions"**
- Permission categories listed:
  - "Content and info about you"
  - "Content and info about channels & conversations"
  - "Content and info about your [workspace]"
- Links: **"Manage permissions"**, **"More permissions"**
- Buttons: **Cancel**, **Allow**

After allowing, a Notion toast appears:
**"Started syncing from Slack. This can take up to 36 hours."**

### Slack tool permissions after connect (Notion Settings)

Under **Tools and access**, Slack appears connected as **tether-labs**.

A permission dropdown for **"All public channels"** shows:

- **Read & Reply** — "Only replies in the thread where it was triggered."
- **Read** (selected in one captured frame)
- **None**

UI also shows **"+ Select channels"** / **"+ Add channel"**.

In a later frame, the tether-labs connection shows **"Read & Reply"**.

### Slack trigger after connect

Settings → **When should this agent run?** now includes:

- "Run agent" (manual)
- "New chat with Customer Feedback Tracker in Notion"
- "When agent is mentioned in Notion" (toggle ON)
- "Weekly on Monday at 9:00 AM" (toggle ON)
- **"Message posted in #new-channel"** with a Slack icon (toggle ON)
- "+ Add trigger"

The Settings header shows unsaved-edit counts at times
("3 unsaved edits", "4 unsaved edits", "5 unsaved edits") plus **Save**.

### Slack-side presence

In Slack workspace **tether-labs**, channel **#new-channel**:

- System message: "naren.sathiya joined #new-channel. Also, Notion AI
  joined."
- **Notion AI** appears under Slack sidebar **"Agents & apps"**

### First Slack post (no mention) did not run

User posted in #new-channel (plain text, no @mention):
"I need my tickets to update at a higher frequency. The data is stale"

In the Notion agent chat, the user asks:
"did the agent run based on the message from slack?"

The agent reply: "Not from what I can see in the agent's session history
today." It states it is configured with a Slack message trigger for:
`slackChannel://tether-labs.slack.com/C0B42UV70AX`

User then asks "did a message run now?" Agent: "No — I don’t see any new
agent session triggered 'just now'. I checked this agent’s recent runs
between 4:40–4:43 PM CT and there were **zero sessions** created in that
window."

During this window, Settings still showed **"5 unsaved edits"** / **Save**.

### Save, then @Notion AI mention, then a successful capture

A toast appears: **"Agent saved successfully."**

User then posts again in #new-channel, tagging **@Notion AI**:

- "@Notion AI I need my tickets to update at a higher frequency. The
  data is stale"
- "@Notion AI process this feedback - 'I need my tickets to update at a
  higher frequency. The data is stale'"

User asks "any updates?" Agent: "Yes: **a new run just started.**" A new
session was created after 4:43 PM CT and its status is **running**.

Recent chats then show:

- "Agent run confirmation from Slack"
- "@naren.sathiya: [@notion_ai]... #new-channel"

A session pane labeled **"Task triggered"** (Aug 31, 4:43 PM) shows the
Slack source message:
`@notion_ai process this feedback - "I need my tickets to update at a
higher frequency. The data is stale"`
from `@naren.sathiya` in `#new-channel`, with **"View in Slack"**.

Status progresses **Cooking** → **3 steps / Success**:

- Queried database
- Created page: "Tickets update too infrequently; data is stale"
- Replied in Slack thread

Slack reply text shown:
"Captured this feedback in the Customer Feedback database as a new
entry: 'Tickets update too infrequently; data is stale.'"

User asks "where is my data". Agent replies that both databases
(**Customer Feedback**, **Customer Feedback Reports**) are stored under
parent page **Welcome to Notion**.

The **Customer Feedback** database ("All feedback" view) shows the new
row:

- TL;DR: "Tickets update too infrequently; data..."
- Verbatim Quote: "I need my tickets to update at..."

### Instructions still include Slack as a source constraint

Visible instruction text includes a quality rule:
"Never re-collect feedback from email, Slack, support tools, calls, or
the web during weekly reporting."

## Notes

Subjective / follow-up (not raw evidence):

- Slack security is explicit at two layers: Slack OAuth consent, then
  Notion-side dropdowns for what the agent can do in channels
  (Read / Read & Reply / None) plus channel selection.
- Connecting Slack as a *tool* and adding Slack as a *trigger* are
  separate steps; Save is required before the config is live.
- A plain-text Slack post (no mention), while settings were unsaved,
  did **not** create a session. After Save + posting again with
  **@Notion AI**, the agent ran, wrote a Customer Feedback row, and
  replied in the Slack thread (matches Read & Reply).
- Unclear from this run alone whether the required ingredient was Save,
  the @mention, or both. The advertised trigger is "Message posted in
  #new-channel", but the successful path used an @mention.
- Custom MCP is advertised in the same connection catalog as Slack.
- Finding the created database still required asking the agent
  ("where is my data") — navigation remains awkward.

Follow-ups:

- Isolate Save vs @mention: post without mention after Save; mention
  without Save.
- Test whether "Message posted in #new-channel" fires on every message
  or only @Notion AI / thread replies.
- Confirm Read vs Read & Reply vs None against Slack reply behavior.
- Test private channels vs "All public channels".
- Inspect what "Add custom MCP" actually requires (auth, schema, host).
