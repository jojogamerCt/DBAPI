from pathlib import Path
import json
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI(title="DBAPI", description="Dragon Ball API", version="0.2.0")

CHARACTERS_FILE = Path(__file__).parent / "data" / "characters.json"
PLANETS_FILE = Path(__file__).parent / "data" / "planets.json"
SAGAS_FILE = Path(__file__).parent / "data" / "sagas.json"


class Character(BaseModel):
    id: int
    name: str
    race: str
    description: str
    ki: int
    originPlanet: str


class Planet(BaseModel):
    id: int
    name: str
    description: str
    galaxy: str


class Saga(BaseModel):
    id: int
    name: str
    description: str


with open(CHARACTERS_FILE) as f:
    _characters: List[Character] = [Character(**c) for c in json.load(f)]

with open(PLANETS_FILE) as f:
    _planets: List[Planet] = [Planet(**p) for p in json.load(f)]

with open(SAGAS_FILE) as f:
    _sagas: List[Saga] = [Saga(**s) for s in json.load(f)]


@app.get("/characters", response_model=List[Character])
def list_characters(
    race: Optional[str] = Query(None, description="Filter by race"),
    name: Optional[str] = Query(None, description="Filter by name substring"),
    originPlanet: Optional[str] = Query(None, description="Filter by origin planet"),
    min_ki: Optional[int] = Query(None, description="Filter by minimum ki level"),
) -> List[Character]:
    """Return characters optionally filtered by race, name, origin planet or ki."""
    results = _characters
    if race:
        results = [c for c in results if c.race.lower() == race.lower()]
    if name:
        results = [c for c in results if name.lower() in c.name.lower()]
    if originPlanet:
        results = [c for c in results if c.originPlanet.lower() == originPlanet.lower()]
    if min_ki is not None:
        results = [c for c in results if c.ki >= min_ki]
    return results


@app.get("/characters/{character_id}", response_model=Character)
def get_character(character_id: int) -> Character:
    for character in _characters:
        if character.id == character_id:
            return character
    raise HTTPException(status_code=404, detail="Character not found")


@app.get("/planets", response_model=List[Planet])
def list_planets(name: Optional[str] = Query(None, description="Filter by name substring")) -> List[Planet]:
    """Return planets optionally filtered by name."""
    results = _planets
    if name:
        results = [p for p in results if name.lower() in p.name.lower()]
    return results


@app.get("/planets/{planet_id}", response_model=Planet)
def get_planet(planet_id: int) -> Planet:
    for planet in _planets:
        if planet.id == planet_id:
            return planet
    raise HTTPException(status_code=404, detail="Planet not found")


@app.get("/sagas", response_model=List[Saga])
def list_sagas(name: Optional[str] = Query(None, description="Filter by name substring")) -> List[Saga]:
    """Return sagas optionally filtered by name."""
    results = _sagas
    if name:
        results = [s for s in results if name.lower() in s.name.lower()]
    return results


@app.get("/sagas/{saga_id}", response_model=Saga)
def get_saga(saga_id: int) -> Saga:
    for saga in _sagas:
        if saga.id == saga_id:
            return saga
    raise HTTPException(status_code=404, detail="Saga not found")

