import socket
from time import timezone
from datetime import datetime, timezone
from quart import Blueprint

started_at = f"{datetime.now(timezone.utc).replace(microsecond=0).isoformat()[:-6]}Z"
hostname = socket.gethostname()
blueprint = Blueprint("health", __name__)


@blueprint.route("/health")
async def list_health():
    return {
        "data": {
            "version": "dev",
            "hostname": hostname,
            "started_at": started_at,
        }
    }
