"""FirstKiro entry point."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Render the greeting page."""
    return (
        "<!doctype html>"
        '<html lang="en">'
        '<head><meta charset="utf-8"><title>FirstKiro</title></head>'
        "<body><h1>Hello from FirstKiro!</h1></body>"
        "</html>"
    )


def main() -> None:
    """Run the web server."""
    app.run(host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
