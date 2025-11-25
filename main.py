# File: main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins for simplicity
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskRequest(BaseModel):
    name: str

def break_task_into_steps(task: str):
    task = task.lower()
    if "blog" in task:
        return [
            "Pick your blog topic",
            "Research the topic for 10 minutes",
            "Write a rough outline",
            "Write the introduction",
            "Write 2–3 main sections",
            "Write the conclusion",
            "Proofread and publish"
        ]
    elif "study" in task:
        return [
            "Decide the chapter/topic to study",
            "Collect notes/videos/resources",
            "Study for 25 minutes",
            "Take a 5-minute break",
            "Revise what you learned",
            "Solve 5–10 questions",
            "Summarize in 3–4 lines"
        ]
    elif "exercise" in task:
        return [
            "Warm-up for 5 minutes",
            "Do your main workout (10–20 mins)",
            "Cool down",
            "Stretch for 3 minutes",
            "Drink water"
        ]
    else:
        return [
            f"Break down the task: {task}",
            "Identify the first small action",
            "Complete that action",
            "Move to next logical step",
            "Review and complete the task"
        ]

# Dummy tasks list
tasks = []

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(task_request: TaskRequest):
    tasks.append({"name": task_request.name})
    return {"message": "Task added"}

@app.post("/generate_task")
def generate_task(task_request: TaskRequest):
    steps = break_task_into_steps(task_request.name)
    return {"task": task_request.name, "steps": steps}

@app.get("/status")
def status():
    return {"status": "Backend is running"}