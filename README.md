# DBAPI

DBAPI is a simple REST API that serves real Dragon Ball data for use in applications, games and prototypes.

## Setup

```bash
pip install -r requirements.txt
# By default the API runs on port 8000. Use --port to specify another port
# if 8000 is already in use, e.g. 8080.
uvicorn dbapi.main:app --reload --port 8080
```

## Endpoints

- `GET /characters` – List all characters. Optional query parameters
  `race`, `name`, `originPlanet` and `min_ki` can be used to filter the results.
- `GET /characters/{id}` – Retrieve a character by its numeric ID.
- `GET /planets` – List all known planets. Optional `name` query parameter.
- `GET /planets/{id}` – Retrieve a planet by its numeric ID.
- `GET /sagas` – List major story sagas. Optional `name` query parameter.
- `GET /sagas/{id}` – Retrieve a saga by its numeric ID.

## Testing

```bash
pytest
```
