"""Generate the static profile SVGs (light + dark) into assets/.

Edit the content below and run:  python scripts/build_assets.py
"""

from brand import (ICON_CSS, MONO, PULSE_CSS, THEMES, chip, chips, corners, esc, panel,
                   pill, svg, text_w, write)

W = 1000

# ---------------------------------------------------------------- content

HERO_LINES = [
    ("role", "AI Engineer"),
    ("focus", "multi-agent systems · MLOps · GenAI & RAG"),
    ("base", "Nairobi, Kenya — working remote"),
]

NAV = [("about", "About"), ("work", "Work"), ("stack", "Stack"), ("now", "Now"), ("contact", "Contact")]

SECTIONS = [
    ("about", "01", "About", "user"),
    ("work", "02", "Selected work", "grid"),
    ("stack", "03", "Stack", "layers"),
    ("now", "04", "Now", "pulse"),
    ("philosophy", "05", "Philosophy", "quote"),
    ("contact", "06", "Contact", "send"),
]

BUILT = [
    ("agents", "Multi-agent systems", "planners, tools and memory that coordinate"),
    ("rag", "RAG pipelines", "answers grounded in real documents and data"),
    ("voice", "Real-time voice agents", "streaming speech in, speech out"),
    ("plug", "MCP servers & agent tools", "safe, typed access to real-world APIs"),
    ("chat", "Conversational assistants", "agents that live where people already talk"),
    ("chart", "ML models & analytics", "from notebook to dashboards people use"),
]

PROJECTS = {
    "mpesa": {
        "idx": "P-01", "status": "PYPI · MCP REGISTRY",
        "title": "M-Pesa Daraja Agent Kit",
        "desc": ["Agent Skills and an MCP server for Safaricom's Daraja API.",
                 "Ask your agent to charge a number; the customer gets a PIN",
                 "prompt; the agent reports back with the receipt."],
        "stack": ["Python", "MCP", "Agent Skills", "Daraja API", "PyPI"],
        "art": "mpesa",
    },
    "whatsapp": {
        "idx": "P-02", "status": "MULTI-AGENT",
        "title": "WhatsApp AI Assistant",
        "desc": ["Multi-agent assistant that lives in WhatsApp:",
                 "reasons over memory, searches the web, calls",
                 "third-party APIs and runs scheduled jobs."],
        "stack": ["Agno", "FastAPI", "PostgreSQL", "Evolution API"],
        "art": "chat",
    },
    "voice": {
        "idx": "P-03", "status": "LIVE",
        "title": "Website Voice Agent",
        "desc": ["Real-time conversational voice agent for",
                 "websites: streaming speech in, speech out,",
                 "with memory and an MCP tool interface."],
        "stack": ["Agno AgentOS", "LiveKit", "Deepgram", "Next.js"],
        "art": "voice",
    },
    "medical": {
        "idx": "P-04", "status": "AI-NATIVE ANALYTICS",
        "title": "Medical Insurance Copilot",
        "desc": ["Data-science showcase on a 96,639-member health portfolio:",
                 "a guided story, BI dashboard and model playground, fronted",
                 "by a copilot that queries data, scores members and cites."],
        "stack": ["Next.js 16", "CopilotKit", "Agno", "scikit-learn"],
        "art": "dash",
    },
}

STACK = [
    ("Agents & GenAI", ["Agno", "CrewAI", "LangChain", "MCP", "OpenAI", "Gemini", "RAG"]),
    ("Machine learning", ["Python", "PyTorch", "TensorFlow", "scikit-learn", "Pandas"]),
    ("Backend & web", ["FastAPI", "Next.js", "React", "TypeScript", "Tailwind", "Node.js"]),
    ("Data", ["PostgreSQL", "MongoDB", "Redis", "Pinecone", "ChromaDB", "Power BI"]),
    ("Cloud & ops", ["Docker", "AWS", "GCP", "Azure", "Vercel", "GitHub Actions"]),
    ("Voice & automation", ["LiveKit", "Deepgram", "VAPI", "n8n", "Make", "Zapier"]),
]

NOW = [
    ("shipping", "mpesa-daraja-mcp — on PyPI and the MCP Registry"),
    ("building", "real-time voice agents with LiveKit + Deepgram"),
    ("exploring", "agent memory, tool safety and evaluation"),
]

QUOTE = {
    "head": ["If AI replaces people while human problems remain",
             "unsolved, we have mistaken the purpose of progress."],
    "body": ["AI should extend human capability and bring expertise where it is needed most.",
             "Its purpose should not be to make people unnecessary, but to meet the needs we",
             "have not had the capacity to address. If we replace workers while leaving those",
             "needs unmet, we have mistaken efficiency for progress."],
    "tag": "Build AI to fill gaps in human capacity, not to create gaps in human livelihoods.",
}

CONTACT_BTNS = [("email", "Email", "ai@gichogumacharia.tech"),
                ("portfolio", "Portfolio", "gichogumacharia.tech"),
                ("linkedin", "LinkedIn", "in/gichogu-macharia"),
                ("whatsapp", "WhatsApp", "+254 101 656 882")]

# ---------------------------------------------------------------- icons

ICONS = {
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
    "layers": '<path d="M12 3 21 8 12 13 3 8Z"/><path d="M3 12.5 12 17.5 21 12.5"/><path d="M3 17 12 22 21 17"/>',
    "pulse": '<path d="M2 12h4l3-7 4 14 3-7h6"/>',
    "quote": '<path d="M9 7H5v6h4v4H5"/><path d="M19 7h-4v6h4v4h-4"/>',
    "send": '<path d="M22 2 11 13"/><path d="M22 2 15 22 11 13 2 9Z"/>',
    "email": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "portfolio": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/>',
    "whatsapp": '<path d="M4 20l1.3-4A8 8 0 1 1 8 18.7Z"/><path d="M9 9c0 3 3 6 6 6"/>',
    "agents": '<path d="M12 9V5M9.5 13.5 6 16M14.5 13.5 18 16"/><circle cx="12" cy="12" r="3"/><circle cx="12" cy="4" r="2"/><circle cx="5" cy="17" r="2"/><circle cx="19" cy="17" r="2"/>',
    "rag": '<ellipse cx="10" cy="5" rx="7" ry="2.5"/><path d="M3 5v10c0 1.4 3.1 2.5 7 2.5M17 5v4"/><path d="M3 10c0 1.4 3.1 2.5 7 2.5"/><path d="M17.5 13a3 3 0 1 0 0 6 3 3 0 0 0 0-6Zm2.2 5.2L22 20.5"/>',
    "voice": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4"/>',
    "plug": '<path d="M9 2v5M15 2v5"/><path d="M6 7h12v4a6 6 0 0 1-12 0Z"/><path d="M12 17v5"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.8A8 8 0 1 1 21 12Z"/><path d="M8.5 12h.01M12 12h.01M15.5 12h.01"/>',
    "chart": '<path d="M3 3v18h18"/><path d="M8 17v-5"/><path d="M13 17V8"/><path d="M18 17v-9"/>',
    "code": '<path d="m8 7-5 5 5 5"/><path d="m16 7 5 5-5 5"/>',
    "play": '<circle cx="12" cy="12" r="9"/><path d="M10 8.5v7l5.5-3.5Z"/>',
    "package": '<path d="M12 2 21 7v10l-9 5-9-5V7Z"/><path d="m3 7 9 5 9-5M12 12v10"/>',
}


def icon(name, x, y, color, size=24, sw=1.8):
    s = size / 24
    return (f'<g transform="translate({x} {y}) scale({s})"><g class="ic ic-{name}" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g></g>')


# ---------------------------------------------------------------- hero

def hero(t):
    h = 360
    css = PULSE_CSS + """
.in{animation:in .6s ease-out both}
@keyframes in{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.cur{animation:blink 1s step-end infinite}
@keyframes blink{50%{opacity:0}}
.flow{stroke-dasharray:4 6;animation:flow 3s linear infinite}
@keyframes flow{to{stroke-dashoffset:-40}}
"""
    b = [f'<rect width="{W}" height="{h}" rx="18" fill="{t["bg"]}"/>',
         f'<rect width="{W}" height="{h}" rx="18" fill="url(#grid)"/>',
         f'<circle cx="790" cy="170" r="260" fill="url(#glow)"/>',
         f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="18" fill="none" stroke="{t["line"]}"/>',
         corners(0, 0, W, h, t, s=18, inset=10)]
    # status bar
    b.append(pill(40, 32, "OPEN TO COLLABORATION", t))
    b.append(f'<text class="mono" x="{W - 40}" y="47" font-size="11" fill="{t["muted"]}" text-anchor="end" letter-spacing="1.5">NAIROBI · EAT · UTC+3</text>')
    # prompt + name (typed via clip)
    b.append(f'<text class="mono in" x="40" y="104" font-size="15" fill="{t["accent"]}" style="animation-delay:.05s">~/gichogu <tspan fill="{t["muted"]}">$</tspan> <tspan fill="{t["text"]}">whoami</tspan></text>')
    b.append(f'<text x="38" y="170" font-size="60" font-weight="700" letter-spacing="-1.5" fill="{t["text"]}" class="in" style="animation-delay:.3s">Gichogu Macharia<tspan fill="{t["accent2"]}">.</tspan></text>')
    b.append(f'<text class="in" x="40" y="208" font-size="19" fill="{t["muted"]}" style="animation-delay:.7s">I build AI agents that leave the demo and go to work.</text>')
    # key/value lines
    for i, (k, v) in enumerate(HERO_LINES):
        y = 254 + i * 28
        b.append(f'<text class="mono in" x="40" y="{y}" font-size="14" style="animation-delay:{1.0 + i * .2:.2f}s">'
                 f'<tspan fill="{t["accent"]}">›</tspan> <tspan fill="{t["muted"]}">{k:<6}</tspan>'
                 f'<tspan fill="{t["text"]}" dx="8">{esc(v)}</tspan></text>')
    b.append(f'<rect class="cur" x="40" y="322" width="9" height="16" fill="{t["accent"]}"/>')
    # agent graph
    cx, cy = 790, 185
    nodes = [("planner", 790, 75), ("memory", 900, 150), ("tools", 880, 285), ("research", 690, 290), ("voice", 670, 150)]
    for _, x, y in nodes:
        b.append(f'<line class="flow" x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{t["accent2"]}" stroke-opacity=".7" stroke-width="1.4"/>')
    for i in range(len(nodes)):
        _, x1, y1 = nodes[i]
        _, x2, y2 = nodes[(i + 1) % len(nodes)]
        b.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{t["faint"]}" stroke-opacity=".5" stroke-dasharray="2 5"/>')
    b.append(f'<circle class="pulse" cx="{cx}" cy="{cy}" r="44" fill="none" stroke="{t["accent"]}" stroke-opacity=".35"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="30" fill="{t["panel"]}" stroke="url(#fire)" stroke-width="2.5"/>')
    b.append(f'<text class="mono" x="{cx}" y="{cy + 5}" font-size="14" font-weight="700" fill="{t["accent"]}" text-anchor="middle">GM</text>')
    for name, x, y in nodes:
        w = text_w(name, 11) + 22
        b.append(f'<rect x="{x - w / 2:.1f}" y="{y - 13}" width="{w:.1f}" height="26" rx="6" fill="{t["panel"]}" stroke="{t["line"]}"/>')
        b.append(f'<circle cx="{x - w / 2 + 10:.1f}" cy="{y}" r="2.5" fill="{t["accent"]}"/>')
        b.append(f'<text class="mono" x="{x + 5}" y="{y + 4}" font-size="11" fill="{t["text"]}" text-anchor="middle">{name}</text>')
    return svg(W, h, "\n".join(b), t, css, "Gichogu Macharia — AI Engineer. I build AI agents that leave the demo and go to work.")


# ---------------------------------------------------------------- nav

def nav_tile(key, label, pos, n, t):
    w, h = 166, 52
    r = 12
    left, right = pos == 0, pos == n - 1
    # draw a rounded rect then square off inner edges so tiles join into one bar
    b = [f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="{r}" fill="{t["panel"]}" stroke="{t["line"]}"/>']
    if not left:
        b.append(f'<rect x="0" y="0.5" width="{r + 1}" height="{h - 1}" fill="{t["panel"]}"/>'
                 f'<path d="M0 0.5H{r + 1}M0 {h - 0.5}H{r + 1}" stroke="{t["line"]}"/>')
    if not right:
        b.append(f'<rect x="{w - r - 1}" y="0.5" width="{r + 1}" height="{h - 1}" fill="{t["panel"]}"/>'
                 f'<path d="M{w - r - 1} 0.5H{w}M{w - r - 1} {h - 0.5}H{w}" stroke="{t["line"]}"/>'
                 f'<path d="M{w - 0.5} 14V{h - 14}" stroke="{t["line"]}"/>')
    b.append(f'<rect width="{w}" height="{h}" fill="url(#grid)" opacity=".6"/>')
    if key == "brand":
        b.append(f'<rect x="22" y="14" width="24" height="24" rx="6" fill="url(#fire)"/>'
                 f'<text class="mono" x="34" y="30.5" font-size="11" font-weight="700" fill="#fff4ec" text-anchor="middle">GM</text>'
                 f'<text x="56" y="31" font-size="14" font-weight="700" fill="{t["text"]}">gichogu<tspan fill="{t["accent2"]}">.</tspan></text>')
    else:
        idx = f"0{[k for k, _ in NAV].index(key) + 1}"
        b.append(f'<text class="mono" x="{w / 2}" y="32" font-size="13" text-anchor="middle" fill="{t["text"]}">'
                 f'<tspan fill="{t["accent"]}" font-size="10">{idx} </tspan>{esc(label)}</text>')
    return svg(w, h, "\n".join(b), t, title=label)


# ---------------------------------------------------------------- section header

def header(num, title, ico, t):
    h = 76
    css = ICON_CSS + """
.sweep{animation:sweep 5s ease-in-out infinite}
@keyframes sweep{0%{transform:translateX(-160px);opacity:0}15%{opacity:1}85%{opacity:1}100%{transform:translateX(620px);opacity:0}}
"""
    tx = 112
    tw = text_w(title, 28, mono=False) + 6
    lx = tx + tw + 24
    b = [f'<circle cx="25" cy="38" r="40" fill="url(#glow)"/>',
         panel(1, 14, 48, 48, t, r=12, brackets=False),
         corners(1, 14, 48, 48, t, s=8, inset=4),
         icon(ico, 13, 26, t["accent"]),
         f'<text class="mono" x="66" y="47" font-size="13" fill="{t["accent"]}" letter-spacing="1">{num}<tspan fill="{t["faint"]}"> /</tspan></text>',
         f'<text x="{tx}" y="48" font-size="28" font-weight="700" letter-spacing="-.5" fill="{t["text"]}">{esc(title)}</text>',
         f'<line x1="{lx}" y1="38" x2="{W - 2}" y2="38" stroke="{t["line"]}" stroke-width="1.5"/>',
         f'<clipPath id="lc"><rect x="{lx}" y="30" width="{W - lx}" height="16"/></clipPath>',
         f'<g clip-path="url(#lc)"><rect class="sweep" x="{lx}" y="37" width="140" height="3" rx="1.5" fill="url(#fire)"/></g>',
         f'<circle cx="{W - 4}" cy="38" r="3.5" fill="{t["accent2"]}"/>']
    return svg(W, h, "\n".join(b), t, css, f"{num} — {title}")


# ---------------------------------------------------------------- about

def about(t):
    cols, tw, th, gap = 3, 322, 118, 17
    top = 96
    rows = (len(BUILT) + cols - 1) // cols
    h = top + rows * th + (rows - 1) * gap + 2
    b = [f'<circle cx="80" cy="30" r="240" fill="url(#glow)" opacity=".6"/>',
         f'<text x="2" y="44" font-size="30" font-weight="700" letter-spacing="-.6" fill="{t["text"]}">I\'m an AI engineer<tspan fill="{t["accent2"]}">.</tspan></text>',
         f'<text x="2" y="76" font-size="17" fill="{t["muted"]}">Some of what I\'ve built:</text>']
    for i, (ico, title, sub) in enumerate(BUILT):
        x = 1 + (i % cols) * (tw + gap)
        y = top + (i // cols) * (th + gap)
        b.append(panel(x, y, tw, th, t, brackets=False))
        b.append(f'<rect x="{x + 20}" y="{y + 20}" width="40" height="40" rx="10" fill="{t["accent2"]}" fill-opacity=".12" stroke="{t["accent2"]}" stroke-opacity=".45"/>')
        b.append(icon(ico, x + 28, y + 28, t["accent"]))
        b.append(f'<text class="mono" x="{x + tw - 20}" y="{y + 36}" font-size="11" fill="{t["faint"]}" text-anchor="end">0{i + 1}</text>')
        b.append(f'<text x="{x + 20}" y="{y + 86}" font-size="16.5" font-weight="700" fill="{t["text"]}">{esc(title)}</text>')
        b.append(f'<text x="{x + 20}" y="{y + 106}" font-size="13" fill="{t["muted"]}">{esc(sub)}</text>')
    return svg(W, h, "\n".join(b), t, ICON_CSS, "I'm an AI engineer. I've built " + "; ".join(f"{a}: {c}" for _, a, c in BUILT))


# ---------------------------------------------------------------- project art

def art(kind, x, y, w, h, t):
    """Placeholder previews; swap the <img> for a demo GIF when ready."""
    b = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{t["panel2"]}" stroke="{t["line"]}"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="url(#dots)" opacity=".5" mask="url(#cornerfade)"/>']
    m = lambda s: f'<text class="mono" {s}</text>'
    if kind in ("mpesa", "chat"):
        bubbles = ([("me", "charge 0712•••678 KES 500"), ("bot", "STK push sent — waiting for PIN"), ("bot", "SUCCESS · receipt QK7H2X9LMP")]
                   if kind == "mpesa" else
                   [("me", "remind me to call Wanjiru at 4"), ("bot", "Done. 16:00 EAT, I'll ping you."), ("me", "and find flights NBO → KGL")])
        by = y + 22
        for who, msg in bubbles:
            bw = text_w(msg, 11) + 24
            bx = x + w - bw - 16 if who == "me" else x + 16
            fill = t["accent2"] if who == "me" else t["panel"]
            col = "#fff4ec" if who == "me" else t["text"]
            b.append(f'<rect x="{bx:.1f}" y="{by}" width="{bw:.1f}" height="28" rx="9" fill="{fill}" stroke="{t["line"]}"/>')
            b.append(m(f'x="{bx + 12:.1f}" y="{by + 18}" font-size="11" fill="{col}">{esc(msg)}'))
            by += 40
    elif kind == "voice":
        n, bw = 28, 6
        gap = (w - 40 - n * bw) / (n - 1)
        for i in range(n):
            bh = 10 + abs(((i * 37) % 23) - 11) * 3.2
            bx = x + 20 + i * (bw + gap)
            b.append(f'<rect class="eq" style="animation-delay:{(i % 7) * .12:.2f}s" x="{bx:.1f}" y="{y + h / 2 - bh / 2:.1f}" '
                     f'width="{bw}" height="{bh:.1f}" rx="3" fill="url(#fire)"/>')
        b.append(m(f'x="{x + 16}" y="{y + h - 14}" font-size="10" fill="{t["muted"]}" letter-spacing="1">● LISTENING · STT → AGENT → TTS'))
    elif kind == "dash":
        vals = [42, 64, 51, 78, 69, 88, 74, 95]
        bw = (w * .55 - 20) / len(vals) - 8
        for i, v in enumerate(vals):
            bh = (h - 70) * v / 100
            b.append(f'<rect x="{x + 18 + i * (bw + 8):.1f}" y="{y + h - 24 - bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="3" '
                     f'fill="{t["accent2"]}" fill-opacity="{.35 + v / 160:.2f}"/>')
        kx = x + w * .6
        for i, (k, v) in enumerate([("members", "96,639"), ("models", "scored live"), ("copilot", "cites report")]):
            ky = y + 26 + i * 44
            b.append(m(f'x="{kx}" y="{ky}" font-size="10" fill="{t["muted"]}" letter-spacing="1">{k.upper()}'))
            b.append(f'<text x="{kx}" y="{ky + 20}" font-size="17" font-weight="700" fill="{t["text"]}">{v}</text>')
    return "\n".join(b)


def card(key, t, wide=True):
    p = PROJECTS[key]
    w, h = (W, 280) if wide else (490, 420)
    css = PULSE_CSS + """
.eq{animation:eq 1.4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes eq{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.35)}}
"""
    b = [panel(0.5, 0.5, w - 1, h - 1, t), f'<circle cx="{w}" cy="0" r="260" fill="url(#glow)" opacity=".8"/>',
         f'<circle cx="0" cy="{h}" r="180" fill="url(#glow)" opacity=".35"/>',
         f'<rect x="32" y="0.5" width="64" height="3" rx="1.5" fill="url(#fire)"/>']
    pad = 32
    if wide:
        ax, ay, aw, ah = w - 400, 32, 368, h - 64
        tx, ty, tw = pad, 46, w - 400 - pad * 2
    else:
        ax, ay, aw, ah = pad, 68, w - pad * 2, 150
        tx, ty, tw = pad, 0, w - pad * 2
    # meta row
    meta_y = ty if wide else 44
    b.append(f'<text class="mono" x="{tx}" y="{meta_y}" font-size="12" fill="{t["faint"]}" letter-spacing="1.5">{p["idx"]}</text>')
    color = "#22c55e" if p["status"] == "LIVE" else t["accent"]
    b.append(pill(tx + 52, meta_y - 15, p["status"], t, color=color, pulse=p["status"] == "LIVE"))
    num = p["idx"][-2:]
    wx, wy = (tx + tw + 10, h - 22) if wide else (w - 28, ay + ah + 128)
    b.append(f'<text x="{wx}" y="{wy}" font-size="120" font-weight="800" letter-spacing="-4" fill="{t["accent2"]}" fill-opacity=".07" text-anchor="end">{num}</text>')
    b.append(f'<rect x="{ax + 6}" y="{ay + 8}" width="{aw}" height="{ah}" rx="10" fill="{t["accent2"]}" fill-opacity=".10"/>')
    b.append(art(p["art"], ax, ay, aw, ah, t))
    b.append(f'<rect x="{ax}" y="{ay}" width="{aw}" height="{ah}" rx="10" fill="none" stroke="url(#edge)"/>')
    y0 = meta_y + 48 if wide else ay + ah + 50
    b.append(f'<text x="{tx}" y="{y0}" font-size="28" font-weight="800" letter-spacing="-.8" fill="{t["text"]}">{esc(p["title"])}</text>')
    for i, line in enumerate(p["desc"]):
        b.append(f'<text x="{tx}" y="{y0 + 32 + i * 23}" font-size="15" fill="{t["muted"]}">{esc(line)}</text>')
    cs, _ = chips(tx, y0 + 32 + len(p["desc"]) * 23 + 4, p["stack"], t, tw)
    b.append(cs)
    return svg(w, h, "\n".join(b), t, css, f'{p["title"]} — {" ".join(p["desc"])}')


# ---------------------------------------------------------------- stack

def stack(t):
    cols, gw, gh, gap = 3, 322, 150, 17
    rows = (len(STACK) + cols - 1) // cols
    h = rows * gh + (rows - 1) * gap + 2
    b = []
    for i, (name, items) in enumerate(STACK):
        x = 1 + (i % cols) * (gw + gap)
        y = 1 + (i // cols) * (gh + gap)
        b.append(panel(x, y, gw, gh, t, brackets=False))
        b.append(f'<text class="mono" x="{x + 20}" y="{y + 32}" font-size="11" fill="{t["accent"]}" letter-spacing="1.5">0{i + 1}</text>')
        b.append(f'<text x="{x + 46}" y="{y + 33}" font-size="16" font-weight="700" fill="{t["text"]}">{esc(name)}</text>')
        cs, _ = chips(x + 20, y + 52, items, t, gw - 40, gap=7, size=11, h=24)
        b.append(cs)
    return svg(W, h, "\n".join(b), t, title="Stack — " + "; ".join(f"{n}: {', '.join(i)}" for n, i in STACK))


# ---------------------------------------------------------------- now

def now(t):
    h = 64 + len(NOW) * 40
    b = [panel(0.5, 0.5, W - 1, h - 1, t),
         pill(28, 22, "CURRENTLY", t)]
    for i, (k, v) in enumerate(NOW):
        y = 82 + i * 40
        b.append(f'<text class="mono" x="32" y="{y}" font-size="14"><tspan fill="{t["accent"]}">{k:<10}</tspan></text>')
        b.append(f'<text x="160" y="{y}" font-size="16" fill="{t["text"]}">{esc(v)}</text>')
        if i < len(NOW) - 1:
            b.append(f'<line x1="32" y1="{y + 16}" x2="{W - 32}" y2="{y + 16}" stroke="{t["line"]}" stroke-dasharray="2 4"/>')
    return svg(W, h, "\n".join(b), t, PULSE_CSS, "Now — " + "; ".join(f"{k}: {v}" for k, v in NOW))


# ---------------------------------------------------------------- quote

def quote(t):
    q = QUOTE
    hy = 78
    by = hy + len(q["head"]) * 38 + 26
    ty = by + len(q["body"]) * 27 + 34
    h = ty + 42
    b = [panel(0.5, 0.5, W - 1, h - 1, t),
         f'<circle cx="120" cy="40" r="220" fill="url(#glow)" opacity=".7"/>',
         f'<text x="48" y="132" font-size="150" font-weight="700" fill="url(#fire)" opacity=".9">“</text>']
    for i, line in enumerate(q["head"]):
        b.append(f'<text x="150" y="{hy + i * 38}" font-size="28" font-weight="700" letter-spacing="-.5" fill="{t["text"]}">{esc(line)}</text>')
    for i, line in enumerate(q["body"]):
        b.append(f'<text x="150" y="{by + i * 27}" font-size="16.5" fill="{t["muted"]}">{esc(line)}</text>')
    b.append(f'<line x1="150" y1="{ty - 4}" x2="186" y2="{ty - 4}" stroke="{t["accent2"]}" stroke-width="2"/>')
    b.append(f'<text class="mono" x="198" y="{ty}" font-size="13" fill="{t["accent"]}">{esc(q["tag"])}</text>')
    return svg(W, h, "\n".join(b), t, title=" ".join(q["head"] + q["body"]) + " " + q["tag"])


# ---------------------------------------------------------------- contact

def cta(t):
    h = 190
    b = [f'<rect width="{W}" height="{h}" rx="18" fill="{t["bg"]}"/>',
         f'<rect width="{W}" height="{h}" rx="18" fill="url(#grid)"/>',
         f'<circle cx="{W / 2}" cy="{h}" r="320" fill="url(#glow)"/>',
         f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="18" fill="none" stroke="{t["line"]}"/>',
         corners(0, 0, W, h, t, s=18, inset=10),
         f'<text x="{W / 2}" y="92" font-size="40" font-weight="700" letter-spacing="-1" fill="{t["text"]}" text-anchor="middle">Have something worth building<tspan fill="{t["accent2"]}">?</tspan></text>',
         f'<text x="{W / 2}" y="132" font-size="17" fill="{t["muted"]}" text-anchor="middle">Collaborations, roles and open-source — my inbox is open.</text>']
    return svg(W, h, "\n".join(b), t, title="Have something worth building? Collaborations, roles and open-source — my inbox is open.")


def button(key, label, sub, t):
    w, h = 240, 64
    b = [panel(0.5, 0.5, w - 1, h - 1, t, r=12, brackets=False),
         f'<rect x="14" y="14" width="36" height="36" rx="9" fill="{t["accent2"]}" fill-opacity=".12" stroke="{t["accent2"]}" stroke-opacity=".4"/>',
         icon(key, 23, 23, t["accent"], size=18, sw=2),
         f'<text x="62" y="30" font-size="15" font-weight="700" fill="{t["text"]}">{esc(label)}</text>',
         f'<text class="mono" x="62" y="48" font-size="10.5" fill="{t["muted"]}">{esc(sub)}</text>',
         f'<path d="M{w - 30} 26l6 6-6 6" fill="none" stroke="{t["accent"]}" stroke-width="2" stroke-linecap="round"/>']
    return svg(w, h, "\n".join(b), t, ICON_CSS, f"{label}: {sub}")


LINKS = [("code", "code", "Code"), ("pypi", "package", "PyPI"), ("demo", "play", "Live demo"),
         ("whatsapp-code", "code", "WhatsApp · Code"), ("voice-demo", "play", "Voice · Live demo"),
         ("voice-code", "code", "Voice · Code")]


def linkbtn(ico, label, t):
    strong = ico == "play"
    w, h = int(text_w(label, 13) + 74), 40
    fill = "url(#fire)" if strong else "url(#pfill)"
    col, icol = ("#fff4ec", "#fff4ec") if strong else (t["text"], t["accent"])
    b = [f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="10" fill="{fill}"/>',
         f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="10" fill="none" stroke="{"none" if strong else "url(#edge)"}"/>',
         icon(ico, 14, 11, icol, size=18, sw=2),
         f'<text class="mono" x="42" y="25" font-size="13" font-weight="600" fill="{col}">{esc(label)}</text>',
         f'<path d="M{w - 24} 15h7v7M{w - 17} 15l-8 8" fill="none" stroke="{icol}" stroke-width="1.8" stroke-linecap="round"/>']
    return svg(w, h, "\n".join(b), t, ICON_CSS, label)


def footer(t):
    h = 70
    b = [f'<rect x="0" y="0" width="{W}" height="3" rx="1.5" fill="url(#fire)"/>',
         f'<text class="mono" x="0" y="44" font-size="12" fill="{t["muted"]}" letter-spacing="1"><tspan fill="{t["accent"]}">GM</tspan>  ·  gichogumacharia.tech</text>',
         f'<text class="mono" x="{W}" y="44" font-size="12" fill="{t["faint"]}" text-anchor="end" letter-spacing="1">BUILT IN NAIROBI · RENDERED IN SVG</text>']
    return svg(W, h, "\n".join(b), t, title="gichogumacharia.tech")


# ---------------------------------------------------------------- main

def main():
    for name, t in THEMES.items():
        write("hero", name, hero(t))
        tiles = [("brand", "gichogu")] + NAV
        for i, (k, label) in enumerate(tiles):
            write(f"nav-{k}", name, nav_tile(k, label, i, len(tiles), t))
        for key, num, title, ico in SECTIONS:
            write(f"h-{key}", name, header(num, title, ico, t))
        write("about", name, about(t))
        for k, ico, label in LINKS:
            write(f"link-{k}", name, linkbtn(ico, label, t))
        for key in PROJECTS:
            write(f"card-{key}", name, card(key, t, wide=key in ("mpesa", "medical")))
        write("stack", name, stack(t))
        write("now", name, now(t))
        write("quote", name, quote(t))
        write("cta", name, cta(t))
        for k, label, sub in CONTACT_BTNS:
            write(f"btn-{k}", name, button(k, label, sub, t))
        write("footer", name, footer(t))
    print("assets written")


if __name__ == "__main__":
    main()
