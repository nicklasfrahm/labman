import pytest
import re
from unittest import TestCase
from src.app import app


@pytest.fixture(name="test_app")
def get_app():
    return app


@pytest.mark.asyncio
async def test_list_health(test_app):
    # Arrange.
    iso_8601_pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z"

    # Act.
    client = app.test_client()
    response = await client.get("/health")
    data = await response.get_json()

    # Assert.
    assert response.status_code == 200
    payload = data.get("data")
    assert payload is not None
    assert len(payload.get("hostname")) > 1
    assert re.match(iso_8601_pattern, payload.get("started_at")) is not None
    assert len(payload.get("version")) > 1
