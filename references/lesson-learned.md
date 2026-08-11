# LESSON LEARNED ENGINE

> This engine follows all shared standards defined in
> `references/organizational-rules.md` and the data contract in
> `references/common-knowledge-object.md` §7. Only logic specific to
> Lesson Learned is defined below — do not restate shared rules here.

## 1. Mission

Transform an unstructured organizational experience into a clear,
accurate, reusable, registration-ready Lesson Learned, while preserving
the factual meaning of the original experience.

The engine is domain-agnostic (Project Management, Engineering, Quality,
HSE, Procurement, Contracts, Finance, HR, IT, Construction, Maintenance,
Operations, Commercial, and other functions) and must not depend on
examples from a specific technical discipline.

---

# 2. Core Objective

The objective is NOT to rewrite the user's text in more professional
language — it is to extract reusable organizational knowledge from an
experience.

Transform: Raw Experience → Structured Experience → Extracted Lesson →
Transferable Knowledge → Professional Lesson Learned → Registration
Draft.

The final product must let a colleague who was not present understand:
what happened, why it mattered, what was done, what happened afterward,
what was learned, and what they should remember or do differently.

---

# 3. Fundamental Principle

A Lesson Learned is not merely a description of an event — it is "an
experience from which useful knowledge can be extracted for future
application."

Distinguish between: event description, problem description, action
description, result description, lesson, and transferable knowledge. A
submission that only describes what happened is not complete — the
reusable lesson must be identifiable.

(Apply the Source-of-Truth Principle and non-fabrication rules from
`references/organizational-rules.md` §6 throughout.)

---

# 4. Experience Model

Reconstruct the experience using this conceptual model — these are
logical components, not mandatory fields; never invent a missing one:

Context → Situation → Problem/Opportunity → Cause/Contributing Factors →
Action → Result → Lesson → Transferability

## Context
Background needed to understand the experience (project, process,
activity, department, environment, equipment, system, phase, relevant
circumstances). Include only context that contributes to understanding
the lesson.

## Situation
What actually happened — factual, no unnecessary narrative or
dramatization.

## Problem / Opportunity
Determine whether the experience involved a problem, failure, risk,
inefficiency, quality/safety/cost/schedule/communication/coordination
issue, an opportunity for improvement, or a successful practice worth
repeating. Not every Lesson Learned requires a problem — successful
practices are valid sources when they generate reusable knowledge.

## Cause / Contributing Factors
Apply `references/organizational-rules.md` §7.

## Action
What was actually done (corrective, preventive, process/technical change,
communication/coordination/management action, new method introduced, or
ineffective method discontinued). Distinguish "action actually performed"
(part of the experience) from "action recommended for the future" (a
possible derived recommendation).

## Result
Extract actual results (problem resolved/reduced, rework/time/cost
reduced, quality/safety/productivity improved, risk reduced, process
stabilized, or no measurable result reported). Only report quantitative
results when quantitative evidence exists — e.g. "the source reports a
reduction in rework" is correct; "the action reduced rework by 30%" is
incorrect unless that figure is explicitly supported.

---

# 5. Positive and Negative Experiences

Support both:

- **Successful:** Successful Situation → Effective Action → Positive
  Result → Why It Worked → Lesson → Reuse Recommendation
- **Unsuccessful:** Problem → Action/Attempt → Unsuccessful or Partial
  Result → What Went Wrong → Lesson → Future Prevention

Do not assume a Lesson Learned must describe a failure.

---

# 6. The Lesson Extraction Step

This is the central reasoning task. After reconstructing the experience,
ask: "What knowledge should an employee retain after reading this
experience?"

The lesson should describe what should be remembered, what principle can
be reused, what practice should be repeated or avoided, what condition
matters, and what action matters in a similar situation. Avoid a generic
statement like "Proper planning is important" unless the source genuinely
supports that conclusion — prefer a specific, source-supported lesson.

---

# 7. Transferability

Apply the levels from `references/organizational-rules.md` §12 and the
generalization control in §13.

---

# 8. Lesson Quality Test

A good Lesson Learned lets a colleague answer: what happened, what
mattered, what was done, what was the result, what should I remember, and
when can I apply this knowledge. If the resulting document can't answer
these, identify the missing information (classify per
`references/organizational-rules.md` §16, ask per §17).

---

# 9. Writing the Fields

## Execution Result
Describe what actually happened after the action — not expected benefits.
Distinguish "expected to reduce rework" (expected) from "the submitted
information reports fewer instances of rework" (actual). If no actual
result is available: "Actual execution result was not provided." Do not
manufacture one.

## Lesson Description
Normally contains: Context/Situation, Problem or Opportunity, Action,
Result, Lesson — adapt as needed. Don't force headings into the final
DANA text if a continuous professional narrative fits better; internal
structure and final presentation format are separate concerns.

## Recommendation
May be derived from the Lesson Learned when supported. Should answer
"what should others consider doing in similar circumstances?" Use
conditional wording ("when similar conditions exist, consider performing
X before Y") rather than an unconditional mandate, unless an authoritative
organizational requirement explicitly supports it.

---

# 10. Duplication and Innovation Awareness

Apply `references/organizational-rules.md` §15 (Duplication) and §14 (Innovation).

---

# 11. Organizational Evaluation Criteria

Current criteria: (1) Clarity and completeness, (2) Technical correctness,
(3) Increased productivity and reduced rework, (4) Non-repetitiveness and
innovation, (5) Practical usefulness.

Use these as a pre-submission quality framework only — do not replace the
official human evaluation process, and do not assign official scores
(1–5) unless explicitly instructed for a separate evaluation task.

---

# 12. Attachment Interpretation

Attachments may contain important evidence. When available: inspect them
when tools permit, use their content as evidence, cross-check the
narrative against the attachment, and identify contradictions. Do not
assume an attachment is correct merely because it was uploaded. Flag any
contradiction for operator review.

---

# 13. Final Draft Principle

The final Lesson Learned should feel like organizational knowledge, not an
AI-generated essay: specific enough to be useful, general enough to be
reusable, evidence-based enough to be trusted, concise enough to be read,
structured enough to be searchable.

---

# 14. Output Contract

## A. Analysis
Knowledge Type: Lesson Learned
Experience Type: Successful / Unsuccessful / Mixed / Improvement / Other
Confidence: High / Medium / Low

## B. Extracted Experience
Context: / Situation: / Problem or Opportunity: / Cause or Contributing
Factors: / Action: / Actual Result:

## C. Extracted Knowledge
Core Lesson: / Transferability: Direct / Conditional / General Principle /
Limited / Recommendation:

## D. Registration Metadata
Title: / Knowledge Tree: / Procedure or Process: / Project: /
Organizational Scope: / Access Level: Normal / Confidential / Highly
Confidential / Colleagues: / Hashtags: / Attachments:

## E. Missing Information
Critical: / Important: / Optional:

## F. DANA Draft
Title / Lesson Description / Execution Result

## G. Quality Review
Clarity and Completeness: / Technical Support: / Practical Usefulness: /
Potential Rework Reduction: / Potential Novelty: / Potential Duplication:
/ Potential Impact:

---

# 15. Human Review Boundary & Core Operating Principle

Apply `references/organizational-rules.md` §21 (Human Review Boundary) and §22 (Core
Operating Principle). This engine's specific sequence within that
principle is:

Understand → Extract (Context/Situation/Problem/Cause/Action/Result) →
Identify the Lesson → Test Transferability → Detect Missing Information →
Write → Quality Check → Produce Draft.
