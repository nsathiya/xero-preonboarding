# Product OS Learning Harness --- V1 PRD / TDD

**Status:** Draft\
**Scope:** Pre-onboarding / personal learning harness\
**Primary user:** Naren\
**Initial domains:** Agent builders, customer sentiment, competitors,
accounting/product knowledge

------------------------------------------------------------------------

## 1. Summary

Build a lightweight, evidence-first learning harness that lets a user
periodically add **evidence** and **context**, then regenerate a current
set of:

-   Insights
-   Hypotheses
-   Implications
-   Experiments / questions to validate

The initial use case is Xero pre-onboarding research. The same
underlying system should support four connected workstreams:

1.  Agent-builder research
2.  Customer feedback / sentiment analysis
3.  Competitive intelligence
4.  Accounting and product knowledge

The system should optimize for **learning and synthesis**, not knowledge
management for its own sake. It should make it easy to trace every
conclusion back to evidence, distinguish observations from inference,
and update conclusions as new evidence arrives.

V1 should be intentionally simple: local files / Markdown, a small
amount of structured metadata, LLM-assisted extraction and synthesis,
and generated Markdown reports. No production integrations, elaborate
database, or custom UI are required.

------------------------------------------------------------------------

# PRD

## 2. Problem

Research and product signals accumulate across disconnected sources:
product usage notes, screenshots, pricing pages, customer conversations,
Slack, interviews, competitor research, and domain-learning material.

The failure mode is not lack of information. It is that:

-   evidence becomes fragmented;
-   observations get mixed with conclusions;
-   patterns across sources are difficult to notice;
-   prior insights become stale as new evidence arrives;
-   conclusions lose provenance;
-   research often becomes a static document rather than a living
    learning system;
-   useful connections across customer, competitive, product, and domain
    evidence are missed.

For the Xero pre-onboarding work specifically, the four requested areas
can become isolated research exercises. A shared evidence-to-insight
harness allows each area to compound the others.

------------------------------------------------------------------------

## 3. Product Thesis

A useful Product OS starts with a simple loop:

> **Context → Evidence → Observations → Patterns → Insights → Hypotheses
> → Implications → Experiments → New Evidence**

The system should not try to be "correct" once. It should maintain a
current set of beliefs that can change as evidence accumulates.

The fundamental design principle is:

> **Evidence persists; interpretations evolve.**

------------------------------------------------------------------------

## 4. V1 Goal

Enable the user to continuously add evidence and context across several
domains and generate evidence-backed synthesis that helps answer:

1.  **What am I observing?**
2.  **What patterns are emerging?**
3.  **What might those patterns mean?**
4.  **Why might they matter for Xero / XeroForce?**
5.  **What do I currently believe?**
6.  **What evidence would strengthen or falsify those beliefs?**
7.  **What should I investigate, test, or ask next?**

### V1 success criterion

After adding a meaningful body of evidence, the harness should surface
at least some **non-obvious, useful, evidence-backed connections or
hypotheses** that are more valuable than a summary of the source
material.

If the output is only a cleaner restatement of the inputs, V1 has
failed.

------------------------------------------------------------------------

## 5. Non-Goals

V1 is **not**:

-   a production Product OS for Xero;
-   a replacement for Xero's existing research or feedback systems;
-   a production customer-feedback ingestion pipeline;
-   an autonomous product decision-maker;
-   a polished collaboration product;
-   a real-time Slack/support integration;
-   a perfect ontology;
-   a comprehensive accounting knowledge graph;
-   an enterprise vector-search platform;
-   an agent swarm;
-   a system that automatically prioritizes roadmap decisions without
    human judgment.

The goal is to learn whether the evidence → insight loop is valuable.

------------------------------------------------------------------------

## 6. Product Principles

### 6.1 Evidence first

Raw evidence should be retained and never silently rewritten into
conclusions.

### 6.2 Provenance by default

Every observation, insight, hypothesis, and implication should be
traceable to the evidence supporting it.

### 6.3 Separate fact from inference

The system should distinguish:

-   **Evidence** --- what the source actually says/shows.
-   **Observation** --- structured description of what was observed.
-   **Insight** --- interpretation across one or more observations.
-   **Hypothesis** --- a belief that could be tested or falsified.
-   **Implication** --- why the insight/hypothesis could matter.
-   **Experiment** --- a way to gather additional evidence.

### 6.4 Context informs; it does not become evidence

Company goals, product goals, strategy, domain knowledge, and long-term
motivations help interpret evidence. They should not be treated as proof
of a conclusion.

### 6.5 Insights are revisable

New evidence may:

-   strengthen an insight;
-   weaken it;
-   contradict it;
-   split it into multiple insights;
-   merge it with another insight;
-   make it obsolete.

### 6.6 Human judgment stays in the loop

The harness proposes patterns and interpretations. The user decides what
deserves attention and what should become an active hypothesis or
experiment.

### 6.7 Prefer simple infrastructure

Use files and generated artifacts until their limitations become real.

------------------------------------------------------------------------

## 7. Conceptual Model

``` text
                         CONTEXT
        ┌─────────────────────────────────────┐
        │ Company goals / strategy            │
        │ Product goals / XeroForce thesis    │
        │ Long-term motivations               │
        │ Accounting / product knowledge      │
        └──────────────────┬──────────────────┘
                           │ informs
                           ▼
                        EVIDENCE
          ┌────────────────┼────────────────┐
          │                │                │
   Agent builders      Customers       Competitors
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                 STRUCTURED OBSERVATIONS
                           │
                           ▼
                    PATTERNS / THEMES
                           │
                           ▼
                        INSIGHTS
                           │
                           ▼
                       HYPOTHESES
                           │
                           ▼
                      IMPLICATIONS
                           │
                           ▼
                 EXPERIMENTS / QUESTIONS
                           │
                           ▼
                      NEW EVIDENCE
```

------------------------------------------------------------------------

## 8. Core Objects

### 8.1 Context

Relatively durable information used to interpret evidence.

Examples:

-   Xero company goals
-   XeroForce product goals
-   target users/personas
-   strategic priorities
-   current product bets
-   long-term AI/product thesis
-   accounting concepts and workflows
-   known constraints
-   relevant product architecture

Suggested fields:

``` yaml
id:
type: company_goal | product_goal | strategy | motivation | domain_knowledge | constraint
title:
content:
source:
effective_date:
confidence:
tags:
```

------------------------------------------------------------------------

### 8.2 Evidence

The atomic source object.

Evidence may be:

-   a note from hands-on product usage;
-   screenshot;
-   documentation excerpt;
-   pricing observation;
-   customer quote;
-   Slack message;
-   interview note;
-   in-product feedback;
-   competitor claim;
-   workflow description;
-   accounting learning note.

Suggested fields:

``` yaml
id:
domain: agent_builder | customer | competitor | product_knowledge
source_type:
source_name:
date:
title:
raw_content:
url:
artifact_path:
author_or_customer:
product_area:
tags:
confidence: direct | documented | secondhand | inferred
```

**Rule:** `raw_content` should preserve the original observation as much
as practical.

------------------------------------------------------------------------

### 8.3 Observation

Structured extraction from evidence.

Examples:

-   "Agent inherits the creator's Notion permissions."
-   "Customer expresses strong frustration with reconciliation
    exceptions."
-   "Competitor positions AI as autonomous workflow completion rather
    than assistance."

Suggested fields:

``` yaml
id:
evidence_ids:
statement:
dimension:
entities:
sentiment:
intensity:
problem:
job_to_be_done:
product_area:
tags:
confidence:
```

Not every field applies to every domain.

------------------------------------------------------------------------

### 8.4 Pattern / Theme

A recurring relationship across observations.

``` yaml
id:
title:
description:
observation_ids:
evidence_ids:
domains:
support_count:
contradicting_evidence_ids:
confidence:
last_updated:
```

Patterns can exist within one domain or across domains.

------------------------------------------------------------------------

### 8.5 Insight

A useful interpretation of one or more patterns.

``` yaml
id:
statement:
why_it_matters:
pattern_ids:
evidence_ids:
context_ids:
confidence:
counter_evidence:
created_at:
updated_at:
status: emerging | supported | challenged | superseded
```

------------------------------------------------------------------------

### 8.6 Hypothesis

A testable belief derived from insights.

Example:

> XeroForce's differentiation may depend more on accounting-specific
> permissions, context, and trust than on agent-creation UX.

``` yaml
id:
statement:
insight_ids:
supporting_evidence_ids:
assumptions:
confidence:
what_would_strengthen:
what_would_falsify:
status: proposed | investigating | supported | rejected
```

------------------------------------------------------------------------

### 8.7 Implication

Why a hypothesis or insight could matter for Xero/XeroForce.

Possible implication types:

-   product
-   UX
-   architecture
-   go-to-market
-   governance
-   pricing
-   organizational
-   research

``` yaml
id:
statement:
type:
insight_ids:
hypothesis_ids:
context_ids:
importance:
confidence:
```

------------------------------------------------------------------------

### 8.8 Experiment / Question

A concrete next learning action.

Experiments do not need to be software experiments. They may be:

-   build a workflow;
-   interview a PM;
-   inspect an internal process;
-   ask a customer;
-   compare two permission models;
-   find counterexamples;
-   analyze another set of feedback.

``` yaml
id:
question:
hypothesis_ids:
method:
expected_learning:
success_or_decision_criteria:
status: backlog | active | complete
result_evidence_ids:
```

------------------------------------------------------------------------

# 9. Initial Domain Schemas

## 9.1 Agent Builder Research

Initial products:

-   HubSpot Agent Builder
-   Notion Custom Agents
-   Viktor
-   Zapier AI Agents

### V1 working locations (scaffolded)

-   **Evidence (agent builders)**: `product-os/evidence/agent-builders/`
    -   Quick capture inbox: `product-os/evidence/agent-builders/_inbox/`
    -   Product folders: `hubspot/`, `notion/`, `viktor/`, `zapier/`
-   **Observation-matrix working notes** (fast capture, not raw evidence):
    `product-os/notes/agent-builders/matrix/` (plus index at
    `product-os/notes/agent-builders/observation-matrix-notes.md`)
    -   Promote strong notes into a proper evidence file under the
        relevant product folder.

### Evidence capture workflow (recommended)

1.  Capture quickly in the matrix notes while researching/using a
    product.
2.  Create 1--3 evidence files for the strongest observations (hands-on
    preferred).
3.  Run validation (`product-os validate`) to keep frontmatter
    consistent.
4.  Only after multiple evidence items exist: draft initial
    insights/hypotheses as *emerging* and explicitly list what evidence
    would falsify them.

### Observation matrix

  -----------------------------------------------------------------------
  Dimension                           What to capture
  ----------------------------------- -----------------------------------
  Getting started                     Setup, templates,
                                      time-to-first-agent

  Creation model                      Prompt, workflow, visual,
                                      conversational, code

  Mental model                        What does the product appear to
                                      believe an agent is?

  Context / knowledge                 Available data, scoping, retrieval

  Tools / actions                     Native actions, external tools,
                                      APIs

  Permissions                         What can the agent know vs. do? How
                                      is authorization inherited?

  Sharing                             Private, team, org, ownership

  MCP / extensibility                 MCP, custom tools, APIs,
                                      authentication

  Triggers                            Manual, scheduled, event-driven

  Human-in-loop                       Approval, confirmation, escalation

  Testing                             Preview, sandbox, test runs

  Debugging                           Ability to understand failures and
                                      behavior

  Observability                       Logs, history, traces, usage/cost

  Failure handling                    Retry, recovery, partial completion

  Iteration UX                        Ease of changing an existing agent

  Discoverability                     How users find/use agents built by
                                      others

  Governance                          Admin controls, auditing, lifecycle

  Pricing                             Seat/run/usage/credit model

  Delight / friction                  Strong positive or negative UX
                                      moments

  Evidence quality                    Direct use, docs, marketing,
                                      inference
  -----------------------------------------------------------------------

### Desired output

Not merely a completed matrix. The harness should find:

-   convergence across products;
-   meaningful differences;
-   unexplained product choices;
-   emerging design patterns;
-   tradeoffs;
-   implications for XeroForce;
-   questions worth validating internally.

------------------------------------------------------------------------

## 9.2 Customer Feedback / Sentiment

V1 customer analysis should go beyond positive / neutral / negative.

Extract where possible:

-   sentiment;
-   sentiment intensity;
-   topic;
-   product area;
-   underlying problem;
-   job-to-be-done;
-   requested solution;
-   severity;
-   recurrence/frequency;
-   customer/persona/segment context;
-   evidence quality.

Example derived observation:

``` text
Topic: reconciliation exceptions
Sentiment: negative
Intensity: high
Problem: diagnosing why reconciliation does not balance
Requested solution: unspecified
Product area: reconciliation
Evidence: customer interview #12
```

### Desired outputs

-   sentiment by theme/product area;
-   recurring problems;
-   emerging themes;
-   high-intensity friction;
-   differences between requested solutions and underlying problems;
-   hypotheses about customer needs;
-   relevance to company/product goals;
-   questions requiring more evidence.

------------------------------------------------------------------------

## 9.3 Competitor Intelligence

Initial competitors include Aider from Karbon and Digits.

Capture:

  -----------------------------------------------------------------------
  Dimension                           Question
  ----------------------------------- -----------------------------------
  Customer                            Who is the target user/customer?

  Problem                             What pain is emphasized?

  Product thesis                      What future are they betting on?

  AI role                             Assistant, copilot, automation,
                                      agent, intelligence?

  Workflow                            Where does AI enter the accounting
                                      workflow?

  UX                                  How does the user interact with AI?

  Trust                               Review, approvals, explanations,
                                      controls

  Differentiation                     What do they claim is unique?

  Integration/context                 What proprietary or connected
                                      context powers the product?

  Business model                      How is value monetized?

  Evidence quality                    Product use, docs, marketing, third
                                      party
  -----------------------------------------------------------------------

### Desired outputs

-   competitor patterns;
-   strategic differences;
-   emerging category assumptions;
-   connections to customer evidence;
-   connections to agent-builder patterns;
-   implications/questions for XeroForce.

------------------------------------------------------------------------

## 9.4 Accounting / Product Knowledge

This domain primarily supplies context.

Capture:

-   concepts;
-   entities;
-   actors;
-   workflows;
-   workflow stages;
-   terminology;
-   controls;
-   dependencies;
-   common pain points;
-   relevant Xero product areas.

For example, month-end-close material should help the harness understand
where later customer or competitor evidence fits in the accounting
workflow.

V1 should **not** attempt to automatically infer strategic insights
solely from educational/domain material.

------------------------------------------------------------------------

# 10. Primary User Flows

## Flow A --- Add evidence

1.  User creates/drops a Markdown/text artifact into the relevant
    evidence folder.
2.  Evidence contains minimal metadata.
3.  Harness assigns/validates an ID.
4.  Harness extracts structured observations.
5.  Original evidence remains available unchanged.

## Flow B --- Add context

1.  User adds/updates company, product, strategic, or domain context.
2.  Context is indexed separately from evidence.
3.  Future synthesis can use the new context.
4.  Existing evidence is not modified.

## Flow C --- Refresh insights

User runs a command such as:

``` bash
product-os synthesize
```

System:

1.  loads current context;
2.  loads all/new evidence;
3.  generates/updates observations;
4.  identifies patterns;
5.  compares patterns with existing insights;
6.  updates insights;
7.  proposes hypotheses;
8.  generates implications;
9.  proposes experiments/questions;
10. produces a report.

## Flow D --- Inspect provenance

For any generated insight/hypothesis:

1.  user can see supporting evidence IDs;
2.  user can inspect counter-evidence;
3.  user can see which context informed the implication;
4.  user can distinguish direct evidence from inference.

## Flow E --- Periodic refresh

Later versions may run the same synthesis automatically on a schedule
and produce a weekly learning report.

V1 only needs the manual command.

------------------------------------------------------------------------

# 11. Outputs

## 11.1 Current Insights

A living artifact such as:

`outputs/current-insights.md`

Each insight should include:

-   statement;
-   why it matters;
-   supporting evidence;
-   counter-evidence;
-   confidence;
-   related hypotheses;
-   last updated.

------------------------------------------------------------------------

## 11.2 Hypothesis Register

`outputs/hypotheses.md`

Include:

-   hypothesis;
-   supporting insights/evidence;
-   assumptions;
-   confidence;
-   what would strengthen it;
-   what would falsify it;
-   status.

------------------------------------------------------------------------

## 11.3 Implications

`outputs/implications.md`

Organized where useful by:

-   Xero;
-   XeroForce;
-   product;
-   UX;
-   architecture;
-   governance;
-   pricing;
-   research.

------------------------------------------------------------------------

## 11.4 Experiment / Question Backlog

`outputs/experiments.md`

Prioritize learning actions rather than only build experiments.

------------------------------------------------------------------------

## 11.5 Synthesis Report

`reports/YYYY-MM-DD-synthesis.md`

Suggested structure:

1.  Executive summary
2.  What changed since the previous synthesis
3.  Strongest emerging insights
4.  New / strengthened / weakened hypotheses
5.  Cross-domain patterns
6.  Customer sentiment / themes
7.  Competitive observations
8.  Agent-builder observations
9.  Implications for Xero/XeroForce
10. Contradictions / uncertainty
11. Highest-value questions and experiments
12. Evidence added this period

For V1 this report is manually generated. A scheduled weekly report is a
later-version capability.

------------------------------------------------------------------------

# 12. Success Metrics

V1 should be evaluated qualitatively.

### Utility

-   Did the system surface something the user had not explicitly written
    as a conclusion?
-   Did it connect evidence across domains?
-   Did it change what the user wanted to investigate next?

### Grounding

-   Can every important claim be traced to evidence?
-   Does the report clearly distinguish evidence from inference?
-   Are contradictions surfaced rather than hidden?

### Maintainability

-   Can new evidence be added in under a few minutes?
-   Can synthesis be rerun without manually rebuilding previous work?
-   Do old insights update cleanly as new evidence arrives?

### Signal-to-noise

-   Are generated insights meaningfully more useful than summaries?
-   Are weak/speculative insights identified as low confidence?
-   Is the number of outputs small enough to reason about?

------------------------------------------------------------------------

# TDD

## 13. Technical Approach

V1 should be a **local, file-based harness** with a small processing
pipeline.

``` text
Markdown / text / artifacts
            │
            ▼
      Evidence loader
            │
            ▼
   Metadata validation
            │
            ▼
 Observation extraction
            │
            ▼
   Evidence / observation index
            │
            ▼
 Pattern + synthesis pass
            │
            ▼
 Insight reconciliation
            │
            ▼
 Hypotheses / implications
            │
            ▼
 Experiments / report
```

No database is required initially.

------------------------------------------------------------------------

## 14. Proposed Repository Structure

``` text
product-os/
│
├── README.md
├── config/
│   ├── domains.yaml
│   └── synthesis.yaml
│
├── context/
│   ├── company/
│   ├── product/
│   ├── xeroforce/
│   ├── strategy/
│   └── accounting/
│
├── evidence/
│   ├── agent-builders/
│   │   ├── hubspot/
│   │   ├── notion/
│   │   ├── viktor/
│   │   └── zapier/
│   ├── customers/
│   ├── competitors/
│   │   ├── aider/
│   │   └── digits/
│   └── product-knowledge/
│
├── derived/
│   ├── observations/
│   ├── patterns/
│   └── index/
│
├── outputs/
│   ├── current-insights.md
│   ├── hypotheses.md
│   ├── implications.md
│   └── experiments.md
│
├── reports/
│
├── prompts/
│   ├── extract-observations.md
│   ├── discover-patterns.md
│   ├── reconcile-insights.md
│   ├── generate-hypotheses.md
│   └── generate-report.md
│
└── src/
    ├── ingest.*
    ├── extract.*
    ├── synthesize.*
    ├── reconcile.*
    └── report.*
```

Implementation language can follow the chosen harness. The architecture
should not depend on a specific framework.

### Current implementation scaffold (created)

A concrete scaffold exists in this workspace at `product-os/` with:

-   `config/` basic validation config
-   `evidence/` and `context/` directories per this spec
-   `notes/agent-builders/observation-matrix-notes.md` for fast capture
-   a minimal CLI:
    -   `product-os new-evidence ...`
    -   `product-os validate`
    -   `product-os build-index`

See `product-os/README.md` for setup/run commands.

------------------------------------------------------------------------

## 15. Storage Strategy

### V1

Use Markdown/YAML files as the system of record.

Benefits:

-   human-readable;
-   git-friendly;
-   easy to edit;
-   easy for an LLM harness to consume;
-   provenance is transparent;
-   no migration/database work;
-   easy to abandon or restructure.

### Optional derived index

If corpus size makes full-context synthesis impractical, add a
lightweight derived index:

-   SQLite; and/or
-   embeddings/vector index.

This should be introduced only when necessary.

**Do not make embeddings a V1 requirement.**

For the initial pre-onboarding corpus, hierarchical LLM synthesis over
files may be sufficient.

------------------------------------------------------------------------

## 16. Deterministic vs. Model Responsibilities

V1 should minimize nondeterministic behavior wherever a stable software rule can do the job.

> **Rule:** If an operation can be expressed as a stable transformation, validation, calculation, lookup, or state-management rule, implement it deterministically. Use the model only where semantic interpretation, synthesis, or judgment is actually required.

The architecture should be divided into three responsibility layers.

### 16.1 Deterministic data layer

Python or equivalent deterministic code owns:

```text
files
  ↓
discovery
  ↓
parsing
  ↓
schema validation
  ↓
normalization
  ↓
ID assignment
  ↓
change detection
  ↓
relationship/provenance management
  ↓
derived-state persistence
```

This layer should manage the factual mechanics of the system.

The model should **not** invent or calculate IDs, counts, dates, source relationships, provenance, file state, or other values that can be derived directly from the corpus.

### 16.2 Semantic extraction layer

Models are used when messy evidence must be interpreted into structured observations.

Example:

```text
Raw evidence:

"I'm constantly having to go back through five accounts
during close because I can't tell which reconciliation
is causing the issue."

        ↓ model extraction

{
  "product_area": "reconciliation",
  "sentiment": "negative",
  "intensity": "high",
  "problem": "difficulty identifying source of reconciliation discrepancy",
  "workflow": "month-end close"
}

        ↓ deterministic validation

schema-valid derived observation
linked to original evidence ID
```

Model output should always be treated as a **proposal** until it passes deterministic schema validation.

Preferred flow:

```text
LLM extraction
      ↓
structured JSON
      ↓
Python validation
      ↓
valid derived object
```

Avoid pipelines where models write unvalidated free-form state directly into the system of record.

### 16.3 Reasoning and synthesis layer

Models are intentionally used for:

```text
observations
    ↓
themes
    ↓
patterns
    ↓
insights
    ↓
hypotheses
    ↓
implications
    ↓
experiments
```

Even here, deterministic code should provide the model with measurable facts where possible, such as:

- number of supporting observations;
- number of independent sources;
- number of products/domains represented;
- number of direct vs. inferred observations;
- contradicting evidence count;
- evidence dates;
- evidence confidence levels;
- previously recorded insight state.

The model interprets those facts rather than inventing them.

### 16.4 Implementation responsibility matrix

| Stage | Default implementation | Why |
|---|---|---|
| File discovery | Python | Fully deterministic |
| Markdown/YAML/frontmatter parsing | Python | Fully deterministic |
| Schema validation | Python | Fully deterministic |
| Stable ID generation | Python | Fully deterministic |
| File hashing / change detection | Python | Fully deterministic |
| Exact duplicate detection | Python | Fully deterministic |
| Evidence → source relationships | Python | Explicit references |
| Context/evidence separation | Python | Based on schema/type/path |
| Date normalization | Python | Rules-based |
| Known-tag normalization | Python | Deterministic when taxonomy exists |
| Entity alias normalization | Python | Deterministic when alias map exists |
| Observation extraction | LLM | Semantic interpretation |
| Sentiment classification | LLM initially | Language-dependent; may later use a classifier |
| Sentiment label normalization | Python | Map model output to controlled vocabulary |
| Problem / JTBD extraction | LLM | Semantic interpretation |
| Product-area classification | Hybrid | Rules/taxonomy where known; LLM when ambiguous |
| Theme discovery | LLM initially | Requires semantic grouping |
| Similarity calculation | Embeddings + Python later | Deterministic once vectors exist |
| Clustering | Python later | Algorithmic once embeddings exist |
| Pattern naming / explanation | LLM | Semantic interpretation |
| Insight generation | LLM | Requires synthesis |
| Hypothesis generation | LLM | Requires reasoning/judgment |
| Xero/XeroForce implications | LLM + context | Contextual interpretation |
| Experiment/question generation | LLM | Reasoning |
| Evidence/support counts | Python | Deterministic |
| Contradiction counts | Python once relationships exist | Deterministic |
| Confidence inputs | Python | Counts, source quality, contradiction metrics |
| Confidence band assignment | Rules preferred | More stable than subjective model confidence |
| Confidence explanation | LLM optional | Narrative only |
| Provenance / citations | Python | Must not be hallucinated |
| Insight versioning | Python | State management |
| New/changed evidence detection | Python | State comparison |
| Strengthened/weakened/challenged insight classification | Hybrid | Deterministic deltas + semantic judgment |
| Markdown report assembly | Python/template | Deterministic |
| Report narrative | LLM | Optional semantic layer |
| Scheduled execution | System scheduler later | Deterministic orchestration |

### 16.5 Normalization vs. interpretation

The boundary between normalization and semantic interpretation should be explicit.

Normalization example:

```text
"Zapier"
"Zapier Agents"
"Zapier AI Agents"

        ↓ Python alias map

zapier_ai_agents
```

Interpretation example:

```text
"Zapier appears optimized for automation builders
rather than end users."

        ↓ model reasoning

product-positioning observation
```

Another normalization example:

```text
"negative"
"Negative"
"NEG"

        ↓ Python

negative
```

But deciding whether a customer statement is negative in the first place is semantic classification and belongs in the model layer.

### 16.6 Confidence should be evidence-driven

Avoid prompting the model with only:

> "How confident are you?"

Instead, deterministic code should calculate or provide inputs such as:

```text
supporting_evidence = 8
independent_sources = 4
direct_observations = 6
contradictions = 1
domains = 3
```

A simple rules-based rubric can then assign:

```text
Low
Medium
High
```

The model may explain the confidence level, but should not be the sole source of it.

### 16.7 Hard system constraints

The following should be treated as architectural constraints:

1. **Models may derive from evidence, but may not mutate source evidence.**
2. **All model-generated objects must carry explicit source evidence IDs.**
3. **Generated objects must record generator/model version and timestamp.**
4. **All structured model output must pass schema validation before persistence.**
5. **Models must never fabricate provenance, counts, dates, IDs, or source relationships.**
6. **Context may influence interpretation but must never be presented as supporting evidence unless it is itself explicitly modeled as evidence.**
7. **Deterministic state should be reproducible from the underlying corpus wherever practical.**

### 16.8 Design objective

The goal is not to remove models from the system. It is to place them exactly where they add value:

> **Software manages truth, state, structure, and provenance. Models manage meaning, synthesis, and interpretation.**

------------------------------------------------------------------------

## 17. Evidence File Format

Example:

``` markdown
---
id: ev-agent-notion-001
domain: agent_builder
source_type: hands_on
source_name: Notion Custom Agents
date: 2026-08-31
product_area: permissions
confidence: direct
tags:
  - permissions
  - sharing
---

# Permission behavior during workflow test

## Raw evidence

When I attempted to have the agent access...

## Notes

Optional human notes. These are commentary and should not be treated as raw evidence.
```

For customer evidence:

``` markdown
---
id: ev-customer-001
domain: customer
source_type: interview
date: 2026-08-31
customer: anonymized-customer-a
product_area: reconciliation
confidence: direct
---

# Interview excerpt

## Raw evidence

...

## Notes

...
```

------------------------------------------------------------------------

## 18. Context File Format

Example:

``` markdown
---
id: ctx-xeroforce-goal-001
type: product_goal
effective_date: 2026-08-31
confidence: documented
---

# XeroForce product goal

[Goal / strategy text]

## Source

[Where this context came from]
```

Context should always carry a source and confidence when possible.

------------------------------------------------------------------------

## 19. Derived Data

Derived artifacts should be reproducible and treated differently from
source material.

Each derived object should contain:

``` yaml
generated_at:
generator_version:
source_evidence_ids:
source_context_ids:
confidence:
```

Do not overwrite raw evidence.

------------------------------------------------------------------------

# 19. Synthesis Pipeline

## Stage 1 --- Ingest

-   scan context/evidence directories;
-   validate metadata;
-   assign stable IDs if needed;
-   detect new/changed files;
-   preserve source paths.

## Stage 2 --- Extract observations

Run domain-aware extraction.

The extraction prompt should explicitly require:

-   no unsupported claims;
-   preserve source meaning;
-   separate observation from interpretation;
-   include evidence ID;
-   capture uncertainty;
-   use domain-specific fields where applicable.

## Stage 3 --- Discover patterns

Analyze observations for:

-   semantic similarity;
-   repeated problems;
-   repeated product choices;
-   convergence;
-   divergence;
-   contradictions;
-   cross-domain relationships.

V1 can use an LLM synthesis pass.

Later, clustering/embeddings can assist with larger corpora.

## Stage 4 --- Reconcile with existing insights

This is important.

Do **not** simply regenerate a completely new insight list every run.

For each existing insight, determine:

``` text
unchanged
strengthened
weakened
challenged
split
merged
superseded
```

Then identify genuinely new insights.

This creates continuity across synthesis runs.

## Stage 5 --- Generate hypotheses

For high-value insights, generate testable hypotheses.

Require:

-   supporting evidence;
-   assumptions;
-   confidence;
-   falsification criteria.

## Stage 6 --- Generate implications

Interpret insights/hypotheses using relevant context.

Explicitly label implications as interpretation rather than evidence.

## Stage 7 --- Generate experiments/questions

Ask:

> What is the cheapest or highest-value next piece of evidence that
> would materially change our confidence?

Prefer learning actions over feature-building.

## Stage 8 --- Generate report

Produce the synthesis report and update living output files.

------------------------------------------------------------------------

# 20. Incremental Update Model

The user should be able to add evidence periodically without rethinking
the system.

At each run:

``` text
Previous corpus
     +
New evidence/context
     ↓
Extract new observations
     ↓
Compare against existing patterns
     ↓
Re-evaluate current insights
     ↓
Update belief state
     ↓
Generate delta report
```

The report should emphasize **what changed**, not just repeat the entire
corpus.

------------------------------------------------------------------------

# 21. Insight Quality Controls

Every insight should pass a simple rubric.

### Evidence

Is it supported by multiple observations or a particularly strong piece
of evidence?

### Novelty

Is it more than a restatement of the inputs?

### Specificity

Is it concrete enough to influence a question, decision, or experiment?

### Relevance

Does it connect to current goals/context?

### Falsifiability

Can additional evidence strengthen or weaken it?

### Provenance

Can the user inspect the evidence underneath it?

Low-scoring outputs should remain observations/patterns rather than
being promoted to insights.

------------------------------------------------------------------------

# 22. Confidence Model

Keep V1 simple.

Suggested levels:

-   **Low** --- plausible but limited evidence / significant inference.
-   **Medium** --- supported by multiple pieces of evidence, but
    meaningful uncertainty remains.
-   **High** --- repeated/direct evidence with little meaningful
    contradiction.

Confidence should never be generated solely from the model's subjective
certainty. It should reflect evidence quality, quantity, independence,
and contradiction.

------------------------------------------------------------------------

# 23. Contradictions

Contradictory evidence is a first-class output.

Example:

``` text
Insight:
Conversational creation appears to reduce agent setup friction.

Supporting:
ev-001, ev-014, ev-019

Contradicting:
ev-027 — experienced user found conversational editing slower than direct workflow configuration.

Interpretation:
Benefit may depend on user sophistication and task complexity.
```

The harness should not force premature consensus.

------------------------------------------------------------------------

# 24. Cross-Domain Synthesis

This is one of the primary reasons to use a shared system.

The synthesis layer should explicitly look for connections such as:

``` text
Agent-builder pattern
        +
Customer problem
        +
Competitor behavior
        +
Accounting context
        ↓
Potential XeroForce insight
```

Example structure:

``` text
Observation A:
Multiple agent builders emphasize approval and permission controls.

Observation B:
Customer evidence shows high sensitivity around autonomous financial actions.

Observation C:
Competitors retain review checkpoints in consequential accounting workflows.

Potential insight:
Trust infrastructure may be a more important differentiator in accounting agents than generic agent-creation UX.

Status:
Emerging

Next evidence needed:
Understand Xero's current authorization model and customer expectations for delegated actions.
```

The example is illustrative, not a current conclusion.

------------------------------------------------------------------------

# 25. Commands / Harness Interface

Exact syntax depends on the chosen coding harness, but conceptually:

``` bash
# Validate new files
product-os ingest

# Process only new/changed evidence
product-os extract

# Refresh all living conclusions
product-os synthesize

# Generate current report
product-os report

# Full pipeline
product-os refresh
```

Optional later:

``` bash
product-os ask "What are we learning about agent permissions?"
product-os evidence insight-014
product-os contradictions hypothesis-007
```

------------------------------------------------------------------------

# 26. Prompt Contracts

## Observation extraction

Model must:

-   use only supplied evidence;
-   avoid adding general knowledge unless explicitly allowed;
-   quote/reference evidence IDs;
-   separate raw observation from interpretation;
-   mark missing information as unknown.

## Pattern discovery

Model must:

-   identify both similarities and contradictions;
-   avoid creating themes from superficial keyword overlap;
-   cite constituent observation/evidence IDs;
-   distinguish within-domain from cross-domain patterns.

## Insight generation

Model must answer:

1.  What is the insight?
2.  What evidence supports it?
3.  What evidence contradicts it?
4.  Why is it non-obvious/useful?
5.  How confident should we be?

## Implication generation

Model receives relevant context separately and must distinguish:

> "Evidence suggests X"

from:

> "Given Xero's stated goal Y, this could imply Z."

## Experiment generation

Model should prioritize evidence-gathering actions that reduce important
uncertainty.

------------------------------------------------------------------------

# 27. V1 Build Sequence

## Phase 1 --- Skeleton

-   repository structure;
-   evidence/context schemas;
-   manual Markdown ingestion;
-   IDs and validation.

## Phase 2 --- Agent-builder corpus

-   create observation matrix;
-   add hands-on evidence;
-   extraction;
-   first synthesis report.

This tests the basic evidence → insight loop.

## Phase 3 --- Customer sentiment

-   add customer evidence;
-   implement customer-specific extraction;
-   generate themes/sentiment;
-   test cross-domain synthesis.

## Phase 4 --- Competitors

-   add Aider/Digits evidence;
-   competitor-specific extraction;
-   refresh synthesis.

## Phase 5 --- Product/accounting context

-   add month-end-close/product knowledge;
-   add company/product/XeroForce context as available;
-   regenerate implications.

At this point all four pre-onboarding workstreams use the same
infrastructure.

------------------------------------------------------------------------

# 28. V1 Acceptance Criteria

V1 is complete when:

-   [ ] User can add a new evidence Markdown file without code changes.
-   [ ] User can add/update context without code changes.
-   [ ] Raw evidence remains unchanged after processing.
-   [ ] System generates structured observations tied to evidence IDs.
-   [ ] System identifies patterns/themes across multiple evidence
    items.
-   [ ] System generates insights with explicit provenance.
-   [ ] System generates hypotheses with falsification criteria.
-   [ ] System generates Xero/XeroForce implications using context.
-   [ ] System generates next questions/experiments.
-   [ ] Re-running after new evidence updates rather than simply
    duplicates conclusions.
-   [ ] Contradictory evidence can be surfaced.
-   [ ] A Markdown synthesis report can be generated on demand.
-   [ ] At least one useful cross-domain connection can be surfaced once
    multiple domains contain evidence.

------------------------------------------------------------------------

# 29. Later Versions

Only pursue these after V1 demonstrates value.

## V1.1 --- Better retrieval

-   SQLite;
-   embeddings;
-   semantic retrieval;
-   deduplication;
-   larger corpus support.

## V1.2 --- Scheduled synthesis

-   weekly report generation;
-   "what changed this week";
-   new/strengthened/weakened insight alerts.

## V1.3 --- Source integrations

Potential ingestion from:

-   Slack;
-   interview transcripts;
-   support systems;
-   product feedback;
-   analytics;
-   documentation;
-   customer calls.

## V1.4 --- Collaboration

-   shared evidence;
-   comments;
-   insight ownership;
-   review/approval;
-   team hypothesis register.

## V2 --- Product OS

Only after observing Xero's actual information flows should the system
expand toward a broader loop connecting:

> **customer evidence → product understanding → decisions → actions →
> outcomes → updated beliefs**

The pre-onboarding harness should be treated as an experiment informing
that future design, not as the architecture for it.

------------------------------------------------------------------------

# 30. Open Questions

1.  What harness/framework will be used to implement V1?
2.  What model(s) should perform extraction vs. synthesis?
3.  Should derived objects live as Markdown, JSON/YAML, or both?
4.  At what corpus size does retrieval become necessary?
5.  How should duplicate evidence be detected?
6.  How much human approval is needed before an AI-generated insight
    becomes part of the living insight set?
7.  Should insights be globally ranked, or only organized by
    domain/question?
8.  What Xero/XeroForce goals and strategy can appropriately be included
    as context during pre-onboarding?
9.  What customer evidence is available and appropriate to use?
10. What is the minimum useful cadence for later synthesis reports?

------------------------------------------------------------------------

# 31. Immediate Three-Day Test

The system should prove itself against the actual pre-onboarding work.

### Input

-   hands-on evidence from four agent builders;
-   initial customer feedback evidence;
-   Aider/Digits research;
-   month-end-close/product knowledge;
-   available Xero/XeroForce goals and context.

### Output

A synthesis that answers:

-   What patterns are emerging across agent builders?
-   What customer themes/sentiment are emerging?
-   What are competitors betting on?
-   What accounting/product context changes how these observations
    should be interpreted?
-   What connections exist across these domains?
-   What might this imply for Xero/XeroForce?
-   Which conclusions are weak or contradictory?
-   What are the 5--10 highest-value things to investigate after
    joining?

### Core test

> **Did the harness help discover something useful rather than merely
> organize what was already known?**

If yes, continue iterating.

If no, improve the evidence model and synthesis process before adding
infrastructure.
