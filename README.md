# Conference REST API

Simple RESTful service for managing conferences and sessions. Supports user authentication and JWT authorization.

Built with **Python** and **Flask**. 

Database: **SQLite**. The database is stored in *data* directory, which is created automatically when the app starts.
## Database Tables
- users
- sessions
- conferences
- registrations
- refresh_tokens

## Features

- User authentication (JWT)
- Manage conferences
- Manage sessions
- Conference registrations
- JSON REST API

## Tech Stack

- Python
- Flask
- Pydantic
- SQLAlchemy
- PyJWT
- Bcrypt

## Run locally

```bash
git clone <repo>
cd <repo>
pip install -r requirements.txt
python app.py
```

## API

Available endpoints:

```
GET /api/v1/users
GET /api/v1/users/<id>
DELETE /api/v1/users/<id>

POST /api/v1/auth/register
POST /api/v1/auth/login

GET /api/v1/sessions
GET /api/v1/sessions/<id>
POST /api/v1/sessions
DELETE /api/v1/sessions/<id>

GET /api/v1/conferences
GET /api/v1/conferences/<id>
POST /api/v1/conferences
DELETE /api/v1/conferences/<id>

GET /api/v1/registrations
GET /api/v1/registrations/<id>
POST /api/v1/registrations
DELETE /api/v1/registrations/<id>
```

## Example Request

POST /api/v1/auth/register
```json
{
    "name": "name",
    "email": "email@gmail.com",
    "phone": "1-012-012-0123",
    "password": "qwerty"
}
```
## Response
```json
{
  "access_token": "...",
  "refresh_token": "..."
}
```