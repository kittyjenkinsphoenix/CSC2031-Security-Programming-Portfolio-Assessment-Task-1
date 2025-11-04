# CSC2031 Security Programming Portfolio – Task 1

Secure Flask-Based Account Registration System with Semantic Validation, Password Policy Enforcement, Context-Aware Sanitization, CSRF Protection, and Security-Aware Logging.

## Overview

This project implements a minimal but security-focused registration workflow built with Flask and Flask‑WTF. It demonstrates secure input validation, strong password policy enforcement, HTML sanitization with bleach, CSRF protection, and detailed logging of security-relevant events.

## Features

- Comprehensive Validation Across All Fields
  - Username: Required, 3–30 chars, letters/underscores only, Reserved Username Check (e.g., admin, root, superuser)
  - Email: Required, valid format, Domain Restriction (.edu, .ac.uk, .org)
  - Password: Required, Minimum Length 12, Regex Complexity (upper/lower/digit/special/no spaces), Common Password Blacklist
  - Confirm Password: Must Match Password
- Context-Aware Sanitization And Secure Rendering
  - Bio/Comment is sanitized using bleach with a safe allowlist of tags (b, i, u, em, strong, a, p, br, ul, ol, li)
  - Jinja2 auto-escaping is used by default; sanitized bio is rendered safely
- CSRF Protection
  - Flask‑WTF CSRF token is rendered with `form.hidden_tag()` and validated server‑side
- Detailed Logging With Context And Awareness
  - UTC Timestamps, Client IP Address (respects X‑Forwarded‑For), Username, Email, And Error Details
  - INFO: Registration Successful
  - WARNING: Validation Failures, Attempt To Register Reserved Username, Bio Sanitized (original vs sanitized snippets)
- Clean, Well‑Structured Code
  - Modular package layout (`app/`), Blueprints, Clear comments
  - Messages are in Title Case and variables use camelCase (per project convention)

## Project Structure

```
CSC2031 Task 1/
	config.py
	requirements.txt
	run.py
	app/
		__init__.py
		forms.py
		routes.py
		templates/
			base.html
			register.html
	instance/
		(created at runtime; logs are written here)
```

## Requirements

- Python 3.11+
- pip

Install dependencies:

```powershell
python -m pip install -r "CSC2031 Task 1\requirements.txt"
```

## Running The Application (Windows PowerShell)

From the repository root:

```powershell
python "CSC2031 Task 1\run.py"
```

The development server will start at:

- http://127.0.0.1:5000

## Configuration

See `CSC2031 Task 1/config.py`:

- `SECRET_KEY`: Used by Flask‑WTF CSRF (development key provided; use a strong secret for production)
- `DEBUG` / `TESTING`: Development defaults

## Endpoints

- `GET /` → Redirects to `/register`
- `GET|POST /register` → Registration form with server‑side validation and sanitization

## Logging

- Location: `instance/registration.log` (created automatically)
- Timestamps: UTC (`logging.Formatter.converter = time.gmtime`)
- Examples:
  - INFO: `Registration Successful - Client_Ip=127.0.0.1 Username=jane Email=jane@school.edu`
  - WARNING: `Registration Validation Failed - Client_Ip=127.0.0.1 Username=jane Errors=email: Invalid Email Address`
  - WARNING: `Attempt To Register Reserved Username - Client_Ip=127.0.0.1 Username=admin`
  - WARNING: `Bio Sanitized - Client_Ip=127.0.0.1 Username=jane Original_Snippet=<script>... Sanitized_Snippet=...`

## Security Notes

- IP Address Resolution: The helper checks `X-Forwarded-For` first, then `request.remote_addr`. In production behind a reverse proxy, configure a proper proxy middleware (e.g., `werkzeug.middleware.proxy_fix.ProxyFix`).
- Passwords are never logged. Only username and email are included in INFO logs.
- Bio content is sanitized with bleach before rendering; only a safe subset of tags is allowed.
- CSRF protection is enabled through Flask‑WTF.

## How To Test The Workflow

1. Open `/register` and try these cases:

- Invalid Email Or Short Username → Page shows clear field errors; WARNING logged
- Reserved Username (e.g., `admin`) → WARNING logged
- Bio With `<script>` → Sanitized result is shown; sanitization WARNING logged
- Valid Submission → INFO log and success message; sanitized bio is echoed back

1. Inspect Logs

- Open `instance/registration.log` while submitting forms to see logged events and context

## License

See `LICENSE` in the repository root.

