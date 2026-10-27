# GitHub Pages deployment — TAFL ATLAS

## Expected public URL

https://aggredicus.github.io/TAFL-Kings-Table-Browser-Game/

The public path is case-sensitive. This document describes the configuration; the link is not guaranteed live until GitHub Pages is enabled and the deployment succeeds.

## One-time GitHub activation

1. Open https://github.com/Aggredicus/TAFL-Kings-Table-Browser-Game/settings/pages as repository administrator.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Set **Branch** to `main` and **Folder** to `/(root)`; click **Save**.
4. Monitor https://github.com/Aggredicus/TAFL-Kings-Table-Browser-Game/actions for the GitHub Pages build/deployment.
5. Open the expected public URL. Check that the TAFL ATLAS game appears, seven rulesets can be selected, and the local QA checks pass on phone and desktop.

## Technical deployment contract

- `index.html` is the entrypoint. It is identical to the downloadable `TAFL_ATLAS_Offline_v1.0.html` in the v1.0.0 release.
- `.nojekyll` disables Jekyll transforms; no build/runtime dependencies are needed.
- Only the static repository contents are published; no backend/game server, secret keys, matchmaking, or account functionality exists.
- All game processing and persistence stay within the visitor's browser. GitHub hosts the page and may log requests under its own policies, so avoid claiming that hosted-page access has zero network traffic.
- No custom domain or DNS setup is necessary.
- Future `main` updates automatically trigger Pages publication with this setting. The published v1.0.0 GitHub Release remains a separate fixed source snapshot.

## If the URL doesn't work

Confirm **Settings → Pages** shows the source branch `main` and `/(root)`, then inspect deployment status in **Actions**. GitHub Pages changes may need a short propagation period. If the page errors, report the latest workflow failure and the browser's exact error. Do not bypass QA or change repository visibility as a workaround.
