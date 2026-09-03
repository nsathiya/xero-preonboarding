---
id: note-agent-builders-matrix-dimension-guide-001
type: reference
effective_date: 2026-08-31
confidence: direct
---

# Agent builders — observation matrix dimension guide

This guide explains what each matrix section means and what to look for.

## How to capture well (rules of thumb)

- **Prefer “what happened” over “what it means.”** Save interpretation for `Notes` or `initial-insights-hypotheses.md`.
- **Capture the “where.”** Screen name, URL, doc page title, or the exact flow you followed.
- **Record constraints and defaults.** What’s the default behavior when you don’t configure anything?
- **Look for tradeoffs.** What did they optimize (speed vs control, power vs safety, builder vs end-user)?
- **Promote strong observations into evidence.** If a note might become an insight, make it an evidence file.

## Dimensions

### Getting started

**Meaning**: Time-to-first-agent and onboarding mechanics.

**Look for**:
- Templates vs blank-slate
- Required prerequisites (workspace setup, data connection, permissions)
- The “first success” moment (what counts as done?)
- Setup friction (account linking, verification, billing)

### Creation model

**Meaning**: How you define the agent.

**Look for**:
- Prompt-first vs workflow-first vs code-first vs hybrid
- Where tools/actions are configured (global vs per-step)
- How context is attached (agent-level vs run-level)
- Reusability patterns (components, subflows, libraries)

### Mental model

**Meaning**: What the product seems to believe an “agent” is.

**Look for**:
- Agent as “chatbot”, “workflow runner”, “autonomous worker”, “assistant with tools”
- Does it emphasize goals, steps, constraints, or outcomes?
- Is the agent stateful? Memory? Long-running?

### Agent abstraction / delegation model

**Meaning**: What the user actually creates, and how much execution logic they specify vs hand to the model.

This is the split across Notion, Viktor, and Zapier. Do not collapse it into “mental model” or “creation model.”

**Ask first**:
- **What does the user create?** Workflow / Agent / AI employee (or task, prompt, automation, responsibility)
- **How much of the execution plan does the user define vs delegate?**

**Look for**:
- Is that object persistent, named, shareable, versioned, with its own activity log?
- Are tools/access granted per object, or to one shared employee?
- Recurring work: configure triggers on the object, or tell the employee “make this recurring”?
- Does marketing contrast itself with “agent builders” or “workflow canvas”?
- Setup burden vs control (higher control usually means more human-specified logic)
- Does marketing say “teammate / employee” while the shipped object is a Zap / workflow / step?

Two plots (place the product; do not force it):

```text
More explicit workflow control              More delegated autonomy

Zapier ────────────── Notion ────────────── Viktor
high-control           persistent agent      high-autonomy
low-autonomy           no full step graph    low-workflow-control
```

Primary abstraction:

```text
Workflow  →  Agent  →  AI employee
 Zapier      Notion      Viktor
```

This is more useful than a feature checklist.

### Context / knowledge

**Meaning**: What information the agent can use and how it’s scoped.

**Look for**:
- Data sources (docs, CRM, spreadsheets, databases)
- Retrieval/search model (implicit vs explicit knowledge bases)
- Scoping controls (which spaces, which records, which timeframe)
- Freshness and sync (real-time vs snapshot)

### Tools / actions

**Meaning**: What the agent can do (capabilities surface).

**Look for**:
- Native actions vs external integrations
- Parameterization (how you pass inputs, map fields)
- Tool discovery UX (catalog, search, recommended tools)
- Guardrails (rate limits, dry-run, approval required)

### Permissions

**Meaning**: Authorization model: what the agent can know vs do.

**Look for**:
- Inheritance (creator’s permissions? runner’s? workspace?)
- Granularity (per-tool, per-connection, per-record)
- Consent flow (OAuth, admin approval, one-time vs per-run)
- Auditability (who authorized what, when)

### Sharing

**Meaning**: Reuse and ownership model.

**Look for**:
- Private vs team vs org
- Copy vs shared single instance
- Ownership transfer / lifecycle
- Discoverability (marketplace, internal gallery)

### MCP / extensibility

**Meaning**: How you extend capabilities beyond built-ins.

**Look for**:
- MCP support, custom tool APIs, SDKs
- Auth strategy for custom tools
- Local vs hosted execution
- Tool schema definition and testing

### Triggers

**Meaning**: How and when the agent runs.

**Look for**:
- Manual run vs scheduled vs event-driven
- Input payload model (what data arrives on trigger)
- Idempotency and dedupe controls
- Multi-run concurrency/limits

### Human-in-loop

**Meaning**: Where approval, review, and escalation live.

**Look for**:
- Approval points (before tool call? before final output? per-step?)
- Who can approve (creator vs admin vs operator)
- Escalation UX (handoff to human, comments, assignments)
- “Safe mode” vs “auto mode”

### Testing

**Meaning**: How you validate behavior before trusting it.

**Look for**:
- Sandbox environments, mock data, preview runs
- Replayability (same inputs → same outputs?)
- Unit-test-like constructs (fixtures, assertions)
- Test coverage visibility

### Debugging

**Meaning**: How you understand and fix failures.

**Look for**:
- Step-by-step trace, tool call inputs/outputs
- Error messages quality and suggested fixes
- Ability to re-run from a step
- Diff between versions of an agent

### Observability

**Meaning**: Operational view over time.

**Look for**:
- Run history, logs, performance, cost/usage
- Attribution (who ran it, what data, what changed)
- Alerts and monitoring
- Governance reporting

### Failure handling

**Meaning**: Recovery and resilience.

**Look for**:
- Retries, backoff, partial completion handling
- Compensation actions (rollback / undo)
- Dead-letter queues / manual remediation
- User messaging when failures happen

### Iteration UX

**Meaning**: How easy it is to evolve an agent.

**Look for**:
- Editing experience (prompt editing, workflow editing)
- Versioning and rollback
- Migration of existing runs/trigger configs
- How changes are tested/deployed

### Discoverability

**Meaning**: How users find and choose agents.

**Look for**:
- Search/browse, recommendations
- Quality signals (ratings, usage, last updated)
- Docs and examples
- Trust signals (verified, admin-approved)

### Governance

**Meaning**: Admin controls and policy enforcement.

**Look for**:
- Admin policy controls (allowed tools, data scopes)
- Audit trails, approvals logs
- Lifecycle controls (disable, archive)
- Compliance posture (data retention, access control)

### Pricing

**Meaning**: How value is monetized and constrained.

**Look for**:
- Seat vs usage vs credits
- Limits (runs, actions, tokens, connectors)
- Overage model and predictability
- Pricing tied to “agent” vs “execution”

### Delight / friction

**Meaning**: The memorable UX moments.

**Look for**:
- “Wow” moments that reduce effort meaningfully
- Sharp friction points (confusing concepts, repeated steps)
- Where you felt uncertainty or lack of control

### Evidence quality (overall)

**Meaning**: How trustworthy your capture is.

**Look for**:
- Hands-on vs docs vs marketing
- First-party vs third-party sources
- Anything you didn’t verify but suspect

