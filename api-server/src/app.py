from quart import Quart
from dotenv import load_dotenv
from os import getenv
from logging import getLogger
from pymongo.errors import OperationFailure, ConnectionFailure, ConfigurationError
from src.routers import health, organization
from src.util import connect
import asyncio
import sys


# Load the ".env" file.
load_dotenv()

# Create a quart application instance.
mongo_uri = getenv("MONGO_URI")
app = Quart(__name__)
app.register_blueprint(health.blueprint)
app.register_blueprint(organization.blueprint)


@app.errorhandler(404)
async def unsupported_endpoint(e):
    return {
        "error": {
            "title": e.name,
            "status": e.status_code,
            "reason": "Unsupported Endpoint",
        }
    }


@app.errorhandler(OperationFailure)
async def operation_failure(err):
    if err.details.get("codeName") == "AuthenticationFailed":
        return {
            "error": {
                "title": "Internal Server Error",
                "status": 500,
                "reason": "Database Authentication Failure",
            }
        }, 500

    raise Exception("Unexpected Exception")


@app.errorhandler(ConnectionFailure)
async def connection_failure(err):
    return {
        "error": {
            "title": "Internal Server Error",
            "status": 500,
            "reason": "Database Connection Failure",
        }
    }, 500


@app.errorhandler(ConfigurationError)
async def configuration_error(err):
    return {
        "error": {
            "title": "Internal Server Error",
            "status": 500,
            "reason": "Database Configuration Invalid",
        }
    }, 500


@app.errorhandler(Exception)
async def unexpected_exception(err):
    return {
        "error": {
            "title": "Internal Server Error",
            "status": 500,
            "reason": "Unexpected Exception",
        }
    }, 500


async def main():
    # Initialize connection to MongoDB server.
    connect(app, mongo_uri)

    if __name__ == "__main__":
        app.run()


# Execute the main function.
asyncio.run(main())
