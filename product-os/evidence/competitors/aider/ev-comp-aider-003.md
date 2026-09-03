---
id: ev-comp-aider-003
domain: competitor
source_type: docs
source_name: Aider (Karbon) tutorial
date: 2026-09-03
title: "Aider tutorial: period-close dashboard, firm template, Ask Client"
confidence: direct
artifact_path: artifacts/competitors/aider/ev-comp-aider-003/
product_area: period_close
tags:
  - aider
  - karbon
  - tutorial
  - period-close
  - checklist
  - ask-client
  - visibility
---

# Aider tutorial: period-close dashboard, firm template, Ask Client

## Raw evidence

Screenshots from an Aider tutorial (researcher-captured 2026-09-03).
Aider logo (speech-bubble "a") is visible on product screens.
Artifacts in `artifacts/competitors/aider/ev-comp-aider-003/`.

These are tutorial/demo screens, not a researcher-owned live firm.

### The problem the tutorial names

Slide text:

> The problem: Managers and partners lack real-time visibility into
> client close status, making it hard to spot bottlenecks and get
> ahead of problems.

Bullets:

- No single view of where every client's close actually stands —
  status lives in weekly meetings and memory.
- This is relevant whether you have 15 or 15,000 clients.
- Capacity and bottleneck issues surface only after they've already
  cost time.

The buyer in this framing is the manager/partner. The pain is
portfolio visibility, not "I need an AI employee."

### Period Close Dashboard

Title: **Period Close Dashboard**. Search: "Search clients and
periods." Filter: Progress — "2 statuses." Footer: Showing 1 to 9
of 9 results.

Rows are **client × period** (Luna Apparel FY 2024 / Oct 2025 /
Nov 2025; Astoria Design; BrightNest; Copper Fox Café;
Harbor & Hops Bar; PulseWave Media; Reach Foundation).

Columns visible:

- Client, Period
- Progress (blue bar, or text **In Review**)
- Document-status dots
- Chat-status dots
- Alerts (green **Pass** or red count: 78, 47, 13, 40, 50, 36, 82)
- Broken-out check categories: **Bank &…**, **Data Qu…**,
  **Invoices**, **Balance…**, **Profit &…**, **Additio…**
  (green 0 vs red counts)

Hover on BrightNest chat dots shows a tooltip:

- 3 scheduled & draft
- 5 with client
- 5 replies
- 13 closed

No named agent, no Bookkeeper/CFO role, no chat employee on this
screen. The object is the period close across the book.

### Firm template: Monthly Close - Accrual

Breadcrumb: `Firm Settings > Period Close Templates > Monthly Close
- Accrual`.

Header: **Monthly Close - Accrual**. Status **Active**. **Applied
to 82 Clients.** Tabs: **Checklist** (selected), **Clients 82**.
Button: **Publish Template**. Note: "This is a draft template."

Checklist sections with **Add Check** on each:

**Bank & Credit Cards**

- Unreconciled Transactions — **Built-in**

**Data Quality**

- Transactions Missing Payee or Vendor — **Automatic - 1 Condition**
- Uncategorized Transactions — **Automatic - 1 Condition**
- Inconsistently Categorized Transactions — **Built-in**
- Transactions Posted to Parent Accounts — **Automatic - 2 Conditions**
- Potential Fixed Asset Transactions — **Automatic - 2 Conditions**
- Clearing or Suspense Account Balances — **Automatic - 2 Conditions**

**Invoices & Bills** — section header visible; checks not in frame.

Checks are Built-in or Automatic-with-N-conditions. Firm publishes
one template onto many clients.

### Exception work + Ask Client

Screen: **8 Uncategorized Transactions**. Copy says these
transactions are incomplete and must be reclassified or they
distort financial statements.

Table: Date, Type, Name, Description, Account, Amount. Example
row being edited: Nov 10, 2025 / Expense / Lowes / $2,700.00 /
Account dropdown **Uncategorized Exp…**. Row actions: thumbs-up,
chat bubble, overflow. **Mark as Reviewed** / **Show Reviewed**
toggle.

Right panel **Ask Client**:

- Contact: Abigail Silvers (abby@reachfoundation.com)
- Transaction details repeated (Lowes $2,700 Uncategorized Expense)
- Brooke Keplan (Dec 1): "Please clarify what this transaction was
  for and attach the receipt. Thank you."
- Abigail Silvers (Dec 2): "Sure thing. It was a purchase of a
  photocopier for the office. Receipt attached." +
  `IMG20251202_104723.jpg`
- Footer: **Sends end of day (5pm, Dec 2)**

Client questions are attached to a specific exception, and outbound
is batched.

## Notes

This tutorial is **period close**, not Karbon AI Agents. Built-in
and Automatic-N-conditions checks are **rules**. Rules are not
agents. Do not use these screens to place Bookkeeper / Tax Admin /
fCFO / Kai on the define-vs-delegate line. We have not seen an
Agents tutorial or the Agents product.

What this *does* show: Aider teaches a defined close workflow and
then the screens that run it.

1. Name the manager problem (no single view of close).
2. Show the portfolio dashboard (exception counts by check type).
3. Show the firm template (one checklist → 82 clients).
4. Show the line-item work (reclassify + Ask Client + EOD send).

Workflow + tool. The human works an exception inbox. Digits uses
the same manage-by-exception idea inside the GL; this product uses
it across clients on top of a GL.

Ask Client batched to end-of-day is a workflow opinion (don't spam
the client). Same pattern described in `ev-comp-aider-001`.

Follow-ups:

- Find the tutorial / early-beta for **Karbon AI Agents** (not
  period close).
- Do "Automatic - N Conditions" expose the actual rule editor?
- Is inline recategorize writing back to Xero, QBO, or both?
