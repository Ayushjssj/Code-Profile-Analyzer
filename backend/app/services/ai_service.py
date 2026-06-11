import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None

    return Groq(api_key=api_key)


def generate_ai_insights(profile):
    client = get_groq_client()

    if not client:
        return "Groq API key missing. Add GROQ_API_KEY in .env file."

    prompt = f"""
Analyze this coding profile and give concise career insights:

{profile}

Give:
Strengths
Weaknesses
Recommended Roles
Improvement Suggestions
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Insights Error: {str(e)}"


def generate_skill_recommendations(profile):
    client = get_groq_client()

    if not client:
        return "Groq API key missing. Add GROQ_API_KEY in .env file."

    prompt = f"""
You are an AI coding mentor.

Analyze this coding profile:

{profile}

Give skill recommendations in this exact format:

Current Level:
...

Recommended DSA Topics:
- topic 1
- topic 2
- topic 3

Recommended Projects:
- project 1
- project 2

Platform Improvement Plan:
- point 1
- point 2

Job Role Fit:
- role 1
- role 2

Keep it short and useful for a fresher software engineer.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Recommendation Error: {str(e)}"