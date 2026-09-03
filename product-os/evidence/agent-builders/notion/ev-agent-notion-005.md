---
id: ev-agent-notion-005
domain: agent_builder
source_type: hands_on
source_name: Notion Custom Agents
date: 2026-08-31
title: Notion: Help promises Activity logs; not visible on this workspace
confidence: direct
product_area: observability
tags:
  - activity
  - audit
  - docs-vs-product
---

# Notion: Help promises Activity logs; not visible on this workspace

## Raw evidence

Help Center page "Custom Agents in Notion"
(https://www.notion.com/help/custom-agents, also
`ev-agent-notion-004`) under **Safe & transparent by design**:

> Agents act only on the pages, databases, and external apps you
> explicitly grant access to. They never have full workspace
> access by default, reducing risk.
>
> Control who can edit, run, or interact with each Agent.
>
> View activity logs to see what an Agent did and when.
>
> Use Version history to review or restore past configurations.
>
> Keep runs reviewable and reversible so you can safely iterate.

Same page, **Audit log visibility (Enterprise)**:

> Key configuration and access changes to Custom Agents (like
> instruction updates, permission changes, and integration
> additions) are recorded in the Notion audit log. This helps
> Enterprise admins track agent changes for security and
> compliance reviews.

Same page also describes every Custom Agent page as having
three tabs: **Chat**, **Activity** ("a log of every agent
run" for Full Access users), **Settings**.

Researcher looked for **activity logs** on the Custom Agents
in this workspace (Customer Feedback Tracker / Customer
Feedback Triage Agent). **Not visible.** Verified; not a
missed click on a first pass.

What this workspace *has* shown on earlier runs (not an
Activity log):

- Per-chat / session step trace ("Cooking" → N steps /
  Success) — `ev-agent-notion-002`, `ev-agent-notion-003`
- Agent home **Recent chats**
- An **Insights** link on the agent home (not opened as a
  full run log)
- Workspace **Analytics** page that requires **Enterprise**
  to unlock AI usage views — `ev-agent-notion-003`

Version history and "reversible" runs were not found in this
check. Workspace audit log is documented as Enterprise-only.

## Notes

Docs sell "safe & transparent" with activity logs, version
history, and reversible runs. The product on this plan shows
a current-run step list and chat history. That is not the
Activity tab the help page describes.

Possible causes (unverified): plan/role gate not labeled in
the help section; feature not shipped to this workspace; UI
renamed or buried. The Enterprise audit-log paragraph is at
least honest about a gate. Activity logs are not marked
Enterprise in the same "Safe & transparent" block.

Follow-ups:

- Version history — also missing, or present elsewhere?
- Does Full Access vs Can View change whether Activity
  appears?
- Business vs Enterprise: is Activity bundled with the
  Analytics upsell?
