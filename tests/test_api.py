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


def test_filter_characters_by_race():
    response = client.get("/characters", params={"race": "Saiyan"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert all(char["race"] == "Saiyan" for char in data)


def test_filter_characters_by_name():
    response = client.get("/characters", params={"name": "go"})
    assert response.status_code == 200
    data = response.json()
    assert any("go" in char["name"].lower() for char in data)


def test_filter_characters_by_origin_planet():
    response = client.get("/characters", params={"originPlanet": "Planet Vegeta"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert all(char["originPlanet"] == "Planet Vegeta" for char in data)


def test_filter_characters_by_min_ki():
    response = client.get("/characters", params={"min_ki": 10000})
    assert response.status_code == 200
    data = response.json()
    assert all(char["ki"] >= 10000 for char in data)


def test_get_character_by_id():
    response = client.get("/characters/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Goku"


def test_get_character_not_found():
    response = client.get("/characters/999")
    assert response.status_code == 404


def test_get_planets():
    response = client.get("/planets")
    assert response.status_code == 200
    data = response.json()
    assert any(planet["name"] == "Earth" for planet in data)


def test_get_planet_by_id():
    response = client.get("/planets/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Earth"


def test_get_planet_not_found():
    response = client.get("/planets/999")
    assert response.status_code == 404


def test_get_sagas():
    response = client.get("/sagas")
    assert response.status_code == 200
    data = response.json()
    assert any(saga["name"] == "Saiyan Saga" for saga in data)


def test_get_saga_by_id():
    response = client.get("/sagas/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Saiyan Saga"


def test_get_saga_not_found():
    response = client.get("/sagas/999")
    assert response.status_code == 404
