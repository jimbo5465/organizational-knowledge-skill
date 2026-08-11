# COMMON KNOWLEDGE OBJECT & ENGINE CONTRACTS

## 1. Purpose

All engines in this Skill operate on a shared conceptual data structure
called the Common Knowledge Object (CKO).

The CKO provides a common language between engines. It prevents each
engine from creating its own incompatible representation of the same
knowledge.

The CKO is an internal workflow object. It does not need to be submitted
directly to DANA.

Organizational policy rules (Access Level, Project, Knowledge Tree) are
NOT defined here — see `references/organizational-rules.md`. This file
defines only the data shape and the engine input/output contracts.

---

# 2. Common Knowledge Object

The Common Knowledge Object contains the following conceptual sections:

## Source
source_material: / source_language: / source_files: / source_media: / source_urls:

## Classification
knowledge_type: / knowledge_subtype: / classification_confidence: / classification_basis:

## Content
title: / description: / context: / problem: / action: / current_state: /
proposed_improvement: / expected_impact: / actual_result: / lesson_learned: /
practical_applicability:

## Metadata
knowledge_tree: / procedure_process: / project: / organizational_scope: /
access_level: / colleagues: / specialized_committee: / suggestion_seed: / hashtags:

## Resources
primary_resource: / attachments: / images: / audio: / video:

## QA
qa_status: / qa_issues: / unsupported_claims: / contradictions: / quality_scores:

## Draft
dana_registration_type: / dana_fields: / operator_actions: / unresolved_items: / draft_status:

---

# 3. Information State

Every important value in the CKO must conceptually have one of these
states:

- **CONFIRMED** — explicitly supported by the operator or source.
- **DERIVED** — logically derived from confirmed information.
- **RECOMMENDED** — suggested by the engine, but operator confirmation is required.
- **UNKNOWN** — cannot currently be determined.
- **NOT_APPLICABLE** — the field does not apply to this knowledge type.

All engines use these five states — see `references/organizational-rules.md` §18 for
how this applies to the Metadata Boundary rule.

---

# 4. Source of Truth (Multi-Source Priority)

When information is available from multiple sources, apply this priority:

1. Explicit operator input
2. Original source material
3. Extracted source content
4. Previous engine output
5. AI inference

AI inference must never override explicit operator input.

(For what an engine is/isn't allowed to invent, see
`references/organizational-rules.md` §6.)

---

# 5. Engine Contract

Every engine must follow: **INPUT → PROCESS → OUTPUT**.

An engine may enrich the CKO but must not silently delete information
produced by previous engines.

---

# 6. Knowledge Classification Engine Contract

**Input:** Raw knowledge information — operator responses, text, images,
audio, video, documents, URLs, operator-supplied context.

**Process:** Determine the most appropriate knowledge category.

Primary categories: Lesson Learned, Suggestion, Explicit Knowledge.

If Explicit Knowledge is selected, determine the subtype: Book, Training
Content, Link, International Report, Podcast, Article, Invention,
Magazine, Standard.

**Output:** `knowledge_type`, `knowledge_subtype`, `classification_confidence`,
`classification_basis`.

The engine must not write the final DANA record.

**Classification principle (shared with the Explicit Knowledge Engine):**
classify by the semantic nature and primary purpose of the material, never
by file format alone — a PDF, MP3, MP4, or URL can each represent several
different knowledge types depending on actual content and purpose.

---

# 7. Lesson Learned Engine Contract

**Input:** CKO with raw source, Classification = Lesson Learned, relevant
contextual information.

**Process:** Transform the experience into a structured organizational
Lesson Learned. Identify, when available: Context, Problem/Challenge,
Action/Experience, Result, Lesson Learned, Practical Applicability.

**Output:** `title`, `context`, `problem`, `action`, `actual_result`,
`lesson_learned`, `practical_applicability`.

The engine must not invent an experience or result.

---

# 8. Suggestion Engine Contract

**Input:** CKO with raw source, Classification = Suggestion.

**Process:** Transform the idea into a structured organizational
suggestion. Identify, when available: Current State, Problem/Opportunity,
Proposed Improvement, Expected Impact, Implementation Status, Actual
Results.

**Output:** `title`, `current_state`, `proposed_improvement`,
`expected_impact`, `implementation_status`, `actual_result`.

Expected results must remain separate from actual results.

---

# 9. Explicit Knowledge Engine Contract

**Input:** CKO with raw source, Classification = Explicit Knowledge.

**Process:** Identify and structure the explicit knowledge resource.
Determine the subtype (Book, Training Content, Link, International
Report, Podcast, Article, Invention, Magazine, Standard).

**Output:** `knowledge_subtype`, `title`, `description`,
`resource_identity`, `resource_metadata`, `primary_resource`.

The engine must not classify a resource solely from its file format.

---

# 10. Metadata Engine Contract

**Input:** CKO after classification and relevant content processing.

**Process:** Map available information to DANA metadata fields.

**Output by knowledge type:**

- *Lesson Learned:* title, knowledge_tree, procedure_process, project,
  organizational_scope, access_level, colleagues, lesson_learned,
  actual_result, hashtags, images, attachments
- *Suggestion:* title, knowledge_tree, specialized_committee,
  suggestion_seed, expected_impact, colleagues, current_state,
  proposed_improvement, actual_result, hashtags, attachments
- *Explicit Knowledge:* knowledge_subtype, title, description,
  knowledge_tree, organizational_scope, project, hashtags, attachments

The Metadata Engine must preserve operator-declared project values
exactly (see `references/organizational-rules.md` §3).

---

# 11. Quality Assurance Engine Contract

**Input:** Complete CKO after content and metadata processing.

**Process:** Validate classification, factual integrity, completeness,
consistency, metadata, non-fabrication, writing quality, registration
readiness.

**Output:** `qa_status` (PASS / REVIEW_REQUIRED / FAIL), plus `qa_issues`,
`unsupported_claims`, `contradictions`, `quality_scores`,
`operator_actions`.

If a critical problem exists: `qa_status = FAIL`.

---

# 12. DANA Draft Engine Contract

**Input:** CKO with completed content, metadata, and QA result.

**Process:** Convert the validated CKO into an operator-ready DANA
registration draft.

**Output:** `dana_registration_type`, `dana_fields`, `operator_actions`,
`unresolved_items`, `draft_status`.

The engine must not: reclassify knowledge, modify project, invent
Knowledge Tree values, change access level, add unsupported information,
or claim successful submission.

---

# 13. Engine Data Flow

RAW INPUT → Knowledge Classification Engine → Common Knowledge Object →
{Lesson Learned Engine / Suggestion Engine / Explicit Knowledge Engine} →
Metadata Engine → Quality Assurance Engine → DANA Draft Engine → FINAL
OPERATOR-READY DRAFT.

---

# 14. Conditional Routing

Only the relevant content engine is executed, based on `knowledge_type`
(Lesson Learned / Suggestion / Explicit Knowledge). All paths then
continue: Metadata → QA → DANA Draft.

---

# 15. Failure Handling

If an engine cannot reliably perform its task, it must NOT fabricate an
answer. It must return:

```
status: NEEDS_OPERATOR_INPUT
reason: ...
missing_information: ...
```

The workflow may continue only when the missing information is not
required for the next stage.

---

# 16. Information Preservation

Every engine must preserve: original source information, operator
declarations, attachments, URLs, technical terminology, numerical values,
project names, document identifiers. An engine may restructure information
but must not silently destroy it.

---

# 17. Final Principle

The engines are specialized workers. The Common Knowledge Object is their
shared workspace. The Orchestrator controls which worker runs and in what
order. No engine should attempt to perform the responsibilities of another
engine.
