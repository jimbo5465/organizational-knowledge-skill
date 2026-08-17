# DANA DRAFT ENGINE

> This engine follows all shared standards defined in
> `references/organizational-rules.md` and the data contract in
> `references/common-knowledge-object.md` §12. Only logic specific to
> drafting is defined below — do not restate shared rules here.

## 1. Mission

Transform a QA-validated knowledge record into a clear, structured,
operator-ready draft for DANA registration. This is a **formatting and
presentation layer** — it does NOT reclassify knowledge, rewrite it
unnecessarily, change factual information, invent missing information,
select unknown taxonomy values, change project names or access levels,
resolve metadata conflicts, or submit information to DANA.

---

# 2. Input & QA Gate

The engine normally receives: Knowledge Classification output, the
relevant Knowledge Engine output, Metadata Engine output, and Quality
Assurance Engine output. Apply the QA gate exactly as defined in
`references/quality-assurance.md` §13 (FAIL → blocked draft with issues
listed; REVIEW_REQUIRED → draft generated but marked "Operator Review
Required"; PASS → generate the registration-ready draft).

---

# 3. Drafting Principle

Preserve the distinction between CONFIRMED INFORMATION and OPERATOR ACTION
REQUIRED — never hide uncertainty inside fluent prose. For an unknown
field, explicitly mark `[OPERATOR INPUT REQUIRED]` rather than inventing a
value; for a genuinely optional field with nothing available, use
`[OPTIONAL - NOT PROVIDED]` instead. Never use "N/A" for a field that's
actually required but unknown.

Apply `references/organizational-rules.md` §11 (Multilingual) for source-language
preservation, §3/§4/§2 for Project/Knowledge Tree/Access Level (preserve
exactly as validated — the Draft Engine never upgrades access level or
corrects a project name on its own judgment), §9 for technical/numerical
integrity, and §24 (No Silent Correction Boundary) — if a correction seems
necessary, report "Potential Correction: ... / Reason: ... / Operator
Confirmation Required" instead of modifying the value.

---

# 4. Draft Structure

All labels below are rendered in Persian per `references/organizational-rules.md`
§26 (Output Language Policy). English technical terms remain unchanged.

Every draft begins with:

```
پیشنویس ثبت دانش در DANA
نوع دانش: ...
وضعیت QA: ...
بازبینی اپراتور: الزامی / غیر الزامی
```

## Lesson Learned
```
### نوع ثبت: درس آموخته
### عنوان / درخت دانش / رویه و فرآیندها / پروژه /
### محدوده سازمانی / سطح دسترسی / همکاران /
### شرح درس آموخته / نتیجه اجرا / هشتگها / تصویر / فایل پیوست
```
Present the Description in logical order: Context/Situation → Problem or
Challenge → Action/Experience → Result → Lesson Learned → Practical
Applicability — but don't force a section the source doesn't support, and
don't fabricate a missing one. Title should be specific, concise,
searchable, and representative (avoid generic titles like "Important
Experience" unless that's genuinely all that's available — see
`references/organizational-rules.md` §10). Never change an operator-approved title
merely for style.

## Suggestion
```
### نوع ثبت: پیشنهاد
### عنوان پیشنهاد / درخت دانش / کمیته تخصصی / بذر پیشنهاد /
### تاثیر اجرای پیشنهاد / همکاران / وضع موجود /
### پیشنهاد بهبود / نتایج حاصل از اجرای پیشنهاد / هشتگها / فایل پیوست
```
Present in logical order: Current State → Problem/Opportunity → Proposed
Improvement → Expected Impact → Implementation Status → Actual Results.
Include only what's actually available; keep expected benefits clearly
separated from actual results.

**تاثیر اجرای پیشنهاد is a two-value field.** Output exactly one of
**کیفی** or **کمی** (see `references/suggestion.md` §5 for the selection
rule — base it on the dominant effect in the document). Never write a
sentence in this field.

**نتایج حاصل از اجرای پیشنهاد is filled with the expected impact.** Since
a Suggestion has not been implemented, this field carries the expected
impact content with the explicit marker `(اثر مورد انتظار — تأیید نشده)`
appended. Never answer "Not Implemented," and never present expected
effects as confirmed actual results.

**DANA form fields only.** The draft must show exactly the DANA form
fields listed above — nothing more. Analysis-layer concepts used to build
the content (Problem/Gap/Opportunity, Implementation Logic, Evidence,
Risks, Transferability — see `references/suggestion.md` §3/§4) are
extraction aids only and must NOT appear as separate headings or fields
in the DANA draft. Fold their content into the closest form field
(e.g. Problem/Gap into «وضع موجود», Implementation Logic into
«پیشنهاد بهبود»).

## Explicit Knowledge
```
### نوع دانش / عنوان / شرح / درخت دانش /
### محدوده سازمانی / پروژه / هشتگها / فایل پیوست
```
Knowledge Type must be one of the nine organizational subtypes. Preserve
the classification produced upstream — this engine must not reclassify
the resource.

---

# 5. Resources, Hashtags, and Missing Fields

**Attachments:** list separately, preserving original filenames (e.g.
`1. filename.pdf`, `2. image.jpg`). Never claim a file "has been uploaded
to DANA" — use "Prepared for upload," not "Uploaded successfully."

**Image / Media:** for Lesson Learned use `Image: ...`; for video/audio
use `Primary Media: ...`. Preserve the media reference supplied by the
workflow — never claim successful upload.

**Hashtags:** display as a concise list (e.g. `#Quality #Welding
#Inspection`) representing the actual content — apply
`references/organizational-rules.md` §19.

---

# 6. Draft Formatting

The final draft should be structured, easy to review, easy to copy into
DANA, free of unnecessary explanation, clearly separated into fields, and
explicit about missing information. It's an operational artifact, not a
narrative explanation.

## Operator Review Checklist
Every draft ends with a checklist: Knowledge Type confirmed / Knowledge
Tree confirmed / Project confirmed / Organizational Scope confirmed /
Access Level confirmed / Colleagues confirmed / Content reviewed /
Attachments reviewed / Hashtags reviewed / QA issues resolved / Final
draft approved for DANA entry. Rendered in Persian per
`references/organizational-rules.md` §26:

```
چکلیست نهایی اپراتور
[ ] نوع دانش تأیید شد
[ ] درخت دانش تأیید شد
[ ] پروژه تأیید شد
[ ] محدوده سازمانی تأیید شد
[ ] سطح دسترسی تأیید شد
[ ] همکاران تأیید شدند
[ ] محتوا بازبینی شد
[ ] فایل پیوست بازبینی شد
[ ] هشتگها بازبینی شدند
[ ] مسائل QA حل شدند
[ ] پیشنویس نهایی برای ثبت در DANA تأیید شد
```

## Unresolved Items
List any remaining items, each explaining what the operator needs to
provide or verify.

---

# 7. Draft Integrity Check

Before returning the draft, verify: Knowledge Type matches QA output;
Title matches validated metadata; Project is unchanged; Knowledge Tree is
confirmed or clearly marked for operator selection; Access Level follows
`references/organizational-rules.md` §2; no unsupported claim was introduced; no
attachment was invented; no field was silently changed; QA status is
accurately represented; operator actions are clearly identified.

---

# 8. Output Contract

All labels below are rendered in Persian per `references/organizational-rules.md`
§26 (Output Language Policy). English technical terms remain unchanged.

```
# پیشنویس ثبت دانش در DANA
## اطلاعات ثبت
## محتوا
## فراداده
## منابع
## وضعیت QA
## بازبینی اپراتور الزامی است
## موارد حلنشده
## چکلیست نهایی اپراتور
```

---

# 9. Submission Boundary & Core Operating Principle

The DANA Draft Engine does NOT submit the record to DANA — it produces a
final human-reviewable draft; the operator enters/submits the final
information into DANA. Apply `references/organizational-rules.md` §21 (Human Review
Boundary) and §22 (Core Operating Principle). This engine's specific
sequence within that principle is:

Validated Knowledge → Validated Metadata → QA Gate → Select DANA
Registration Type → Map Fields → Preserve Validated Content → Mark Missing
Information → Generate Operator-Ready Draft → Human Review → DANA
Registration.

Never invent. Never silently correct. Never silently classify. Never
silently change metadata. Never claim submission success. The DANA Draft
Engine formats validated knowledge — it does not make organizational
decisions.
