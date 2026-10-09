import os

import requests
from openai import OpenAI

from .prompts import MISSION_SYSTEM_PROMPT


def _build_user_prompt(
    duration: int,
    environment: str,
    interest: str,
    energy: str,
) -> str:
    return f"""
Create one outdoor observation mission.

Duration: {duration} minutes
Environment: {environment}
Interest: {interest}
Energy level: {energy}

Return only the final mission.
"""


def _generate_with_ollama(
    duration: int,
    environment: str,
    interest: str,
    energy: str,
) -> str:

    ollama_url = os.getenv(
        "OLLAMA_URL",
        "http://localhost:11434",
    )

    ollama_model = os.getenv(
        "OLLAMA_MODEL",
        "gemma4:e4b",
    )

    response = requests.post(
        f"{ollama_url.rstrip('/')}/api/generate",
        json={
            "model": ollama_model,
            "system": MISSION_SYSTEM_PROMPT,
            "prompt": _build_user_prompt(
                duration,
                environment,
                interest,
                energy,
            ),
            "stream": False,
            "options": {
                "temperature": 0.7,
            },
        },
        timeout=180,
    )

    response.raise_for_status()

    result = response.json().get(
        "response",
        "",
    ).strip()

    if not result:
        raise ValueError(
            "Ollama returned an empty response."
        )

    return result


def _generate_with_openrouter(
    duration: int,
    environment: str,
    interest: str,
    energy: str,
) -> str:

    api_key = os.getenv(
        "OPENROUTER_API_KEY"
    )

    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY is not configured."
        )

    model = os.getenv(
        "OPENROUTER_MODEL",
        "openai/gpt-oss-20b",
    )

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": MISSION_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": _build_user_prompt(
                    duration,
                    environment,
                    interest,
                    energy,
                ),
            },
        ],
        temperature=0.7,
        max_tokens=500,
    )

    if not response.choices:
        raise ValueError(
            "OpenRouter returned no choices."
        )

    content = response.choices[0].message.content

    if not content:
        raise ValueError(
            "OpenRouter returned empty content."
        )

    return content.strip()


def generate_mission(
    duration: int,
    environment: str,
    interest: str,
    energy: str,
    provider: str = "ollama",
) -> str:

    provider = provider.lower().strip()

    if provider == "ollama":
        return _generate_with_ollama(
            duration,
            environment,
            interest,
            energy,
        )

    if provider == "openrouter":
        return _generate_with_openrouter(
            duration,
            environment,
            interest,
            energy,
        )

    raise ValueError(
        f"Unsupported AI provider: {provider}"
    )