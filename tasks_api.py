#A task CRUD API in python
from fastapi import FastAPI

app = FastAPI()

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
