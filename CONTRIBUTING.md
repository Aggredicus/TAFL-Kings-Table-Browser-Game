# Contributing

TAFL ATLAS is a dependency-free, single-file offline browser anthology. Changes should preserve compatibility with shared match codes and existing user saves whenever possible.

Before modifying gameplay, document the affected historical variant and source, distinguish attested evidence from reconstruction, and add a regression case. Verify the browser layout on phone and desktop, especially after moving pieces.

Run `python3 -m unittest discover -s tests -v`, the in-app 31+ QA tests, and JavaScript syntax validation. Review imports and persistence for untrusted input and keep user-entered text out of `innerHTML`.

Bug reports should include variant, theme, browser, reproducible steps, expected and actual behavior, and sanitized match codes when helpful. Remove notifications and personal details from public screenshots. Preserve GPL-3.0 license and credit original outside research sources.
