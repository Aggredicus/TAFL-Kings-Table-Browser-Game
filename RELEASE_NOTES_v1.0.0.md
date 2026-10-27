# TAFL ATLAS v1.0.0 — First Public Release

A self-contained, offline tafl board-game anthology for modern browsers on mobile and desktop. Download `TAFL_ATLAS_Offline_v1.0.html` and open it directly in a browser; no installation, account, or internet connection is required to play.

## Included
- **Seven playable ruleset presets:** Copenhagen Hnefatafl (11×11), Fetlar Hnefatafl (11×11), Sámi Tablut (9×9), Irish Brandubh (7×7), Welsh Tawlbwrdd (11×11), Scottish Ard Rí (7×7), and Alea Evangelii (19×19).
- **Eight customizable themes:** locally rendered historic-material and ornamental designs, automatic cultural theme matching, and persistent manual overrides.
- Pass-and-play on one device, a heuristic local computer opponent, manual cross-device match-code exchange, learn/research panels, board zoom, and offline local save/undo.
- Built-in rule/geometry regression suite and published QA and security notes.
- Independent GPL-3.0-licensed source code; no network dependencies or tracking.

## Verification
The built-in suite passed **31/31 tests** at tested phone, tablet, and desktop viewport widths before release. Repository source checks and JavaScript syntax checks passed in CI. Automated tests are not a substitute for real-device accessibility, historical, or tournament certification.

## Known limitations and research integrity
- Copenhagen exit-fort and closed-encirclement outcomes can require player agreement and are **not** a fully automatic tournament arbiter.
- Alea Evangelii's playable setup is an interpretive modern reconstruction.
- Some historical tafl rulesets are disputed or incompletely attested; historical notes identify the uncertainty.
- Cross-device multiplayer is **manual match-code exchange**, not real-time network synchronization.
- Browser storage can be ephemeral when opening files through Android content-provider URLs. Export match codes for backups.
- The previous internal development build was numbered v2.0; **v1.0.0 is the first public release**. Match-code compatibility is retained.

The `TAFL_ATLAS_v1.0_Offline_Public.zip` archive contains the offline playable HTML and source documentation. `SHA256SUMS.txt` contains checksums for both downloadable assets.
