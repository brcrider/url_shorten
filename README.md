# URL Shortener

Simple Flask-based URL shortener using SQLite. From Roadmap.sh ("https://roadmap.sh/projects/url-shortening-service")

Overview
--------
This small project exposes three HTTP endpoints to create, retrieve and update shortened URLs. It stores mappings in a local SQLite database (`db.db`). The database table is created automatically when running the app.

Features
--------
- Shorten a long URL (generates a 6-character alphanumeric code).
- Retrieve the stored record for a short code.
- Update the long URL for an existing short code.

Prerequisites
-------------
- Python 3.8+ (3.10/3.11 recommended)
- pip

Install
-------
1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install Flask:

```powershell
pip install flask
```

Run
---
Start the Flask app from the project root:

```powershell
python apps.py
```

The app runs in debug mode by default and will create the `db.db` SQLite file if missing.

HTTP API
--------
1) POST /shorten
- Description: Create a short code for a long URL.
- Request JSON: { "url": "https://example.com/very/long/path" }
- Response: 201 Created
- Body: { "short_url": "abc123" }

2) GET /retrieve/<short>
- Description: Retrieve the database row for a short code.
- Response on success: 200 OK
- Body: { "long_url": [id, shortCode, url, created_at, updated_at] }
- Response on not found: 404 with { "error": "Short URL not found" }

3) PUT /update/<short>
- Description: Update the long URL associated with a short code.
- Request JSON: { "url": "https://new.example.com/" }
- Response on success: 200 OK
- Body: { "result": [id, shortCode, url, created_at, updated_at] }
- Response on not found: 404 with { "error": "Short URL not found" }

Examples (using curl in PowerShell)
---------------------------------

Create a short URL:

```powershell
curl -X POST http://127.0.0.1:5000/shorten -H "Content-Type: application/json" -d '{"url":"https://example.com"}'
```

Retrieve:

```powershell
curl http://127.0.0.1:5000/retrieve/abc123
```

Update:

```powershell
curl -X PUT http://127.0.0.1:5000/update/abc123 -H "Content-Type: application/json" -d '{"url":"https://new.example.com"}'
```

Notes
-----
- The project uses a local SQLite file `db.db` in the project root. The schema is created by calling `create_table()` at startup.
- Current API returns the full DB row as a list for the retrieve/update endpoints. You can change `models.py` / `routes.py` to return a cleaned JSON object if desired.

