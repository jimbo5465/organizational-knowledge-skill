# KNOWLEDGE CLASSIFICATION ENGINE

> This engine follows all shared standards defined in
> `references/organizational-rules.md` and the data contract in
> `references/common-knowledge-object.md` §6. Only logic specific to
> classification is defined below — do not restate shared rules here.

## 1. Mission

Determine the actual nature of submitted organizational knowledge and
assign it to the most appropriate category. The engine is domain-agnostic
(Project Management, Engineering, Quality, HSE, Procurement, Contracts,
Finance, HR, IT, Operations, Construction, Maintenance, and other
domains) and does not depend on the user's job title, technical
discipline, or department. Its purpose is classification, not rewriting.

---

# 2. Supported Knowledge Classes

1. Lesson Learned
2. Suggestion
3. Explicit Knowledge
4. Ambiguous / Insufficient Information (when none of the above can be
   reliably determined — do not force a classification)

---

# 3. Fundamental Classification Principle

Classify according to what the submitted information **actually
represents** — never based solely on the user's provided title, requested
category, keywords, file format, profession, department, or attachment
name. Semantic nature has priority over labels.

Example: the user says "register this as a suggestion," but the content
describes an actual experience, an implemented action, and an actual
result → classify as **Lesson Learned**, and explain why the requested
category was overridden.

---

# 4. Classification Decision Hierarchy

**Step 1 — Identify the source nature:** does the information primarily
represent (A) an experience/event that occurred, (B) an idea/proposed
change, (C) an existing knowledge resource, or (D) insufficient
information?

**Step 2 — Actual experience?** Look for an actual event, work activity,
project situation, problem, failure, success, a performed action, an
implemented intervention, or an actual result/consequence. If
substantially experience-based → consider Lesson Learned.

**Step 3 — Proposing change?** Look for current state, problem/gap,
proposed improvement, proposed action, expected benefit, or a
future-oriented recommendation not yet implemented. If the primary nature
is proposing rather than documenting → consider Suggestion.

**Step 4 — Existing knowledge resource?** Look for a book, training
material, URL, international report, podcast, article, invention,
magazine, or standard. If the primary purpose is sharing an existing
resource rather than reporting an experience or proposing improvement →
classify as Explicit Knowledge.

---

# 5. Lesson Learned vs Suggestion

The most important classification boundary:

- **Lesson Learned:** "What happened, what did we do, what happened
  afterward, and what did we learn?" Evidence signals (in combination, not
  as isolated keywords): "we encountered...", "during the project...",
  "we implemented...", "the result was...", "we learned...", "after this
  change...". Does not require failure — a successful experience is a
  valid Lesson Learned when it produces reusable knowledge.

- **Suggestion:** "What exists now, what should change, and what
  improvement is proposed?" Structure: Current State → Problem/Opportunity
  → Proposed Improvement → Expected Impact. Evidence signals: "I
  suggest/propose...", "it would be better if...", "we should...", "it is
  recommended to..." — these phrases alone are NOT sufficient; determine
  whether the proposal is grounded in a documented experience or is a
  genuinely new/proposed improvement.

## Implemented Suggestion Rule
If a submission contains a proposal AND evidence it was actually
implemented AND an actual result, evaluate whether the core knowledge is
now an experience. If the valuable knowledge comes primarily from the
implemented experience and its result → Lesson Learned. If it remains
primarily a proposal with no implementation results → Suggestion. Do not
automatically classify every implemented suggestion as Lesson Learned —
evaluate the semantic center of the submission.

## Recommendation Rule
A recommendation inside a Lesson Learned does not automatically turn it
into a Suggestion — e.g. "we changed the inspection sequence and reduced
rework; we recommend this approach for future projects" stays Lesson
Learned, because the recommendation is derived from an actual experience.

---

# 6. Explicit Knowledge

Classify as Explicit Knowledge when the material is primarily an existing
resource meant to be shared (book, training content, link, international
report, podcast, article, invention, magazine, standard — regardless of
its physical/digital/web/audio/video form).

For detailed per-subtype classification criteria (evidence for Book vs
Article vs Standard, etc.), see `references/explicit-knowledge.md` §5 — this
engine only needs to determine that Explicit Knowledge is the primary
class and make a provisional subtype call for routing; the Explicit
Knowledge Engine performs the authoritative subtype classification. Apply
`references/common-knowledge-object.md` §6: classification is never based on file
format alone.

---

# 7. Mixed Knowledge

A single submission may contain multiple knowledge forms (e.g. an actual
experience + a recommendation + a reference to a standard + a proposed
future improvement). Identify the **primary** knowledge type; report
secondary elements separately when useful. Do not split one submission
into multiple records unless explicitly instructed.

## Primary Knowledge Determination
Ask: "What would another employee primarily gain from this submission?"
Knowledge from an actual experience → Lesson Learned. An idea or proposed
improvement → Suggestion. Access to an existing resource → Explicit
Knowledge.

---

# 8. Ambiguous Classification

Use "Ambiguous / Insufficient Information" when evidence can't distinguish
between categories (e.g. "I found a better way to do this" with no further
detail, or an uninspectable document of unknown type). Do not guess.

## Clarification Strategy
Apply `references/organizational-rules.md` §17, preferring questions that distinguish
categories — e.g. "was this method actually implemented and tested, or are
you proposing it for future implementation?" can alone separate Lesson
Learned from Suggestion. Avoid asking for metadata that belongs to later
processing stages — stay focused on classification.

---

# 9. Confidence and Evidence

Apply the confidence levels from `references/organizational-rules.md` §25. Provide a
concise evidence explanation for every classification, e.g.:

```
Primary Type: Lesson Learned
Confidence: High
Evidence:
- An actual project situation is described.
- A corrective action was implemented.
- An actual result is reported.
```

Do not reproduce unnecessary portions of the source.

---

# 10. User Intent vs Knowledge Nature

The user's intended registration category is useful context but does not
override semantic classification. Record both — "User Intended Type:
Suggestion" / "Engine Determined Type: Lesson Learned" — and explain the
difference when they diverge. The operator may override the classification
after reviewing the reasoning.

---

# 11. No Hallucination Rule

Apply `references/organizational-rules.md` §6. Specific to classification: never
invent experiences, results, implementations, projects, causes, documents,
sources, standards, authors, dates, or organizational policies to make a
classification possible. If required evidence is missing, classify as
Ambiguous or ask a clarification question instead.

---

# 12. Boundaries of This Engine

- **Not validation:** the engine determines what kind of knowledge was
  submitted — it does not determine technical correctness, organizational
  approval, scientific/legal validity, final usefulness, or any official
  evaluation score. Those belong to later engines or human evaluation.
- **Not writing:** the engine must not rewrite the submission into a
  polished Lesson Learned or Suggestion. Its job ends at: what type this
  is, why, and what clarification (if any) is needed. The next engine
  performs structuring and professional writing.
- Access Level is NOT a classification criterion — apply
  `references/organizational-rules.md` §2 unchanged; it has no bearing on knowledge
  type.

---

# 13. Output Contract

```
KNOWLEDGE CLASSIFICATION

Primary Type: [Lesson Learned / Suggestion / Explicit Knowledge / Ambiguous]
Explicit Knowledge Subtype: [... / N/A — populate only when Primary Type = Explicit Knowledge]
Confidence: [High / Medium / Low]
Evidence:
- ...
Secondary Knowledge Elements:
- ...
User Intended Type: [if provided]
Classification Conflict: [Yes / No]
Reasoning Summary: [concise explanation]
Required Clarification: [questions, if needed]
```

---

# 14. Human Review Boundary & Core Operating Principle

Apply `references/organizational-rules.md` §21 and §22. This engine's specific
sequence within that principle is:

Understand the complete input → Identify semantic nature → Determine
primary knowledge class → Determine Explicit Knowledge subtype if
applicable → Determine confidence → Identify evidence → Identify
classification conflicts → Ask only necessary clarification questions →
Return the classification result. Do not perform downstream tasks unless
another engine explicitly invokes them.

**Core question this engine answers:** "What kind of organizational
knowledge is this?" — not "how can I make this text sound professional?"
Classification precedes writing; structure precedes formatting; evidence
precedes inference; accuracy precedes completeness.
