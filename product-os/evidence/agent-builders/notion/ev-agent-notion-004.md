---
id: ev-agent-notion-004
domain: agent_builder
source_type: docs
source_name: Notion Help
date: 2026-08-31
title: Notion Help: Custom Agents are persistent workspace objects
confidence: direct
url: https://www.notion.com/help/custom-agents
product_area: creation_model
tags:
  - custom-agent
  - docs
  - abstraction
---

# Notion Help: Custom Agents are persistent workspace objects

## Raw evidence

Fetched 2026-08-31 from
https://www.notion.com/help/custom-agents

Opening definition:

> Custom Agents live inside Notion and run on your instructions.
> Once you set them up, they can: Read from Notion pages and
> databases and certain connected apps. Run on recurring triggers
> and workspace events. Take actions such as posting reports,
> filing bugs, updating records, or sending messages. Hand off
> part of a job to other Custom Agents you give them access to.
> Unlike Notion Agent, Custom Agents are designed to run
> automatically in the background based on triggers and schedules.

> Custom Agents automate recurring, manual workflows for your
> entire team. They run automatically in the background on set
> triggers using your existing docs and databases as context.
> Set them up once to handle repetitive tasks like weekly reports
> or triaging feedback, and they become a shared resource the
> whole team relies on.

Access is per agent, not workspace-wide by default:

> Agents act only on the pages, databases, and external apps you
> explicitly grant access to. They never have full workspace
> access by default.
> Control who can edit, run, or interact with each Agent.
> View activity logs to see what an Agent did and when.
> Use Version history to review or restore past configurations.

Create paths: AI chat, template, or **Create blank**. Configure
instructions, triggers, access, and model, then Save.

Triggers listed: recurring schedule; Notion events (comment,
page added/updated/removed, AI meeting note finished); Slack
events (message posted, emoji reaction, agent mentioned).

Handoffs:

> A Custom Agent can pass part of a job to other Custom Agents
> during a run. This works when a workflow has separate jobs
> that need their own instructions, context, access, or model.

Model is a per-agent setting (Auto, Claude, GPT, Gemini, Grok).

Sharing uses page-like permissions: Full Access / Can Edit /
Can View and Interact.

Every Custom Agent page has three tabs: **Chat**, **Activity**
("a log of every agent run"), **Settings** (Instructions,
Triggers, access, model). Version history can restore a past
configuration (who changed what, when).

## Notes

First-party docs describe the thing you create as a named,
shareable, versioned agent object — not a one-off brief.
Matches hands-on `ev-agent-notion-001` / `003` (Customer
Feedback Tracker / Customer Feedback Triage Agent + Settings).

Activity / version history / handoffs / agent-level share were
not fully exercised in the first hands-on runs. Docs claim
them. Follow-up `ev-agent-notion-005`: researcher looked for
activity logs on these agents and they were **not visible**.

Follow-ups:

- Version history / handoff still unopened.
- Whether Activity is plan- or role-gated despite the help
  page not saying so.
