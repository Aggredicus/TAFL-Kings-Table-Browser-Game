# AGENTS.md — code review and release procedure

- The executable source of truth is `index.html`; the named offline `TAFL_ATLAS_Offline_v1.0.html` must remain identical for the public release.
- Maintain offline, single-HTML play with no runtime dependencies, remote assets, trackers or network calls.
- Specify behavior, risk, rule provenance, and tests before modifications; use reversible, focused diffs.
- Rules must be checked per variant: setup, legal moves, captures, king safety, escape, repetition, win/loss, imported match replay.
- Threat-model untrusted match codes, local settings and user-entered QA feedback. Never render untrusted content as HTML; preserve bounds and allowlists.
- Visual regression: all tracks remain square and equal after moves on 7/9/11/19 grids and phone/desktop widths.
- Run static unit tests, JS syntax, in-app QA, mobile and desktop browser tests, negative match-code cases; report actual outcomes, not assumed outcomes.
- Use independent functional and security reviews; report severity, file/line, reproducible failure, fix, outcome. Normally cap loops at 3.
- Do not claim formal tournament certification or complete security proof. Preserve rollback notes and GPL-3.0 license.
