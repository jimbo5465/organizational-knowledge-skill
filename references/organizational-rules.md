# ORGANIZATIONAL RULES

## 1. Purpose

This file is the single source of truth for organizational policy rules and
cross-engine writing/behavior standards.

Every engine must comply with this file instead of restating these rules
internally. When an engine's instructions and this file appear to conflict,
this file governs.

---

# 2. Access Level

Default:

Normal

Change the value only when the source material or operator explicitly
indicates:

Confidential
or
Highly Confidential

Never infer confidentiality from subject matter (contract, technical, or
project information does not automatically imply Confidential).

---

# 3. Project Rule

Project is an operator-declared value.

Preserve it exactly as provided. Do not:

- rename it
- translate it
- normalize it
- replace it
- match it against a project database

If the project conflicts with information in the source, flag the conflict
and request operator confirmation.

---

# 4. Knowledge Tree Rule

Knowledge Tree is an organizational controlled taxonomy.

**Official taxonomy: `references/knowledge-tree.md` (active).** Use it as
the authoritative reference for every Knowledge Tree assignment,
recommendation, or validation.

- Select values only from this taxonomy — do not invent nodes, rename
  them, merge them, move them, or create alternative categories.
- Do not translate an operator-selected taxonomy value into a different
  organizational category.
- When preparing a DANA draft, preserve the selected path exactly
  (e.g. `Design and Engineering > Electrical Engineering > Transformers`).
- If the correct node is ambiguous between two plausible branches, do not
  guess — mark it `RECOMMENDED` (per `references/common-knowledge-object.md` §3) and
  request operator selection.
- If a future submission doesn't fit this taxonomy at all, do not invent a
  new node — flag it as a taxonomy gap for operator/administrator
  review rather than silently creating one.

---

# 5. Fact vs Interpretation vs Assumption vs Expectation

Maintain a strict distinction between:

- **Fact** — explicitly stated or directly supported by the source.
- **Interpretation** — a reasonable understanding derived from the source.
- **Assumption** — information that may be true but is not supported.
- **Expectation** — what is expected/believed to happen, not yet confirmed.
- **Proposal** (Suggestion-type knowledge only) — what should be changed.

Facts and carefully supported interpretations may be used in the final
draft. Assumptions and expectations must never be presented as facts or as
confirmed results.

---

# 6. Source-of-Truth Principle

The submitted information is the primary source of truth. An engine may:

- Reorganize information, clarify wording, remove repetition, improve
  logical sequence.
- Make implicit relationships explicit when strongly supported.
- Convert informal language into professional organizational language.
- Summarize lengthy descriptions and extract structured facts.
- Identify missing information.

An engine must never invent facts, results, causes, numerical values,
dates, people, projects, costs, savings, percentages, technical
specifications, approvals, or any other detail not supported by the source.
If information is unknown, it remains unknown — do not fabricate it.

(See also `references/common-knowledge-object.md` §4 for the multi-source
priority order, and §3 for how unknown values must be labeled.)

---

# 7. Cause and Contributing Factors

When identifying why something happened, distinguish between:

- Confirmed cause
- Contributing factor
- Suspected cause
- Unknown cause

Do not convert a plausible explanation into a confirmed root cause, and do
not perform unsupported root-cause analysis. If the source does not
establish the cause, use:

"Not established in the submitted information."

---

# 8. Professional Writing Standard

Final written knowledge must be:

Clear, concise, structured, technically precise, objective, reusable, and
appropriate for an organizational knowledge-management system.

Avoid: excessive storytelling, emotional language, marketing language,
self-congratulation, unnecessary first-person narrative, repetition, empty
management terminology, unsupported claims, and unsupported superlatives.

The objective is knowledge transfer, not literary quality.

---

# 9. Preserve Technical Meaning

Preserve technical terminology when necessary. Do not simplify or replace
technical terms if doing so could change the meaning. This includes:
standards, codes, equipment names, technical abbreviations, process names,
project names, document/specification numbers, and other technical
identifiers.

If terminology is ambiguous, retain the original term and flag it for
operator confirmation when necessary.

---

# 10. Title Generation

Generate a concise, specific title that communicates the knowledge itself
— not a generic label. Avoid titles such as "An Important Experience," "My
Suggestion," "A New Idea," "Improving the Process." Prefer a title that
names the actual subject and outcome, only when supported by the source.

---

# 11. Multilingual Knowledge

Source material may be Persian, English, mixed Persian/English, Persian
with English technical terminology, or English with Persian organizational
terminology. Preserve the original technical meaning regardless of
language.

Default output language: the dominant language of the source, unless the
user specifies otherwise. The Skill itself is written in English while
producing organizational knowledge drafts in Persian (or the source
language) for DANA.

---

# 12. Transferability

Determine how a piece of knowledge can be reused:

- **Directly Transferable** — the same method/proposal can likely be used
  in similar situations.
- **Conditionally Transferable** — reusable when specified conditions
  exist.
- **General Principle / Potentially Broad** — the exact method may not
  transfer, but the underlying principle is useful.
- **Limited / Context-Specific** — highly dependent on the original
  context.

Do not claim broad organizational applicability without evidence.

---

# 13. Generalization Control

Knowledge produced for one project, one department, one equipment type, one
process, one customer, or one exceptional circumstance must not
automatically become a universal organizational rule or solution.

Distinguish: Specific Experience → Reusable Lesson/Proposal → Possible
Broader Application. These are not equivalent. Preserve the original scope
unless broader applicability is explicitly supported.

---

# 14. Innovation / Novelty Awareness

An engine may identify whether the submission appears to contain a new
method, a modified method, a novel solution, or a known practice applied
effectively.

An engine must NOT assign an official innovation score or declare content
"highly innovative" without supporting evidence. Official innovation
evaluation belongs to the organizational evaluation process.

---

# 15. Duplication Awareness

If submitted material suggests possible duplication of existing knowledge,
flag it as:

"Potential duplication — comparison with existing knowledge is required."

Never declare content duplicate without comparison data, and never invent
existing records to compare against.

---

# 16. Missing Information Classification

Classify missing information into:

- **Critical** — without it, the knowledge cannot be reliably understood
  or evaluated.
- **Important** — the knowledge can be understood, but its practical
  value/evaluability is reduced.
- **Optional** — may improve the document but is not required.

Ask questions primarily for Critical information. Ask for Important
information only when it materially improves the final knowledge. Do not
ask for Optional information unless requested.

---

# 17. Minimum Clarification Strategy

When information is incomplete, ask the smallest number of questions that
can significantly improve the output. Do not automatically ask every
possible question — ask only what the submitted information actually
requires.

---

# 18. Metadata Boundary

An engine may identify metadata when clearly available but must never
invent organizational metadata. Use the CKO Information State values
(`references/common-knowledge-object.md` §3) to mark unknown fields —
typically `RECOMMENDED` (needs operator confirmation) or `UNKNOWN`.

---

# 19. Hashtag Generation

Generate a small number of meaningful hashtags reflecting subject, process,
technical domain, or relevant organizational area. Avoid generating large
numbers of hashtags. Do not invent official taxonomy terms merely to
create hashtags.

---

# 20. Evaluation Boundary

An engine may prepare the information required for evaluation but must
never approve, reject, assign an official committee decision, assign an
official score, or claim technical/financial feasibility without evidence.
Human or authorized organizational evaluation remains necessary.

---

# 21. Human Review Boundary

Every engine produces a draft only. The operator remains responsible for
verifying facts, confirming metadata/technical content/access
level/contributors, making final edits, and submitting the knowledge to
the organizational system.

An engine must never imply that its output has already been approved,
validated, evaluated, or published.

---

# 22. Core Operating Principle

Every engine must follow the same top-level sequence: **Understand →
Extract → Structure → Identify the knowledge → Detect missing information
→ Write → Quality check → Produce draft.**

Never reverse this order and never start by writing. Understand first,
then structure, then write. (Each engine's own instructions define its
specific extraction steps within this sequence.)

---

# 23. Numerical Integrity

Preserve all validated numerical information exactly — percentages,
measurements, quantities, dates, document numbers, standard numbers,
revision numbers — across every stage of the pipeline (source → engine
output → metadata → final draft). Do not round, reinterpret, or silently
alter a value. If a numerical value changes during processing, flag it.

---

# 24. No Silent Correction Boundary

Distinguish what may be auto-corrected from what must never be. May
auto-correct: obvious formatting problems, duplicate spaces, minor
punctuation, clear structural duplication. Must NEVER be auto-corrected:
technical facts, project names, Knowledge Tree values, access level /
confidentiality, numerical claims, dates, standards, authors, publication
metadata, organizational decisions.

For anything in the second group, never silently modify the value —
instead report:

Potential Correction: ... / Reason: ... / Operator Confirmation Required.

---

# 25. Confidence Levels

Any classification or recommendation that carries uncertainty must state
one of:

- **High** — strong, direct evidence clearly supports it.
- **Medium** — probable, but some ambiguity or incompleteness exists.
- **Low** — tentative; confirmation or clarification is recommended.

Never present a Low-confidence result as definitive, and never upgrade
confidence merely because a value sounds plausible.

---

# 26. Output Language Policy

The Skill's internal documents remain in English, but **every output
label, section header, field name, checklist item, status value, and
prompt/question rendered to the operator must be in Persian**, in the
dominant language of the source (per §11). English technical terms,
standards, project names, document numbers, official taxonomy values, and
proper nouns inside the content stay unchanged.

## 26.1 Mandatory Label Mapping

Render operator-facing labels using the canonical Persian mapping below.
Use these exactly; do not invent alternative Persian spellings for the
same label.

| English Label | Persian Label |
|---|---|
| Knowledge Classification | طبقهبندی دانش |
| Primary Type | نوع اصلی |
| Explicit Knowledge Subtype | زیرنوع دانش صریح |
| Classification Confidence | اطمینان طبقهبندی |
| Classification Basis | مبنای طبقهبندی |
| Evidence | شواهد |
| Secondary Knowledge Elements | عناصر دانش ثانویه |
| User Intended Type | نوع مدنظر کاربر |
| Classification Conflict | تعارض طبقهبندی |
| Reasoning Summary | جمعبندی استدلال |
| Required Clarification | ابهامات نیازمند پرسش |
| Knowledge Type | نوع دانش |
| Knowledge Subtype | زیرنوع دانش |
| Title | عنوان |
| Description | شرح |
| Context | زمینه |
| Situation | وضعیت |
| Problem, Gap or Opportunity | مشکل، شکاف یا فرصت |
| Cause or Contributing Factors | علت یا عوامل مؤثر |
| Action | اقدام |
| Actual Result | نتیجه واقعی |
| Core Lesson | درس اصلی |
| Lesson Learned | درس آموخته |
| Lesson Description | شرح درس آموخته |
| Execution Result | نتیجه اجرا |
| Transferability | قابلیت انتقال |
| Recommendation | توصیه |
| Current State | وضع موجود |
| Proposed Improvement | پیشنهاد بهبود |
| Implementation Logic | منطق پیادهسازی |
| Expected Impact | اثر مورد انتظار |
| Implementation Status | وضعیت پیادهسازی |
| Actual Implementation | اجرای انجامشده |
| Evidence | شواهد |
| Potential Risks | ریسکهای بالقوه |
| Suggestion Status | وضعیت پیشنهاد |
| Resource Identity | هویت منبع |
| Resource Metadata | فراداده منبع |
| Main Subject | موضوع اصلی |
| Main Findings or Conclusions | یافتهها یا نتیجهگیریهای اصلی |
| Practical Value | ارزش عملی |
| Organizational Relevance | ارتباط سازمانی |
| Knowledge Tree | درخت دانش |
| Organizational Scope | محدوده سازمانی |
| Project | پروژه |
| Procedure or Process | رویه یا فرآیند |
| Access Level | سطح دسترسی |
| Colleagues | همکاران |
| Specialized Committee | کمیته تخصصی |
| Suggestion Seed | بذر پیشنهاد |
| Suggestion Title | عنوان پیشنهاد |
| Impact of Implementation | تاثیر اجرای پیشنهاد |
| Results of Implementation | نتایج حاصل از اجرای پیشنهاد |
| Hashtags | هشتگها |
| Attachments | فایل پیوست |
| Primary Resource | منبع اصلی |
| Source Language | زبان منبع |
| Missing Information | اطلاعات ناقص |
| Critical | حیاتی |
| Important | مهم |
| Optional | اختیاری |
| Metadata Confidence | اطمینان فراداده |
| Operator Confirmation Required | نیازمند تأیید اپراتور |
| Registration Information | اطلاعات ثبت |
| Content | محتوا |
| Metadata | فراداده |
| Resources | منابع |
| QA Status | وضعیت QA |
| Operator Review Required | بازبینی اپراتور الزامی است |
| Unresolved Items | موارد حلنشده |
| Final Operator Checklist | چکلیست نهایی اپراتور |
| Operator Review | بازبینی اپراتور |
| Overall Status | وضعیت کلی |
| Quality Scores | امتیازهای کیفیت |
| Critical Issues | مسائل حیاتی |
| High Issues | مسائل مهم |
| Medium Issues | مسائل متوسط |
| Low Issues | مسائل جزئی |
| Unsupported Claims | ادعاهای بیپشتوانه |
| Metadata Issues | مسائل فراداده |
| Classification Issues | مسائل طبقهبندی |
| Contradictions | تناقضها |
| Operator Actions | اقدامات اپراتور |
| Final QA Decision | تصمیم نهایی QA |
| Quality Review | بازبینی کیفیت |
| Problem Clarity | وضوح مسئله |
| Proposal Clarity | وضوح پیشنهاد |
| Evidence Quality | کیفیت شواهد |
| Potential Duplication | احتمال تکراریبودن |
| Information Gaps | شکافهای اطلاعاتی |
| Confidence | اطمینان |
| Not Implemented | پیادهسازینشده |
| Partially Implemented | پیادهسازی جزئی |
| Fully Implemented | پیادهسازیشده کامل |
| Implementation Status Unknown | وضعیت پیادهسازی نامشخص |
| Not Provided | ارائه نشده |
| Not Specified | مشخص نشده |
| Recommended | پیشنهادی |
| Confirmed | تأییدشده |
| Unknown | نامشخص |
| Not Applicable / N/A | قابل اعمال نیست |
| Pass | قبول |
| Review Required | نیازمند بازبینی |
| Fail | رد |
| New | جدید |

## 26.2 Application

- All four engine Output Contracts (§ Output Contract in each engine file)
  and the DANA Draft structure (references/dana-draft.md §4, §6, §8) are
  rendered with these Persian labels.
- Status values such as High / Medium / Low, Pass / Review Required /
  Fail, Confirmed / Recommended / Unknown are also rendered in Persian
  (High → بالا، Medium → متوسط، Low → پایین; Confirm→ تأیید، etc.) while
  the technical meaning is preserved.
- English abbreviations and technical terms that have no Persian
  equivalent (e.g. DANA, QA, DCS, PLC, Holiday Test, Knowledge Tree as a
  taxonomy name) are kept in English inside the Persian output.
- This policy governs display only. Internal processing logic and the
  canonical English field names in `references/common-knowledge-object.md`
  remain unchanged.
