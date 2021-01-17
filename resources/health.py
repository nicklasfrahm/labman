import socket
from datetime import datetime
from quart import Blueprint

started_at = datetime.utcnow().isoformat()
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
