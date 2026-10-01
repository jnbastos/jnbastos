"""Render the profile header as light and dark terminal-style SVGs.

Run `python3 build.py`. GitHub Actions reruns it monthly so the uptime line stays current.
"""
import re
import urllib.request
from datetime import date
from html import escape
from pathlib import Path

LOGIN = "jnbastos"
CAREER_START = date(2022, 1, 1)  # first engineering role, ToChair research fellowship

# (is_command, text); {uptime} and {contributions} are filled in at build time
LINES = [
    (True, "whoami"),
    (False, "João Bastos · Software Engineer · backend, data & machine learning"),
    (True, "cat now.txt"),
    (False, "Building live sports data and analytics for Fan of the Match at PluggableAI"),
    (True, "ls ~/stack"),
    (False, "python fastapi sqlalchemy mysql mongodb redis docker azure"),
    (True, "uptime"),
    (False, "{uptime} building software · Braga, Portugal"),
    (True, "cat activity.txt"),
    (False, "{contributions:,} contributions in the past year, mostly in private work repos"),
]

THEMES = {
    "light": {"bg": "#f6f8fa", "border": "#d0d7de", "text": "#1f2328", "prompt": "#0969da", "dim": "#57606a"},
    "dark": {"bg": "#0d1117", "border": "#30363d", "text": "#e6edf3", "prompt": "#58a6ff", "dim": "#8b949e"},
}

WIDTH, TOP, STEP = 840, 72, 28
HEIGHT = TOP + STEP * (len(LINES) + 1)


def uptime(start: date, today: date) -> str:
    months = (today.year - start.year) * 12 + today.month - start.month - (today.day < start.day)
    years, months = divmod(max(months, 0), 12)
    parts = [f"{n} {unit}{'s' if n != 1 else ''}" for n, unit in ((years, "year"), (months, "month")) if n]
    return "up " + (", ".join(parts) or "0 months")


def parse_contributions(html: str) -> int:
    m = re.search(r"([\d,]+)\s+contributions?\s+in the last year", html)
    if not m:
        raise ValueError("contribution total not found on the public calendar")
    return int(m.group(1).replace(",", ""))


def yearly_contributions() -> int:
    """The past-year total anyone can see on the public profile. Private work is counted
    anonymously by GitHub, so no token is needed and no repository names are read."""
    with urllib.request.urlopen(f"https://github.com/users/{LOGIN}/contributions", timeout=30) as r:
        return parse_contributions(r.read().decode())


def svg(theme: str, today: date, contributions: int) -> str:
    c = THEMES[theme]
    fill = {"uptime": uptime(CAREER_START, today), "contributions": contributions}
    rows = []
    for i, (is_command, text) in enumerate(LINES):
        y = TOP + i * STEP
        text = escape(text.format(**fill))
        body = (f'<tspan fill="{c["prompt"]}">$ </tspan><tspan fill="{c["dim"]}">{text}</tspan>'
                if is_command else text)
        rows.append(f'<text x="24" y="{y}">{body}</text>')
    y = TOP + len(LINES) * STEP  # idle prompt with a blinking cursor; the only animation, so static renders stay readable
    rows.append(f'<text x="24" y="{y}"><tspan fill="{c["prompt"]}">$ </tspan></text>'
                f'<rect class="cursor" x="42" y="{y - 13}" width="9" height="17" fill="{c["text"]}"/>')
    alt = escape(" ".join(t for cmd, t in LINES if not cmd).format(**fill))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="t d">
<title id="t">João Bastos</title><desc id="d">{alt}</desc>
<style>
text {{ font: 15px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill: {c["text"]}; }}
.cursor {{ animation: blink 1.1s steps(1) infinite; }}
@keyframes blink {{ 50% {{ opacity: 0; }} }}
@media (prefers-reduced-motion: reduce) {{ .cursor {{ animation: none; }} }}
</style>
<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{HEIGHT - 1}" rx="10" fill="{c["bg"]}" stroke="{c["border"]}"/>
<circle cx="22" cy="20" r="6" fill="#ff5f57"/><circle cx="42" cy="20" r="6" fill="#febc2e"/><circle cx="62" cy="20" r="6" fill="#28c840"/>
<text x="{WIDTH // 2}" y="25" text-anchor="middle" style="fill:{c["dim"]};font-size:13px">joao@braga: ~</text>
<line x1="0" y1="38" x2="{WIDTH}" y2="38" stroke="{c["border"]}"/>
{chr(10).join(rows)}
</svg>
"""


if __name__ == "__main__":
    contributions = yearly_contributions()  # fails loudly, so a bad fetch never replaces the last good header
    out = Path(__file__).parent / "assets"
    out.mkdir(exist_ok=True)
    for theme in THEMES:
        (out / f"header-{theme}.svg").write_text(svg(theme, date.today(), contributions), encoding="utf-8")
