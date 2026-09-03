---
id: ev-agent-notion-001
domain: agent_builder
source_type: hands_on
source_name: Notion Custom Agents
date: 2026-08-31
title: Notion: Collect customer feedback template (hands-on)
confidence: direct
artifact_path: artifacts/agent-builders/notion/ev-agent-notion-001/Collect-customer-feedback-template.mov
product_area: getting_started
---

# Notion: Collect customer feedback template (hands-on)

## Raw evidence

This evidence is based on a hands-on flow recorded in:
`artifacts/agent-builders/notion/ev-agent-notion-001/Collect-customer-feedback-template.mov`

Additional artifacts:

- `artifacts/agent-builders/notion/ev-agent-notion-001/Screenshot 2026-08-31 at 3.40.49 PM.png`
- `artifacts/agent-builders/notion/ev-agent-notion-001/notion-page-permissions-dropdown.png`
- `artifacts/agent-builders/notion/ev-agent-notion-001/notion-credits.png`

### Agent creation (template selection)

Screen shows a modal titled **"Create a new agent"** with tabs such as:
**"For everyone"**, **"Eng & Product"**, **"Sales & Success"**,
**"Marketing"**, **"Support"**, **"Other"**.

This suggests templates are organized by multiple org/vertical lenses
within the product.

Template options visible under "Sales & Success" include (with short
descriptions shown in the UI):

- **Account pulse** — "Tracks call notes, feedback, and outside signals
  for an account and surfaces what needs attention"
- **Pipeline manager** — "Pulls deal data from your CRM and reports on
  deal status, pipeline movement, and risks"
- **Sales enablement navigator** — "Answers product and competitive
  questions, surfaces the right assets, and drafts customer-ready
  emails"

### Agent run / build steps (Customer Feedback Tracker)

The agent page title shows **"Customer feedback tracker"** / **"Customer
Feedback Tracker"**.

The run/build trace shows steps such as (as displayed in the UI):

- "Creating database"
- "Loaded Notion tools"
- "Searched"
- "Loaded page ✨ Welcome to Notion"
- "Created database 🗣️ Customer Feedback"
- "Created database 📊 Customer Feedback Reports"
- "Updated database 🗣️ Customer Feedback"
- "Updated Customer Feedback Tracker"
- "Updated permission: edit access to 🗣️ Customer Feedback"
- "Updated permission: edit access to 📊 Customer Feedback Reports"
- "Added trigger: Weekly on Monday at 9:00 AM"
- "Updated instructions"

### Settings (triggers, instructions, tools/access)

Right-side panel labeled **"Settings"** shows:

- A note: **"Agent won't run until you save"** with a **Save** button.
- **Triggers** section with prompt "When should this agent run?"
  - "Run agent"
  - "New chat with Customer feedback tracker in Notion"
  - "When agent is mentioned in Notion" (toggle shown)
  - A schedule trigger shown as: **"Weekly on Monday at 9:00 AM"**
  - "+ Add trigger" (button)
- **Instructions** section with prompt "What should the agent do every
  time it runs? Here are a few best practices."
  - Instructions appear as a single long editable text box (one primary
    editable area).
  - Visible instruction text includes: "quote or equivalent TL;DR,
    source, and date. Do not create duplicates."
  - Additional bullets visible include:
    - "If several feedback items are supplied together, split them into
      separate entries."
    - "After capture, respond briefly with what was recorded and any
      fields left unknown."
- **Tools and access** section with prompt "What can the agent use? Add
  tools, pages, and connections it can access."
  - A **Web access** toggle is shown.
  - A **Notion** tool section shows:
    - "Pages shared with everyone in Naren Sathiya's Space"
    - Pages listed include **Customer Feedback** and **Customer Feedback
      Reports**, each showing **"Can edit content"**
    - "+ Add" (to add pages)
  - A "Notion agents" section appears with "+ Add agents"
  - A "+ Add connection" button is shown
- **Advanced** section shows:
  - **Model** set to "Auto"
  - **Trusted URLs** input with placeholder "Add domain, e.g. github.com"
  - **Allow every URL** toggle shown

### Notion tool permissions dropdown

A Notion page permission dropdown shows options including:

- "Full access" — "Full access to edit, change database views and
  structure, and control permissions"
- "Can edit content" — "Can edit content, but not database views or
  structure" (selected)
- "Can comment" — "Suggest and comment"
- "Can view"
- "Remove"

### Credits / usage panel

A panel titled **"Notion credits"** shows:

- "15 / 300 Notion credits" and a label "Resets Sep 30"
- "This period's usage" metrics including:
  - "Agent builders" — "1 members creating Custom Agents"
  - "Agents in action" — "1 live Custom Agents this month"
  - "Agents driving value" — "9 runs completed"

### Template output behavior (report generation)

In a chat titled **"Generate feedback report"**, the agent response shows:

- "Done — I generated this week's report (week of 2026-08-24). It
  records that no feedback entries were captured for 2026-08-24 through
  2026-08-30, so there are no themes/quotes to summarize."

The generated report page (right panel) shows:

- "Reporting period: 2026-08-24 to 2026-08-30 (7 days)"
- "Total feedback captured: 0"
- "Top themes" (followed by "No feedback entries were captured in this
  period, so nothing to report on themes/quotes to summarize.")
- "Newly rising" (shows "N/A ...")
- "Other signals" (shows "None.")

## Notes

Follow-ups to validate in a future run:

- Explore additional templates across categories ("Eng & Product",
  "Marketing", "Support", etc.) and compare differences in:
  - default tools/access
  - trigger models
  - degree of “workflow scaffolding”
- How permission inheritance works when someone else runs the agent (vs.
  the creator running it).
- Whether "Web access" and "Trusted URLs" defaults affect what URLs are
  actually reachable in practice.
- Whether the weekly trigger runs even if there is no interaction, and
  where those scheduled outputs land.

Subjective takeaways from the session:

- Navigation felt non-obvious for returning to the created pages/databases.
- Credits felt easy to understand at a glance.
