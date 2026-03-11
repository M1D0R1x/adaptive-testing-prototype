import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_study_plan(missed_topics, final_ability, ability_band):
    """
    Generates a personalized study plan using Gemini.
    """

    if missed_topics:
        topics = ", ".join(
            [f"{topic} ({count} errors)" for topic, count in missed_topics]
        )
    else:
        topics = "No clear weak topics detected."

    prompt = f"""
You are an expert GRE tutor.

Student diagnostic summary:

Ability score (0-1 scale): {final_ability:.2f}
Ability category: {ability_band}

Weak topics identified:
{topics}

Create a concise personalized improvement plan.

Rules:
- Exactly 3 steps
- Each step must include concrete practice advice
- Avoid generic motivational language
- Keep explanations short and practical
"""

    try:

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
        )

        return response.text.strip()

    except Exception:

        return f"""
Fallback Study Plan

Ability level: {ability_band}

1. Review the theory for weak topics: {topics}

2. Practice 15–20 problems daily near difficulty level {final_ability:.2f}

3. Take another adaptive diagnostic test after 1 week to measure improvement
"""