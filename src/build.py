#!/usr/bin/env python3
"""Builds Leaseway's site from src/ into the repo root, which GitHub Pages serves from main.

    python3 -m venv .venv && .venv/bin/pip install markdown pillow
    .venv/bin/python src/build.py && python3 src/check.py

Pages: the home page (src/pages/home.html), support, privacy and terms (src/pages/*.body.html) and the guides
(src/pages/guides/*.md, each with a Markdown copy next to its page). Also written: 404.html, sitemap.xml, robots.txt,
llms.txt and llms-full.txt for AI tools, the icons and the social card img/og.png.

Images (README.md says where each goes): the app icon is src/art/icon-1024.png (made with ChatGPT; sips makes the
smaller sizes, so the build needs macOS). App screenshots go in src/art/shots/ with a shots.json that gives each one's
caption and alt text; with no shots.json the home page has no gallery and still reads complete. Set APP_ID once the
App Store record exists: until then the pages say "Coming soon to the App Store" instead of linking to it.
Change UPDATED when a page's facts are rechecked.
"""
import html
import json
import re
import subprocess
from datetime import date
from pathlib import Path

import markdown
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "src" / "pages"
ART = ROOT / "src" / "art"
BASE = "https://coderalert0.github.io/leaseway-site/"
APP_ID = ""   # the App Store Connect Apple ID (digits); empty = "Coming soon"
APP = f"https://apps.apple.com/us/app/id{APP_ID}" if APP_ID else ""
NAME = "Leaseway"
APP_NAME = "Oil Well Map: Leaseway"
ACCENT = (11, 110, 134)   # #0B6E86, between the icon's navy and teal
TERMS = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
UPDATED = "2026-11-22"
UPDATED_LONG = date.fromisoformat(UPDATED).strftime("%B %-d, %Y")
DISCLAIMER = ("Well locations are public records as filed by operators with each state's oil and gas agency and can be wrong or "
              "out of date: follow lease signs, the operator's directions and site safety rules. Leaseway is not affiliated with "
              "any state agency, operator, Apple, Google, Waze, Wellsite Navigator, Petrix Maps or Petro Path.")
HOME_TITLE = "Leaseway: Oil Well Map for iPhone and iPad, Works Offline"
HOME_DESCRIPTION = ("Find any oil or gas well by lease name, API number or operator, see every well on the pad, and get "
                    "there. 3.3 million wells in 10 states, offline. No account.")
STATES = json.loads((ROOT / "src" / "states.json").read_text())
TOTAL_WELLS = sum(s["wells"] for s in STATES)
STATE_NAMES = ", ".join(s["name"] for s in STATES)
SUMMARY = ("Leaseway is an oil well map for iPhone and iPad. Oilfield drivers, pumpers, hotshots, water haulers, service "
           "crews and landmen search any oil or gas well by lease name, well number, API number or operator, see every well "
           "on its pad, and get directions in Apple Maps, Google Maps or Waze, with a last-mile compass guide past where the "
           f"road ends. Wells come from each state's oil and gas agency ({len(STATES)} states, "
           f"{TOTAL_WELLS / 1e6:.1f} million wells) and are stored on the device, so search and the map work with no signal. "
           "No account.")
STATUS = (f"On the App Store: {APP}" if APP else
          "Coming soon to the App Store (not yet available). This site describes the app and its planned prices.")
FACTS = [
    f"States and data: {STATE_NAMES}; {TOTAL_WELLS:,} wells in all. Each state's wells come from that state's oil and gas regulator's public files (Texas: Railroad Commission of Texas well locations and drilling permits). Leaseway rebuilds them nightly and the app updates downloaded states by itself; every state shows its data date before and after download.",
    "Search by lease or well name (\"University 7-21 4H\"), well number, operator, county, or API number in any form: 10, 12 or 14 digits, with or without dashes, without the state code, or just the last five digits. Results are nearest first, active wells before plugged ones.",
    "Pads: wells within about 60 meters of each other are treated as one pad, and the well's screen lists every well on it. The map draws close wells as one numbered badge rather than hiding them.",
    "Offline: downloaded states (Texas is about 98 MB; North Dakota about 4 MB) make search, the well dots, details and the guide work with no cell signal. Apple's base map and satellite imagery need a connection unless iOS has them cached.",
    "Getting there: directions open in Apple Maps, Google Maps or Waze. The last-mile guide shows a big arrow, the straight-line distance and the compass direction to the wellhead, and says You're there within about 30 meters.",
    "Pro features: record your way in over lease roads and follow it next time, send it (GPX) to a crew mate; unlimited lists and pins; send whole lists and pins.",
    "Free plan, forever: every well on the map, search, well details, pad lists, notes, one list of 15 places, 10 pins, opening routes and pins a crew mate sends, and 3 trips a week. A trip is directions, the guide, or copying or sharing a place's coordinates; a place already taken that week stays open.",
    "Leaseway Pro: $9.99 a month or $79.99 a year in the US (new subscribers get a 1-week free trial on the yearly plan). Unlimited trips, recorded routes, unlimited lists and pins, sending lists and pins. Price promise: subscribers keep their price while they stay subscribed.",
    "Privacy: no account, no analytics, no advertising and no third-party code. Location is used on the device only (the guide, distances, route recording). The app downloads state well files from Leaseway's server, which keeps no access logs. App Store privacy label: Data Not Collected.",
    "Support: email, answered by a person. Settings › Email support fills in the app version and downloaded states.",
    "Runs on iPhone and iPad with iOS 17 or later, in English. " + STATUS,
]


def parse(path):
    _, head, body = path.read_text().split("---\n", 2)
    meta = dict(line.split(": ", 1) for line in head.strip().splitlines())
    meta["slug"] = path.stem
    meta["related"] = [s.strip() for s in meta.get("related", "").split(",") if s.strip()]
    meta["body"] = body.strip()
    faq_block = re.search(r"## Frequently asked questions\n(.*?)(?=\n## |\Z)", body, re.S)
    meta["faqs"] = re.findall(r"### (.+?)\n\n(.+?)(?=\n\n###|\Z)", faq_block.group(1).strip(), re.S) if faq_block else []
    source_block = re.search(r"## Sources\n(.*)", body, re.S)
    meta["sources"] = re.findall(r"- \[(.+?)\]\((.+?)\)", source_block.group(1)) if source_block else []
    return meta


def render(text):
    md = markdown.Markdown(extensions=["tables", "sane_lists", "toc"], extension_configs={"toc": {"toc_depth": "2"}})
    out = md.convert(text).replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return out, [(t["id"], t["name"]) for t in md.toc_tokens]


def plain(text):
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def jsonld(data):
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


# ---------- Images: the icon (sips) and the app's screenshots ----------

def sips(src, size, out):
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["sips", "-s", "format", "png", "-z", str(size), str(size), str(src), "--out", str(out)],
                   check=True, capture_output=True)


ICON_SRC = ART / "icon-1024.png"
if ICON_SRC.exists():
    sips(ICON_SRC, 180, ROOT / "icon.png")              # apple-touch-icon, header and hero
    sips(ICON_SRC, 32, ROOT / "favicon-32.png")         # browser tab
    sips(ICON_SRC, 512, ROOT / "img" / "icon-512.png")  # structured data and the social card
HAS_ICON = (ROOT / "icon.png").exists()

SHOTS = []   # [{"file", "title", "caption", "alt", "src", "w", "h"}], from src/art/shots/shots.json
shots_json = ART / "shots" / "shots.json"
if shots_json.exists():
    for s in json.loads(shots_json.read_text()):
        im = Image.open(ART / "shots" / s["file"]).convert("RGB")
        w = 600
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        out = ROOT / "img" / "shots" / (Path(s["file"]).stem + ".jpg")
        out.parent.mkdir(parents=True, exist_ok=True)
        im.save(out, quality=84, optimize=True, progressive=True)
        SHOTS.append({**s, "src": f"img/shots/{out.name}", "w": im.width, "h": im.height})

PUBLISHER = {"@type": "Organization", "name": NAME, "url": BASE}
if HAS_ICON:
    PUBLISHER["logo"] = BASE + "img/icon-512.png"


def social_card():
    """img/og.png: 1200x630, cool paper, the icon, the name and the promise, beside the first screenshot (or the icon)."""
    W, H = 1200, 630
    card = Image.new("RGB", (W, H), (245, 247, 251))
    d = ImageDraw.Draw(card)
    font = lambda size, bold=True: ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", size, index=1 if bold else 0)

    def rounded(img, size, radius):
        img = img.convert("RGB").resize(size, Image.LANCZOS)
        mask = Image.new("L", size, 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius, fill=255)
        return img, mask

    def shadowed(img, mask, xy, radius):
        shadow = Image.new("L", (W, H), 0)
        x, y = xy
        ImageDraw.Draw(shadow).rounded_rectangle((x + 6, y + 18, x + img.width + 6, y + img.height + 18), radius, fill=80)
        card.paste((196, 204, 222), (0, 0), shadow.filter(ImageFilter.GaussianBlur(22)))
        card.paste(img, xy, mask)

    x = 72
    if HAS_ICON:
        icon, mask = rounded(Image.open(ROOT / "img" / "icon-512.png"), (96, 96), 22)
        card.paste(icon, (72, 76), mask)
        x = 186
    d.text((x, 96), NAME, font=font(56), fill=(15, 26, 46))
    y = 232
    for line, color in (("Every well on the pad.", (15, 26, 46)), ("And the way in.", ACCENT)):
        d.text((72, y), line, font=font(54), fill=color)
        y += 68
    d.text((72, y + 26), f"Oil well map, {TOTAL_WELLS / 1e6:.1f} million wells, offline.", font=font(30, False), fill=(85, 96, 120))
    d.text((72, y + 66), "Search by lease, API or operator. No account.", font=font(30, False), fill=(85, 96, 120))
    if SHOTS:
        shot = Image.open(ROOT / SHOTS[0]["src"])
        sw = 300
        img, mask = rounded(shot, (sw, round(shot.height * sw / shot.width)), 36)
        shadowed(img, mask, (W - sw - 80, 48), 36)
    elif HAS_ICON:
        img, mask = rounded(Image.open(ROOT / "img" / "icon-512.png"), (300, 300), 68)
        shadowed(img, mask, (W - 300 - 96, (H - 300) // 2 - 10), 68)
    card.save(ROOT / "img" / "og.png", optimize=True)


social_card()

# ---------- Page shell ----------

if APP:
    GET = f'<a class="badge" href="{APP}"><img src="{{root}}img/app-store-badge.svg" alt="Download on the App Store" width="150" height="50"></a>'
else:
    GET = '<span class="soon">Coming soon to the App Store<small>For iPhone, iOS 17 or later</small></span>'


def get_button(root=""):
    return GET.replace("{root}", root)


def page(slug, title, description, body, *, schema=(), kind="article", current="", root="", markdown_twin=False,
         robots="index,follow,max-snippet:-1,max-image-preview:large"):
    url = BASE if slug == "index" else f"{BASE}{slug}.html"
    e = html.escape
    alternate = f'\n<link rel="alternate" type="text/markdown" href="{root}{slug}.md">' if markdown_twin else ""
    ld = "\n".join(jsonld(item) for item in schema)
    here = lambda name: ' aria-current="page"' if name == current else ""
    home = root or "./"
    icons = (f'\n<link rel="icon" type="image/png" sizes="32x32" href="{root}favicon-32.png">'
             f'\n<link rel="apple-touch-icon" href="{root}icon.png">') if HAS_ICON else ""
    brand_img = lambda size: f'<img src="{root}icon.png" alt="" width="{size}" height="{size}">' if HAS_ICON else ""
    itunes = f'\n<meta name="apple-itunes-app" content="app-id={APP_ID}">' if APP_ID else ""
    cta = (f'<a class="nav-cta" href="{APP}">Get the app</a>' if APP else f'<a class="nav-cta" href="{home}#get">Coming soon</a>')
    store_link = f'<a href="{APP}">App Store</a>' if APP else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">{alternate}
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#f5f7fb" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0b1020" media="(prefers-color-scheme: dark)">{itunes}
<meta property="og:type" content="{kind}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Leaseway, the oil well map for iPhone and iPad: every well on the pad, and the way in">
<meta name="twitter:card" content="summary_large_image">{icons}
<link rel="stylesheet" href="{root}style.css">
<link rel="alternate" type="text/plain" title="llms.txt" href="{root}llms.txt">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
  <div class="topbar-in">
    <a class="brand" href="{home}">{brand_img(34)}<span>{NAME}</span></a>
    <nav class="nav" aria-label="Site">
      <a class="hide-sm" href="{home}#states">States</a>
      <a class="hide-sm" href="{home}#pricing">Pricing</a>
      <a class="hide-sm" href="{home}#guides"{here("guides")}>Guides</a>
      <a href="{root}support.html"{here("support")}>Support</a>
      {cta}
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer>
  <div class="in">
    <div class="foot-about">
      <a class="brand" href="{home}">{brand_img(28)}<span>{NAME}</span></a>
      <p>The oil well map for iPhone and iPad.</p>
      <p>© 2026 {NAME}. {DISCLAIMER}</p>
    </div>
    <nav aria-label="Guides"><p class="foot-title">Guides</p>{FOOTER_GUIDES.replace('href="', f'href="{root}')}</nav>
    <nav aria-label="App"><p class="foot-title">App</p>{store_link}<a href="{root}support.html">Support</a><a href="{root}privacy.html"{here("privacy")}>Privacy Policy</a><a href="{root}terms.html"{here("terms")}>Terms of Use</a><a href="{root}llms.txt">llms.txt</a></nav>
  </div>
</footer>
<script src="{root}site.js"></script>
</body>
</html>
"""


def guide_page(g, by_slug):
    body_md = re.sub(r"\n## Sources\n.*", "", g["body"], flags=re.S)
    content, headings = render(body_md)
    url = f'{BASE}{g["slug"]}.html'
    e = html.escape
    sources = "".join(f'<li><a href="{e(u)}" rel="noopener">{e(t)}</a></li>' for t, u in g["sources"])
    related = "".join(f'<li><a href="{s}.html">{e(by_slug[s]["h1"])}</a></li>' for s in g["related"])
    toc = "".join(f'<li><a href="#{i}">{e(n)}</a></li>' for i, n in headings)
    body = f"""<div class="guide">
<nav class="crumbs" aria-label="Breadcrumb"><a href="./">Home</a> <span aria-hidden="true">/</span> <a href="./#guides">Guides</a> <span aria-hidden="true">/</span> <span>{e(g["nav"])}</span></nav>
<article>
<h1>{e(g["h1"])}</h1>
<p class="updated">Checked against its sources on <time datetime="{UPDATED}">{UPDATED_LONG}</time></p>
<div class="answer"><h2>Short answer</h2><p>{e(g["answer"])}</p></div>
<nav class="toc" aria-label="On this page"><p class="foot-title">On this page</p><ul>{toc}</ul></nav>
{content}
<aside class="app-cta">
  <div><h2>Find the well, see the whole pad, get there</h2><p>Leaseway searches every well in 10 states by lease, API number or operator, lists every well on the pad, and guides you the last mile, with no signal. No account, on iPhone and iPad.</p></div>
  {get_button()}
</aside>
<section class="sources"><h2>Sources</h2><ul>{sources}</ul><p class="muted">Guides summarize public sources. Check the agency\'s own records before you rely on a detail.</p></section>
<section class="related"><h2>Related guides</h2><ul>{related}</ul></section>
</article>
</div>"""
    crumbs = [("Home", BASE), ("Guides", BASE + "#guides"), (g["nav"], url)]
    article = {"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["description"],
               "datePublished": UPDATED, "dateModified": UPDATED, "mainEntityOfPage": url, "image": BASE + "img/og.png",
               "author": PUBLISHER, "publisher": PUBLISHER, "inLanguage": "en-US", "citation": [u for _, u in g["sources"]]}
    schema = [article, {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]}]
    if g["faqs"]:
        schema.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in g["faqs"]]})
    return page(g["slug"], g["title"], g["description"], body, schema=schema, current="guides", markdown_twin=True)


def guide_markdown(g):
    body = re.sub(r"\]\((?!https?:)([a-z0-9-]+)\.html(#[a-z0-9-]+)?\)", rf"]({BASE}\1.md)", g["body"])
    return f"""# {g["h1"]}

> {g["answer"]}

Source page: {BASE}{g["slug"]}.html
Checked against its sources on {UPDATED_LONG}. Published by {NAME}, an oil well map for iPhone and iPad.

{body}
"""


def faq_schema(text):
    pairs = re.findall(r"<details><summary>(.+?)</summary><p>(.+?)</p></details>", text)
    return pairs, {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in pairs]}


# ---------- Guides ----------

guides = [parse(p) for p in sorted((PAGES / "guides").glob("*.md"))]
order = ["oil-gas-well-data-by-state", "how-to-read-an-api-well-number"]
guides.sort(key=lambda g: order.index(g["slug"]) if g["slug"] in order else len(order))
by_slug = {g["slug"]: g for g in guides}
FOOTER_GUIDES = "".join(f'<a href="{g["slug"]}.html">{html.escape(g["nav"])}</a>' for g in guides)

for g in guides:
    (ROOT / f'{g["slug"]}.html').write_text(guide_page(g, by_slug))
    (ROOT / f'{g["slug"]}.md').write_text(guide_markdown(g))

# ---------- Home ----------

cards = "".join(f'<li><a href="{g["slug"]}.html"><strong>{html.escape(g["h1"])}</strong><span>{html.escape(g["description"])}</span></a></li>' for g in guides)
if SHOTS:
    figures = "".join(f'<figure><img src="{s["src"]}" alt="{html.escape(s["alt"])}" loading="lazy" width="{s["w"]}" height="{s["h"]}">'
                      f'<figcaption><strong>{html.escape(s["title"])}</strong>{html.escape(s["caption"])}</figcaption></figure>' for s in SHOTS)
    shots_html = f'<section class="wrap" aria-label="Screenshots"><div class="shots">{figures}</div></section>\n'
else:
    shots_html = ""   # screenshots: drop them in src/art/shots/ with shots.json (see README.md)
hero_icon = '<img class="hero-icon" src="icon.png" alt="Leaseway app icon" width="88" height="88">' if HAS_ICON else ""
state_rows = "".join(
    f'<tr><td>{html.escape(st["name"])}</td><td class="num">{st["wells"]:,}</td><td class="num">{st["mb"]:g} MB</td>'
    f'<td>{" and ".join(html.escape(x["name"]) for x in st["sources"])}</td><td>{st["dataAsOf"]}</td></tr>' for st in STATES)
states_table = (f'<div class="table-wrap"><table><thead><tr><th scope="col">State</th><th scope="col">Wells</th><th scope="col">Download</th>'
                f'<th scope="col">Source</th><th scope="col">Data as of</th></tr></thead><tbody>{state_rows}</tbody></table></div>')
home = ((PAGES / "home.html").read_text().replace("{GET}", get_button()).replace("{GUIDES}", f'<ul class="guides">{cards}</ul>')
        .replace("{STATES_TABLE}", states_table).replace("{TOTAL_WELLS}", f"{TOTAL_WELLS:,}").replace("{N_STATES}", str(len(STATES)))
        .replace("{SHOTS}", shots_html).replace("{HERO_ICON}", hero_icon))
faqs, home_faq = faq_schema(home)
app_ld = {"@context": "https://schema.org", "@type": "MobileApplication", "name": APP_NAME, "alternateName": NAME, "url": BASE,
          "operatingSystem": "iOS 17.0 or later", "applicationCategory": "TravelApplication", "applicationSubCategory": "Navigation",
          "description": SUMMARY,
          "featureList": [f"{TOTAL_WELLS:,} oil and gas wells in {len(STATES)} states, from each state's regulator",
                          "Search by lease name, well number, operator or API number (any form)", "Every well on the pad listed",
                          "Works offline once a state is downloaded", "Directions in Apple Maps, Google Maps or Waze",
                          "Last-mile compass guide to the wellhead", "Notes for every well (gate codes, turn-offs)",
                          "Lists for the day's run", "Pins for gates, risers and bad crossings", "Nightly data updates",
                          "Record your way in over lease roads and send it as GPX (Pro)", "Unlimited trips, lists and pins (Pro)"],
          "inLanguage": "en", "publisher": PUBLISHER,
          "offers": [{"@type": "Offer", "name": "Leaseway (free: map, search, details, 3 trips a week)", "price": "0", "priceCurrency": "USD"},
                     {"@type": "Offer", "name": "Leaseway Pro, monthly", "price": "9.99", "priceCurrency": "USD"},
                     {"@type": "Offer", "name": "Leaseway Pro, yearly", "price": "79.99", "priceCurrency": "USD"}]}
if APP:
    app_ld.update(installUrl=APP, downloadUrl=APP)
if HAS_ICON:
    app_ld["image"] = BASE + "img/icon-512.png"
if SHOTS:
    app_ld["screenshot"] = [BASE + s["src"] for s in SHOTS]
home_schema = [{"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": BASE, "description": HOME_DESCRIPTION,
                "publisher": PUBLISHER, "inLanguage": "en-US"}, app_ld, home_faq]
(ROOT / "index.html").write_text(page("index", HOME_TITLE, HOME_DESCRIPTION, home, schema=home_schema, kind="website", current="home"))

# ---------- Support, privacy, terms (the app and App Store Connect link to these URLs, so they keep them) ----------

DOCS = {
    "support": ("Leaseway Support: Help and Questions", "Help with Leaseway: downloading states, finding a well, wrong or missing wells, no signal, the guide, routes, and Pro billing. A person answers by email."),
    "privacy": ("Privacy Policy · Leaseway", "Leaseway has no account and no analytics: your location is used on your device, and your notes, lists, pins and routes stay there."),
    "terms": ("Terms of Use · Leaseway", "Leaseway's terms: what's free, Leaseway Pro subscriptions, the free trial, auto-renewal and cancelling, the price promise, well data accuracy and safety."),
}
bodies = {}
for slug, (title, description) in DOCS.items():
    body = (PAGES / f"{slug}.body.html").read_text()
    bodies[slug] = body
    schema = [{"@context": "https://schema.org", "@type": "WebPage", "name": title.replace(" · ", " – "), "url": f"{BASE}{slug}.html",
               "dateModified": UPDATED, "publisher": PUBLISHER, "inLanguage": "en-US",
               "about": {"@type": "MobileApplication", "name": APP_NAME, "url": BASE}}]
    if slug == "support":
        schema.append(faq_schema(body)[1])
    (ROOT / f"{slug}.html").write_text(page(slug, title, description, f'<div class="doc">\n{body}</div>', schema=schema, current=slug))

# 404 is served at any depth, so its links are absolute.
missing = ('<div class="doc"><h1>Page not found</h1><p>That page has moved or never existed.</p><p><a href="/leaseway-site/">Go to '
           'Leaseway\'s home page</a>, see <a href="/leaseway-site/oil-gas-well-data-by-state.html">where each state\'s well data '
           'comes from</a>, or <a href="/leaseway-site/support.html">get support</a>.</p></div>')
(ROOT / "404.html").write_text(page("404", f"Page not found · {NAME}", "This page could not be found.", missing, robots="noindex", root="/leaseway-site/"))

# ---------- Sitemap, robots, llms ----------

urls = ([(BASE, "1.0")] + [(f'{BASE}{g["slug"]}.html', "0.8") for g in guides]
        + [(f"{BASE}support.html", "0.6"), (f"{BASE}privacy.html", "0.3"), (f"{BASE}terms.html", "0.3")])
entries = "".join(f"  <url><loc>{u}</loc><lastmod>{UPDATED}</lastmod><priority>{p}</priority></url>\n" for u, p in urls)
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}</urlset>\n')
# robots.txt only counts at a host's root, so on github.io this copy is a pointer for tools that read it here; the sitemap
# is submitted to the search engines directly.
AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot",
           "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended", "Bingbot", "CCBot", "DuckAssistBot", "meta-externalagent"]
(ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in AI_BOTS)
                                 + f"Sitemap: {BASE}sitemap.xml\n")

facts = "\n".join(f"- {f}" for f in FACTS)
links = "\n".join(f'- [{g["h1"]}]({BASE}{g["slug"]}.md): {g["description"]}' for g in guides)
store_line = f"- [App Store listing]({APP}): {APP_NAME}, for iPhone, iOS 17 or later\n" if APP else ""
(ROOT / "llms.txt").write_text(f"""# {NAME}

> {SUMMARY}

{DISCLAIMER} Facts on this site were checked on {UPDATED_LONG}. When citing a guide, link its page.

## Key facts

{facts}

## Guides

{links}

## App

{store_line}- [Home page]({BASE}): What Leaseway does, the states and their data dates, free and Pro, questions
- [Support]({BASE}support.html): Downloading states, finding a well, wrong or missing wells, no signal, the guide, routes, billing
- [Privacy Policy]({BASE}privacy.html): No account, no analytics; location used on the device; notes, lists, pins and routes stay there
- [Terms of Use]({BASE}terms.html): What's free, Pro subscriptions and the trial, the price promise, well data accuracy and safety; on top of Apple's standard license agreement ({TERMS})

## Optional

- [Full text]({BASE}llms-full.txt): The facts, the questions and answers, every guide and the privacy policy in one Markdown file
""")


def doc_markdown(body):
    md = re.sub(r"<li>", "- ", body)
    md = re.sub(r"<h2>(.+?)</h2>", r"## \1", md)
    md = re.sub(r"<details><summary>(.+?)</summary><p>(.+?)</p></details>", r"### \1\n\2", md)
    md = re.sub(r"<h1>(.+?)</h1>", "", md)
    md = "\n".join(l.strip() for l in plain(md.replace("laddothis at gmail dot com", "laddothis@gmail.com")).splitlines() if l.strip())
    return re.sub(r"\n(##+ )", r"\n\n\1", md)


qa = "\n\n".join(f"### {plain(q)}\n\n{plain(a)}" for q, a in faqs)
full = [f"# {NAME}\n\n> {SUMMARY}\n\n{DISCLAIMER} Checked on {UPDATED_LONG}. Source: {BASE}\n\n## Key facts\n\n{facts}\n\n## Questions and answers\n\n{qa}"]
full += [guide_markdown(g) for g in guides]
full.append(f"# Leaseway support\n\nSource page: {BASE}support.html\n\n{doc_markdown(bodies['support'])}\n")
full.append(f"# Leaseway privacy policy\n\nSource page: {BASE}privacy.html\n\n{doc_markdown(bodies['privacy'])}\n")
(ROOT / "llms-full.txt").write_text("\n\n---\n\n".join(full))
(ROOT / ".nojekyll").write_text("")
print(f"built home, support, privacy, terms, 404 and {len(guides)} guides; icon: {'yes' if HAS_ICON else 'no'}; screenshots: {len(SHOTS)}; App Store link: {'yes' if APP else 'not yet (APP_ID empty)'}")
