from time import timezone
from datetime import datetime, timezone
from quart import Blueprint
from src.util import db

resource_name = "organizations"
blueprint = Blueprint(resource_name, __name__)


@blueprint.route("/" + resource_name)
async def list_organization():
    docs = await db().get_collection("test").find().to_list(10)
    return {"data": docs}
