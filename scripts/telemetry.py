"""Render assets/telemetry-{dark,light}.svg from live GitHub data.

Needs GITHUB_TOKEN (the Actions token is enough). Run daily by
.github/workflows/profile.yml.
"""

import json
import os
import urllib.request
from datetime import date, datetime, timezone

from brand import PULSE_CSS, THEMES, esc, panel, pill, svg, write

USER = os.environ.get("PROFILE_USER", "Mr-Macharia")
W, H = 1000, 250

QUERY = """
query($login:String!){ user(login:$login){
  followers{totalCount}
  pullRequests{totalCount}
  repositories(ownerAffiliations:OWNER, isFork:false, privacy:PUBLIC, first:100){
    totalCount
    nodes{ stargazerCount languages(first:8, orderBy:{field:SIZE,direction:DESC}){ edges{size node{name color}} } }
  }
  contributionsCollection{ contributionCalendar{ totalContributions weeks{ contributionDays{ date contributionCount } } } }
}}"""


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    if "errors" in data:
        raise SystemExit(data["errors"])
    return data["data"]["user"]


def summarise(u):
    repos = u["repositories"]["nodes"]
    langs = {}
    for r in repos:
        for e in r["languages"]["edges"]:
            n = e["node"]["name"]
            if n == "Jupyter Notebook":  # notebook JSON bytes swamp everything else
                n = "Python"
            langs[n] = langs.get(n, 0) + e["size"]
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:5]

    days = [d for w in u["contributionsCollection"]["contributionCalendar"]["weeks"] for d in w["contributionDays"]]
    days = [d for d in days if date.fromisoformat(d["date"]) <= date.today()]
    streak, best, run = 0, 0, 0
    for d in days:
        run = run + 1 if d["contributionCount"] else 0
        best = max(best, run)
    for i, d in enumerate(reversed(days)):
        if d["contributionCount"]:
            streak += 1
        elif i:  # today may still be empty
            break
    recent = [d["contributionCount"] for d in days[-56:]]
    return {
        "contributions": u["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "repos": u["repositories"]["totalCount"],
        "stars": sum(r["stargazerCount"] for r in repos),
        "prs": u["pullRequests"]["totalCount"],
        "followers": u["followers"]["totalCount"],
        "streak": streak, "best": best,
        "langs": [(n, s / total) for n, s in top],
        "recent": recent,
    }


def render(s, t):
    b = [panel(0.5, 0.5, W - 1, H - 1, t),
         pill(28, 22, "LIVE TELEMETRY", t, color="#22c55e"),
         f'<text class="mono" x="{W - 28}" y="37" font-size="11" fill="{t["faint"]}" text-anchor="end" letter-spacing="1">'
         f'SYNCED {datetime.now(timezone.utc):%Y-%m-%d} UTC</text>']
    stats = [("contributions", s["contributions"], "past year"), ("streak", s["streak"], f'best {s["best"]} days'),
             ("public repos", s["repos"], "original work"), ("pull requests", s["prs"], "all time"),
             ("stars", s["stars"], f'{s["followers"]} followers')]
    cw = (W - 56) / len(stats)
    for i, (k, v, sub) in enumerate(stats):
        x = 28 + i * cw
        if i:
            b.append(f'<line x1="{x - 12:.1f}" y1="72" x2="{x - 12:.1f}" y2="138" stroke="{t["line"]}"/>')
        b.append(f'<text class="mono" x="{x:.1f}" y="82" font-size="10.5" fill="{t["muted"]}" letter-spacing="1.5">{k.upper()}</text>')
        b.append(f'<text x="{x:.1f}" y="118" font-size="34" font-weight="700" letter-spacing="-1" fill="{t["text"]}">{v:,}</text>')
        b.append(f'<text class="mono" x="{x:.1f}" y="138" font-size="10.5" fill="{t["faint"]}">{esc(sub)}</text>')
    # language bar
    shades = [t["accent2"], "#faa307", t["hot"], t["muted"], t["faint"]]
    x, bw, y = 28, 560, 178
    b.append(f'<text class="mono" x="28" y="166" font-size="10.5" fill="{t["muted"]}" letter-spacing="1.5">LANGUAGES</text>')
    b.append(f'<clipPath id="bar"><rect x="28" y="{y}" width="{bw}" height="10" rx="5"/></clipPath><g clip-path="url(#bar)">')
    for (n, f), c in zip(s["langs"], shades):
        b.append(f'<rect x="{x:.1f}" y="{y}" width="{bw * f + 1:.1f}" height="10" fill="{c}"/>')
        x += bw * f
    b.append("</g>")
    lx = 28
    for (n, f), c in zip(s["langs"], shades):
        label = f"{n} {f * 100:.0f}%"
        b.append(f'<circle cx="{lx + 4}" cy="{y + 30}" r="4" fill="{c}"/>'
                 f'<text class="mono" x="{lx + 14}" y="{y + 34}" font-size="11" fill="{t["text"]}">{esc(label)}</text>')
        lx += len(label) * 6.7 + 30
    # 8-week activity sparkline bars
    rx, rw = 640, W - 28 - 640
    peak = max(s["recent"]) or 1
    b.append(f'<text class="mono" x="{rx}" y="166" font-size="10.5" fill="{t["muted"]}" letter-spacing="1.5">LAST 8 WEEKS</text>')
    step = rw / len(s["recent"])
    for i, c in enumerate(s["recent"]):
        hh = 2 + 40 * c / peak
        b.append(f'<rect x="{rx + i * step:.1f}" y="{222 - hh:.1f}" width="{step - 1.5:.1f}" height="{hh:.1f}" rx="1" '
                 f'fill="{t["accent2"] if c else t["line"]}" fill-opacity="{.4 + .6 * c / peak:.2f}"/>')
    title = f'{s["contributions"]} contributions in the past year, {s["streak"]}-day streak, {s["repos"]} public repos'
    return svg(W, H, "\n".join(b), t, PULSE_CSS, title)


NOW_QUERY = """
query($login:String!, $since:DateTime!){ user(login:$login){
  recent: repositories(ownerAffiliations:OWNER, isFork:false, privacy:PUBLIC, first:30, orderBy:{field:PUSHED_AT,direction:DESC}){
    nodes{ name description releases(first:1, orderBy:{field:CREATED_AT,direction:DESC}){ nodes{ tagName createdAt } } }
  }
  newest: repositories(ownerAffiliations:OWNER, isFork:false, privacy:PUBLIC, first:5, orderBy:{field:CREATED_AT,direction:DESC}){
    nodes{ name description createdAt }
  }
  contributionsCollection(from:$since){
    commitContributionsByRepository(maxRepositories:10){
      repository{ name description isPrivate owner{login} } contributions{ totalCount }
    }
  }
}}"""


def gql(query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    if "errors" in data:
        raise SystemExit(data["errors"])
    return data["data"]["user"]


def ago(iso):
    days = (datetime.now(timezone.utc) - datetime.fromisoformat(iso.replace("Z", "+00:00"))).days
    if days < 1:
        return "today"
    if days < 2:
        return "yesterday"
    if days < 30:
        return f"{days} days ago"
    if days < 60:
        return "a month ago"
    return f"{days // 30} months ago"


def now_rows():
    """Three live rows: latest release, most-committed repo this week, newest repo."""
    since = datetime.now(timezone.utc).replace(microsecond=0)
    since = since.fromtimestamp(since.timestamp() - 7 * 86400, timezone.utc).isoformat()
    u = gql(NOW_QUERY, {"login": USER, "since": since})
    skip = {USER}
    rows = []

    released = [(r, r["releases"]["nodes"][0]) for r in u["recent"]["nodes"] if r["releases"]["nodes"] and r["name"] not in skip]
    if released:
        r, rel = max(released, key=lambda x: x[1]["createdAt"])
        rows.append(("shipping", r["name"], f'{rel["tagName"]} · {ago(rel["createdAt"])}', r["description"]))

    skip |= {r[1] for r in rows}  # one repo per row
    busy = [c for c in u["contributionsCollection"]["commitContributionsByRepository"]
            if not c["repository"]["isPrivate"] and c["repository"]["owner"]["login"] == USER
            and c["repository"]["name"] not in skip]
    if busy:
        c = max(busy, key=lambda c: c["contributions"]["totalCount"])
        n = c["contributions"]["totalCount"]
        rows.append(("building", c["repository"]["name"], f'{n} commit{"s" * (n != 1)} this week', c["repository"]["description"]))
    else:
        r = next(r for r in u["recent"]["nodes"] if r["name"] not in skip)
        rows.append(("building", r["name"], "most recent push", r["description"]))

    skip |= {r[1] for r in rows}
    new = next((r for r in u["newest"]["nodes"] if r["name"] not in skip), u["newest"]["nodes"][0])
    rows.append(("exploring", new["name"], f'started {ago(new["createdAt"])}', new["description"]))
    return rows


def fit(s, size, max_w):
    """Trim text to a pixel width (sans-serif estimate) with an ellipsis."""
    limit = int(max_w / (size * 0.52))
    return s if len(s) <= limit else s[:limit - 1].rstrip(" ,.;:—-") + "…"


def render_now(rows, t):
    top, row_h = 66, 64
    h = top + len(rows) * row_h + 14
    label_x, name_x, right = 32, 168, W - 32
    b = [panel(0.5, 0.5, W - 1, h - 1, t),
         pill(28, 22, "CURRENTLY", t, color="#22c55e"),
         f'<text class="mono" x="{right}" y="37" font-size="11" fill="{t["faint"]}" text-anchor="end" letter-spacing="1">'
         f'FROM GITHUB · {datetime.now(timezone.utc):%Y-%m-%d}</text>']
    for i, (label, name, meta, desc) in enumerate(rows):
        y = top + i * row_h
        if i:
            b.append(f'<line x1="{label_x}" y1="{y}" x2="{right}" y2="{y}" stroke="{t["line"]}" stroke-dasharray="2 4"/>')
        meta_w = len(meta) * 11.5 * 0.61 + 24
        b.append(f'<text class="mono" x="{label_x}" y="{y + 28}" font-size="13" fill="{t["accent"]}" letter-spacing=".5">{label}</text>')
        b.append(f'<text x="{name_x}" y="{y + 28}" font-size="16.5" font-weight="700" fill="{t["text"]}">'
                 f'{esc(fit(name, 16.5, right - meta_w - name_x))}</text>')
        b.append(f'<text class="mono" x="{right}" y="{y + 28}" font-size="11.5" fill="{t["muted"]}" text-anchor="end">{esc(meta)}</text>')
        b.append(f'<text x="{name_x}" y="{y + 49}" font-size="13.5" fill="{t["muted"]}">'
                 f'{esc(fit(desc or "No description yet.", 13.5, right - name_x))}</text>')
    title = "Now — " + "; ".join(f"{l}: {n} ({m})" for l, n, m, _ in rows)
    return svg(W, h, "\n".join(b), t, PULSE_CSS, title)


def main():
    s = summarise(fetch())
    rows = now_rows()
    for name, t in THEMES.items():
        write("telemetry", name, render(s, t))
        write("now", name, render_now(rows, t))
    print(rows)
    print(json.dumps({k: v for k, v in s.items() if k != "recent"}))


if __name__ == "__main__":
    main()
