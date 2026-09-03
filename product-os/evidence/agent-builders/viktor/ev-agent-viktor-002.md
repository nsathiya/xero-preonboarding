---
id: ev-agent-viktor-002
domain: agent_builder
source_type: docs
source_name: Viktor
date: 2026-08-31
title: Viktor docs: brief an employee, do not build a workflow
confidence: direct
url: https://viktor.com/blog/how-to-write-tasks-for-your-ai-employee
product_area: creation_model
tags:
  - task
  - employee
  - docs
  - marketing
  - abstraction
---

# Viktor docs: brief an employee, do not build a workflow

## Raw evidence

### How to Write Tasks for Your AI Employee

Fetched 2026-08-31 from
https://viktor.com/blog/how-to-write-tasks-for-your-ai-employee
By Kris Newlin. "Written with Viktor, the AI employee."

> A good task reads like a brief you would give a sharp new
> hire, not a search query. Say what you want, where the inputs
> are, and what the finished thing looks like.

A good task states **goal**, **inputs**, and **output**.
"You are writing a brief for a capable colleague, not a program."

Name source and destination. Example contrast:

- Bad: `@Viktor how are we doing on sales?`
- Good: `@Viktor look at the #sales channel from this week and
  our new-business pipeline in HubSpot. Post a 5-bullet summary
  here with total closed, biggest open deal, and anything stuck
  more than 5 days.`

Boundaries live in the task text: "show me before sending",
"read-only" / "do not change anything." Access settings are
"standing policy"; a phrase in the task is the per-task override.

Iteration: reply in the same thread with one correction. Memory
is supposed to make later briefs shorter.

Recurring: "Turn a task you repeat into a saved routine" —
e.g. "every Monday at 9, post last week's Google Ads and Meta
Ads changes to #growth in five bullets."

### Hire page (marketing)

Fetched 2026-08-31 from https://viktor.com/hire-an-ai-employee

Headline: **"Hire an AI Employee. Not Another Tool."**

> No rollout project and no prompt engineering. Install Viktor
> where your team already works, connect your tools, and
> delegate the first task in minutes.

> **No workflows to build. Just delegate.** Agent builders hand
> you a canvas and a manual. With an AI employee you describe
> the outcome — Viktor figures out the steps, the tools, and
> the schedule.

> A chatbot answers. An AI employee finishes.

FAQ: "Can my whole team share one AI employee?"

## Notes

Viktor is explicitly selling against the agent-builder /
workflow-canvas model. The unit you create is a **brief**
(goal / source / destination / shape / boundary) to one shared
employee, not a named agent object with its own instructions,
tools, model, and share settings.

Matches hands-on `ev-agent-viktor-001`: Slack "customer
feedback pipeline I fully run" → Viktor proposed the plan;
user approved. No Customer Feedback Agent object was created
on the portal (Tasks stayed empty).

Caveat: the task editor on the web is still unopened. If that
editor is a full per-task builder (instructions, tools, model,
activity), the marketing line is stronger than the product.

Follow-ups:

- Open a saved / approved task on the web and list what fields
  exist vs Notion Settings.
- Whether one Viktor can hold many named responsibilities that
  are shareable like Notion agents.
