# Hello World - Unit Tests

# Imports
import pytest
from fastapi.testclient import TestClient

# Load settings
from app.config.config import Settings
from app.functions.get_settings import get_settings
from app.main import app

client = TestClient(app)


def get_settings_override():
    return Settings()


app.dependency_overrides[get_settings] = get_settings_override


@pytest.mark.dependency()
def test_helloworld(request):
    response = client.get("/v1/helloworld")
    assert response.status_code == 200
