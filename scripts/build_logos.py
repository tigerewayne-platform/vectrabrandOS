"""Generate Vectra Split V logo SVGs with outlined type.

Wordmark: lowercase "vectra" in Geist 700 with the descriptor ("shop" or "group") in Geist 300.
Needs Geist-700.ttf and Geist-300.ttf (static instances of the Geist variable font, made with
fontTools.varLib.instancer) and Manrope-700.ttf for banner lines. Usage: python3 scripts/build_logos.py <fontdir> brand/assets
PNGs are rendered from these SVGs with a headless browser.
"""
import sys, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONTDIR, OUT = sys.argv[1], sys.argv[2]
GB = TTFont(os.path.join(FONTDIR, "Geist-700.ttf"))
GL = TTFont(os.path.join(FONTDIR, "Geist-300.ttf"))
MANR = TTFont(os.path.join(FONTDIR, "Manrope-700.ttf"))

C = dict(graphite="#1B2330", copper="#E8641C", ink="#F2F4F7", copper_text="#B84A0D",
         copper_light="#F08A4B", blade_dim="#263142", white="#FFFFFF",
         slate="#5D6878", slate_light="#9AA5B3")

def text_path(font, text, size, tracking_em=0.0):
    """Return (svg path d, width, capheight) for text set at `size` px, baseline at y=0 (y down)."""
    upm = font["head"].unitsPerEm
    s = size / upm
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    pen = SVGPathPen(gs)
    x = 0.0
    names = [cmap[ord(ch)] for ch in text]
    for i, gn in enumerate(names):
        tp = TransformPen(pen, (s, 0, 0, -s, x, 0))
        gs[gn].draw(tp)
        adv = gs[gn].width * s
        x += adv + (tracking_em * size if i < len(names) - 1 else 0)
    cap = font["OS/2"].sCapHeight * s
    # exact ink width
    bp = BoundsPen(gs)
    return pen.getCommands(), x, cap

# Mark geometry: box x 6..94, y 12..88 in a 100 grid. Normalised to origin.
LEFT = [(6, 12), (29, 12), (50, 72), (50, 88)]
RIGHT = [(94, 12), (71, 12), (50, 72), (50, 88)]
MW, MH, MX0, MY0 = 88, 76, 6, 12

def mark(x, y, h, left, right):
    k = h / MH
    def pts(P):
        return " ".join(f"{(px-MX0)*k+x:.2f},{(py-MY0)*k+y:.2f}" for px, py in P)
    return (f'<polygon fill="{left}" points="{pts(LEFT)}"/>'
            f'<polygon fill="{right}" points="{pts(RIGHT)}"/>'), MW * k

def svg(w, h, body, bg=None, title="Vectra"):
    rect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" '
            f'width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}"><title>{title}</title>{rect}{body}</svg>\n')

def cap_size(font, cap):
    return cap / (font["OS/2"].sCapHeight / font["head"].unitsPerEm)

def words(desc, cap):
    """Paths for 'vectra' (bold) and the descriptor (light). Both set at the same size."""
    size = cap_size(GB, cap) * 1.18
    d_w, w_w, _ = text_path(GB, "vectra", size, -0.035)
    d_d, w_d, _ = text_path(GL, desc.lower(), size, -0.01)
    return d_w, w_w, d_d, w_d

def inline_group(word_fill, desc_fill, left, right, desc, x0=0, y0=0, cap=100):
    """One-line lockup: mark, 'vectra' and the descriptor on a shared baseline. Returns (body, width, height)."""
    d_w, w_w, d_d, w_d = words(desc, cap)
    mh = cap * 1.3
    mbody, mw = mark(x0, y0, mh, left, right)
    base = y0 + (mh + cap) / 2
    tx = x0 + mw + cap * 0.38
    dx = tx + w_w + cap * 0.22
    body = mbody
    body += f'<path fill="{word_fill}" transform="translate({tx:.2f},{base:.2f})" d="{d_w}"/>'
    body += f'<path fill="{desc_fill}" transform="translate({dx:.2f},{base:.2f})" d="{d_d}"/>'
    return body, (dx - x0) + w_d, mh

def lockup_group(word_fill, desc_fill, left, right, desc, x0=0, y0=0, cap=100, stacked=False):
    """Horizontal is the one-line lockup. Stacked puts the mark centred above the words."""
    if not stacked:
        return inline_group(word_fill, desc_fill, left, right, desc, x0, y0, cap)
    d_w, w_w, d_d, w_d = words(desc, cap)
    gap = cap * 0.22
    width = w_w + gap + w_d
    mh = cap * 1.9
    mw = MW * mh / MH
    mbody, _ = mark(x0 + (width - mw) / 2, y0, mh, left, right)
    base = y0 + mh + cap * 0.55 + cap * 1.18
    body = mbody
    body += f'<path fill="{word_fill}" transform="translate({x0:.2f},{base:.2f})" d="{d_w}"/>'
    body += f'<path fill="{desc_fill}" transform="translate({x0+w_w+gap:.2f},{base:.2f})" d="{d_d}"/>'
    return body, width, base - y0 + cap * 0.32

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(content)

P = 24  # padding (clear space) for lockup files, in px at cap=100

# ---- Marks
marks = {
    "vectra-mark-colour": (C["graphite"], C["copper"], None),
    "vectra-mark-reverse": (C["ink"], C["copper"], C["graphite"]),
    "vectra-mark-mono-graphite": (C["graphite"], C["graphite"], None),
    "vectra-mark-mono-white": (C["white"], C["white"], None),
    "vectra-mark-on-copper": (C["graphite"], C["white"], C["copper"]),
}
for name, (l, r, bg) in marks.items():
    pad = 12
    b, mw = mark(pad, pad, 152, l, r)
    write(f"{OUT}/logo/mark/{name}.svg", svg(mw + 2 * pad, 152 + 2 * pad, b, bg, "Vectra"))

# ---- Lockups
# Descriptor colour (light ground, dark ground): copper for the shop, slate for the company.
DESC = {"Shop": (C["copper_text"], C["copper_light"]), "Group": (C["slate"], C["slate_light"])}
for desc in ("Shop", "Group"):
    dl = desc.lower()
    for orient in ("horizontal", "stacked"):
        st = orient == "stacked"
        variants = {
            "colour": (C["graphite"], DESC[desc][0], C["graphite"], C["copper"], None),
            "reverse": (C["ink"], DESC[desc][1], C["ink"], C["copper"], C["graphite"]),
            "mono-graphite": (C["graphite"], C["graphite"], C["graphite"], C["graphite"], None),
            "mono-white": (C["white"], C["white"], C["white"], C["white"], None),
        }
        for vname, (wf, df, l, r, bg) in variants.items():
            body, w, h = lockup_group(wf, df, l, r, desc, P, P, 100, st)
            write(f"{OUT}/logo/lockup/vectra-{dl}-{orient}-{vname}.svg",
                  svg(w + 2 * P, h + 2 * P, body, bg, f"Vectra {desc}"))

# ---- Inline lockups (one line, for headers and tight bars)
for desc in ("Shop", "Group"):
    dl = desc.lower()
    variants = {
        "colour": (C["graphite"], DESC[desc][0], C["graphite"], C["copper"], None),
        "reverse": (C["ink"], DESC[desc][1], C["ink"], C["copper"], C["graphite"]),
        "mono-graphite": (C["graphite"], C["graphite"], C["graphite"], C["graphite"], None),
        "mono-white": (C["white"], C["white"], C["white"], C["white"], None),
    }
    for vname, (wf, df, l, r, bg) in variants.items():
        body, w, h = inline_group(wf, df, l, r, desc, P, P, 100)
        write(f"{OUT}/logo/lockup/vectra-{dl}-inline-{vname}.svg", svg(w + 2 * P, h + 2 * P, body, bg, f"Vectra {desc}"))

# ---- Favicon (transparent, full colour)
fh = 60 * MH / MW
write(f"{OUT}/logo/favicon/favicon.svg", svg(64, 64, mark(2, (64 - fh) / 2, fh, C["graphite"], C["copper"])[0], None, "Vectra"))
# app icon: graphite tile, reverse mark at 56% width
def app_icon(size):
    mw_t = size * 0.58
    mh_t = mw_t * MH / MW
    b, _ = mark((size - mw_t) / 2, (size - mh_t) / 2 + size * 0.02, mh_t, C["ink"], C["copper"])
    return svg(size, size, b, C["graphite"], "Vectra")
write(f"{OUT}/logo/favicon/app-icon.svg", app_icon(512))

# ---- Social profile (square, safe for circle crop: mark within 60% diameter)
def profile(size=1080):
    mw_t = size * 0.46
    mh_t = mw_t * MH / MW
    b, _ = mark((size - mw_t) / 2, (size - mh_t) / 2 + size * 0.015, mh_t, C["ink"], C["copper"])
    return svg(size, size, b, C["graphite"], "Vectra")
write(f"{OUT}/social/profile-1080.svg", profile())

# ---- Banners
BANNERS = {"linkedin-banner": (1584, 396), "facebook-cover": (1640, 624), "x-header": (1500, 500)}
TAG = {"Shop": "No surprises. Just tech.", "Group": "IT equipment supply for South African business."}
def banner(desc, w, h):
    body = ""
    # oversized mark bleeding off the right edge
    big_h = h * 1.3
    big_w = big_h * MW / MH
    b, bw = mark(w - big_w * 0.72, -h * 0.12, big_h, C["blade_dim"], C["copper"])
    body += b
    cap = h * 0.13
    lb, lw, lh = inline_group(C["ink"], DESC[desc][1], C["ink"], C["copper"], desc, 0, 0, cap)
    lx = w * 0.30 if w / h < 3.5 else w * 0.26
    ly = (h - lh) / 2 - h * 0.06
    body += f'<g transform="translate({lx:.2f},{ly:.2f})">{lb}</g>'
    tsize = cap * 0.42 / (MANR["OS/2"].sCapHeight / MANR["head"].unitsPerEm) * 0.72
    td, tw, _ = text_path(MANR, TAG[desc], tsize, 0.0)
    body += f'<path fill="#9AA5B3" transform="translate({lx:.2f},{ly+lh+cap*1.2:.2f})" d="{td}"/>'
    return svg(w, h, body, C["graphite"], f"Vectra {desc}")
for desc in ("Shop", "Group"):
    for key, (w, h) in BANNERS.items():
        write(f"{OUT}/social/vectra-{desc.lower()}-{key}-{w}x{h}.svg", banner(desc, w, h))
print("done")
