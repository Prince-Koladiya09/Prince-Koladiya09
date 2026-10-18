#!/usr/bin/env python3
"""Builds assets/commit-year.svg: a dark, themed 12-month contribution graph.

Usage: python scripts/build_commit_graph.py [github-username] [output.svg]
Uses only the standard library and GitHub's public contribution calendar.
"""
import datetime as dt
import html
import re
import sys
import urllib.request

USER = sys.argv[1] if len(sys.argv) > 1 else "Prince-Koladiya09"
OUT = sys.argv[2] if len(sys.argv) > 2 else "assets/commit-year.svg"

req = urllib.request.Request(
    f"https://github.com/users/{USER}/contributions",
    headers={"User-Agent": "Mozilla/5.0"},
)
page = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")

# ---- parse cells + per-day counts -------------------------------------------------
counts_by_id = {}
for tid, num in re.findall(
    r'<tool-tip[^>]*for="([^"]+)"[^>]*>\s*(No|\d+)\s+contributions?\s+on', page
):
    counts_by_id[tid] = 0 if num == "No" else int(num)

days = []
for tag in re.findall(r"<td [^>]*data-date=[^>]*>", page):
    date = re.search(r'data-date="([\d-]+)"', tag).group(1)
    cid = re.search(r'id="([^"]+)"', tag).group(1)
    level = int(re.search(r'data-level="(\d)"', tag).group(1))
    days.append((dt.date.fromisoformat(date), counts_by_id.get(cid, 0), level))
days.sort()
if not days:
    sys.exit("No contribution data found")

total = sum(c for _, c, _ in days)
best = max(days, key=lambda d: d[1])
longest = cur = 0
for _, c, _ in days:
    cur = cur + 1 if c > 0 else 0
    longest = max(longest, cur)
current = 0
for _, c, _ in reversed(days):
    if c > 0:
        current += 1
    elif current == 0 and _ == days[-1][0]:
        continue  # today may still be empty
    else:
        break

# ---- layout -----------------------------------------------------------------------
CELL, GAP = 12, 3
PITCH = CELL + GAP
LEFT, TOP = 58, 96
first = days[0][0]
offset = (first.weekday() + 1) % 7          # Sunday = 0
weeks = ((days[-1][0] - first).days + offset) // 7 + 1
W = LEFT + weeks * PITCH + 26
GRID_H = 7 * PITCH
H = TOP + GRID_H + 100

LEVELS = ["#18233A", "#4A2A45", "#8A3550", "#E0566B", "#F2A65A"]
FONT = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono','Fira Code',Consolas,Menlo,'DejaVu Sans Mono','Courier New',monospace"

cells, months, last_month = [], [], None
for d, c, lvl in days:
    wk = ((d - first).days + offset) // 7
    row = (d.weekday() + 1) % 7
    x, y = LEFT + wk * PITCH, TOP + row * PITCH
    delay = 0.2 + wk * 0.035
    cells.append(
        f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" fill="{LEVELS[lvl]}" opacity="0">'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="{delay:.2f}s" fill="freeze"/></rect>'
    )
    if d.day <= 7 and row == 0 and d.month != last_month:
        months.append(f'<text x="{x}" y="{TOP-10}">{d.strftime("%b")}</text>')
        last_month = d.month
    elif last_month is None:
        last_month = d.month

wd = "".join(
    f'<text x="{LEFT-12}" y="{TOP + r*PITCH + 10}" text-anchor="end">{n}</text>'
    for r, n in ((1, "Mon"), (3, "Wed"), (5, "Fri"))
)

legend_x = W - 26 - (5 * PITCH) - 70
legend = f'<text x="{legend_x}" y="{TOP+GRID_H+22}" text-anchor="end" fill="#9AA7BD">Less</text>' + "".join(
    f'<rect x="{legend_x+10+i*PITCH}" y="{TOP+GRID_H+11}" width="{CELL}" height="{CELL}" rx="3" fill="{c}"/>'
    for i, c in enumerate(LEVELS)
) + f'<text x="{legend_x+10+5*PITCH+6}" y="{TOP+GRID_H+22}" fill="#9AA7BD">More</text>'

def stat(x, value, label, color):
    return (f'<text x="{x}" y="{H-38}" font-size="24" font-weight="800" fill="{color}" font-family="{FONT}">{html.escape(value)}</text>'
            f'<text x="{x}" y="{H-18}" font-size="11.5" letter-spacing="1.5" fill="#9AA7BD">{html.escape(label)}</text>')

span = f'{days[0][0].strftime("%b %Y")} – {days[-1][0].strftime("%b %Y")}'
stats = (
    stat(LEFT, f"{total:,}", "CONTRIBUTIONS", "#7FB8E6")
    + stat(LEFT + 200, f"{best[1]}", f"BEST DAY · {best[0].strftime('%b %d').upper()}", "#E0566B")
    + stat(LEFT + 430, f"{longest} days", "LONGEST STREAK", "#F2A65A")
    + stat(LEFT + 620, f"{current} days", "CURRENT STREAK", "#F0C6CF")
)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{total} contributions in the last year">
  <defs>
    <clipPath id="r"><rect width="{W}" height="{H}" rx="16"/></clipPath>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B1220"/><stop offset="0.65" stop-color="#111B30"/><stop offset="1" stop-color="#1F1B33"/></linearGradient>
    <radialGradient id="g1" cx="1" cy="1" r="0.7"><stop offset="0" stop-color="#E0566B" stop-opacity="0.25"/><stop offset="1" stop-color="#E0566B" stop-opacity="0"/></radialGradient>
    <radialGradient id="g2" cx="0" cy="0" r="0.6"><stop offset="0" stop-color="#7FB8E6" stop-opacity="0.14"/><stop offset="1" stop-color="#7FB8E6" stop-opacity="0"/></radialGradient>
    <linearGradient id="ln" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#E0566B"/><stop offset="1" stop-color="#7FB8E6" stop-opacity="0"/></linearGradient>
  </defs>
  <g clip-path="url(#r)" font-family="{MONO}" font-size="12" fill="#9AA7BD">
    <rect width="{W}" height="{H}" fill="url(#bg)"/><rect width="{W}" height="{H}" fill="url(#g1)"/><rect width="{W}" height="{H}" fill="url(#g2)"/>
    <text x="{LEFT}" y="38" font-size="19" font-weight="800" fill="#F2F4F8" font-family="{FONT}" letter-spacing="1">COMMIT ACTIVITY · LAST 12 MONTHS</text>
    <text x="{LEFT}" y="58" font-size="12.5" fill="#9AA7BD">{html.escape(span)}  ·  github.com/{html.escape(USER)}</text>
    <rect x="{LEFT}" y="68" width="{W-LEFT-26}" height="2" fill="url(#ln)"/>
    {''.join(months)}{wd}
    {''.join(cells)}
    {legend}
    <rect x="{LEFT}" y="{H-70}" width="{W-LEFT-26}" height="1" fill="#25324D"/>
    {stats}
  </g>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="15" fill="none" stroke="#25324D" stroke-width="2"/>
</svg>'''

import os
os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
open(OUT, "w", encoding="utf-8").write(svg)
print(f"wrote {OUT}: {total} contributions, best {best[1]} on {best[0]}, longest {longest}, current {current}, {W}x{H}")
