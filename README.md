# TAFL ATLAS v1.0.0 — Public Release

A self-contained HTML tafl collection. Open `TAFL_ATLAS_Offline_v1.0.html` in a modern browser. Nothing else needs to be installed; there are no external scripts, images, fonts, APIs, trackers, or CDNs.

## Getting started

1. Open the HTML file from the device's file manager (or download it to the device and open in a browser).
2. Use **Play > Game and rules** to choose one of seven presets.
3. Select a piece and an indicated destination; use **Undo** if needed.
4. Two friends on one device choose **Two players · pass & play**; for a local computer opponent choose **One player · local computer**.
5. From **Artwork** select Automatic or lock a manual design. For more options open **Atelier**.
6. For turn-based play across two devices, copy a match code, send it using any communication method you already have, and have your friend import it. The HTML file itself never sends or receives network messages.
7. Use the **QA lab** for local self-tests and exportable field feedback.

### Rules and historical evidence

| Preset | Board | Attacker / defender / king | Escape | Evidence | Important caveat |
|---|---|---:|---|---|---|
| Copenhagen Hnefatafl | 11×11 | 24 / 12 / 1 | Corner | 2012 modern standard | Shieldwall automated; **exit-fort and full encirclement are player adjudicated** |
| Fetlar Hnefatafl | 11×11 | 24 / 12 / 1 | Corner | Fetlar Museum 2018 | Modern reconstruction |
| Tablut | 9×9 | 16 / 8 / 1 | Any edge | Linnaeus 1732; retranslation | Castle-throne behavior has documented variants; this is one playable interpretation |
| Brandubh | 7×7 | 8 / 4 / 1 | Corner | Irish writings, Ballinderry board | Rule completion is modern; repetition is a local draw convention |
| Tawlbwrdd | 11×11 | 24 / 12 / 1 | Any edge | Robert ap Ifan 1587 | Partial historical text; missing movement and winning rules reconstructed |
| Ard Rí | 7×7 | 8 / 4 / 1 | Any edge | Sparse evidence | Selects smaller modern reconstruction, **not** the 16 vs 8 historical account sometimes listed |
| Alea Evangelii | 19×19 | 48 / 24 / 1 | Corner | MS 122 manuscript board | **Interpretive symmetric piece layout**, not verified full manuscript transcription; modern mechanics |

These are game presets, not claims that Viking-age rules were consistently identical. The article [Tafl games](https://en.wikipedia.org/wiki/Tafl_games) is the overview. Sources are linked from the built-in **Research** panel.

## Visual atelier

Eight independent, switchable styles:

- **Borre bronze** — Scandinavian ring-chain and close interlace
- **Urnes silver** — sinuous Norse ribbons
- **Sámi field** — textile/hide and antler material cues; avoids copying sacred symbols
- **Insular yew** — Irish spiral and pegboard inspiration
- **Welsh carved stone** — incised stone / interlace
- **Highland stone** — ring and incised carving motifs
- **Illuminated leaf** — Anglo-Saxon manuscript framing and vegetation
- **Modern clarity** — minimal high-contrast pieces

Artwork is **original, culturally inspired illustration**, not a scan, direct replica or attested historical playing set. Board motifs preserve visual readability; the art never changes the rules. The user may lock an artwork theme across all variants or return to regional Automatic.

## Safety and privacy

- Offline CSP: `default-src 'none'`, `connect-src 'none'`, `object-src 'none'`, `frame-src 'none'`, `base-uri 'none'`; scripts and CSS inline only for single-file use.
- No dependencies or web calls; external source links open only when deliberately clicked.
- Board UI and imported match data are handled through validated types and DOM-safe APIs. Imported codes have an overall size cap, an allowlist of variant names, a move-count cap, per-move legal validation and UTF-8 decode checking.
- Stored settings and match history are held locally, best effort. Browser `content://` / private mode environments may not allow persistent localStorage; **export match codes before closing** if persistence is uncertain.
- Match codes are shareable unencrypted gameplay records and **not authenticated**. Do not interpret them as verified identities or tournament results.
- No automatic wireless peer discovery or real-time multiplayer. The built-in two-device option is manual exchange only.

## Tested (automated)

- Chromium headless browser at 320, 390, 768 and 1280px widths: no page errors or document horizontal overflow.
- Every variant changes board dimensions and renders the documented starting army counts.
- Tested piece selection, legal move, undo, artwork overrides, variant switching, 19×19 pan/fit zoom, TA2 code copy/import, browser-local AI and the QA lab.
- Built-in QA harness passes **31/31** checks; it includes a visual regression for rows changing size after moving a piece, plus king-capture and shieldwall fixtures.

### Unfinished validation

This is an **independently built playable prototype**, not certified by the World Tafl Federation. Specialized tournament adjudication (e.g., unbreakable forts, encirclement, full repetition responsibility), exhaustive position testing, accessibility audits with human users, and performance checks on low-end devices remain to be completed. The local computer player is heuristic, not a professional tafl engine. Verify unusual positions against the linked original rules before competitive use.

## Credits / research starting points

- https://en.wikipedia.org/wiki/Tafl_games
- https://aagenielsen.dk/copenhagen_rules.php
- https://aagenielsen.dk/fetlar_rules2018visual.pdf
- https://aagenielsen.dk/brandubh2_rules_en.pdf
- https://aagenielsen.dk/historical_summary.php
- https://rules.moddable.games/tafl/variants/tawlbwrdd/
- https://hnefataflgame.com/ard-ri/
- https://hnefataflgame.com/alea-evangelii/
- https://www.britishmuseum.org/collection/term/x95679
- https://askaboutireland.ie/learning-zone/secondary-students/art/art-in-ireland/themes-in-irish-art/abstract-art/spirals-and-interlace/

The game code and vector styling in this package were newly authored for this project; no third-party screenshots, source artwork or commercial game assets have been embedded.
## Public v1.0.0 release

This is the first **public** version of the previously tested TAFL ATLAS development build. Open `TAFL_ATLAS_Offline_v1.0.html` (or `index.html`) as a standalone document. The original match-code prefix `TA2` and local settings keys remain unchanged for compatibility. The repository already contains a GPL-3.0 license, which is retained.

`index.html` makes the same game usable on static hosting if GitHub Pages is separately enabled. Committing it does not itself enable hosting or create an official GitHub Release/tag.
