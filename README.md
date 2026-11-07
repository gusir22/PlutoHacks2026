# Northstar Security Lab — Django CTF

A deliberately vulnerable, **localhost-only** Django application designed for beginner security students. Contains **10 distinct exercises** with synthetic flags, a flag submission dashboard, difficulty ratings, hints, and session-based points. No Docker.

## Requirements

- Python 3.11 or newer
- Windows PowerShell, macOS Terminal, or Linux shell
- Internet only for the initial Django package installation

## Setup (Windows PowerShell)

```powershell
cd ctf_django_lab
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate --run-syncdb
python manage.py seed_lab
python manage.py runserver 127.0.0.1:8000
```

If PowerShell refuses to activate the virtual environment, run `.venv\Scripts\python.exe` instead of `python` in the remaining commands.

## Setup (Linux / macOS)

```bash
cd ctf_django_lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate --run-syncdb
python manage.py seed_lab
python manage.py runserver 127.0.0.1:8000
```

Visit **http://127.0.0.1:8000/**.

## Challenges

| No. | Category | Difficulty | Points |
|---|---|---|---|
| 1 | HTML source exposure | Easy | 50 |
| 2 | Public JavaScript secret | Easy | 50 |
| 3 | robots.txt information disclosure | Easy | 50 |
| 4 | Insecure direct object reference (IDOR) | Medium | 100 |
| 5 | SQL injection | Medium | 150 |
| 6 | Reflected cross-site scripting | Medium | 150 |
| 7 | Stored cross-site scripting | Medium | 150 |
| 8 | Client-controlled cookie authorization | Easy | 100 |
| 9 | Mass assignment | Hard | 200 |
| 10 | Predictable reset tokens | Hard | 200 |

**Total: 1,200 points.** Flags have the form `FLAG{...}`.

## What to document

Copy `STUDENT_WORKSHEET.md` for each participant. For each exercise include the vulnerable route, why it is vulnerable, your proof-of-concept request or steps, the observed result, the flag, the impact on a real system, and a suggested secure fix.

## Security boundaries

**This app is intentionally unsafe.** It exposes a SQL injection flaw, unsanitized HTML, fake staff-role controls, weak reset-token logic, and purposefully disabled CSRF enforcement on selected exercise routes.

- **Never** put it on the public internet, Railway, a VPS, or your production Django project.
- Run the exact loopback-only `runserver 127.0.0.1:8000` command. Do not use `0.0.0.0`.
- Use **only** fabricated seed data; never insert personal data, credentials, or production databases.
- Prefer a disposable local Python virtual environment and browser profile. The stored XSS exercise intentionally runs student-supplied JavaScript in the lab's browser origin.
- Do not use the app as a dependency, Django security example, or production starter.
- `INSTRUCTOR_SOLUTIONS.md` and `lab/challenges.py` contain spoilers. Distribute only the lab instructions to students if you want independent discovery.
- The XSS proof endpoint is an educational convenience, **not** cryptographic proof that XSS actually executed; it can be queried separately. Instructors should require screenshots or browser-console evidence.
- Flags are static and available to anyone who can access this project's source. This is a local learning exercise, not a secure multi-user competition platform.

## Reset lab data and progress

```bash
python manage.py seed_lab
```

Click **Reset progress** on the dashboard to reset captured flags and the demo profile for that browser session. Clear cookies for `127.0.0.1` to fully reset session and modified role-cookie state.

## Check the project

```bash
python manage.py check
python manage.py test
```

No separate web server, Redis, Docker, Celery, or Node build step is necessary.
