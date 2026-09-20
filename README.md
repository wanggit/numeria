# Numeria

**Numeria: Finance Calculators** — 69 offline financial calculators for iPhone:
mortgages, auto loans, investing, retirement, US federal & state tax, and
everyday money maths. Every calculation runs on-device: no account, no ads,
no network.

This repository hosts the app's public web presence on GitHub Pages.

| Page | URL |
| --- | --- |
| Site home | <https://wanggit.github.io/numeria/> |
| Privacy policy (9 languages) | <https://wanggit.github.io/numeria/privacy/> |
| Technical support (English / Chinese) | <https://wanggit.github.io/numeria/support/> |
| Support / issue tracker | <https://github.com/wanggit/numeria/issues> |

The privacy policy URL above is the one declared in the App Store listing and
hard-coded in the app (`lib/core/app_info.dart` → `kPrivacyPolicyUrl`); it is
also asserted by `test/release_readiness_test.dart`.

## Repository layout

```
index.html          site landing page
privacy/index.html  privacy policy, self-contained, 9 localisations
support/index.html  technical support, English and Simplified Chinese
tools/              generator + content sources for the privacy page
```

## Editing the privacy policy

`privacy/index.html` is generated — do not hand-edit it. Change the text in
`tools/content_*.py`, then rebuild and re-run the checks:

```sh
python3 tools/build_privacy.py          # regenerate privacy/index.html
python3 tools/build_privacy.py --check  # validate without writing
```

The generator asserts, for every localisation: 10 numbered sections, one
6-row storage table, the support URL, the GitHub Pages log disclosure, and no
placeholder text. It also fails the build if any external subresource
(CDN font, script, stylesheet, tracker) is referenced.

## Privacy stance

The app collects nothing (App Store label: *Data Not Collected*). The only
data it writes is a handful of local preferences that never leave the device.
This site likewise loads no external assets and sets `Referrer-Policy:
no-referrer`; the sole third-party involvement is GitHub Pages' own access
logging, which the policy discloses explicitly.

© 2026 wanggit
