#A task CRUD API in python
from fastapi import FastAPI

app = FastAPI()

list_of_tasks = [
    {"id": 1, "title": "Task 1", "done": False},
    {"id": 2, "title": "Task 2", "done": True},
    {"id": 3, "title": "Task 3", "done": False}
]

@app.get("/")
async def api_description():
    return { 
       "name": "Task API",
       "version": "1.0",
       "endpoints": ["/tasks"] 
    }

@app.get("/health")
async def health_check():
    return {
        "status": "Ok"
    }

@app.get("/tasks")
async def get_tasks():
    return list_of_tasks

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in list_of_tasks:
        if task["id"] == task_id:
            return task
    return { "error": f"Task {task_id} not found" }