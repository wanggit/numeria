#!/usr/bin/env python3
"""Build privacy/index.html for the Numeria GitHub Pages site.

Renders one self-contained HTML document holding the privacy policy in all
nine App Store localisations. No external assets: no CDN, no webfont, no
analytics, no tracker. Everything (CSS + JS + text) is inline so the page
cannot leak a visitor beyond the GitHub Pages access log already disclosed
in section 5 of the policy itself.

Usage:
    python3 tools/build_privacy.py            # writes privacy/index.html
    python3 tools/build_privacy.py --check    # validate only, no write
"""

import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content_en_zh import EN, ZH, PAGES_URL, SUPPORT_URL  # noqa: E402
from content_ja_ar import JA, AR  # noqa: E402
from content_eu_hi import ES, PT, FR, DE, HI  # noqa: E402

# Display order: primary language first, then CJK, then European, then the
# remaining scripts. Mirrors lib/l10n ordering in the app.
LANGS = [EN, ZH, JA, AR, ES, PT, FR, DE, HI]

REPO_URL = "https://github.com/wanggit/numeria"

# --------------------------------------------------------------------------
# Static chrome (language-neutral, so it lives outside the translation dicts)
# --------------------------------------------------------------------------

CHROME = {
    "lang_picker_label": {
        "en": "Language", "zh": "语言", "ja": "言語", "ar": "اللغة",
        "es": "Idioma", "pt": "Idioma", "fr": "Langue", "de": "Sprache",
        "hi": "भाषा",
    },
    "footer_source": {
        "en": "Source and issue tracker",
        "zh": "源代码与问题反馈",
        "ja": "ソースと課題管理",
        "ar": "المصدر ومتتبع المشاكل",
        "es": "Código fuente y seguimiento de incidencias",
        "pt": "Código-fonte e rastreador de problemas",
        "fr": "Source et suivi des anomalies",
        "de": "Quellcode und Issue-Tracker",
        "hi": "स्रोत और समस्या ट्रैकर",
    },
    "skip_to_content": {
        "en": "Skip to content", "zh": "跳到正文", "ja": "本文へスキップ",
        "ar": "تخطَّ إلى المحتوى", "es": "Saltar al contenido",
        "pt": "Pular para o conteúdo", "fr": "Aller au contenu",
        "de": "Zum Inhalt springen", "hi": "सामग्री पर जाएँ",
    },
}


def esc(text):
    """Escape for use in an HTML attribute value."""
    return html.escape(text, quote=True)


def render_block(block, lang_code):
    """Turn one content block into HTML.

    Deliberately uses str.replace-free concatenation: translated payloads may
    contain characters that %-formatting and str.format both treat as special.
    """
    kind, payload = block

    if kind == "h2":
        return '      <h2>' + payload + '</h2>\n'

    if kind == "p":
        return '      <p>' + payload + '</p>\n'

    if kind == "ul":
        items = "\n".join('        <li>' + it + '</li>' for it in payload)
        return '      <ul>\n' + items + '\n      </ul>\n'

    if kind == "note":
        return ('      <aside class="note" role="note">\n'
                '        <span class="note-mark" aria-hidden="true">!</span>\n'
                '        <div>' + payload + '</div>\n'
                '      </aside>\n')

    if kind == "table":
        head = "\n".join('          <th scope="col">' + h + '</th>'
                         for h in payload["head"])
        rows = []
        for row in payload["rows"]:
            cells = "\n".join('          <td>' + c + '</td>' for c in row)
            rows.append('        <tr>\n' + cells + '\n        </tr>')
        body = "\n".join(rows)
        caption = esc(CHROME["lang_picker_label"][lang_code])
        return (
            '      <div class="table-wrap">\n'
            '      <table>\n'
            '        <caption class="visually-hidden">' + caption + '</caption>\n'
            '        <thead>\n        <tr>\n' + head + '\n        </tr>\n        </thead>\n'
            '        <tbody>\n' + body + '\n        </tbody>\n'
            '      </table>\n'
            '      </div>\n'
        )

    raise ValueError("unknown block kind: " + repr(kind))


def render_panel(spec):
    """Render one <section class="panel"> for a single language."""
    code = spec["code"]
    blocks = "".join(render_block(b, code) for b in spec["blocks"])

    parts = [
        '  <section class="panel" id="' + code + '" lang="' + esc(spec["html_lang"]) + '"',
        '           dir="' + spec["dir"] + '" aria-labelledby="' + code + '-h1">\n',
        '    <header class="doc-head">\n',
        '      <h1 id="' + code + '-h1">' + spec["h1"] + '</h1>\n',
        '      <p class="product">' + spec["product"] + '</p>\n',
        '      <p class="effective"><time>' + spec["effective"] + '</time></p>\n',
        '    </header>\n\n',
        '    <div class="tldr">\n',
        '      <h2 class="tldr-head">' + spec["tldr_head"] + '</h2>\n',
        '      <p>' + spec["tldr"] + '</p>\n',
        '    </div>\n\n',
        blocks,
        '\n    <div class="disclaimer">\n',
        '      <h2>' + spec["disclaimer_head"] + '</h2>\n',
        '      <p>' + spec["disclaimer"] + '</p>\n',
        '    </div>\n',
        '  </section>\n',
    ]
    return "".join(parts)


def render_nav():
    links = []
    for spec in LANGS:
        links.append(
            '      <a href="#' + spec["code"] + '" data-lang="' + spec["code"] + '"'
            ' lang="' + esc(spec["html_lang"]) + '" hreflang="' + esc(spec["html_lang"]) + '"'
            ' title="' + esc(spec["label"]) + '">' + esc(spec["label"]) + '</a>'
        )
    return "\n".join(links)


CSS = r"""
:root {
  --bg: #fbfbfd;
  --surface: #ffffff;
  --ink: #1d1d1f;
  --ink-soft: #515154;
  --ink-faint: #86868b;
  --line: #d2d2d7;
  --line-soft: #e8e8ed;
  --accent: #1a56db;
  --accent-soft: #eef2ff;
  --note-bg: #f0f7ff;
  --note-line: #b6d0f7;
  --warn-bg: #fffbf0;
  --warn-line: #f0dcae;
  --radius: 14px;
  --max: 46rem;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0b0b0d;
    --surface: #161618;
    --ink: #f5f5f7;
    --ink-soft: #c7c7cc;
    --ink-faint: #8e8e93;
    --line: #2c2c2e;
    --line-soft: #232325;
    --accent: #7aa2f7;
    --accent-soft: #17203a;
    --note-bg: #111a2c;
    --note-line: #24406e;
    --warn-bg: #231d10;
    --warn-line: #5a4722;
  }
}

* { box-sizing: border-box; }

html {
  -webkit-text-size-adjust: 100%;
  scroll-behavior: smooth;
  /* Reserve the sticky topbar's height so native anchor jumps (and the
     browser's own scroll-to-hash on load) never hide a heading under it.
     The topbar is one row on wide screens, two rows once the nine language
     pills wrap, hence the responsive value. */
  scroll-padding-top: 5.5rem;
}

@media (max-width: 63.99rem) {
  html { scroll-padding-top: 11rem; }
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans", "Noto Sans Arabic",
    "Noto Sans Devanagari", "Noto Sans Hebrew", "Hiragino Sans",
    "Hiragino Kaku Gothic ProN", "PingFang SC", "Microsoft YaHei",
    "Yu Gothic", sans-serif;
  font-size: 17px;
  line-height: 1.68;
  font-kerning: normal;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

/* ---------- top bar ---------- */

.topbar {
  position: sticky;
  top: 0;
  z-index: 10;
  background: color-mix(in srgb, var(--surface) 86%, transparent);
  -webkit-backdrop-filter: saturate(180%) blur(14px);
  backdrop-filter: saturate(180%) blur(14px);
  border-bottom: 1px solid var(--line-soft);
}

@supports not (background: color-mix(in srgb, red, blue)) {
  .topbar { background: var(--surface); }
}

.topbar-inner {
  /* Wider than the reading column on purpose: nine language pills plus the
     brand fit on one row at >=1024px, and wrap gracefully below that. */
  max-width: 72rem;
  margin: 0 auto;
  padding: 0.7rem 1.25rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  font-weight: 650;
  letter-spacing: -0.015em;
  color: var(--ink);
  text-decoration: none;
  flex: 0 0 auto;
}

.brand-mark {
  display: grid;
  place-items: center;
  width: 1.7rem;
  height: 1.7rem;
  border-radius: 8px;
  background: linear-gradient(150deg, #2f6ff0, #1a3fa8);
  color: #fff;
  font-size: 0.95rem;
  font-weight: 700;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.22);
}

.langs {
  display: flex;
  gap: 0.25rem;
  flex-wrap: wrap;
  margin-inline-start: auto;
}

.langs a {
  padding: 0.22rem 0.6rem;
  border-radius: 999px;
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--ink-soft);
  text-decoration: none;
  border: 1px solid transparent;
  transition: background 0.15s, color 0.15s, border-color 0.15s;
  white-space: nowrap;
}

.langs a:hover { background: var(--line-soft); color: var(--ink); }
.langs a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

.langs a[aria-current="true"] {
  background: var(--accent-soft);
  color: var(--accent);
  border-color: color-mix(in srgb, var(--accent) 30%, transparent);
  font-weight: 600;
}

@supports not (background: color-mix(in srgb, red, blue)) {
  .langs a[aria-current="true"] { border-color: var(--accent); }
}

/* ---------- document ---------- */

main {
  max-width: var(--max);
  margin: 0 auto;
  padding: 2.25rem 1.25rem 3rem;
}

.panel { animation: fade 0.22s ease-out; }

@keyframes fade {
  from { opacity: 0; transform: translateY(3px); }
  to   { opacity: 1; transform: none; }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .panel { animation: none; }
}

.doc-head { margin-bottom: 1.75rem; }

h1 {
  margin: 0 0 0.6rem;
  font-size: clamp(1.85rem, 5.5vw, 2.4rem);
  line-height: 1.18;
  letter-spacing: -0.028em;
  font-weight: 700;
}

.product {
  margin: 0;
  font-size: 0.9375rem;
  color: var(--ink-soft);
}

.effective {
  margin: 0.3rem 0 0;
  font-size: 0.8125rem;
  color: var(--ink-faint);
  font-variant-numeric: tabular-nums;
}

h2 {
  margin: 2.1rem 0 0.6rem;
  font-size: 1.22rem;
  line-height: 1.35;
  letter-spacing: -0.015em;
  font-weight: 650;
}

p { margin: 0 0 0.95rem; }

ul {
  margin: 0 0 1.05rem;
  padding-inline-start: 1.35rem;
}

li { margin-bottom: 0.4rem; }
li::marker { color: var(--ink-faint); }

a { color: var(--accent); text-decoration-thickness: 1px; text-underline-offset: 2px; }
a:hover { text-decoration-thickness: 2px; }

strong { font-weight: 650; }

/* ---------- callouts ---------- */

.tldr, .note, .disclaimer {
  border-radius: var(--radius);
  padding: 1.1rem 1.25rem;
  margin: 0 0 1.4rem;
}

.tldr {
  background: var(--accent-soft);
  border: 1px solid color-mix(in srgb, var(--accent) 22%, transparent);
}

.tldr-head {
  margin: 0 0 0.35rem;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: var(--accent);
}

.tldr p { margin: 0; font-size: 1.02rem; }

@supports not (background: color-mix(in srgb, red, blue)) {
  .tldr { border-color: var(--accent); }
}

.note {
  display: flex;
  gap: 0.85rem;
  align-items: flex-start;
  background: var(--note-bg);
  border: 1px solid var(--note-line);
}

.note-mark {
  flex: 0 0 auto;
  display: grid;
  place-items: center;
  width: 1.35rem;
  height: 1.35rem;
  margin-top: 0.18rem;
  border-radius: 50%;
  background: var(--accent);
  color: #fff;
  font-size: 0.85rem;
  font-weight: 700;
  line-height: 1;
}

.note div { flex: 1 1 auto; }
.note p:last-child { margin-bottom: 0; }

.disclaimer {
  background: var(--warn-bg);
  border: 1px solid var(--warn-line);
  margin-top: 2.5rem;
}

.disclaimer h2 {
  margin: 0 0 0.4rem;
  font-size: 0.98rem;
}

.disclaimer p { margin: 0; font-size: 0.9375rem; color: var(--ink-soft); }

/* ---------- table ---------- */

.table-wrap {
  margin: 0 0 1.4rem;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  overflow: hidden;
  background: var(--surface);
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9375rem;
}

caption { text-align: start; }

th, td {
  padding: 0.72rem 0.95rem;
  text-align: start;
  vertical-align: top;
  border-bottom: 1px solid var(--line-soft);
}

thead th {
  background: var(--line-soft);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ink-soft);
}

tbody tr:last-child td { border-bottom: 0; }
tbody tr:nth-child(even) { background: color-mix(in srgb, var(--line-soft) 45%, transparent); }

@supports not (background: color-mix(in srgb, red, blue)) {
  tbody tr:nth-child(even) { background: var(--line-soft); }
}

td:first-child { font-weight: 550; width: 46%; }

/* On narrow screens the table becomes stacked cards. */
@media (max-width: 34rem) {
  .table-wrap { border: 0; background: transparent; }
  table, tbody, tr, td { display: block; width: 100%; }
  thead { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
  tbody tr {
    border: 1px solid var(--line);
    border-radius: 12px;
    background: var(--surface);
    padding: 0.35rem 0;
    margin-bottom: 0.6rem;
  }
  td { border: 0; padding: 0.4rem 0.9rem; }
  td:first-child { width: 100%; }
  td:last-child { color: var(--ink-soft); font-size: 0.875rem; }
}

/* ---------- footer ---------- */

footer.site {
  border-top: 1px solid var(--line-soft);
  background: var(--surface);
  padding: 1.6rem 1.25rem 2.4rem;
  font-size: 0.8125rem;
  color: var(--ink-faint);
}

footer.site .inner {
  max-width: var(--max);
  margin: 0 auto;
  display: flex;
  gap: 0.5rem 1.5rem;
  flex-wrap: wrap;
  align-items: baseline;
}

footer.site a { color: var(--ink-soft); }

/* ---------- a11y helpers ---------- */

.visually-hidden {
  position: absolute;
  width: 1px; height: 1px;
  margin: -1px; padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.skip {
  position: absolute;
  inset-inline-start: 1rem;
  top: -4rem;
  z-index: 20;
  padding: 0.5rem 0.9rem;
  border-radius: 8px;
  background: var(--accent);
  color: #fff;
  font-size: 0.875rem;
  text-decoration: none;
  transition: top 0.15s;
}

.skip:focus { top: 0.75rem; }

/* RTL: flip the visual rhythm without touching logical properties above. */
[dir="rtl"] body { line-height: 1.85; }
[dir="rtl"] .note-mark { font-style: normal; }

/* ---------- panel visibility ---------- */

/* With scripting ON, .is-active is the single source of truth. */
.js .panel { display: none; }
.js .panel.is-active { display: block; }

/* With scripting OFF the .js class is never added, so :target drives the
   switch instead. Scoped to html:not(.js) on purpose: unscoped, the
   `main:not(:has(...)) .panel:not(#en)` rule below carries an ID in its
   :not() and would out-specify `.js .panel.is-active`, breaking clicks. */
html:not(.js) main:has(.panel:target) .panel:not(:target) { display: none; }
html:not(.js) main:not(:has(.panel:target)) .panel:not(#en) { display: none; }

/* ---------- print ---------- */

@media print {
  .topbar, .skip, footer.site { display: none !important; }
  body { background: #fff; color: #000; font-size: 11pt; }
  main { max-width: none; padding: 0; }
  .js .panel { display: none !important; }
  .js .panel.is-active { display: block !important; }
  .tldr, .note, .disclaimer, .table-wrap { border-color: #999; background: #fff; }
  a { color: #000; text-decoration: underline; }
  a[href^="http"]::after { content: " (" attr(href) ")"; font-size: 9pt; color: #444; }
  h2 { break-after: avoid; }
  tr, .note, .disclaimer { break-inside: avoid; }
}
"""

JS = r"""
(function () {
  'use strict';

  var docEl = document.documentElement;
  docEl.classList.add('js');

  var CODES = __CODES__;
  var TITLES = __TITLES__;
  var STORE_KEY = 'numeria-privacy-lang';

  var panels = {};
  CODES.forEach(function (c) { panels[c] = document.getElementById(c); });
  var links = Array.prototype.slice.call(document.querySelectorAll('.langs a'));

  function supported(code) {
    return Object.prototype.hasOwnProperty.call(panels, code) && !!panels[code];
  }

  function readStored() {
    try { return window.localStorage.getItem(STORE_KEY); } catch (e) { return null; }
  }

  function writeStored(code) {
    try { window.localStorage.setItem(STORE_KEY, code); } catch (e) { /* private mode */ }
  }

  /* Match a BCP-47 tag ("zh-Hans-CN", "ar-SA", "pt-BR") against our codes,
     most specific first so zh-Hant does not silently land on zh. */
  function fromTag(tag) {
    if (!tag) return null;
    var parts = String(tag).toLowerCase().split(/[-_]/);
    while (parts.length) {
      var cand = parts.join('-');
      for (var i = 0; i < CODES.length; i++) {
        if (CODES[i] === cand) return CODES[i];
      }
      /* Our panels use bare primary subtags except zh, so also try that. */
      if (supported(parts[0])) return parts[0];
      parts.pop();
    }
    return null;
  }

  function pick() {
    var hash = (window.location.hash || '').replace('#', '');
    if (supported(hash)) return hash;

    var stored = readStored();
    if (supported(stored)) return stored;

    var nav = window.navigator;
    var tags = [];
    if (nav) {
      if (nav.languages && nav.languages.length) tags = tags.concat(nav.languages);
      if (nav.language) tags.push(nav.language);
    }
    for (var i = 0; i < tags.length; i++) {
      var m = fromTag(tags[i]);
      if (m) return m;
    }
    return 'en';
  }

  function activate(code, opts) {
    opts = opts || {};
    if (!supported(code)) code = 'en';

    CODES.forEach(function (c) {
      var on = c === code;
      panels[c].classList.toggle('is-active', on);
      if (on) { panels[c].removeAttribute('aria-hidden'); }
      else { panels[c].setAttribute('aria-hidden', 'true'); }
    });

    links.forEach(function (a) {
      if (a.getAttribute('data-lang') === code) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });

    var panel = panels[code];
    docEl.lang = panel.getAttribute('lang') || code;
    docEl.dir = panel.getAttribute('dir') || 'ltr';
    document.title = TITLES[code] || TITLES.en;

    if (opts.persist !== false) writeStored(code);
    if (opts.scroll) {
      window.scrollTo({ top: 0, behavior: 'auto' });
    }
  }

  links.forEach(function (a) {
    a.addEventListener('click', function (ev) {
      var code = a.getAttribute('data-lang');
      if (!supported(code)) return;
      ev.preventDefault();
      activate(code, { scroll: true });
      if (history.replaceState) history.replaceState(null, '', '#' + code);
      else window.location.hash = code;
    });
  });

  window.addEventListener('hashchange', function () {
    var hash = (window.location.hash || '').replace('#', '');
    if (supported(hash)) activate(hash, { scroll: false });
  });

  activate(pick(), { scroll: false });
})();
"""


def build():
    panels = "".join(render_panel(spec) for spec in LANGS)
    nav = render_nav()

    codes = ", ".join("'" + s["code"] + "'" for s in LANGS)
    titles = ", ".join(s["code"] + ": '" + s["doc_title"].replace("'", "\\'") + "'"
                       for s in LANGS)
    js = JS.replace("__CODES__", "[" + codes + "]").replace("__TITLES__",
                                                            "{" + titles + "}")

    skip_links = " ".join(
        '<a class="visually-hidden" href="#' + s["code"] + '">'
        + esc(CHROME["skip_to_content"][s["code"]]) + '</a>'
        for s in LANGS
    )

    alternates = "\n".join(
        '  <link rel="alternate" hreflang="' + esc(s["html_lang"]) + '" href="'
        + PAGES_URL + "#" + s["code"] + '">'
        for s in LANGS
    )

    footer_bits = (
        '<span><a href="' + REPO_URL + '" rel="noopener">'
        + esc(CHROME["footer_source"]["en"]) + '</a></span>'
    )

    doc = TEMPLATE
    for token, value in (
        ("@@ALTERNATES@@", alternates),
        ("@@SKIP_LINKS@@", skip_links),
        ("@@NAV@@", nav),
        ("@@PANELS@@", panels),
        ("@@CSS@@", CSS.strip("\n")),
        ("@@JS@@", js.strip("\n")),
        ("@@FOOTER_BITS@@", footer_bits),
        ("@@SUPPORT_URL@@", SUPPORT_URL),
        ("@@REPO_URL@@", REPO_URL),
        ("@@CANONICAL@@", PAGES_URL),
    ):
        doc = doc.replace(token, value)
    return doc


TEMPLATE = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="color-scheme" content="light dark">
  <title>Numeria — Privacy Policy</title>
  <meta name="description" content="Numeria: Finance Calculators collects no personal data. Privacy policy available in nine languages.">
  <meta name="robots" content="index, follow">
  <meta name="author" content="wanggit">
  <meta name="referrer" content="no-referrer">
  <link rel="canonical" href="@@CANONICAL@@">
@@ALTERNATES@@
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Numeria">
  <meta property="og:title" content="Numeria — Privacy Policy">
  <meta property="og:description" content="Numeria collects no personal data: no account, no ads, no analytics, no server.">
  <meta property="og:url" content="@@CANONICAL@@">
  <meta property="og:locale" content="en_US">
  <meta property="og:locale:alternate" content="zh_CN">
  <meta property="og:locale:alternate" content="ja_JP">
  <meta property="og:locale:alternate" content="ar_SA">
  <meta property="og:locale:alternate" content="es_ES">
  <meta property="og:locale:alternate" content="pt_BR">
  <meta property="og:locale:alternate" content="fr_FR">
  <meta property="og:locale:alternate" content="de_DE">
  <meta property="og:locale:alternate" content="hi_IN">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%231a56db'/%3E%3Ctext x='16' y='23' font-family='-apple-system,Helvetica,Arial' font-size='19' font-weight='700' fill='white' text-anchor='middle'%3EN%3C/text%3E%3C/svg%3E">
  <style>
@@CSS@@
  </style>
</head>
<body>
  @@SKIP_LINKS@@

  <div class="topbar">
    <div class="topbar-inner">
      <a class="brand" href="@@REPO_URL@@" rel="noopener">
        <span class="brand-mark" aria-hidden="true">N</span>
        <span>Numeria</span>
      </a>
      <nav class="langs" aria-label="Language">
@@NAV@@
      </nav>
    </div>
  </div>

  <main id="main">
@@PANELS@@  </main>

  <footer class="site">
    <div class="inner">
      @@FOOTER_BITS@@
      <span aria-hidden="true">&middot;</span>
      <span><a href="@@SUPPORT_URL@@" rel="noopener">Support</a></span>
      <span aria-hidden="true">&middot;</span>
      <span>&copy; 2026 wanggit</span>
    </div>
  </footer>

  <script>
@@JS@@
  </script>
</body>
</html>
"""


def check(doc):
    """Validate the rendered document. Returns a list of problems."""
    problems = []

    for spec in LANGS:
        code = spec["code"]
        if 'id="%s"' % code not in doc:
            problems.append("missing panel id=%s" % code)
        if 'data-lang="%s"' % code not in doc:
            problems.append("missing nav link for %s" % code)
        for key in ("h1", "tldr", "product", "effective",
                    "disclaimer_head", "disclaimer"):
            if not spec.get(key):
                problems.append("%s: empty %s" % (code, key))
        h2s = [b[1] for b in spec["blocks"] if b[0] == "h2"]
        if len(h2s) != 10:
            problems.append("%s: expected 10 sections, got %d" % (code, len(h2s)))
        tables = [b for b in spec["blocks"] if b[0] == "table"]
        if len(tables) != 1:
            problems.append("%s: expected exactly 1 table" % code)
        else:
            rows = tables[0][1]["rows"]
            if len(rows) != 6:
                problems.append("%s: expected 6 storage rows, got %d"
                                % (code, len(rows)))
        # Every localisation must state the two URLs that ASC and the app use.
        body = str(spec["blocks"])
        if SUPPORT_URL not in body:
            problems.append("%s: support URL absent from contact section" % code)
        # Placeholder scan is case-SENSITIVE on purpose: "todo" is a real
        # Spanish/Portuguese word ("Desbloquear todo") and must not trip it.
        blob = str(spec)
        for needle in ("TODO", "TBD", "FIXME", "PLACEHOLDER", "XXX", "lorem ipsum",
                       "{{", "}}", "@@"):
            if needle in blob:
                problems.append("%s: placeholder %r left in content" % (code, needle))

    # Document-level guarantees.
    for needle in ("http://fonts.", "cdn.", "google-analytics", "googletagmanager",
                   "unpkg.com", "jsdelivr", "cdnjs", "<script src=",
                   "<link rel=\"stylesheet\" href="):
        if needle in doc:
            problems.append("external resource reference: %s" % needle)

    if doc.count("<html") != 1 or doc.count("</html>") != 1:
        problems.append("malformed html element")
    if doc.count("<!DOCTYPE html>") != 1:
        problems.append("missing or duplicated doctype")

    # Every build token must have been substituted.
    if "@@" in doc:
        problems.append("unsubstituted @@token@@ remains in output")
    for token in ("__CODES__", "__TITLES__"):
        if token in doc:
            problems.append("unsubstituted %s remains in output" % token)

    # Unbalanced tags for the elements we generate in bulk.
    for tag in ("section", "table", "thead", "tbody", "tr", "ul", "aside",
                "h1", "h2", "nav", "main", "footer", "script", "style"):
        opens = doc.count("<%s " % tag) + doc.count("<%s>" % tag)
        closes = doc.count("</%s>" % tag)
        if opens != closes:
            problems.append("unbalanced <%s>: %d open vs %d close"
                            % (tag, opens, closes))

    return problems


def main():
    doc = build()
    problems = check(doc)

    if problems:
        sys.stderr.write("VALIDATION FAILED (%d):\n" % len(problems))
        for p in problems:
            sys.stderr.write("  - %s\n" % p)
        return 1

    if "--check" in sys.argv:
        sys.stdout.write("ok: %d languages, %d bytes, no problems\n"
                         % (len(LANGS), len(doc.encode("utf-8"))))
        return 0

    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(here, "privacy")
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(doc)

    size = os.path.getsize(out_path)
    sys.stdout.write("wrote %s (%d languages, %.1f KB)\n"
                     % (out_path, len(LANGS), size / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
