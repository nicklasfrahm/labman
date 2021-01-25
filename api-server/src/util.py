from datetime import datetime, timezone
from urllib.parse import urlparse
from quart_motor import Motor
import sys

# Cache the client for subsequent connection attempts.
motor = None


def initialize(app, mongo_uri):
    """Configure the MongoDB database driver."""
    global motor

    if motor is None:
        motor = Motor(
            app,
            mongo_uri,
            connectTimeoutMS=500,
            serverSelectionTimeoutMS=500,
        )


def db():
    """Fetches the instance of the asynchronous MongoDB database."""
    return motor.db


def default_datetime() -> datetime:
    """Returns the current time in UTC format as a datetime object."""
    return datetime.now(timezone.utc).replace(microsecond=0)