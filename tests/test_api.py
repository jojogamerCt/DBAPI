import os
import sys

from fastapi.testclient import TestClient

# Ensure project root is on sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dbapi.main import app

client = TestClient(app)


def test_get_characters():
    response = client.get("/characters")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(char["name"] == "Goku" for char in data)


def test_get_character_by_id():
    response = client.get("/characters/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Goku"


def test_get_character_not_found():
    response = client.get("/characters/999")
    assert response.status_code == 404
