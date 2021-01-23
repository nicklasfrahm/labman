from quart import Quart
from routers import health

app = Quart(__name__)
app.register_blueprint(health.blueprint)


@app.errorhandler(404)
def unsupported_endpoint(e):
    return {
        "error": {
            "title": e.name,
            "status": e.status_code,
            "reason": "Unsupported Endpoint",
        }
    }


if __name__ == "__main__":
    app.run()
