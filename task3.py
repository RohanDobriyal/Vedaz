from dotenv import load_dotenv
import os
import sys
import requests

# ── 1. Load env vars from .env.local ─────────────────────────────────────────────
load_dotenv(".env.local")

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
if not TOGETHER_API_KEY:
    print("Error: TOGETHER_API_KEY not set in .env.local", file=sys.stderr)
    sys.exit(1)

TOGETHER_API_URL = "https://api.together.ai/v1/chat/completions"

# ── 2. Astrological agent function ───────────────────────────────────────────────
def astrological_agent_together(reading: str) -> str:
    """
    Calls Together.ai chat API to get:
      1) One concise life insight (2–3 sentences)
      2) Two actionable tips
    based on a palm‑reading or horoscope summary.
    """
    # System + user messages per Together.ai chat API
    messages = [
        {
            "role": "system",
            "content": (
                "You are VedazAI, an empathetic digital astrologer. "
                "Given a palm‑reading description or horoscope summary, "
                "provide one concise life insight (2–3 sentences) "
                "and two actionable tips. "
                "Use a supportive, clear, and encouraging tone."
            )
        },
        {"role": "user", "content": reading}
    ]

    payload = {
        "model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        "messages": messages,
        "max_tokens": 120,
        "temperature": 0.7
    }
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    resp = requests.post(TOGETHER_API_URL, json=payload, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip()

# ── 3. Main execution ───────────────────────────────────────────────────────────
def main():
    dummy_reading = (
        "The heart line forks near the end, and the head line intersects the sun line."
    )
    advice = astrological_agent_together(dummy_reading)

    print("Input Reading:")
    print(f"  {dummy_reading}\n")
    print("VedazAI’s Insight & Tips:")
    print(advice)

if __name__ == "__main__":
    main()