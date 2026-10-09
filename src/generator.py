from openai import OpenAI

from .prompts import MISSION_SYSTEM_PROMPT


MODEL = "openai/gpt-oss-20b"


def generate_mission(
    client: OpenAI,
    duration: int,
    environment: str,
    interest: str,
    energy: str,
) -> str:

    user_prompt = f"""
Create one outdoor observation mission.

Duration: {duration} minutes
Environment: {environment}
Interest: {interest}
Energy level: {energy}

Keep it concise, complete, safe, and specific.
Return only the final mission.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": MISSION_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0.7,
        max_tokens=500,
    )

    if not response.choices:
        raise ValueError("OpenRouter returned no choices.")

    content = response.choices[0].message.content

    if not content:
        raise ValueError("OpenRouter returned empty content.")

    return content.strip()