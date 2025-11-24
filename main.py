from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from datetime import datetime

app = FastAPI()

# Load Gemini Key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

class TaskRequest(BaseModel):
    tasks: list[str]
    mood: str

@app.get("/")
def home():
    return {"message": "Life Automation API Active"}

@app.get("/status")
def status():
    return {"status": "ok"}

@app.post("/tasks")
def generate_plan(req: TaskRequest):
    tasks_list = ", ".join(req.tasks)
    prompt = f"""
    Generate a clear, structured day plan based on this mood and tasks:
    Mood: {req.mood}
    Tasks: {tasks_list}

    Make it motivational, concise, and actionable.
    """

    try:
        model="models/gemini-1.5-flash"

        response = model.generate_content(prompt)

        return {
            "generated_at": datetime.now().strftime("%I:%M %p"),
            "plan": response.text
        }

    except Exception as e:
        return {"error": str(e)}
