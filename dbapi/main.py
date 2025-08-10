from pathlib import Path
import json
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="DBAPI", description="Dragon Ball API", version="0.1.0")

DATA_FILE = Path(__file__).parent / "data" / "characters.json"

class Character(BaseModel):
    id: int
    name: str
    race: str
    description: str
    ki: int
    originPlanet: str

with open(DATA_FILE) as f:
    _characters: List[Character] = [Character(**c) for c in json.load(f)]

@app.get("/characters", response_model=List[Character])
def list_characters() -> List[Character]:
    return _characters

@app.get("/characters/{character_id}", response_model=Character)
def get_character(character_id: int) -> Character:
    for character in _characters:
        if character.id == character_id:
            return character
    raise HTTPException(status_code=404, detail="Character not found")

