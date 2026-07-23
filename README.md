# FlyRank Task API

A simple RESTful Task Management API built with **FastAPI** as part of the FlyRank Backend AI Engineering assignment.

The API demonstrates the implementation of basic CRUD (Create, Read, Update, Delete) operations using an in-memory data store.

---

## Features

- View API information
- Health check endpoint
- Retrieve all tasks
- Retrieve a task by ID
- Create a new task
- Update an existing task
- Delete a task
- Interactive Swagger documentation

---

## Tech Stack

- Python 3.12+
- FastAPI
- Uvicorn

---

## Project Structure

```
.
├── tasks_api.py
├── requirements.txt
├── README.md
└── venv/
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/leonorawalo/FlyRank-AI-_-Backend-AI-Engineering.git

cd FlyRank-AI-_-Backend-AI-Engineering
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate it

**Windows PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install fastapi "uvicorn[standard]"
```

---

## Running the API

```bash
python -m uvicorn tasks_api:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive Swagger documentation.

Visit:

```
http://127.0.0.1:8000/docs
```

or the ReDoc documentation:

```
http://127.0.0.1:8000/redoc
```

---

## Available Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/` | Returns API information |
| GET | `/health` | Returns API health status |
| GET | `/tasks` | Returns all tasks |
| GET | `/tasks/{id}` | Returns a single task |
| POST | `/tasks` | Creates a task |
| PUT | `/tasks/{id}` | Updates a task |
| DELETE | `/tasks/{id}` | Deletes a task |

---

## Example Response

### GET `/tasks`

```json
[
  {
    "id": 1,
    "title": "Study FastAPI",
    "done": false
  },
  {
    "id": 2,
    "title": "Push project to GitHub",
    "done": true
  }
]
```

---

## Swagger Screenshot

> Replace the image below with your own screenshot after completing the assignment.

![Swagger UI](images/swagger.png)

---

## Testing

The API can be tested using:

- Swagger UI (`/docs`)
- curl
- Postman

---

## Notes

This project uses an **in-memory list** to store tasks. Data is not persisted, so restarting the server resets all tasks.

---

## Author

**Leonora Awalo**