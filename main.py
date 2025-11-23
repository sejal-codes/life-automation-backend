from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "running", "message": "Life Automation API working!"})

@app.route("/daily-plan", methods=["POST"])
def daily_plan():
    data = request.get_json()

    tasks = data.get("tasks", [])
    mood = data.get("mood", "neutral")

    now = datetime.datetime.now().strftime("%I:%M %p")

    response = {
        "generated_at": now,
        "tasks_received": tasks,
        "plan": f"Your mood is {mood}. Start with the most important task: '{tasks[0]}'"
        if tasks else "No tasks provided."
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
