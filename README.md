# Leaseway website

Leaseway's site on GitHub Pages: <https://coderalert0.github.io/leaseway-site/>. The app (private repo
coderalert0/leaseway-app) links to its support, privacy and terms pages, so keep those paths.

Everything in the repo root is generated: edit `src/`, then build and check.

    python3 -m venv .venv && .venv/bin/pip install markdown pillow     (or use ~/doorproof-site/.venv)
    .venv/bin/python src/build.py && python3 src/check.py            (--external also checks outside links)

- `src/pages/home.html`, `support.body.html`, `privacy.body.html`, `terms.body.html`: page bodies.
- `src/pages/guides/*.md`: guides, each with front matter and a Sources list; each also gets a `.md` copy for AI tools.
  `research/` holds the checked facts behind them.
- `src/states.json`: the states table (well counts, sizes, sources, data dates), taken from the live manifest
  `https://leaseway.5-78-157-32.sslip.io/v1/manifest.json`. Refresh it with the snippet at the top of `src/build.py`'s
  history or by hand when states are added; `UPDATED` in `src/build.py` is the date facts were last checked.
- `src/art/icon-1024.png`: the app icon (ChatGPT, option 1 of 5, Nov 22 2026). `src/art/shots/` + `shots.json`: App
  Store screenshots shown on the home page (none until the store set is made).
- `APP_ID` in `src/build.py`: empty means "Coming soon"; set it to the App Store Connect Apple ID once the record exists.

Search and AI: JSON-LD (MobileApplication, FAQPage, Article, BreadcrumbList), sitemap.xml, robots.txt naming the AI
crawlers, llms.txt and llms-full.txt, Markdown twins of the guides. Verification files in the root: Google
(`googlebcd67451a2e45ce3.html`, coderalert0's Search Console), Bing (`BingSiteAuth.xml`) and the IndexNow key
(`46e5f2425cc92a9e37d221a6b26acfaa.txt`). Support email is written by `site.js` so it isn't in the page source.
