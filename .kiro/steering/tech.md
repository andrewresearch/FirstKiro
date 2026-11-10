# Tech Stack

## Stack
- Language: Python 3.11+
- Package manager: pip with a virtual environment (`.venv`)
- Dependencies: listed in `requirements.txt`
- Testing: pytest (add only when tests are requested)
- Formatting/linting: ruff (optional, add when needed)

## Common Commands
- Create venv: `python3 -m venv .venv && source .venv/bin/activate`
- Install: `pip install -r requirements.txt`
- Run: `python -m src.main`
- Test: `pytest`
- Lint/format: `ruff check . && ruff format .`

## Conventions
- Follow PEP 8; use type hints on public functions.
- Use docstrings for modules, classes and public functions.
- Prefer the standard library; do not add dependencies without a clear need.
- Never commit secrets or `.venv`; use environment variables.
