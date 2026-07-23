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

@app.post("/tasks")
async def create_task(task: dict):
    task_id = len(list_of_tasks) + 1
    task["id"] = task_id
    list_of_tasks.append(task)
    return task

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, updated_task: dict):
    for task in list_of_tasks:
        if task["id"] == task_id:
            task.update(updated_task)
            return task
    return { "error": f"Task {task_id} not found" }

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in list_of_tasks:
        if task["id"] == task_id:
            list_of_tasks.remove(task)
            return { "message": f"Task {task_id} deleted" }
    return { "error": f"Task {task_id} not found" }