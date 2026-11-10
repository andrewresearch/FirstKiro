# Tech Stack

## Stack
- Language: Python 3.11+
- Web framework: Flask 3.x (pinned in `requirements.txt`)
- Package manager: pip with a virtual environment (`.venv`)
- Dependencies: listed and pinned in `requirements.txt`
- Testing: pytest with Flask's test client (add only when tests are requested)
- Formatting/linting: ruff (optional, add when needed)

## Common Commands
- Create venv: `python3 -m venv .venv && source .venv/bin/activate`
- Install: `pip install -r requirements.txt`
- Run dev server: `python -m src.main` (serves http://127.0.0.1:5000)
- Alternative: `flask --app src.main run --debug`
- Test: `pytest`
- Lint/format: `ruff check . && ruff format .`

## Conventions
- Follow PEP 8; use type hints on public functions and route handlers.
- Use docstrings for modules, classes and public functions.
- The Flask `app` object lives in `src/main.py`; define routes with `@app.route`.
- Prefer the standard library and Flask built-ins; do not add dependencies without a clear need.
- The built-in dev server is for local development only; never enable debug mode in production.
- Never commit secrets or `.venv`; use environment variables for configuration.
