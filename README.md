# Organizational Knowledge Skill

مهارت مدیریت دانش سازمانی برای ثبت در سیستم مدیریت دانش **DANA** — ارکستراتور + موتورها + مراجع + خروجی PDF/Word راست‌چین.

## ساختار

```
├── SKILL.md                       ← ارکستراتور (ترتیب اجرای موتورها)
├── references/
│   ├── organizational-rules.md    ← قوانین مشترک سازمانی (۲۵ قاعده) + واژه‌نامه برچسب‌ها
│   ├── common-knowledge-object.md ← ساختار داده مشترک (CKO) + قرارداد موتورها
│   ├── knowledge-classification.md ← موتور طبقه‌بندی دانش
│   ├── lesson-learned.md           ← موتور تجربه
│   ├── suggestion.md               ← موتور پیشنهاد
│   ├── explicit-knowledge.md       ← موتور دانش صریح
│   ├── metadata.md                 ← موتور متادیتا
│   ├── quality-assurance.md        ← موتور تضمین کیفیت
│   ├── dana-draft.md               ← موتور پیشنویس DANA (فقط فیلدهای واقعی فرم)
│   ├── knowledge-tree.md           ← درخت دانش رسمی (MAPNA)
│   └── output-rendering.md         ← قوانین خروجی راست‌چین (PDF/Word، RTL/bidi، جداول)
├── scripts/
│   ├── make_dana_pdf.py            ← تولید PDF راست‌چین (reportlab)
│   └── make_dana_docx.py           ← تولید Word راست‌چین (python-docx، run-level RTL)
└── KNOWLEDGE_REGISTRATION_DESIGN.md ← سند طراحی ثبت دانش از WelderBot (Rev 0)
```

## پایپلاین

```
ورودی خام → طبقه‌بندی → موتور محتوا (تجربه/پیشنهاد/دانش صریح)
→ متادیتا → تضمین کیفیت → پیشنویس DANA → بازبینی انسانی → ثبت نهایی
```

## نصب در Hermes

مهارت در `~/.hermes/skills/knowledge-management/organizational-knowledge-skill/` نصب است (نسخهٔ 2.2.0).

## نکات نسخه 2.2.0

- پیشنویس DANA فقط فیلدهای واقعی فرم را نمایش می‌دهد؛ مفاهیم لایه تحلیل
  (مشکل/شکاف/فرصت، منطق پیاده‌سازی، شواهد، ریسک‌ها، قابلیت انتقال) فقط برای
  استخراج‌اند و در نزدیک‌ترین فیلد فرم ادغام می‌شوند (ببینید `references/suggestion.md` §15).
- واژه‌نامه فارسی تأییدشدهٔ اپراتور: عنوان پیشنهاد، درخت دانش، کمیته تخصصی،
  بذر پیشنهاد، تاثیر اجرای پیشنهاد، همکاران، وضع موجود، پیشنهاد بهبود،
  نتایج حاصل از اجرای پیشنهاد، هشتگ‌ها، فایل پیوست.

---

**نسخه:** 2.2.0 · **مجوز:** MIT
