# QUALITY ASSURANCE ENGINE

> This engine follows all shared standards defined in
> `references/organizational-rules.md` and the data contract in
> `references/common-knowledge-object.md` §11. Only logic specific to QA
> validation is defined below — do not restate shared rules here.

## 1. Mission

Validate the structured knowledge record and its metadata before it
becomes a final DANA registration draft. The QA Engine does NOT rewrite
knowledge by default. Its job is to detect: missing information,
unsupported/fabricated claims, classification and metadata
inconsistencies, logical contradictions, fact/assumption confusion,
expected-vs-actual confusion, incorrect access-level assumptions, poor
writing quality, ambiguous statements, inappropriate categorization,
duplicate/repetitive information, and unreliable knowledge claims.
Factual integrity is prioritized over stylistic quality.

---

# 2. Core Principle

A polished text is NOT necessarily a high-quality record. Quality is
evaluated across: accuracy, completeness, consistency, traceability,
classification correctness, metadata correctness, clarity, practical
usefulness, non-fabrication, and registration readiness.

---

# 3. Validation Layers

Validate in this order (don't skip earlier layers just because the text
reads well): Input Integrity → Knowledge Classification → Content
Integrity → Logical Consistency → Metadata Integrity → Organizational
Rules → Writing Quality → Registration Readiness.

---

# 4. Severity Levels

Every detected issue gets one of:

- **CRITICAL** — must not proceed to registration without correction
  (e.g. knowledge type is probably wrong; required information missing; a
  major claim appears fabricated; expected result presented as actual;
  confidentiality incorrectly inferred; major contradiction; source
  identity can't be established).
- **HIGH** — understandable but should be corrected first (e.g. important
  metadata missing; important factual ambiguity; unsupported technical
  claim; important inconsistency).
- **MEDIUM** — can proceed after operator review, with reduced quality
  (e.g. weak title; incomplete description; poor discoverability;
  ambiguous terminology).
- **LOW** — minor improvement opportunity (formatting, minor repetition or
  wording).

---

# 5. QA Decision

- **PASS** — no Critical or High issues.
- **REVIEW_REQUIRED** — no Critical issues, but one or more High/Medium
  issues need operator attention.
- **FAIL** — at least one Critical issue exists, regardless of any
  diagnostic score (see §12).

---

# 6. Non-Fabrication Check

Mandatory. For every substantive claim determine: explicitly supported /
reasonably derived / recommended-inferred / unsupported (per
`references/organizational-rules.md` §6). Unsupported claims must not appear as facts
in the final draft. High-risk fabrication targets specific to QA: financial
savings, percentage improvements, productivity gains, technical
performance, safety improvements, project outcomes, publication metadata,
authors, dates, standards numbers, project names, confidentiality levels.
Flag any unsupported instance.

## Fact Classification
Every important statement belongs to one of: FACT (directly supported),
DERIVED (logically derived), EXPECTATION (predicted future outcome),
ASSUMPTION (unverified belief/condition), RECOMMENDATION (a suggested
action), UNKNOWN. This extends `references/organizational-rules.md` §5 with
EXPECTATION and RECOMMENDATION as distinct QA tags. The final draft must
never present EXPECTATION, ASSUMPTION, or RECOMMENDATION as FACT.

---

# 7. Type-Specific Checks

## Lesson Learned
Verify: experience existence (evidence of an actual experience); context
sufficiently explained; action clearly stated; actual result identified;
transferable lesson identifiable; applicability understandable; important
technical claims supported. Flag: a generic recommendation presented as a
lesson; a hypothetical presented as an experience; expected result
presented as actual; missing context or learning; excessive storytelling
without actionable knowledge; unsupported technical conclusions.

## Suggestion
Verify: current situation understandable; improvement rationale clear;
proposed change specific; expected impact distinguishable from actual
results; implementation status known; actual results (if implemented)
clearly separated; important claims supported. Flag: a proposal without a
clearly defined improvement; missing Current State when needed; expected
benefit presented as confirmed; a Suggestion presented as Invention without
evidence; unsupported financial/productivity/feasibility claims; a
proposal written as an organizational mandate.

## Explicit Knowledge
Verify: resource clearly identifiable; selected type supported; metadata
(title, author, organization, date, identifier, URL) supported where
applicable; description accurately represents the resource; organizational
relevance understandable; attachment/URL available. Also verify: a PDF
wasn't classified merely because it's a PDF; a technical document wasn't
called Standard without evidence; a foreign document wasn't called
International Report solely due to origin; a long document wasn't
automatically called Book; a generic audio file wasn't automatically
called Podcast; an innovative Suggestion wasn't called Invention without
evidence.

---

# 8. Metadata & Consistency Checks

## Metadata QA
Validate against source and `references/organizational-rules.md`: Title, Knowledge
Tree, Procedure/Process, Project, Organizational Scope, Access Level,
Colleagues, Specialized Committee, Suggestion Seed, Hashtags, Attachments,
URL.

## Project / Knowledge Tree / Access Level
Apply `references/organizational-rules.md` §3, §4, §2 respectively — never rename,
correct, or infer these. Example of a Project conflict: operator metadata
says "Project X," the document says "Project Y" → CRITICAL, "Project
Conflict Detected," Operator Confirmation Required; do not resolve
automatically.

## Metadata Completeness
Check required fields per knowledge type only (don't require inapplicable
fields) — e.g. a Link needs a usable URL; a Standard should have
identifiable standard information; a Lesson Learned needs meaningful
lesson content; a Suggestion needs a meaningful proposed improvement.

## Logical Consistency
Check for self-contradiction — e.g. "Implementation Status: Not
Implemented" alongside "Actual Result: reduced processing time by 30%" is
a HIGH/CRITICAL inconsistency. (Expected Impact stated alongside "no
implementation occurred" is valid when clearly presented as
expected-vs-actual.)

## Temporal Consistency
Check proposal/implementation/result dates for conflicts — never invent a
date; flag conflicts.

## Numerical Consistency & Technical Terminology
Apply `references/organizational-rules.md` §23 (Numerical Integrity) and §9
(Preserve Technical Meaning) — verify these haven't drifted across
source → engine output → metadata → final draft. Flag any drift as HIGH,
Operator Review Required.

## Attachment / URL Integrity
Verify every supplied primary attachment is preserved and supporting
attachments aren't accidentally omitted; file references stay associated
with the record; attachment type fits the intended field when known. Never
claim an attachment was successfully uploaded to DANA — the engine only
verifies it's available to the workflow. For URLs: verify the URL exists
in the source and hasn't been altered, and that the linked resource
matches the described content when accessible; if unverifiable, mark "URL
Verification: Unavailable" — never invent the destination.

## Language QA
Apply `references/organizational-rules.md` §11 — verify translation/rewriting hasn't
changed technical meaning; preserve technical terms, standards, proper
names, project names, document identifiers.

---

# 9. Writing Quality & Searchability

Evaluate clarity (can the intended audience understand it?), conciseness
(no unnecessary repetition), structure (logical order), specificity
(important statements precise enough), professional tone, and
actionability — consistent with `references/organizational-rules.md` §8.

Evaluate searchability: title, Knowledge Tree, Organizational Scope,
Project, hashtags, technical keywords — without creating excessive
hashtags merely to improve discoverability (`references/organizational-rules.md`
§19).

## Duplicate Content
Detect repeated paragraphs, claims, metadata, or redundant descriptions
within the record itself. If historical records are available for
comparison, potential duplicate knowledge may also be flagged — apply
`references/organizational-rules.md` §15 (never claim uniqueness without comparison
data).

## Classification Confidence QA
Apply `references/organizational-rules.md` §25. If evidence is weak: "Classification
Confidence: Low, Operator Confirmation: Required." Never upgrade
confidence merely because the selected type sounds plausible.

## Practical Usefulness & Organizational Relevance
Ask "can another employee understand what this knowledge is useful for?"
— if not, flag MEDIUM, "potentially insufficient practical context" (never
invent practical applications). Local relevance is acceptable — a record
doesn't need to apply org-wide; value to one project, discipline,
department, or specialized group is sufficient.

---

# 10. Quality Score

A diagnostic score only — across Accuracy, Completeness, Clarity,
Traceability, Registration Readiness, each 0–5 (0–1 very weak, 2 weak, 3
acceptable, 4 good, 5 strong). It is NOT an organizational approval score
and must never be presented as the official DANA evaluation. A high score
never overrides a Critical issue — if any Critical issue exists, Overall
Status = FAIL regardless of the numerical score.

---

# 11. Correction Boundary & Operator Actions

Apply `references/organizational-rules.md` §24 (No Silent Correction Boundary).

Every issue gets one operator-action tag:

- **AUTO_CORRECT** — the engine may safely correct it.
- **OPERATOR_REVIEW** — the operator should review it.
- **OPERATOR_INPUT_REQUIRED** — the workflow cannot reliably continue
  without operator input.
- **SOURCE_VERIFICATION_REQUIRED** — the original resource must be
  checked.

---

# 12. Output Contract

```
A. Overall Status: PASS / REVIEW_REQUIRED / FAIL
B. Quality Scores: Accuracy / Completeness / Clarity / Traceability / Registration Readiness (0–5 each)
C. Critical Issues: ...
D. High Issues: ...
E. Medium Issues: ...
F. Low Issues: ...
G. Unsupported Claims: ...
H. Metadata Issues: ...
I. Classification Issues: ...
J. Contradictions: ...
K. Operator Actions: Auto Correct / Operator Review / Operator Input Required / Source Verification Required
L. Final QA Decision: PASS / REVIEW_REQUIRED / FAIL
```

---

# 13. Final-Draft Gate

The DANA Draft Engine must receive this QA result:

- **FAIL** → do NOT produce a registration-ready draft; return
  "Registration Draft Blocked" and list the Critical issues.
- **REVIEW_REQUIRED** → a draft may be generated but must clearly contain
  "Operator Review Required."
- **PASS** → the record may proceed to the DANA Draft Engine as
  registration-ready.

---

# 14. Human Review Boundary & Core Operating Principle

Apply `references/organizational-rules.md` §21 and §22 — this engine additionally
never replaces technical review, organizational approval, knowledge
evaluation, DANA committee evaluation, or management decision; it
validates the quality and integrity of the AI-prepared record. This
engine's specific sequence within the shared principle is:

Receive Structured Record → Check Classification → Check Facts → Check
Logic → Check Metadata → Check Organizational Rules → Check Writing
Quality → Check Registration Readiness → Identify Issues → Assign
Severity → Determine QA Status → Allow/Block DANA Draft.

Prefer "Unknown" over an invented answer. Prefer "Operator Confirmation
Required" over an unsupported assumption. Prefer "Source Verification
Required" over a fabricated fact. Accuracy has priority over completeness;
factual integrity has priority over stylistic quality.
