# Instructor-only walkthrough — contains every flag

Use only on the localhost training app. These examples are deliberately specific to this fictional sandbox.

1. **HTML comment** — On `/` use View Page Source and find `FLAG{html_comments_are_public}` in an HTML comment. Fix: do not put private material in page source.
2. **JavaScript exposure** — Inspect `/static/lab/app.js`, whose first comment includes `FLAG{frontend_code_is_not_secret}`. Fix: never place secrets in client assets.
3. **robots.txt** — Visit `/robots.txt`, then `/hidden/backups/ops.txt` for `FLAG{robots_is_not_access_control}`. Fix: enforce authentication/authorization; disallow rules are public hints.
4. **IDOR** — Directory lists `/directory/1/` and `/directory/2/`; manually visit `/directory/3/` and find `FLAG{ids_are_not_permissions}`. Fix: object-level access checks; no unauthorized access based solely on guessing IDs.
5. **SQL injection** — `/archive/?q=%27%20OR%201%3D1%20--%20` produces a SQL condition that returns a restricted document containing `FLAG{parameterize_your_sql}`. Fix: use ORM filters or parameterized SQL and restrict visibility independently.
6. **Reflected XSS** — In greeting field submit `<script>claimXssFlag('reflected')</script>`; a displayed proof contains `FLAG{escape_reflected_input}`. Fix: HTML escape untrusted strings, use CSP defense-in-depth. Browser must run script in the vulnerable page (console-only execution does not demonstrate the flaw).
7. **Stored XSS** — Submit `<script>claimXssFlag('stored')</script>` to `/guestbook/`; on saved page or revisit the proof contains `FLAG{sanitize_stored_content}`. Fix: escape stored text; allowlisted HTML sanitization only if rich content is required.
8. **Role-cookie forgery** — In browser console on `/staff/`, run `document.cookie='role=admin; path=/'` then refresh to find `FLAG{never_trust_client_roles}`. Fix: server-side authorization checks based on authenticated server-managed identities.
9. **Mass assignment** — In browser console, run `fetch('/api/profile/', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({is_vip:true})}).then(r=>r.json()).then(console.log)` then visit `/vip/` for `FLAG{allowlist_mutable_fields}`. Fix: explicit mutation allowlists; never let callers control privileged attributes.
10. **Predictable recovery** — `/directory/3/` reveals Alex's employee number 1042. POST `/reset/` username `alex`, token `1042` to find `FLAG{randomize_reset_tokens}`. Fix: cryptographically random, single-use, short-lived reset tokens; account-bound and rate-limited. No actual password is changed in this lab.

**Note:** Students can read `lab/challenges.py` or query the unprotected XSS training helper to bypass some intended exercises. This is intentionally a source-available practice app rather than a hardened examination server. In graded settings require a reproducible exploit demonstration and written root-cause analysis, not the flag alone.
