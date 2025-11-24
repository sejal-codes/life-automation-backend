from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)

# Initialize Google GenAI client
client = genai.Client()

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "ok"})


@app.route("/tasks", methods=["POST"])
def generate_plan():
    try:
        data = request.get_json()
        tasks = data.get("tasks", [])
        mood = data.get("mood", "neutral")

        prompt = f"""
        You are Life Automation AI.
        The user's mood is: {mood}.
        These are the tasks: {tasks}.

        Generate a short, motivating, structured plan for the day.
        """

        # Correct API call for latest Gemini models
        response = client.models.generate_content(
            model="models/gemini-1.5-flash",
            contents=prompt
        )

        ai_output = response.text

        return jsonify({
            "generated_plan": ai_output
        })

    except Exception as e:
        return jsonify({"err
