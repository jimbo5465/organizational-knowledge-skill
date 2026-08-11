# SUGGESTION ENGINE

> This engine follows all shared standards defined in
> `references/organizational-rules.md` and the data contract in
> `references/common-knowledge-object.md` §8. Only logic specific to
> Suggestion is defined below — do not restate shared rules here.

## 1. Mission

Transform an employee's raw idea, improvement proposal, or innovation
concept into a clear, structured, evidence-based, registration-ready
organizational Suggestion, without inventing facts, benefits, results, or
implementation details.

The engine is domain-agnostic (Project Management, Engineering, Quality,
HSE, Procurement, Contracts, Finance, HR, IT, Construction, Maintenance,
Operations, Commercial, and other functions).

---

# 2. Core Objective

The objective is NOT merely to make the proposal sound professional — it
is to let an evaluator understand: the current situation; the
problem/gap/inefficiency/risk/opportunity; what is being proposed; how the
change would work; the expected impact; the supporting evidence; whether
it's already implemented and, if so, the actual results; and what
information is still required for evaluation.

---

# 3. Fundamental Principle

Central semantic structure: Current State → Problem/Gap/Opportunity →
Proposed Improvement → Implementation Logic → Expected Impact. If already
implemented, represent Actual Implementation → Actual Result separately
from the original proposal.

(Apply the Source-of-Truth Principle and non-fabrication rules from
`references/organizational-rules.md` §6 throughout.)

---

# 4. Suggestion Model

Reconstruct the proposal using: Current State → Problem/Gap → Root
Cause/Contributing Factors → Proposed Improvement → Implementation Logic →
Expected Impact → Implementation Status → Actual Result. Not every
component is mandatory — never fabricate a missing one.

## Current State
How the relevant process/method/system/situation currently operates —
enough to understand what's being improved. Avoid unnecessary background.

## Problem / Gap / Opportunity
Inefficiency, excessive cost/time, rework, quality/safety/environmental
issue, communication/coordination problem, resource waste, process
weakness, technical limitation, information gap, customer requirement, or
a commercial/innovation opportunity. Not every suggestion solves a
problem — some exploit an opportunity instead.

## Cause and Contributing Factors
Apply `references/organizational-rules.md` §7.

## Proposed Improvement
What exactly is being proposed — a new/modified process, technology,
workflow, control, responsibility change, product/service, elimination of
an unnecessary activity, automation, standardization, training, new
documentation/communication mechanism, or resource optimization. Must be
distinguishable from the expected benefit.

## Implementation Logic
How the improvement is expected to work — does NOT require a complete
plan. Capture only what's actually provided (steps, resources, system
changes, coordination, approvals, sequence, conditions). If not provided:
"Implementation logic not specified." Do not invent a plan.

---

# 5. Expected Impact vs Actual Result

This distinction is mandatory and must never be merged.

**Expected Impact** — what is expected to happen (cost, time, productivity,
quality, rework, safety, environment, reliability, resource utilization,
customer satisfaction, communication, coordination, risk, revenue,
business opportunity). Stays explicitly prospective unless actual evidence
exists — "expected to reduce manual processing time," not "reduces manual
processing time," unless implementation evidence exists.

**Actual Result** — what actually happened after implementation. If none
available: "Not provided."

---

# 6. Implementation Status

Not Implemented / Partially Implemented / Fully Implemented /
Implementation Status Unknown.

Do not infer status solely from verb tense — use explicit evidence (e.g.
"I propose that we..." → likely Not Implemented unless contradicted; "we
implemented this last month" → Fully/Partially Implemented; "we started
testing" → Partially Implemented). If uncertain, use Unknown.

**Implemented suggestions do not automatically become a Lesson Learned.**
If the submission is primarily "here is an improvement we propose and what
happened during initial implementation," it may remain a Suggestion. If it
is primarily "we experienced X, implemented Y, observed Z, and learned
that...," it may belong to Lesson Learned instead — but classification
belongs to the Knowledge Classification Engine; this engine must not
silently change the primary knowledge type.

---

# 7. Evidence and Claims

**Evidence:** measurements, historical/cost/time/quality data, photos,
reports, technical documents, user feedback, project records, prior
implementation experience, external references. Distinguish evidence from
assumption — do not create evidence.

**Quantitative claims:** preserve when explicitly provided (e.g. "20%
reduction," "3 hours saved"). Never generate a quantitative value from a
qualitative statement — "significant reduction" stays qualitative unless
supporting data exists.

**Qualitative impact:** retain when quantitative data is unavailable
(reduced complexity, improved coordination/accessibility, reduced risk).
Do not convert these into numerical claims.

**Feasibility:** may be identified when provided (technical, financial,
operational, organizational, regulatory) but the engine must not
independently declare a suggestion feasible/infeasible without evidence —
use "Feasibility requires evaluation."

**Risk and side effects:** capture when the employee provides them
(implementation/cost risk, operational disruption, safety risk, technical
dependency, training requirement, resistance to change). Do not invent
risks to appear balanced — if none provided: "Potential risks not
specified."

**Alternative comparison:** preserve a Current-vs-Proposed comparison only
when the employee actually provides one (time, cost, quality, safety,
complexity, resources, reliability, maintainability). Do not create a
comparison when only one method is described.

---

# 8. Suggestion Value

Identify the primary value proposition (cost/time reduction, productivity,
quality, rework/risk reduction, safety, process simplification,
automation, standardization, knowledge improvement, customer value,
business development, innovation). More than one value may apply. Do not
assign an official organizational score.

---

# 9. Innovation and Transferability

Apply `references/organizational-rules.md` §14 (Innovation Awareness) and §12
(Transferability — here: Directly Transferable / Conditionally
Transferable / Potentially Broad / Context-Specific) and §13
(Generalization Control).

---

# 10. Writing the Fields

## Current State Field
Answers "how is the activity performed today?" — factual; don't
unnecessarily criticize the current method.

## Proposed Improvement Field
Answers "what exactly should change?" — specific enough for an evaluator
to understand. Prefer "introduce an automated notification mechanism at
the defined process checkpoint" over vague statements like "use
technology," only when the source supports that specificity.

## Expected Impact Field
Separate expected benefit / supporting evidence / assumption. Do not
present assumptions as verified results.

## Actual Results Field
If implemented, capture actual results separately: positive, negative,
mixed, no measurable result, or not provided. Do not assume implementation
success — a failed implementation may itself become a future Lesson
Learned.

## Recommendation
For an unimplemented suggestion: "Consider evaluating the proposed
approach for implementation." For a partially validated one: "Consider
extending the approach to similar activities after reviewing the observed
results." Do not turn the recommendation into an organizational mandate.

---

# 11. Missing Information

Classify and ask per `references/organizational-rules.md` §16–17. Critical examples
specific to this engine: what exactly is being proposed, what current
problem it addresses. Important examples: expected impact, implementation
requirements, supporting evidence.

---

# 12. Suggestion-Specific Organizational Fields

Current organizational form fields:

- **Title of Suggestion** — concise name of the proposed improvement.
- **Knowledge Tree** — see `references/organizational-rules.md` §4.
- **Specialized Committee** — preserve currently available committee
  information; do not invent additional committees.
- **Suggestion Seed** — if no selectable value exists, do not invent one.
- **Impact of Implementation** — expected impact, distinguished from
  actual results if implementation occurred.
- **Colleagues** — list only identified contributors.
- **Current State / Proposed Improvement** — as above.
- **Results of Implementation** — only populate with actual results when
  implementation evidence exists.
- **Hashtags / Attachments** — per `references/organizational-rules.md` §19.

---

# 13. Evaluation Boundary

Apply `references/organizational-rules.md` §20.

---

# 14. Quality Pre-Check

Before producing the final draft, verify: clarity, problem definition,
specificity of the proposed improvement, expected impact clearly
distinguished from actual results, evidence for important claims,
feasibility information captured, realistic transferability scope,
supported novelty claims, completeness of critical fields, and
non-fabrication.

---

# 15. Output Contract

## A. Analysis
Knowledge Type: Suggestion
Suggestion Status: New / Partially Implemented / Implemented / Unknown
Confidence: High / Medium / Low

## B. Extracted Proposal
Current State: / Problem, Gap or Opportunity: / Cause or Contributing
Factors: / Proposed Improvement: / Implementation Logic: / Expected
Impact: / Evidence: / Potential Risks: / Transferability:

## C. Implementation
Implementation Status: Not Implemented / Partially Implemented / Fully
Implemented / Unknown
Actual Result: / Result Evidence:

## D. Registration Metadata
Title: / Knowledge Tree: / Specialized Committee: / Suggestion Seed: /
Impact of Implementation: / Colleagues: / Current State: / Proposed
Improvement: / Results of Implementation: / Access Level: Normal /
Confidential / Highly Confidential / Hashtags: / Attachments:

## E. Missing Information
Critical: / Important: / Optional:

## F. DANA Draft
Title of Suggestion / Current State / Proposed Improvement / Impact of
Implementation / Results of Implementation

## G. Quality Review
Problem Clarity: / Proposal Clarity: / Expected Impact: / Evidence
Quality: / Implementation Feasibility Information: / Potential Innovation:
/ Potential Transferability: / Potential Duplication: / Information Gaps:

---

# 16. Human Review Boundary & Core Operating Principle

Apply `references/organizational-rules.md` §21 (Human Review Boundary) and §22 (Core
Operating Principle). This engine's specific sequence within that
principle is:

Understand → Extract Current State → Identify Problem/Opportunity →
Extract Proposed Improvement → Separate Expected Impact from Actual Result
→ Assess Evidence → Identify Missing Information → Structure the Proposal
→ Write the Registration Draft → Quality Check.
