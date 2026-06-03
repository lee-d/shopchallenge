from fpdf import FPDF
import math

OUTPUT = "ShopChallenge.pdf"

# ── Palette ───────────────────────────────────────────────────────────────────
BLUE_DARK  = (160,  35,  10)   # deep burnt-orange  #a0230a
BLUE_MID   = (255,  82,  41)   # main colour        #ff5229
BLUE_LIGHT = (255, 230, 222)   # light tint         #ffe6de
ACCENT     = (251, 191,  36)   # amber / "gold"
WHITE      = (255, 255, 255)
GRAY_DARK  = ( 31,  41,  55)
GRAY_MID   = (107, 114, 128)
GRAY_LIGHT = (243, 244, 246)
RED_SOFT   = (220,  38,  38)
GREEN_SOFT = ( 21, 128,  61)


# ── Helper: draw a rounded rectangle ─────────────────────────────────────────
def rounded_rect(pdf, x, y, w, h, r, style="F"):
    k = pdf.k
    hp = pdf.h
    pdf._out(
        f"{(x + r) * k:.2f} {(hp - y) * k:.2f} m "
        f"{(x + w - r) * k:.2f} {(hp - y) * k:.2f} l "
        f"{(x + w) * k:.2f} {(hp - y) * k:.2f} {(x + w) * k:.2f} {(hp - y - r) * k:.2f} v "
        f"{(x + w) * k:.2f} {(hp - y - h + r) * k:.2f} l "
        f"{(x + w) * k:.2f} {(hp - y - h) * k:.2f} {(x + w - r) * k:.2f} {(hp - y - h) * k:.2f} v "
        f"{(x + r) * k:.2f} {(hp - y - h) * k:.2f} l "
        f"{x * k:.2f} {(hp - y - h) * k:.2f} {x * k:.2f} {(hp - y - h + r) * k:.2f} v "
        f"{x * k:.2f} {(hp - y - r) * k:.2f} l "
        f"{x * k:.2f} {(hp - y) * k:.2f} {(x + r) * k:.2f} {(hp - y) * k:.2f} v "
        f"{'f' if style == 'F' else 'S'}"
    )


# ── Draw a simple shopping-cart logo using basic shapes ──────────────────────
def draw_cart_logo(pdf, cx, cy, size=14):
    """Draw a tiny vector shopping cart centred at (cx, cy)."""
    lw = size / 14

    # body trapezoid  (simplified as rectangle)
    bx, by = cx - size * 0.55, cy - size * 0.1
    bw, bh = size * 1.1, size * 0.6
    pdf.set_fill_color(*WHITE)
    pdf.rect(bx, by, bw, bh, "F")

    # handle bar
    pdf.set_draw_color(*WHITE)
    pdf.set_line_width(lw * 1.8)
    pdf.line(cx - size * 0.9, cy - size * 0.55, cx - size * 0.55, cy - size * 0.1)

    # front vertical
    pdf.line(cx + size * 0.55, by, cx + size * 0.55, by + bh)

    # wheels
    pdf.set_fill_color(*WHITE)
    r = size * 0.12
    pdf.ellipse(cx - size * 0.30, by + bh - r, r * 2, r * 2, "F")
    pdf.ellipse(cx + size * 0.30, by + bh - r, r * 2, r * 2, "F")


FONT_DIR = r"C:\Windows\Fonts"

class PDF(FPDF):
    def footer(self):
        self.set_y(-13)
        self.set_font("Body", "", 8)
        self.set_text_color(*GRAY_MID)
        self.cell(0, 8, f"Seite {self.page_no()}", align="C")


# ── Build the document ────────────────────────────────────────────────────────
pdf = PDF(format="A4")
pdf.set_auto_page_break(auto=True, margin=18)

# Register Unicode-capable fonts so umlauts and typographic characters work
pdf.add_font("Body",  "",  rf"{FONT_DIR}\arial.ttf",    uni=True)
pdf.add_font("Body",  "B", rf"{FONT_DIR}\arialbd.ttf",  uni=True)
pdf.add_font("Body",  "I", rf"{FONT_DIR}\ariali.ttf",   uni=True)
pdf.add_font("Body",  "BI",rf"{FONT_DIR}\arialbi.ttf",  uni=True)
pdf.add_font("Mono",  "",  rf"{FONT_DIR}\cour.ttf",     uni=True)
pdf.add_font("Mono",  "B", rf"{FONT_DIR}\courbd.ttf",   uni=True)
pdf.add_page()

PAGE_W = pdf.w
MARGIN = 18
CONTENT_W = PAGE_W - 2 * MARGIN

# ════════════════════════════════════════════════════════════════════════════
# HERO HEADER
# ════════════════════════════════════════════════════════════════════════════
HEADER_H = 52
# dark blue background
pdf.set_fill_color(*BLUE_DARK)
pdf.rect(0, 0, PAGE_W, HEADER_H, "F")

# subtle diagonal accent stripe
pdf.set_fill_color(*BLUE_MID)
for i in range(8):
    stripe_x = PAGE_W - 60 + i * 14
    # thin parallelogram via two triangles (approximated as thin rects rotated)
    # We'll just draw thin vertical bars fading to right as a decorative touch
    pdf.set_fill_color(37 + i * 3, 99 + i * 4, 235)
    pdf.rect(stripe_x, 0, 8, HEADER_H, "F")

# amber top accent line
pdf.set_fill_color(*ACCENT)
pdf.rect(0, 0, PAGE_W, 3.5, "F")

# ── Cart icon on the left ────────────────────────────────────────────────────
ICON_BG_SIZE = 30
icon_x = MARGIN
icon_y = (HEADER_H - ICON_BG_SIZE) / 2
pdf.set_fill_color(*BLUE_MID)
rounded_rect(pdf, icon_x, icon_y, ICON_BG_SIZE, ICON_BG_SIZE, 6, "F")
draw_cart_logo(pdf, icon_x + ICON_BG_SIZE / 2, icon_y + ICON_BG_SIZE / 2, 13)

# ── Title text ───────────────────────────────────────────────────────────────
text_x = icon_x + ICON_BG_SIZE + 8
pdf.set_text_color(*WHITE)
pdf.set_font("Body", "B", 26)
pdf.set_xy(text_x, 11)
pdf.cell(0, 10, "ShopChallenge")
pdf.ln(10)

pdf.set_font("Body", "", 11)
pdf.set_text_color(*ACCENT)
pdf.set_x(text_x)
pdf.cell(0, 7, "Coding Challenge  -  REST API  -  Spring Boot")
pdf.ln(7)

# ════════════════════════════════════════════════════════════════════════════
# SECTION HELPER
# ════════════════════════════════════════════════════════════════════════════
def section_title(pdf, text, emoji=""):
    pdf.ln(7)
    pdf.set_fill_color(*BLUE_LIGHT)
    pdf.set_draw_color(*BLUE_MID)
    pdf.set_line_width(0)
    y = pdf.get_y()
    pdf.set_fill_color(*BLUE_LIGHT)
    rounded_rect(pdf, MARGIN, y, CONTENT_W, 9, 3, "F")
    pdf.set_draw_color(*BLUE_MID)
    pdf.set_line_width(0.8)
    pdf.line(MARGIN, y + 9, MARGIN + CONTENT_W, y + 9)
    pdf.set_line_width(0.2)
    pdf.set_font("Body", "B", 12)
    pdf.set_text_color(*BLUE_DARK)
    pdf.set_xy(MARGIN + 3, y + 0.8)
    # no emoji prefix – just the text
    pdf.cell(CONTENT_W - 3, 8, text)
    pdf.ln(10)
    pdf.set_text_color(*GRAY_DARK)


def body_text(pdf, text, indent=0, line_height=6):
    pdf.set_font("Body", "", 10)
    pdf.set_text_color(*GRAY_DARK)
    pdf.set_x(MARGIN + indent)
    pdf.multi_cell(CONTENT_W - indent, line_height, text)
    pdf.ln(1)


def bullet(pdf, text, indent=5):
    pdf.set_font("Body", "", 10)
    pdf.set_text_color(*GRAY_DARK)
    x = MARGIN + indent
    pdf.set_xy(x, pdf.get_y())
    pdf.cell(5, 6, "-")
    pdf.set_x(x + 5)
    pdf.multi_cell(CONTENT_W - indent - 5, 6, text)


def endpoint_row(pdf, method, path, description):
    colors = {"GET": (21, 128, 61), "POST": (37, 99, 235), "DELETE": (220, 38, 38)}
    col = colors.get(method, GRAY_MID)
    y = pdf.get_y()
    # method badge
    m_w = 18
    pdf.set_fill_color(*col)
    rounded_rect(pdf, MARGIN + 3, y + 1, m_w, 6, 2, "F")
    pdf.set_font("Body", "B", 7.5)
    pdf.set_text_color(*WHITE)
    pdf.set_xy(MARGIN + 3, y + 0.8)
    pdf.cell(m_w, 6.5, method, align="C")
    # path
    pdf.set_font("Mono", "B", 9)
    pdf.set_text_color(*BLUE_DARK)
    pdf.set_xy(MARGIN + 24, y + 1)
    pdf.cell(60, 6, path)
    # description
    pdf.set_font("Body", "", 9)
    pdf.set_text_color(*GRAY_DARK)
    pdf.set_xy(MARGIN + 86, y + 1)
    pdf.multi_cell(CONTENT_W - 86, 6, description)
    pdf.ln(1)


def code_block(pdf, lines):
    """Render a dark code-block box."""
    pdf.set_fill_color(30, 41, 59)   # slate-800
    padding = 4
    line_h = 5.5
    block_h = len(lines) * line_h + padding * 2
    x0, y0 = MARGIN, pdf.get_y()
    rounded_rect(pdf, x0, y0, CONTENT_W, block_h, 4, "F")
    pdf.set_font("Mono", "", 8.5)
    for i, line in enumerate(lines):
        pdf.set_xy(x0 + padding + 1, y0 + padding + i * line_h)
        # simple syntax colouring: keywords in amber
        pdf.set_text_color(*ACCENT)
        pdf.cell(CONTENT_W - padding * 2, line_h, line)
    pdf.ln(block_h + 2)
    pdf.set_text_color(*GRAY_DARK)


def bug_card(pdf, number, title, description):
    """Draw a clearly visible bug card."""
    card_x = MARGIN
    card_y = pdf.get_y()

    pdf.set_fill_color(*RED_SOFT)
    pdf.rect(card_x, card_y, 3, 60, "F")

    inner_x = card_x + 7
    inner_w = CONTENT_W - 7

    badge_label = f"Bug #{number}"
    pdf.set_fill_color(*RED_SOFT)
    rounded_rect(pdf, inner_x, card_y + 2, 24, 7, 2.5, "F")
    pdf.set_font("Body", "B", 8)
    pdf.set_text_color(*WHITE)
    pdf.set_xy(inner_x, card_y + 2.5)
    pdf.cell(24, 6, badge_label, align="C")

    pdf.set_font("Body", "B", 11)
    pdf.set_text_color(*RED_SOFT)
    pdf.set_xy(inner_x + 28, card_y + 2)
    pdf.cell(inner_w - 28, 7, title)

    pdf.set_xy(inner_x, card_y + 12)

    pdf.set_font("Body", "", 9.5)
    pdf.set_text_color(*GRAY_DARK)
    pdf.set_x(inner_x)
    pdf.multi_cell(inner_w, 5.5, description)
    pdf.ln(3)

    card_h = pdf.get_y() - card_y
    pdf.set_fill_color(*RED_SOFT)
    pdf.rect(card_x, card_y, 3, card_h, "F")
    pdf.ln(3)


# ════════════════════════════════════════════════════════════════════════════
# SECTION 1 – EINFÜHRUNG
# ════════════════════════════════════════════════════════════════════════════
pdf.set_y(HEADER_H + 6)

section_title(pdf, "Einfuehrung")

body_text(pdf,
    "Willkommen zur ShopChallenge! Diese Aufgabe dreht sich um eine REST-API, "
    "die einen kleinen Online-Shop simuliert. Die API bietet einen Produktkatalog "
    "an, aus dem Kunden Artikel auswählen und in einem persönlichen Warenkorb "
    "sammeln können.")

body_text(pdf,
    "Jeder Warenkorb wird über eine eindeutige UUID identifiziert und speichert "
    "alle hinzugefügten Produkte samt ihrer Menge. Für jede Position im Warenkorb "
    "werden folgende Informationen ausgewiesen:")

for item in [
    "Produktname und Produkt-ID",
    "Nettopreis pro Einheit",
    "Bruttopreis pro Einheit (Nettopreis zzgl. 19 % MwSt.)",
    "Gesamtnettobetrag der Position (Nettopreis x Menge)",
    "Gesamtbruttobetrag der Position (Bruttopreis x Menge)",
]:
    bullet(pdf, item)

pdf.ln(2)
body_text(pdf,
    "Am Ende gibt der Warenkorb außerdem den summierten Gesamtnettobetrag sowie "
    "den Gesamtbruttobetrag aller Positionen aus. Die Dokumentation der API ist "
    "direkt über Swagger UI erreichbar und erlaubt es, alle Endpunkte interaktiv "
    "auszuprobieren.")

# ════════════════════════════════════════════════════════════════════════════
# SECTION 2 – ENDPUNKTE
# ════════════════════════════════════════════════════════════════════════════
section_title(pdf, "Verfuegbare Endpunkte")

endpoint_row(pdf, "GET",  "/products",
             "Gibt alle Produkte des Katalogs zurück (ID, Name, Nettopreis).")
endpoint_row(pdf, "GET",  "/baskets/{id}",
             "Gibt den Warenkorb mit der angegebenen UUID zurück – inklusive "
             "aller Positionen und dem Gesamt-Netto- sowie Bruttopreis.")
endpoint_row(pdf, "POST", "/baskets/{id}/items",
             "Fügt ein Produkt (productId + quantity) zum Warenkorb hinzu. "
             "Existiert der Warenkorb noch nicht, wird er automatisch angelegt.")
endpoint_row(pdf, "GET",  "/swagger-ui.html",
             "Interaktive API-Dokumentation via Swagger UI.")

pdf.ln(2)
body_text(pdf,
    "Zum Einstieg steht ein vorbefüllter Test-Warenkorb bereit. Er enthält "
    "bereits drei Artikel und kann direkt abgerufen werden:")

code_block(pdf, [
    "GET /baskets/00000000-0000-0000-0000-000000000001",
])

# ════════════════════════════════════════════════════════════════════════════
# SECTION 3 – AUFGABE / BUGS
# ════════════════════════════════════════════════════════════════════════════
section_title(pdf, "Aufgabe - Fehler finden & beheben")

body_text(pdf,
    "Bei der Implementierung der API haben sich zwei Fehler eingeschlichen. "
    "Deine Aufgabe besteht darin, beide Fehler zu finden und zu korrigieren.")

pdf.ln(3)

# ── Bug 1 ────────────────────────────────────────────────────────────────────
bug_card(
    pdf,
    number=1,
    title="Mengenakkumulation im Warenkorb",
    description=(
        "Wird dasselbe Produkt mehrfach dem Warenkorb hinzugefügt, sollte sich "
        "die Gesamtmenge entsprechend erhöhen. Jedoch verhält sich die Schnittstelle anders."
    ),
)

# ── Bug 2 ────────────────────────────────────────────────────────────────────
bug_card(
    pdf,
    number=2,
    title="Falscher Gesamtbruttobetrag",
    description=(
        "Der angezeigte Bruttopreis pro Einheit sowie der Gesamtbruttobetrag "
        "des Warenkorbs sind nicht korrekt. Für ein Produkt mit einem Nettopreis "
        "von 100,00 EUR sollte der Bruttopreis (inkl. 19 % MwSt.) "
        "119,00 EUR betragen – der tatsächlich ausgewiesene Wert weicht jedoch "
        "deutlich davon ab."
    ),
)

# ════════════════════════════════════════════════════════════════════════════
# Footer strip
# ════════════════════════════════════════════════════════════════════════════
pdf.set_fill_color(*BLUE_DARK)
pdf.rect(0, pdf.h - 10, PAGE_W, 10, "F")
pdf.set_fill_color(*ACCENT)
pdf.rect(0, pdf.h - 10, PAGE_W, 1.5, "F")

# ── Output ───────────────────────────────────────────────────────────────────
pdf.output(OUTPUT)
print(f"PDF erstellt: {OUTPUT}")
