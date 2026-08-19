# -*- coding: utf-8 -*-
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display

FONT = "Tahoma"
pdfmetrics.registerFont(TTFont(FONT, r"C:\Windows\Fonts\tahoma.ttf"))
pdfmetrics.registerFont(TTFont(FONT + "-Bold", r"C:\Windows\Fonts\tahomabd.ttf"))


def fa(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


W = "white"

s_h1 = ParagraphStyle("h1", fontName=FONT + "-Bold", fontSize=15, leading=20,
                      alignment=1, textColor=colors.HexColor("#0b3d62"),
                      spaceAfter=6)
s_h2 = ParagraphStyle("h2", fontName=FONT + "-Bold", fontSize=11.5, leading=16,
                      alignment=2, textColor=colors.HexColor("#0b3d62"),
                      spaceBefore=10, spaceAfter=4)
s_h3 = ParagraphStyle("h3", fontName=FONT + "-Bold", fontSize=10.5, leading=14,
                      alignment=2, textColor=colors.HexColor("#333"),
                      spaceBefore=6, spaceAfter=2)
s_body = ParagraphStyle("body", fontName=FONT, fontSize=10.5, leading=16,
                        alignment=2, wordWrap="RTL", spaceAfter=3)
s_small = ParagraphStyle("small", fontName=FONT, fontSize=9, leading=13,
                         alignment=2, textColor=colors.HexColor("#555"))
s_cell = ParagraphStyle("cell", fontName=FONT, fontSize=9.5, leading=13,
                        alignment=2, wordWrap="RTL")
s_cellhead = ParagraphStyle("cellhead", fontName=FONT + "-Bold", fontSize=9.5,
                            leading=13, alignment=2, textColor=colors.HexColor("#0b3d62"))
s_li = ParagraphStyle("li", fontName=FONT, fontSize=10.5, leading=16,
                      alignment=2, wordWrap="RTL", leftIndent=10, spaceAfter=2)


def P(text, style):
    return Paragraph(fa(text), style)


def header_row(items):
    return [Paragraph(fa(x), s_cellhead) for x in items]


def make_table(rows, widths=None):
    t = Table(rows, colWidths=widths, hAlign="RIGHT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dce8f3")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#999")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


out_pdf = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\shaterian_m\Documents\Default Project\knowledge creation\پیش‌نویس DANA - پیشنهاد تغییر پوشش مخازن (راست‌چین).pdf"
doc = SimpleDocTemplate(
    out_pdf,
    pagesize=A4, rightMargin=18 * mm, leftMargin=18 * mm,
    topMargin=18 * mm, bottomMargin=18 * mm,
    title="پیش‌نویس ثبت دانش در DANA")

story = []
story.append(P("پیش‌نویس ثبت دانش در DANA", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#0b3d62"), spaceAfter=8))

story.append(P("اطلاعات ثبت", s_h2))
story.append(P("<b>نوع دانش:</b> پیشنهاد", s_body))
story.append(P("<b>وضعیت QA:</b> نیازمند بازبینی", s_body))
story.append(P("<b>بازبینی اپراتور:</b> الزامی", s_body))

story.append(P("محتوا", s_h2))
story.append(P("عنوان پیشنهاد", s_h3))
story.append(P("تغییر سیستم پوشش مخازن دفنی دیلوج و استوریج کولینگ کمکی از قیری داغ (Bituminous) به اپوکسی کولتار (Coal Tar Epoxy)", s_body))
story.append(P("وضعیت فعلی", s_h3))
story.append(P("طبق پروسیجر پروژه (MD1-TU-00-GN-W-00-PW2-003)، پوشش اصلی مخازن دفنی دیلوج و استوریج کولینگ کمکی (ACS) نیروگاه فردوسی از نوع قیری داغ است. این سیستم در شرایط فعلی پروژه با محدودیت‌های اجرایی، کمبود نیروی ماهر و تجهیزات مناسب مواجه است.", s_body))
story.append(P("بهبود پیشنهادی", s_h3))
story.append(P("جایگزینی پوشش قیری داغ با اپوکسی کولتار بدون حلال (Solvent-Free Coal Tar Epoxy)؛ نمونه پیشنهادی RTB-1319 شرکت روناس با مواد جامد ۹۵–۹۹٪، مقاومت بالا در برابر رطوبت/خاک/محیط قلیایی، اجرای ساده‌تر (Airless Spray، غلتک، قلم)، کنترل ضخامت دقیق‌تر و بدون نیاز به گرم‌کردن.", s_body))
story.append(P("اثر پیاده‌سازی (مورد انتظار)", s_h3))
story.append(P("افزایش دوام و عمر سرویس (۲۰–۳۰ سال در برابر ۵–۱۰ سال)، چسبندگی قوی‌تر، اجرای سریع‌تر و ایمن‌تر، کاهش هزینه نگهداری در طول عمر پروژه، کیفیت یکنواخت و کاهش آسیب در Backfilling. (اثر مورد انتظار — هنوز تأیید نشده)", s_body))
story.append(P("نتایج پیاده‌سازی", s_h3))
story.append(P("ارائه نشده (پیاده‌سازی نشده است)", s_body))

story.append(P("فراداده", s_h2))
meta_rows = [
    header_row(["فیلد", "مقدار"]),
    [P("شجره دانش", s_cell), P("[پیشنهادی] Design and Engineering &gt; Process Engineering &gt; Painting and Coating — ورودی اپراتور الزامی", s_cell)],
    [P("کمیته تخصصی", s_cell), P("کمیته پیشنهادات مدیریت پروژه — ورودی اپراتور الزامی", s_cell)],
    [P("بذر پیشنهاد", s_cell), P("[اختیاری - ارائه نشده]", s_cell)],
    [P("اثر پیاده‌سازی", s_cell), P("مطابق بخش محتوا (اثر مورد انتظار)", s_cell)],
    [P("همکاران", s_cell), P("[اختیاری - ارائه نشده]", s_cell)],
    [P("سطح دسترسی", s_cell), P("عادی", s_cell)],
    [P("هشتگ‌ها", s_cell), P("#CoalTarEpoxy #پوشش_ضدخوردگی #مخازن_دفنی #Painting_Coating", s_cell)],
]
story.append(make_table(meta_rows, widths=[35 * mm, 139 * mm]))

story.append(P("منابع", s_h2))
story.append(P("<b>پیوست‌ها (آماده برای بارگذاری، نه بارگذاری‌شده):</b>", s_body))
story.append(P("۱. پیشنهاد تغییر سیستم پوشش مخازن دفنی دیلوج و استوریج کولینگ کمکی.pdf", s_li))
story.append(P("۲. پیشنهاد تغییر سیستم پوشش مخازن دفنی دیلوج و استوریج کولینگ کمکی.docx", s_li))

story.append(P("وضعیت QA", s_h2))
story.append(P("نیازمند بازبینی — بدون مسئله حیاتی؛ نیاز به تأیید شجره دانش، پروژه، ادعاهای فنی و کمیته.", s_body))

story.append(P("بازبینی اپراتور الزامی است", s_h2))
story.append(P("بله — موارد زیر نیازمند بازبینی/تأیید است: شجره دانش، پروژه، اعتبار ادعاهای فنی محصول، کمیته.", s_body))

story.append(P("موارد حل‌نشده", s_h2))
for item in [
    "انتخاب و تأیید نهایی شجره دانش (پیشنهادی: Painting and Coating).",
    "تأیید نام رسمی پروژه (نیروگاه فردوسی/TOUS، قرارداد 3600/19).",
    "تأیید منبع ادعاهای فنی (تأییدیه NACE/API/ISO و پژوهشگاه پلیمر و پتروشیمی ایران).",
    "تأیید کمیته پیشنهادات و بذر پیشنهاد.",
    "[اصلاح احتمالی] قالب شماره مستند مرجع: «MD1-TU-00-GN-W-00-PW2-003» در برابر «MD1/TU-00-GN-W-00-PW2-003» — تأیید اپراتور الزامی است.",
]:
    story.append(P("• " + item, s_li))

story.append(P("چک‌لیست نهایی اپراتور", s_h2))
cl_rows = [header_row(["مورد", "وضعیت"])] + [
    [P(x, s_cell), P("☐", s_cell)] for x in [
        "نوع دانش تأیید شد (پیشنهاد)",
        "شجره دانش تأیید شد",
        "پروژه تأیید شد",
        "محدوده سازمانی تأیید شد",
        "سطح دسترسی تأیید شد",
        "همکاران تأیید شدند",
        "محتوا بازبینی شد",
        "پیوست‌ها بازبینی شدند",
        "هشتگ‌ها بازبینی شدند",
        "مسائل QA حل شدند",
        "پیش‌نویس نهایی برای ثبت در DANA تأیید شد",
    ]
]
story.append(make_table(cl_rows, widths=[120 * mm, 54 * mm]))

story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#ccc"), spaceAfter=6))
story.append(P("تولید شده توسط organizational-knowledge-skill — پیش‌نویس برای بازبینی و تأیید انسانی؛ ثبت نهایی در DANA بر عهده اپراتور است.", s_small))

doc.build(story)
print("OK")