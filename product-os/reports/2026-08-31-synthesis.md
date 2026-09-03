# Synthesis report — 2026-08-31

_Generated at: 2026-08-31T22:24:13.260746+00:00_


## Evidence included

- `ev-agent-notion-001` — Notion: Collect customer feedback template (hands-on) (Notion Custom Agents)
- `ev-agent-notion-002` — Notion: Connect Slack as a trigger (hands-on) (Notion Custom Agents)
- `ev-agent-notion-003` — Notion: Custom feedback triage agent with email write + HITL (Notion Custom Agents)

## Strongest emerging insights


### `ev-agent-notion-001`

- **Account pulse** — "Tracks call notes, feedback, and outside signals
- **Pipeline manager** — "Pulls deal data from your CRM and reports on
- **Sales enablement navigator** — "Answers product and competitive
- "Creating database"
- "Loaded Notion tools"
- "Searched"

### `ev-agent-notion-002`

- From the existing **Customer Feedback Tracker** agent Settings panel, an
- **Add connection** modal opens.
- Left-side integration list includes (visible across frames):
- Calendar, Mail, Slack, Amplitude, Attio, Box, Buildkite, ClickHouse,
- Figma, GitHub, Grafana, Intercom, Linear, Mercury, Miro, Mixpanel, n8n,
- PostHog, Ramp, Sentry, Stripe, Wiz.

### `ev-agent-notion-003`

- Feedback summary
- Product area
- Underlying problem
- Sentiment
- Severity
- Theme

## Highest-value questions / experiments


### `ev-agent-notion-001`

- Explore additional templates across categories ("Eng & Product",
- default tools/access
- trigger models
- degree of “workflow scaffolding”
- How permission inheritance works when someone else runs the agent (vs.
- Whether "Web access" and "Trusted URLs" defaults affect what URLs are
- Whether the weekly trigger runs even if there is no interaction, and
- Navigation felt non-obvious for returning to the created pages/databases.
- Credits felt easy to understand at a glance.

### `ev-agent-notion-002`

- Slack security is explicit at two layers: Slack OAuth consent, then
- Connecting Slack as a *tool* and adding Slack as a *trigger* are
- A plain-text Slack post (no mention), while settings were unsaved,
- Unclear from this run alone whether the required ingredient was Save,
- Custom MCP is advertised in the same connection catalog as Slack.
- Finding the created database still required asking the agent
- Isolate Save vs @mention: post without mention after Save; mention
- Test whether "Message posted in #new-channel" fires on every message
- Confirm Read vs Read & Reply vs None against Slack reply behavior.
- Test private channels vs "All public channels".

### `ev-agent-notion-003`

- Custom start is instruction-schema-first: you paste a richer
- Write actions to Mail are gated by OAuth + granular toggles
- Test UX is strong: Run agent + chat chips that generate a page,
- Observability is step-level for the current chat, not an audit log
- Confirm whether Reject vs Continue is enforced by the Mail
- After send: is there any message-level unsend, or only Gmail’s own
- Open Credits and document what analytics actually exist.
- Compare this custom agent’s schema vs the template Customer

## Contradictions / uncertainty

- Not computed in V0.1 deterministic scaffold (needs multi-evidence comparison).
