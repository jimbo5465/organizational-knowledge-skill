---
name: organizational-knowledge-skill
description: Use when preparing org knowledge for DANA registration.
version: 2.0.2
author: Mohsen Shaterian
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [knowledge-management, dana, lesson-learned, suggestion, explicit-knowledge, qa]
    related_skills: [telegram-bot-ai-integration]
---

# ORGANIZATIONAL KNOWLEDGE MANAGEMENT SKILL

## Overview

Structures raw organizational knowledge (experiences, suggestions, documents, links, media) into classified, metadata-rich, QA-validated DANA registration drafts. This SKILL.md is the Orchestrator: it routes between seven engine files, while all policy rules and the shared data contract live in the references listed in File Map (Section 2).

## When to Use

- When organizational knowledge must be prepared for registration in the DANA knowledge management system.
- When input (text, documents, audio/video, images, URLs, or operator messages; Persian, English, or mixed) needs classification as Lesson Learned, Suggestion, or Explicit Knowledge.
- When a DANA record needs structured content, metadata mapping, quality assurance, or a final operator-ready registration draft.
- The skill prepares drafts only — it never submits to DANA and never replaces human review.

## Version

2.0.2 — Mandatory report format: the final DANA draft must be rendered as the complete report per `references/dana-draft.md` §8 (all sections + Final Operator Checklist).
2.0.1 — Hermes-registered: added YAML frontmatter, moved all engines under `references/`, normalized every cross-file reference, LF line endings.
2.0.0 — restructured into an Orchestrator + Engines + References
architecture. All engine-specific logic and shared standards were moved
out of this file into the files listed in §2. This file contains
orchestration logic only.

---

# 1. Purpose

This Skill enables an AI agent to identify, structure, quality-check, and
prepare organizational knowledge for registration in the DANA knowledge
management system.

Sources: employee experiences, lessons learned, suggestions, documents,
educational materials, links, books, articles, reports, standards,
podcasts, magazines, inventions, and other explicit knowledge resources.

The Skill is application-independent — it may receive information from a
human operator, a Telegram bot (e.g. welderbot), a web application,
uploaded documents, audio, video, images, URLs, or other AI agents. It may
process Persian, English, or mixed Persian/English content.

---

# 2. File Map — Required Context

This SKILL.md is the Orchestrator only. It does not contain classification
rules, writing rules, metadata rules, QA rules, or drafting rules — those
live in the files below. Load them as follows:

## Always load (base context for every step)

- `references/organizational-rules.md` — all shared policy rules and
  cross-engine writing/behavior standards (Access Level, Project Rule,
  Knowledge Tree Rule, non-fabrication, professional writing, missing-
  information handling, confidence levels, human review boundary, etc).
- `references/common-knowledge-object.md` — the shared data structure
  (Common Knowledge Object), Information States, Source-of-Truth
  priority, and every engine's INPUT → PROCESS → OUTPUT contract.

## Load conditionally, per active step

| Step | File |
|---|---|
| Classification | `references/knowledge-classification.md` |
| Content (Lesson Learned) | `references/lesson-learned.md` |
| Content (Suggestion) | `references/suggestion.md` |
| Content (Explicit Knowledge) | `references/explicit-knowledge.md` |
| Metadata | `references/metadata.md` + `references/knowledge-tree.md` |
| Quality Assurance | `references/quality-assurance.md` + `references/knowledge-tree.md` |
| DANA Draft | `references/dana-draft.md` + `references/knowledge-tree.md` |

`references/knowledge-tree.md` is the official, active organizational
taxonomy (`references/organizational-rules.md` §4) — load it whenever the current
step assigns, validates, or drafts a Knowledge Tree value. It's not
needed for the Classification or Content-engine steps unless a subtype
decision genuinely depends on it.

If any engine file referenced by the current step is unavailable, do not
improvise its logic — report `ENGINE FILE UNAVAILABLE: [name]` and stop
that step rather than guessing.

---

# 3. Core Objective

Transform raw organizational knowledge into: correctly classified
knowledge → professionally structured content → correct organizational
metadata → quality-controlled information → a final operator-ready DANA
registration draft.

Priorities: **factual accuracy over completeness**, **traceability over
fluent speculation**. Never fabricate organizational information (see
`references/organizational-rules.md` §6).

---

# 4. Important Boundary

This Skill is NOT the DANA system. It does not submit information to
DANA — it prepares a high-quality draft for human review and
registration. The final decision to submit belongs to the human operator
(`references/organizational-rules.md` §21).

---

# 5. Organizational Knowledge Model

1. Lesson Learned
2. Suggestion
3. Explicit Knowledge — Book, Training Content, Link, International
   Report, Podcast, Article, Invention, Magazine, Standard

---

# 6. Process Overview

```
RAW INPUT
    ↓
Knowledge Classification Engine
    ↓
Relevant Knowledge Engine (Lesson Learned / Suggestion / Explicit Knowledge)
    ↓
Metadata Engine
    ↓
Quality Assurance Engine
    ↓
DANA Draft Engine
    ↓
Operator Review
    ↓
DANA Registration
```

Only the relevant Knowledge Engine is executed, based on the
Classification Engine's output (see `references/common-knowledge-object.md` §14 for
the routing contract).

---

# 7. Orchestration Steps

1. Run the Knowledge Classification Engine.
2. Run only the relevant Knowledge Engine (Lesson Learned / Suggestion /
   Explicit Knowledge).
3. Run the Metadata Engine.
4. Run the Quality Assurance Engine.
5. Run the DANA Draft Engine (subject to the QA gate —
   `references/quality-assurance.md` §13).
6. Return the draft and remaining operator actions.

An engine may enrich the Common Knowledge Object but must not silently
delete information from a previous engine, and must not perform another
engine's responsibilities (`references/common-knowledge-object.md` §5, §17).

---

# 8. Handling Incomplete Input

Do not reject incomplete knowledge immediately:

1. Extract what is available.
2. Identify the knowledge type.
3. Structure the available information.
4. Identify missing critical information
   (`references/organizational-rules.md` §16).
5. Ask only the necessary questions (§9 below).
6. Continue processing once sufficient information exists.

---

# 9. Operator Interaction

Ask only for information that is genuinely required — apply
`references/organizational-rules.md` §17 (Minimum Clarification Strategy). Do not ask
for information reliably extractable from the submitted material, and do
not ask generic questions merely to make the record look more complete.

Prefer a specific question ("Which Knowledge Tree node should be
assigned?") over a generic one ("Can you provide more information?") when
a specific field is missing.

---

# 10. Multimedia, Document, and URL Input

- **Multimedia** (images, audio, video): extract usable information when
  capabilities are available. Never claim to have analyzed inaccessible
  media — return `MEDIA VERIFICATION REQUIRED` instead.
- **Documents**: extract facts, metadata, technical terminology, dates,
  identifiers, context, results, and supporting evidence. Never invent
  what's missing.
- **URLs**: preserve exactly. When accessible, extract resource identity,
  type, description, and metadata (`references/explicit-knowledge.md` §8). When
  inaccessible, return `URL VERIFICATION UNAVAILABLE` — never invent the
  content.

---

# 11. Final Output to the Operator

The final answer should normally contain: (1) knowledge classification,
(2) important metadata requiring confirmation, (3) QA status, (4) the
final DANA draft, (5) remaining operator actions. Do not expose internal
reasoning or chain-of-thought — provide conclusions, evidence-based
explanations, and actionable issues.

**Mandatory report format:** the final DANA draft in (4) must be rendered
as the complete DANA KNOWLEDGE REGISTRATION DRAFT report defined in
`references/dana-draft.md` §8 — all eight sections (Registration
Information, Content, Metadata, Resources, QA Status, Operator Review
Required, Unresolved Items, Final Operator Checklist), including the
Operator Review Checklist from `references/dana-draft.md` §6. Never return
a condensed draft that omits any of these sections.

---

# 12. End-to-End Execution Model

```
RAW ORGANIZATIONAL KNOWLEDGE
        ↓
CLASSIFICATION
        ↓
LESSON LEARNED / SUGGESTION / EXPLICIT KNOWLEDGE
        ↓
STRUCTURED KNOWLEDGE
        ↓
DANA METADATA
        ↓
QUALITY ASSURANCE
        ↓
DANA DRAFT
        ↓
OPERATOR REVIEW
        ↓
DANA REGISTRATION
```

END OF ORCHESTRATOR
