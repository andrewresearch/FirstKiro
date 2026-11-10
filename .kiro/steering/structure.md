# Project Structure

```
FirstKiro/
├── .kiro/steering/   # Steering files (product, tech, structure)
├── src/
│   ├── __init__.py
│   └── main.py       # Flask app object, routes and dev-server entry point
├── requirements.txt  # Pinned Python dependencies (Flask)
├── .gitignore
└── README.md         # Project overview, setup and run instructions
```

## Guidelines
- Source code lives in `src/`; tests go in `tests/` once they exist.
- Keep routes in `src/main.py` while the app is small. As it grows, move routes
  into a Flask Blueprint module (e.g. `src/routes.py`) and HTML into
  `src/templates/` using Jinja templates instead of inline strings.
- Put static assets (CSS, JS, images) in `src/static/` when they are needed.
- Keep modules focused on one responsibility.
- Update this file when the layout changes.
