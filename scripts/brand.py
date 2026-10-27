"""Brand tokens and SVG primitives shared by build_assets.py and telemetry.py.

Palette and type follow the Gich AI Nexus website. SVGs rendered through
<img> cannot load web fonts, so each stack falls back to system faces.
"""

from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"

SANS = "'Host Grotesk','Georama','Segoe UI',Helvetica,Arial,sans-serif"
MONO = "'Fira Code','JetBrains Mono',SFMono-Regular,Consolas,monospace"

THEMES = {
    "dark": {
        "bg": "#0b1222",
        "panel": "#0f172a",
        "panel2": "#131d33",
        "line": "#1e293b",
        "grid": "#e85d04",
        "grid_op": "0.07",
        "text": "#fff4ec",
        "muted": "#94a3b8",
        "faint": "#475569",
        "accent": "#f48c06",
        "accent2": "#e85d04",
        "hot": "#dc2f02",
        "gold": "#faa307",
        "chip": "#1a2540",
        "glow_op": "0.30",
    },
    "light": {
        "bg": "#fff8f2",
        "panel": "#ffffff",
        "panel2": "#fff4ec",
        "line": "#f1dccb",
        "grid": "#e85d04",
        "grid_op": "0.08",
        "text": "#0f172a",
        "muted": "#64748b",
        "faint": "#cbb6a5",
        "accent": "#dc2f02",
        "accent2": "#e85d04",
        "hot": "#dc2f02",
        "gold": "#c2410c",
        "chip": "#fff1e6",
        "glow_op": "0.18",
    },
}


def esc(s: str) -> str:
    return escape(str(s), quote=True)


def text_w(s: str, size: float, mono: bool = True) -> float:
    """Rough rendered width, good enough for laying out chips."""
    return len(s) * size * (0.61 if mono else 0.55)


def svg(w: int, h: int, body: str, t: dict, css: str = "", title: str = "") -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">
<title>{esc(title)}</title>
<style>
text{{font-family:{SANS}}}
.mono{{font-family:{MONO}}}
@media (prefers-reduced-motion: reduce){{*{{animation:none!important}}}}
{css}
</style>
<defs>
  <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
    <path d="M24 0H0V24" fill="none" stroke="{t['grid']}" stroke-opacity="{t['grid_op']}" stroke-width="1"/>
  </pattern>
  <pattern id="dots" width="12" height="12" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="{t['accent2']}" fill-opacity="0.35"/>
  </pattern>
  <radialGradient id="glow" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="{t['accent2']}" stop-opacity="{t['glow_op']}"/>
    <stop offset="100%" stop-color="{t['accent2']}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="fire" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{t['hot']}"/>
    <stop offset="50%" stop-color="{t['accent2']}"/>
    <stop offset="100%" stop-color="#faa307"/>
  </linearGradient>
  <radialGradient id="fade" cx="100%" cy="0%" r="90%">
    <stop offset="0%" stop-color="#fff" stop-opacity="1"/>
    <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
  </radialGradient>
  <mask id="cornerfade"><rect width="{w}" height="{h}" fill="url(#fade)"/></mask>
  <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{t['accent2']}" stop-opacity=".9"/>
    <stop offset="28%" stop-color="{t['line']}"/>
    <stop offset="72%" stop-color="{t['line']}"/>
    <stop offset="100%" stop-color="{t['accent2']}" stop-opacity=".55"/>
  </linearGradient>
  <linearGradient id="pfill" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{t['panel2']}"/>
    <stop offset="100%" stop-color="{t['panel']}"/>
  </linearGradient>
  <linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{t['accent']}" stop-opacity="0"/>
    <stop offset="50%" stop-color="{t['accent']}" stop-opacity=".8"/>
    <stop offset="100%" stop-color="{t['accent']}" stop-opacity="0"/>
  </linearGradient>
</defs>
{body}
</svg>
"""


def panel(x, y, w, h, t, r=14, fill=None, grid=True, brackets=True) -> str:
    """Layered panel: gradient fill, grid texture, gradient edge, top sheen."""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill or "url(#pfill)"}"/>']
    if grid:
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="url(#grid)"/>')
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="none" stroke="url(#edge)" stroke-width="1.2"/>')
    out.append(f'<rect x="{x + w * .15:.1f}" y="{y}" width="{w * .7:.1f}" height="1.2" fill="url(#sheen)"/>')
    if brackets:
        out.append(corners(x, y, w, h, t))
    return "\n".join(out)


def corners(x, y, w, h, t, s=14, inset=6) -> str:
    a, c = inset, t["accent"]
    x0, y0, x1, y1 = x + a, y + a, x + w - a, y + h - a
    d = (f"M{x0} {y0 + s}V{y0}H{x0 + s} M{x1 - s} {y0}H{x1}V{y0 + s} "
         f"M{x1} {y1 - s}V{y1}H{x1 - s} M{x0 + s} {y1}H{x0}V{y1 - s}")
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="1.5" stroke-linecap="square"/>'


def chip(x, y, label, t, size=12, pad=10, h=24, strong=False) -> tuple[str, float]:
    w = text_w(label, size) + pad * 2
    fill = t["accent2"] if strong else t["chip"]
    stroke = t["accent2"] if strong else t["line"]
    color = "#fff4ec" if strong else t["text"]
    s = (f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h}" rx="{h / 2}" fill="{fill}" stroke="{stroke}"/>'
         f'<text class="mono" x="{x + w / 2:.1f}" y="{y + h / 2 + size * 0.36:.1f}" font-size="{size}" '
         f'fill="{color}" text-anchor="middle">{esc(label)}</text>')
    return s, w


def chips(x, y, labels, t, max_w, gap=8, size=12, h=24) -> tuple[str, float]:
    """Flow chips left to right, wrapping at max_w. Returns markup and bottom y."""
    out, cx, cy = [], x, y
    for lab in labels:
        w = text_w(lab, size) + 20
        if cx + w > x + max_w and cx > x:
            cx, cy = x, cy + h + gap
        s, w = chip(cx, cy, lab, t, size=size, h=h)
        out.append(s)
        cx += w + gap
    return "\n".join(out), cy + h


def pill(x, y, label, t, color=None, pulse=True) -> str:
    color = color or t["accent"]
    w = len(label) * (11 * 0.61 + 1) + 34
    return (f'<rect x="{x}" y="{y}" width="{w:.1f}" height="22" rx="11" fill="{color}" fill-opacity="0.12" stroke="{color}" stroke-opacity="0.5"/>'
            f'<circle class="{"pulse" if pulse else ""}" cx="{x + 12}" cy="{y + 11}" r="3.5" fill="{color}"/>'
            f'<text class="mono" x="{x + 21}" y="{y + 15}" font-size="11" fill="{color}" letter-spacing="1">{esc(label)}</text>')


PULSE_CSS = """
.pulse{animation:pulse 2.4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.45;transform:scale(.8)}}
"""


# Looping icon motion in the spirit of AnimateIcons (which needs JS and hover,
# neither of which a README has). Each loop moves briefly, then rests.
ICON_CSS = """
.ic *{transform-box:fill-box;transform-origin:center}
.ic-user{animation:bob 4s ease-in-out infinite}
@keyframes bob{0%,70%,100%{transform:none}80%{transform:translateY(-2px)}90%{transform:translateY(1px)}}
.ic-grid rect{animation:pop 4s ease-in-out infinite}
.ic-grid rect:nth-child(2){animation-delay:.12s}.ic-grid rect:nth-child(3){animation-delay:.24s}.ic-grid rect:nth-child(4){animation-delay:.36s}
@keyframes pop{0%,70%,100%{transform:scale(1)}78%{transform:scale(.6)}86%{transform:scale(1.1)}}
.ic-layers path:first-child{animation:lift 4s ease-in-out infinite}
@keyframes lift{0%,65%,100%{transform:none}78%{transform:translateY(-3px)}}
.ic-pulse path,.ic-voice path:last-child{stroke-dasharray:60;animation:draw 4s ease-in-out infinite}
@keyframes draw{0%{stroke-dashoffset:60}45%,100%{stroke-dashoffset:0}}
.ic-quote{animation:tilt 4s ease-in-out infinite}
@keyframes tilt{0%,70%,100%{transform:none}78%{transform:rotate(-8deg)}88%{transform:rotate(5deg)}}
.ic-send{animation:fly 4s ease-in-out infinite}
@keyframes fly{0%,60%,100%{transform:none;opacity:1}72%{transform:translate(8px,-8px);opacity:0}73%{transform:translate(-8px,8px);opacity:0}86%{transform:none;opacity:1}}
.ic-email path{animation:flap 4s ease-in-out infinite}
@keyframes flap{0%,70%,100%{transform:none}80%{transform:scaleY(-1) translateY(2px)}}
.ic-portfolio path{animation:spin 6s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.ic-linkedin,.ic-plug,.ic-code{animation:nudge 4s ease-in-out infinite}
@keyframes nudge{0%,70%,100%{transform:none}80%{transform:scale(.88)}90%{transform:scale(1.06)}}
.ic-whatsapp,.ic-chat{animation:ring 4s ease-in-out infinite}
@keyframes ring{0%,70%,100%{transform:none}74%{transform:rotate(-12deg)}78%{transform:rotate(10deg)}82%{transform:rotate(-6deg)}86%{transform:rotate(3deg)}}
.ic-agents circle:not(:first-child){animation:orbit 4s ease-in-out infinite}
@keyframes orbit{0%,65%,100%{transform:scale(1)}80%{transform:scale(1.35)}}
.ic-rag path:last-child{animation:scan 4s ease-in-out infinite}
@keyframes scan{0%,60%,100%{transform:none}75%{transform:translate(-3px,-3px)}88%{transform:translate(1px,1px)}}
.ic-chart path:nth-child(n+2){animation:grow 4s ease-in-out infinite;transform-origin:bottom}
.ic-chart path:nth-child(3){animation-delay:.12s}.ic-chart path:nth-child(4){animation-delay:.24s}
@keyframes grow{0%,65%,100%{transform:scaleY(1)}76%{transform:scaleY(.3)}88%{transform:scaleY(1.1)}}
.ic-play{animation:nudge 4s ease-in-out infinite}
.ic-package{animation:bob 4s ease-in-out infinite}
"""


def write(name: str, theme: str, content: str) -> None:
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / f"{name}-{theme}.svg").write_text(content, encoding="utf-8")
