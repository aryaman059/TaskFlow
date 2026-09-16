from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="TaskFlow API")


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


tasks = []


@app.get("/")
def root():
    return {"message": "TaskFlow API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/tasks")
def create_task(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task


@app.get("/tasks")
def get_tasks():
    return tasks


@app.patch("/tasks/{task_id}")
def complete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")