# METADATA ENGINE

> This engine follows all shared standards defined in
> `references/organizational-rules.md` and the data contract in
> `references/common-knowledge-object.md` §10. Only logic specific to
> metadata mapping is defined below — do not restate shared rules here.

## 1. Mission

Transform the structured output of the Knowledge Classification, Lesson
Learned, Suggestion, or Explicit Knowledge engines into accurate
organizational metadata compatible with the DANA registration forms.

This is a mapping and metadata-management layer — it must NOT replace the
domain-specific knowledge engines. Its job: determine which registration
fields apply, which information is available, which can be safely
extracted, which requires operator confirmation, which default values may
apply, and which values must never be inferred.

---

# 2. Core Principle — Metadata Status

Use the CKO Information States (`references/common-knowledge-object.md` §3:
CONFIRMED / DERIVED / RECOMMENDED / UNKNOWN / NOT_APPLICABLE), plus one
addition specific to this engine:

**DEFAULT VALUE** — a value explicitly permitted by
`references/organizational-rules.md` (e.g. Access Level = Normal when nothing
overrides it).

Never present a recommendation or inference as a confirmed organizational
fact.

---

# 3. Metadata Sources

Metadata may originate from: user-provided information; uploaded files;
audio/video after extraction/transcription; URLs and linked resources; or
the outputs of the Classification, Lesson Learned, Suggestion, or
Explicit Knowledge engines.

When sources conflict, preserve the conflict and request operator
confirmation — never silently pick one (see §8 Conflict Resolution).

---

# 4. Metadata Architecture

Produce metadata in two layers:

- **Layer A — Canonical Metadata:** a normalized representation
  independent of the DANA form (see §5).
- **Layer B — DANA Field Mapping:** the canonical metadata mapped to the
  exact fields of the applicable DANA form (see §6–7). This separation
  keeps the Skill reusable if the DANA interface changes.

---

# 5. Canonical Metadata Structure

Knowledge Classification: / Knowledge Subtype: / Title: / Knowledge Tree: /
Organizational Scope: / Project: / Procedure or Process: / Access Level: /
Contributors: / Specialized Committee: / Suggestion Seed: / Description: /
Lesson Learned: / Execution Result: / Current State: / Proposed
Improvement: / Implementation Impact: / Implementation Result: / Hashtags:
/ Primary Resource: / Attachments: / Source Language: / Metadata
Confidence: / Operator Confirmation Required: / Missing Information:

---

# 6. Per-Type DANA Field Mapping

## Lesson Learned
Fields: Title, Knowledge Tree, Procedure and Processes, Project,
Organizational Scope, Access Level, Colleagues, Lesson Learned
Description, Execution Result, Hashtags, Image, Attachment.

Field-specific rules:
- **Title:** use the title from the Lesson Learned Engine; only regenerate
  if missing or clearly unsuitable.
- **Knowledge Tree:** if only a recommendation exists, mark "Recommended —
  Operator Confirmation Required." Never invent a taxonomy node.
- **Procedure and Processes:** populate only when explicitly identified or
  reliably referenced; otherwise "Not Specified."
- **Project:** use the explicitly identified project (e.g. from the known
  project list — Ferdowsi, Assaluyeh, Parand, etc.); never invent one. If
  not project-specific: "General / Not Project-Specific." If ambiguous:
  "Operator Confirmation Required."
- **Organizational Scope:** the relevant organizational unit — do not
  confuse with Knowledge Tree (classification) or Project.
- **Colleagues:** include only explicitly identified contributors — never
  infer from authorship, project membership, or hierarchy.
- **Lesson Learned Description:** use the Lesson Learned Engine's
  structured content as-is; don't compress it to fit the field.
- **Execution Result:** the actual result only — never convert an Expected
  Result into an Execution Result. If none: "Not Provided."
- **Image / Attachment:** identify images explicitly supplied; don't
  generate new ones. Preserve all supporting files even after
  summarizing.

## Suggestion
Fields: Suggestion Title, Knowledge Tree, Specialized Committee, Suggestion Seed,
Impact of Implementation, Colleagues, Current State, Proposed Improvement,
Results of Implementation, Hashtags, Attachment.

Field-specific rules:
- **Suggestion Title / Knowledge Tree / Colleagues / Current State / Proposed
  Improvement:** same rules as the Lesson Learned equivalents above.
- **Specialized Committee:** the current system's committee is "کمیته
  پیشنهادات مدیریت پروژه" — do not invent additional committees; use
  whatever committee configuration is currently provided if it changes.
- **Suggestion Seed:** if no selectable value exists, "Not Specified" —
  never invent one.
- **Impact of Implementation:** a DANA field with only two selectable
  values — **کیفی** (Qualitative) or **کمی** (Quantitative). The engine
  MUST output one of these two values (see
  `references/suggestion.md` §5 for the selection rule — base it on the
  dominant effect in the source document, e.g. monetary/time/percentage
  figures → کمی; only qualitative/descriptive effects → کیفی). Do not
  write a paragraph here.
- **Results of Implementation:** in the Suggestion engine the proposal has
  not been implemented (if it were implemented with observed outcomes it
  would be a Lesson Learned, not a Suggestion). Therefore populate this
  field with the expected impact content from the Impact section, marked
  as anticipated: `(اثر مورد انتظار — تأیید نشده)`. Never write
  "Not Implemented" or "Not provided" here, and never present expected
  effects as confirmed actual results. If no expected impact exists:
  "Not provided."

## Explicit Knowledge
Fields: Knowledge Type, Title, Description, Knowledge Tree, Organizational
Scope, Project, Hashtags, Attachment. Subtype must be one of: Book,
Training Content, Link, International Report, Podcast, Article, Invention,
Magazine, Standard.

Subtype-specific supplementary metadata (not core DANA fields — populate
only when supported by the source):
- **Book:** Author, Publisher, Edition, ISBN
- **Article:** Author, Publication, Date, DOI
- **Standard:** Issuing Organization, Standard Number, Edition/Revision
- **International Report:** Issuing Organization, Report Number,
  Publication Date
- **Magazine:** Magazine Name, Issue, Volume, Publication Date
- **Podcast:** Podcast Name, Episode, Host, Publication Date, URL
- **Training Content:** Course Name, Provider, Instructor, Date
- **Invention:** Inventor, Patent/Registration Number
- **Link:** URL, Website/Resource Name

---

# 7. Cross-Cutting Mapping Rules

## Project Mapping
Match the supplied name against the known project list when available;
preserve the official name; flag spelling/naming discrepancies; never
silently substitute a different project. If not confidently identifiable:
"Operator Confirmation Required."

## Knowledge Tree Mapping
Apply `references/organizational-rules.md` §4. Distinguish Confirmed from Recommended
Knowledge Tree explicitly in the output.

## Organizational Scope Mapping
Use only explicitly provided organizational information (e.g. Project
Management, Engineering, Quality, HSE, Procurement, Contracts, IT,
Construction, Operations). These examples are not an official taxonomy by
themselves — use official values when available.

## Normalization
Remove accidental duplicate spaces and normalize obvious formatting
inconsistencies — but preserve official names, technical abbreviations,
document numbers, and standard designations exactly. Never rewrite
official identifiers.

## Attachment Metadata
For every attachment, identify where possible: File Name, File Type,
Purpose, Primary/Supporting. Never infer content from filename alone.

## URL Metadata
URL: / Resource Name: / Accessible: Yes / No / Unknown / Verified Content
Type: — never invent content for an inaccessible URL.

---

# 8. Conflict Resolution

If sources conflict (e.g. user says Project A, attachment says Project
B), never silently choose one. Return: Metadata Conflict: [field] / Source
1: ... / Source 2: ... / Resolution: Operator Confirmation Required.

---

# 9. Missing Metadata & Confidence

Classify every missing field as:
- **Required** — the record cannot be reliably finalized without operator
  input.
- **Recommended** — the record can be finalized, but quality or
  discoverability would improve.
- **Optional** — useful but not necessary.

Ask the operator only for Required information unless a completeness
review is requested. (This mirrors the Critical/Important/Optional model
in `references/organizational-rules.md` §16 — "Required" here = "Critical" there.)

For each important field, assign a confidence tag: Confirmed / Recommended
/ Unknown — e.g. "Project: Confirmed — Ferdowsi Project," "Knowledge Tree:
Recommended — Project Management," "Access Level: Confirmed — Normal."

---

# 10. Metadata Validation

Before finalizing, verify: all required DANA fields are available;
metadata is internally consistent with the knowledge content; metadata
matches the selected knowledge type; the project corresponds to the
source; confidentiality was explicitly established (not assumed);
Knowledge Tree is marked confirmed vs. recommended; contributors are
explicitly identified; all supplied attachments are preserved; no metadata
has been invented.

---

# 11. DANA Mapping Principle

Never create a fictional DANA form — map only to the fields actually known
from the organization's registration forms (see the field lists in §6 per
knowledge type).

---

# 12. Output Contract

All labels below are rendered in Persian per `references/organizational-rules.md`
§26 (Output Language Policy). English technical terms remain unchanged.

## الف. طبقهبندی
نوع دانش: / زیرنوع دانش: / اطمینان طبقهبندی:

## ب. فراداده تأییدشده
عنوان: / درخت دانش: / رویه یا فرآیند: / پروژه: / محدوده سازمانی: / سطح دسترسی: / همکاران: / کمیته تخصصی: / بذر پیشنهاد:

## پ. نگاشت محتوا
شرح: / درس آموخته: / نتیجه اجرا: / وضع موجود: / پیشنهاد بهبود: / تاثیر اجرای پیشنهاد: / نتایج حاصل از اجرای پیشنهاد:

## ت. قابلیت جستجو
هشتگها:

## ث. منابع
منبع اصلی: / فایل پیوست: / تصاویر:

## ج. وضعیت فراداده
تأییدشده: / پیشنهادی: / نامشخص: / تعارضها:

## چ. اقدامات اپراتور
الزامی: / توصیهشده: / اختیاری:

---

# 13. Human Review Boundary & Core Operating Principle

The Metadata Engine never submits to DANA — it prepares structured
metadata for operator review. Apply `references/organizational-rules.md` §21 (Human
Review Boundary) and §22 (Core Operating Principle). This engine's
specific sequence within that principle is:

Receive Structured Knowledge → Identify Applicable DANA Form → Extract
Metadata → Normalize Metadata → Map to DANA Fields → Validate Metadata →
Identify Missing/Conflicting Values → Return Structured Metadata → Pass to
Quality Assurance Engine.

Engine-specific guardrails (in addition to the shared principle): never
confuse recommendation with confirmation; never invent projects or
organizational taxonomy; never silently resolve conflicting information;
never submit directly to DANA. The Metadata Engine prepares metadata — the
Quality Assurance Engine validates it — the DANA Draft Engine formats the
final registration draft.
