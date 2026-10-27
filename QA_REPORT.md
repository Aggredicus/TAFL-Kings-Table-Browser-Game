# TAFL ATLAS v1.0.0 — QA and security notes

Date: 2026-10-27.

## Tested runtime behavior

| Test area | Outcome |
|---|---|
| Internal logic and geometry regression suite | 31/31 pass |
| Seven board presets / army configurations | Verified programmatically in Chromium |
| Four viewports (320 / 390 / 768 / 1280 pixels) | No JS exceptions / no page-level horizontal overflow |
| Move interactions, selection, undo | Passed |
| Offline match-code export and import | Passed valid-code roundtrip, rejected invalid prefix and illegal replay |
| Computer opponent | Completed opening move in 7×7 and 19×19 samples |
| Theme selection and cross-variant preference | Passed |
| 19×19 zoom / local board scroll / fit | Passed |
| Inherited user v1.0 row-height bug | CSS equal grid tracks and DOM fixture regression pass |

## Threat model and controls

1. **Hostile match code**: UTF-8 decoding, an exact prefix, a bounded code length, a preset ID allowlist, integer move pairs, a 900-move cap and replay through the actual engine. No user-provided text is rendered with `innerHTML`.
2. **Remote code / data loading**: CSP defaults to deny, no connect permissions, no imports, no network fetch, no remote images or fonts.
3. **Unexpected file access**: No programmatic file read. Browser download uses a user-initiated Blob containing only the match or QA report.
4. **Privacy**: Local-only state; no telemetry. Source links are opt-in; when clicked, they naturally open external sites.
5. **Untrusted metadata**: Match code is not signed. A person can modify it and recalculate legal moves, so it cannot establish identity or fairness.
6. **Persistence**: Browser-controlled and not guaranteed when opened from content-provider URIs. Copy/export manually to preserve important matches.

## Remaining known gaps

- Copenhagen **exit fort** and **fully closed encirclement** are human-adjudicated rather than automatically solved; manual claims are available only in pass-and-play.
- Special perpetual repetition attribution is a simplified preset-level decision; not a substitute for formal tournament arbiter.
- Rare king/throne capture edge cases are not exhaustively proven. Compare unusual game states with governing source.
- Alea Evangelii uses an identified, explicitly interpretive 19×19 layout with correct army counts, **not** a claim of verified museum/manuscript transcription.
- No synchronous LAN, Bluetooth, WebRTC or online multiplayer; the entire document runs offline. Manual match codes are the cross-device multiplayer pathway.
- No independent formal verification, penetration test, screen-reader study, battery-performance audit, or real-device Android confirmation was performed in this run.

## QA feedback next step

If a board size changes after moving a piece, include a screenshot, phone/browser version, chosen variant, artwork theme, move number and a match code. Attach the exported QA field report for reproducibility.
## v1.0.0 public release verification (2026-10-27)

- The public package is the previously tested internal v2 development build with only the visible version label changed. The `TA2` match protocol and persistence keys remain compatible.
- Re-executed the in-app QA in headless Chromium at 320px, 390px, 768px and 1280px: **31 PASS per viewport**, no JavaScript exceptions, no page-level horizontal overflow.
- Seven dependency-free release source tests pass; standalone JavaScript syntax check passes.
- Original user-submitted Android screenshot is intentionally excluded to avoid publishing personal notification content.
- The existing repo GPL-3.0 license is preserved. Source references identify outside rules/art reference material, not copied assets.
