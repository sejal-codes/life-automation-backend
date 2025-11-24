from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

app = FastAPI()

client = genai.Client()

class TaskRequest(BaseModel):
    tasks: list
    mood: str

@app.post("/tasks")
def generate_task_plan(req: TaskRequest):
    prompt = f"""
    Mood: {req.mood}
    Tasks: {", ".join(req.tasks)}
    Generate a structured productivity plan.
    """

    response = client.models.generate_content(
        model="models/gemini-1.5-flash-latest",
        contents=prompt
    )

    return {
        "plan": response.text
    }

