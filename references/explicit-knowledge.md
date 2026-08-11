# EXPLICIT KNOWLEDGE ENGINE

> This engine follows all shared standards defined in
> `references/organizational-rules.md` and the data contract in
> `references/common-knowledge-object.md` §9. Only logic specific to
> Explicit Knowledge is defined below — do not restate shared rules here.

## 1. Mission

Transform an existing explicit knowledge resource (document, media, or
URL) into a structured, accurate, searchable, registration-ready
organizational knowledge record: recognize its nature, select the correct
Explicit Knowledge subtype, extract its useful information, and prepare a
registration draft.

The engine is domain-agnostic (Project Management, Engineering, Quality,
HSE, Procurement, Contracts, Finance, HR, IT, Construction, Maintenance,
Operations, Commercial, Research, and other functions).

---

# 2. Organizational Explicit Knowledge Types

The organizational system currently provides these registration
categories — use them exactly; do not invent additional official types:

1. Book · 2. Training Content · 3. Link · 4. International Report ·
5. Podcast · 6. Invention · 7. Magazine · 8. Article · 9. Standard

---

# 3. Core Objective

The objective is NOT to summarize the resource — it is to answer: what is
this resource; which type best represents it; what is its subject; what
useful knowledge does it contain; who may benefit; what organizational
context does it relate to; what metadata is reliably extractable; what's
missing; how should it be registered.

(Apply the Source-of-Truth Principle and non-fabrication rules from
`references/organizational-rules.md` §6. Non-fabrication here specifically covers:
authors, publication dates, publishers, standard numbers, report
organizations, URLs, edition numbers, ISBNs, technical claims,
conclusions, credentials, citations.)

---

# 4. Classification Principle

Classification is based on the semantic nature and primary purpose of the
resource, **not** its file format. A PDF may be a Book, Article, Standard,
International Report, or Training Content depending on content and
purpose; an MP3 may be a Podcast or Training Content; a URL may point to
any of these. **File format ≠ Knowledge Type.**

## Classification Priority
When multiple categories seem plausible: identify the primary nature →
original purpose → publishing/organizational form → intended use → use
available metadata → compare candidates → select the strongest-evidence
category. If it remains ambiguous, do NOT force a classification — return
Primary Candidate / Alternative Candidate / Reason / Operator Confirmation
Required: Yes.

## Classification Confidence
For every classification: High (strong direct evidence), Medium (probable,
some ambiguity), Low (tentative, confirmation recommended).

## Multiple-Type Conflict
When a resource plausibly fits multiple categories (e.g. a training
organization's technical report also used in training), determine the
primary organizational nature: Primary Type / Secondary Characteristics.
Do not register under multiple categories unless explicitly requested.

---

# 5. Type Definitions

For each type below, evidence supports the classification but is not by
itself sufficient — the resource's actual purpose governs.

**Book** — a substantive book/book-like publication. Evidence: title,
author(s), publisher, edition, ISBN, table of contents, chapter structure,
cover, publication metadata. Length alone does not make something a Book.

**Training Content** — primary purpose is teaching/training/structured
learning (manuals, presentations, educational modules, course materials,
learning packages, instructional documents, educational video/audio).
Containing educational information isn't enough — the *primary* purpose
must be learning/training.

**Link** — the principal asset being registered is a URL itself. Inspect
the destination when possible; the description should explain what it
contains and why it's useful. Don't default every webpage to "Link" if the
content itself should be Article/Standard/Training Content etc. — but
preserve Link when it's the organization's deliberate registration choice.

**International Report** — a report from an international organization,
institution, or research body, with a reporting/analysis/assessment
purpose. Evidence: report title, issuing organization, publication
metadata, report number, executive summary, methodology, international
scope. Foreign origin alone is insufficient.

**Podcast** — an episodic/published audio program for podcast-style
consumption. Evidence: episode title, series, host, episode number,
publication date, platform, audio format. An arbitrary recording isn't
automatically a Podcast — training audio may instead be Training Content.

**Article** — a published article (technical, research, professional, or
similar standalone written piece). Evidence: title, author, journal/
publication, date, abstract, keywords, DOI, volume/issue, references. Not
every short document is an Article.

**Invention** — explicitly relates to an invention/IP asset. Evidence:
patent info, inventor, patent number, invention title, technical
description, novel mechanism, IP documentation. An innovative-sounding
Suggestion is not automatically an Invention.

**Magazine** — a magazine/periodical/multi-article publication. Evidence:
title, issue number, volume, date, editorial structure, multiple articles,
cover. A single article extracted from a magazine is normally Article, not
Magazine.

**Standard** — an actual formal standard, specification, code, or
normative document. Evidence: standard organization, designation, number,
edition/revision, official title, normative structure, scope,
requirements. Containing technical requirements is not enough — the
document itself must be a standard or equivalent.

---

# 6. Content Understanding & Value Extraction

After classification, identify: main subject, main purpose, key topics,
main conclusions/findings, practical applications, relevant organizational
functions, target audience (when identifiable). Avoid a generic summary
that ignores the resource's actual purpose.

Identify what makes it useful as organizational knowledge — one or more
of: technical reference, training resource, process guidance, industry
insight, regulatory guidance, standardization, research, benchmarking,
strategic insight, professional development, innovation, operational
support.

## Summary Principle
The description should not reproduce the resource — it should let an
employee understand "what is this?" and "why should I care?", faithfully
to the source, without adding unsupported recommendations.

## Technical Accuracy
Apply `references/organizational-rules.md` §9 (Preserve Technical Meaning) —
including formulas when relevant.

---

# 7. Metadata Extraction & Verification

Extract metadata only when explicitly available: title, author,
organization, publisher, publication date, edition, version, ISBN, DOI,
standard number, report number, issue number, volume, URL, language, file
type, subject, keywords.

Distinguish **Confirmed Metadata** from **Inferred Metadata** (e.g.
Author: "John Smith" — Confirmed; Publisher: "Unknown" rather than
inferring from visual branding unless sufficiently clear). If metadata
conflicts between the file and user-provided information, flag the
conflict.

## Organizational Fields
Current form: Title, Description, Knowledge Tree, Organizational
Scope/Department, Project, Hashtags, Attachment. Prepare these when
information is available.

## Knowledge Tree
Apply `references/organizational-rules.md` §4. Distinguish "Recommended Knowledge
Tree" from "officially confirmed Knowledge Tree" — if the official
taxonomy isn't available, use "Requires operator selection."

## Organizational Scope
Identify the relevant unit/functional area only when explicitly supported
(e.g. Project Management, Engineering, Quality, HSE, Procurement,
Contracts, IT). Do not infer a precise unit merely from technical
relevance — use "Recommended scope: ..." when it's an inference.

## Project
Identify only if explicitly related. If no project relationship: "Not
specified / General." Do not assign a project based solely on department.

## Hashtags
Apply `references/organizational-rules.md` §19.

---

# 8. Resource Handling

## Attachment vs URL
If supplied as a file, record it as an attachment. If supplied as a URL,
record the URL as the primary resource. If both exist, determine the
primary knowledge asset — do not discard supporting attachments.

## External Resource Handling
When a URL is supplied and access is available: access the resource,
verify the destination, identify the resource type, extract available
metadata, summarize relevant content, generate the draft. If it cannot be
accessed, do not invent its contents — return "External Resource Status:
Unavailable for verification" and request the resource/content from the
user if necessary.

## Copyright and Content Preservation
Summarize copyrighted resources rather than reproducing large portions.
Do not reproduce entire books, articles, reports, or other protected
content — extract only what's necessary for classification and
registration.

## Duplicate Awareness
Apply `references/organizational-rules.md` §15. Without access to existing records,
do NOT claim a resource is unique — use "Duplicate status cannot be
determined from the available information."

---

# 9. Quality Assessment

Before the final draft, verify: classification is supported; main subject
correctly identified; metadata fields are evidence-backed; organizational
relevance is clear; another employee can understand the resource's value
from the description; unsupported claims avoided; critical registration
fields are available.

---

# 10. Missing Information

Classify and ask per `references/organizational-rules.md` §16–17. Critical examples
specific to this engine: resource identity, resource type, primary URL
(when Link is selected), basic title. Important examples: author,
publication date, organizational relevance, Knowledge Tree.

---

# 11. Registration Draft & Type-Specific Metadata

Generic draft structure: Knowledge Type / Title / Description / Knowledge
Tree / Organizational Scope / Project / Hashtags / Attachment or URL. The
selected subtype must be clearly identified.

Preserve subtype-specific metadata where useful, only when supported by
the source:

- **Book:** Author, Publisher, Edition, ISBN
- **Article:** Author, Publication, Date, DOI
- **Standard:** Standard Organization, Standard Number, Edition/Revision
- **International Report:** Issuing Organization, Report Date, Report Number
- **Magazine:** Magazine, Issue, Volume, Date
- **Podcast:** Podcast, Episode, Host, Date, URL
- **Training Content:** Course/Training Name, Provider, Instructor, Date
- **Invention:** Inventor, Patent/Registration Number, relevant IP info
- **Link:** URL, Website/Resource Name

---

# 12. Output Contract

## A. Classification
Knowledge Type: / Confidence: High / Medium / Low / Alternative Type: /
Reason: / Operator Confirmation Required: Yes / No

## B. Resource Identification
Title: / Author or Creator: / Organization or Publisher: / Publication
Date: / Edition or Version: / Identifier: / URL:

## C. Knowledge Extraction
Main Subject: / Purpose: / Key Topics: / Main Findings or Conclusions: /
Practical Value: / Organizational Relevance:

## D. Organizational Metadata
Knowledge Tree: / Organizational Scope: / Project: / Access Level: Normal
/ Confidential / Highly Confidential / Hashtags: / Attachments:

## E. Missing Information
Critical: / Important: / Optional:

## F. DANA Draft
Knowledge Type / Title / Description / Knowledge Tree / Organizational
Scope / Project / Hashtags / Attachment or URL

## G. Quality Review
Classification Confidence: / Content Understanding: / Metadata
Completeness: / Organizational Relevance: / Potential Duplication: /
Information Gaps:

---

# 13. Human Review Boundary & Core Operating Principle

Apply `references/organizational-rules.md` §21 (Human Review Boundary) and §22 (Core
Operating Principle). This engine's specific sequence within that
principle is:

Identify Resource → Understand Resource → Classify Knowledge Type →
Extract Metadata → Extract Knowledge Value → Map Organizational Metadata →
Identify Missing Information → Write Registration Draft → Quality Check.

Engine-specific guardrails (in addition to the shared principle): never
classify solely from file extension; never confuse file format with
knowledge type; never confuse a Suggestion with an Invention; never
confuse an educational resource with Training Content without evidence;
never confuse a technical document with a Standard without evidence; never
classify a foreign document as International Report solely due to origin.
