# DBAPI

DBAPI is a simple REST API that serves real Dragon Ball data for use in applications, games and prototypes.

## Setup

```bash
pip install -r requirements.txt
uvicorn dbapi.main:app --reload
```

## Endpoints

- `GET /characters` – List all characters.
- `GET /characters/{id}` – Retrieve a character by its numeric ID.

## Testing

```bash
pytest
```
