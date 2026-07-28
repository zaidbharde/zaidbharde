from __future__ import annotations

import math
import random
from pathlib import Path


OUT = Path("assets/banners")
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1180, 610
USERNAME = "zaidbharde"
NAME = "Zaid Bharde"
ROLE = "Cybersecurity Enthusiast"
LOCATION = "Navi Mumbai, India"
STATUS = "Learning Offense to Build Defense"
EMAIL = "zaidbharde09@gmail.com"
LINKEDIN = "zaid-bharde-472933334"
INSTAGRAM = "zxidd09"


def esc(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def portrait_points(seed: int = 9) -> list[tuple[float, float, float]]:
    """Procedural dither portrait based on the supplied reference pose."""
    random.seed(seed)
    pts: list[tuple[float, float, float]] = []
    px, py = 88, 142
    sw, sh = 306, 352

    for y in range(0, 340, 4):
        for x in range(0, 300, 4):
            nx = (x - 150) / 150
            ny = (y - 168) / 168

            # Head tilted up-left, shoulders and ornate coat silhouette.
            head = ((nx + 0.03) / 0.46) ** 2 + ((ny + 0.44) / 0.43) ** 2 < 1
            hair = ((nx + 0.01) / 0.52) ** 2 + ((ny + 0.70) / 0.25) ** 2 < 1 and y < 118
            neck = abs(nx + 0.02) < 0.18 and 92 < y < 180
            torso = ((nx + 0.02) / 0.72) ** 2 + ((ny - 0.62) / 0.66) ** 2 < 1 and y > 166
            shoulder_l = ((nx + 0.58) / 0.56) ** 2 + ((ny - 0.34) / 0.36) ** 2 < 1 and y > 182
            shoulder_r = ((nx - 0.52) / 0.56) ** 2 + ((ny - 0.34) / 0.36) ** 2 < 1 and y > 182
            fg = head or hair or neck or torso or shoulder_l or shoulder_r
            if not fg:
                continue

            # Tone map: face, hair, gold uniform lines, and shadows.
            tone = 0.24
            if head:
                tone += 0.40 * max(0, 1 - ((nx + 0.05) ** 2 + (ny + 0.44) ** 2) * 1.8)
            if hair:
                tone += 0.26
            if torso:
                tone += 0.14
            if abs(nx + ny * 0.45) < 0.035 and y > 160:
                tone += 0.55
            if abs(nx - 0.38 + ny * 0.35) < 0.035 and y > 145:
                tone += 0.60
            if shoulder_l or shoulder_r:
                tone += 0.30

            # Glasses, brows, beard, collar marks.
            eye_band = 77 < y < 101 and -0.44 < nx < 0.45
            if eye_band and (abs((nx + 0.22) / 0.18) + abs((y - 88) / 20) < 1.1):
                tone += 0.55
            if eye_band and (abs((nx - 0.18) / 0.18) + abs((y - 88) / 20) < 1.1):
                tone += 0.55
            if 118 < y < 156 and abs(nx) < 0.34:
                tone += 0.26
            if 134 < y < 184 and abs(nx + 0.01) < 0.25:
                tone += 0.22

            tone += random.uniform(-0.16, 0.14)
            if random.random() < max(0.08, min(0.92, tone)):
                pts.append((px + x * sw / 300, py + y * sh / 340, 1.0 + random.random() * 1.1))
    return pts


def logo_points(kind: str, cx: float, cy: float, scale: float) -> list[tuple[float, float]]:
    pts: list[tuple[float, float]] = []
    for i in range(680):
        t = i / 680 * math.tau
        if kind == "arch":
            r = 1 - (i % 37) / 45
            x = cx + scale * (math.sin(t) * (0.44 + 0.18 * math.cos(3 * t))) * r
            y = cy - scale * (0.62 * math.cos(t) - 0.26 * math.cos(2 * t)) * r
            if y > cy + scale * 0.30 and abs(x - cx) < scale * 0.18:
                continue
        elif kind == "bird":
            r = 0.42 + 0.27 * math.sin(2 * t)
            x = cx + scale * (math.cos(t) * r + 0.22 * math.cos(3 * t))
            y = cy + scale * (math.sin(t) * r - 0.18 * math.sin(2 * t))
            if i % 5 == 0:
                x -= scale * 0.62 * random.random()
                y -= scale * 0.38 * random.random()
        else:
            # Terminal prompt >_
            if i < 340:
                u = i / 340
                x = cx - scale * 0.38 + scale * 0.42 * abs((u * 2) - 1)
                y = cy - scale * 0.26 + scale * 0.52 * u
            else:
                u = (i - 340) / 340
                x = cx - scale * 0.02 + scale * 0.50 * u
                y = cy + scale * 0.32
        pts.append((x, y))
    return pts


def dotted_portrait(points: list[tuple[float, float, float]], color: str, intro_prefix: str) -> str:
    groups = [[] for _ in range(60)]
    for idx, (x, y, r) in enumerate(points):
        groups[idx % 60].append(f"M{x:.1f},{y:.1f}h{r:.1f}v{r:.1f}h-{r:.1f}z")
    parts = []
    for i, group in enumerate(groups):
        begin = 0.04 * i
        parts.append(
            f'<path d="{"".join(group)}" fill="{color}" opacity="0">'
            f'<animate id="{intro_prefix}{i}" attributeName="opacity" values="0;1" '
            f'dur="0.55s" begin="{begin:.2f}s" fill="freeze"/></path>'
        )
    return "\n".join(parts)


def traveller_layer(color: str) -> str:
    random.seed(23)
    kinds = ["arch", "bird", "terminal"]
    logos = [logo_points(k, 250, 315, 110) for k in kinds]
    paths = []
    count = min(620, *(len(points) for points in logos))
    for i in range(count):
        p0, p1, p2 = logos[0][i], logos[1][i], logos[2][i]
        paths.append(
            f'<circle cx="{p0[0]:.1f}" cy="{p0[1]:.1f}" r="1.85" fill="{color}" opacity="0">'
            f'<animate attributeName="cx" dur="14.2s" repeatCount="indefinite" '
            f'keyTimes="0;0.21;0.30;0.45;0.54;0.69;0.78;1" '
            f'values="{p0[0]:.1f};{p0[0]:.1f};{p1[0]:.1f};{p1[0]:.1f};{p2[0]:.1f};{p2[0]:.1f};{p0[0]:.1f};{p0[0]:.1f}"/>'
            f'<animate attributeName="cy" dur="14.2s" repeatCount="indefinite" '
            f'keyTimes="0;0.21;0.30;0.45;0.54;0.69;0.78;1" '
            f'values="{p0[1]:.1f};{p0[1]:.1f};{p1[1]:.1f};{p1[1]:.1f};{p2[1]:.1f};{p2[1]:.1f};{p0[1]:.1f};{p0[1]:.1f}"/>'
            f'<animate attributeName="opacity" dur="14.2s" repeatCount="indefinite" '
            f'keyTimes="0;0.17;0.21;0.78;0.83;1" values="0;0;1;1;0;0"/></circle>'
        )
    return "\n".join(paths)


def info_rows(text: str, accent: str, muted: str) -> str:
    rows = [
        ("Subject", NAME),
        ("Role", ROLE),
        ("Origin", LOCATION),
        ("Education", "Cybersecurity + AI/ML"),
        ("Status", STATUS),
        ("Core.Lang", "Python | Kotlin | JavaScript | SQL"),
        ("Core.Frontend", "HTML | CSS | React basics"),
        ("Core.Backend", "FastAPI | Flask | REST APIs"),
        ("Core.Database", "SQLite | Firebase"),
        ("Core.Infra", "Linux | WSL | Git | Docker | Vercel"),
        ("Grid.Mail", EMAIL),
        ("Grid.Portfolio", "coming soon"),
        ("Grid.LinkedIn", LINKEDIN),
        ("Grid.GitHub", USERNAME),
        ("Grid.Instagram", INSTAGRAM),
    ]
    out = []
    y = 150
    for label, value in rows:
        dots = "." * max(4, 24 - len(label))
        out.append(
            f'<text x="548" y="{y}" fill="{muted}" font-size="13" textLength="196" '
            f'lengthAdjust="spacingAndGlyphs">{esc(label)} {dots}</text>'
            f'<text x="758" y="{y}" fill="{text}" font-size="13" font-weight="600" '
            f'textLength="330" lengthAdjust="spacingAndGlyphs">{esc(value[:42])}</text>'
        )
        y += 24
    return "\n".join(out)


def svg(theme: str) -> str:
    dark = theme == "dark"
    bg = "#090608" if dark else "#fff7eb"
    panel = "#130b10" if dark else "#ffffff"
    text = "#fff1dd" if dark else "#24130d"
    muted = "#b9a790" if dark else "#7a614d"
    border = "#6f2d19" if dark else "#d7a45e"
    gold = "#f3b84d"
    red = "#7e1414" if dark else "#b83324"
    portrait = "#f0b344" if dark else "#6f2015"
    pts = portrait_points()

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{NAME} GitHub profile banner">
<style>
text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
.win {{ filter: drop-shadow(0 24px 48px rgba(0,0,0,.35)); }}
.pulse {{ animation: pulse 1.2s infinite; }}
@keyframes pulse {{ 0%,100% {{ opacity: .45 }} 50% {{ opacity: 1 }} }}
</style>
<defs>
<radialGradient id="bg" cx="22%" cy="16%" r="78%">
<stop offset="0" stop-color="{red}" stop-opacity="{'.60' if dark else '.22'}"/>
<stop offset=".48" stop-color="{bg}"/>
<stop offset="1" stop-color="{bg}"/>
</radialGradient>
<linearGradient id="trim" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="{gold}"/>
<stop offset=".55" stop-color="#8f4b1c"/>
<stop offset="1" stop-color="{gold}"/>
</linearGradient>
</defs>
<rect width="1180" height="610" fill="url(#bg)"/>
<g class="win">
<rect x="42" y="46" width="1096" height="516" rx="18" fill="{panel}" stroke="{border}" stroke-width="1.5"/>
<rect x="42" y="46" width="1096" height="42" rx="18" fill="{('#190b0c' if dark else '#fff0da')}"/>
<circle cx="70" cy="67" r="6" fill="#ff5f56"/><circle cx="91" cy="67" r="6" fill="#ffbd2e"/><circle cx="112" cy="67" r="6" fill="#27c93f"/>
<text x="562" y="72" text-anchor="middle" fill="{muted}" font-size="13">profile.sh --live</text>
<text x="88" y="119" fill="{gold}" font-size="13" font-weight="700">VISUAL.MAP</text>
<text x="548" y="119" fill="{gold}" font-size="13" font-weight="700">SYSTEM.INFO</text>
<rect x="960" y="101" width="56" height="24" rx="12" fill="#b91c1c"/><text x="988" y="118" text-anchor="middle" fill="#fff" font-size="12" class="pulse">LIVE</text>
<rect x="1026" y="101" width="88" height="24" rx="12" fill="{gold}" opacity=".18" stroke="{gold}"/><text x="1070" y="118" text-anchor="middle" fill="{gold}" font-size="13">@{USERNAME}</text>
<rect x="82" y="138" width="346" height="386" rx="12" fill="{('#080506' if dark else '#fffaf0')}" stroke="url(#trim)" stroke-width="1.5"/>
<g shape-rendering="crispEdges">
{dotted_portrait(pts, portrait, theme)}
</g>
<g>{traveller_layer(gold)}</g>
<text x="548" y="548" fill="{muted}" font-size="12">morph: portrait -> arch -> custom mark -> terminal</text>
{info_rows(text, gold, muted)}
<path d="M82 504 C164 548 292 556 428 510" fill="none" stroke="{gold}" stroke-width="2" opacity=".6"/>
</g>
</svg>'''


if __name__ == "__main__":
    for mode in ("dark", "light"):
        (OUT / f"{mode}.svg").write_text(svg(mode), encoding="utf-8")
    print("Generated assets/banners/dark.svg and assets/banners/light.svg")
