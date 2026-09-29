import os

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)

# Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Please add it to your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)


def build_prompt(content_type, topic, tone, length, audience):
    prompt = f"""
You are a professional content creator and AI writing assistant.

Create the following type of content:

Content type: {content_type}
Topic: {topic}
Target audience: {audience}
Tone: {tone}
Length: {length}

Requirements:
- Make the content clear and useful.
- Match the requested tone.
- Write for the specified target audience.
- Organize the content appropriately.
- Do not invent statistics, facts, qualifications, or sources.
- Avoid unnecessary repetition.
- Produce polished, ready-to-use content.

Return only the generated content.
"""

    return prompt


@app.route("/")
def index():
    return render_template("index.html")


@app.post("/generate")
def generate():
    try:
        data = request.get_json() or {}

        content_type = data.get("content_type")
        topic = data.get("topic")
        tone = data.get("tone")
        length = data.get("length")
        audience = data.get("audience") or "general readers"

        if not content_type or not topic or not tone or not length:
            return jsonify({
                "error": "Please complete all required fields."
            }), 400

        prompt = build_prompt(
            content_type,
            topic,
            tone,
            length,
            audience
        )

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return jsonify({
            "content": response.text,
            "mode": "gemini"
        })

    except Exception as e:
        print("AI ERROR:", e)

        return jsonify({
            "error": "The AI could not generate the content. "
                     "Check your API key and internet connection."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)