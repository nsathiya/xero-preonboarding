---
id: ev-agent-viktor-003
domain: agent_builder
source_type: hands_on
source_name: Viktor
date: 2026-08-31
title: Viktor: Tasks portal empty; employee says backend task is live
confidence: direct
product_area: observability
tags:
  - slack
  - portal
  - tasks
  - disconnect
---

# Viktor: Tasks portal empty; employee says backend task is live

## Raw evidence

Follow-up to `ev-agent-viktor-001`. Researcher tried to open the
web task editor for the customer-feedback pipeline. The Tasks
portal still showed no task (count **0** / empty list). The
editor was not reachable from the portal.

Viktor (in Slack), after the researcher sent a screenshot,
replied (paraphrase kept close; quoted claims are Viktor's):

- Researcher is "in the right place and signed in correctly."
- Viktor "re-verified the task directly in the system:
  **Customer Feedback Weekly Digest** exists, is **active**
  (not paused), and is tied to [the researcher's] user."
- "The Tasks page showing '0' while the task is live in the
  backend looks like a portal sync/display bug on Viktor's
  side."

Viktor suggested:

- Sign out and back in (fresh session).
- Check the **Calendar** view (top right) — "sometimes the
  list and calendar views load separately."

If still empty: Viktor offered to file an issue with the
Viktor team, or email `support@getviktor.com`.

Viktor's diagnosis:

> this is purely a display issue. The schedule runs from the
> backend, so your Monday 9 AM digest will arrive either way —
> nothing about the pipeline is broken.

Researcher then tried Viktor's two fixes. **Sign out and back
in** did not populate Tasks. **Calendar view** also empty / no
task. Editor still unreachable.

Researcher did not independently open a backend admin view.
The Monday digest has not yet fired (not yet Monday 9 AM
Chicago).

## Notes

The inspectable object still does not exist on the portal after
a later session, a sign-out, and Calendar view. Viktor's two
suggested fixes failed. Slack / "the system" is the only place
that will assert the job exists. That may be a real portal bug.
It may also be that a Slack-created task is not a first-class
portal object.

Either way, the operator cannot open an editor, cannot see
steps / scopes / test, and is told to trust the employee that
the job will run. Support also lives in Slack (the employee
offers to file the ticket).

Do not treat "purely a display issue" or "pipeline is not
broken" as verified. Those are Viktor's claims.

Follow-ups:

- Does Monday 9 AM actually deliver the digest?
- If the task ever appears (support ticket / later session),
  what does the editor contain?
