# Security policy

TAFL ATLAS v1.0.0 is self-contained HTML. No runtime dependencies, accounts, trackers, telemetry, API requests, automatic device discovery or online match server are included. Research links open external websites only when the player chooses them.

## Trust boundaries
- Match codes are **untrusted and unauthenticated**. They have size and structure limits and must replay through the legal-move engine. They cannot verify player identity, fair play or match results.
- Browser localStorage is best-effort and may be ephemeral in Android content-provider views. Export match codes before clearing data.
- The CSP denies connections and most external resources, but permits inline script/style to meet the one-file requirement. This is a deliberate tradeoff, not an XSS-proofing guarantee.
- No automatic file reads, remote executable scripts, analytics, or third-party fonts/images.

## Report a vulnerability
Use the repository's private vulnerability reporting feature if available, or contact the owner privately. Do not post private match records, passwords, or notification-filled screenshots in public issues.

## Disclosed limitations
No formal penetration test, verified competitive adjudicator, third-party accessibility certification, or real-time multiplayer security claim is made.
