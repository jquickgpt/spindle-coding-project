import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()  # Load OpenAI API key from .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def parse_math_problem(user_input):
    """Uses OpenAI API to parse a natural language math problem and extract structured data."""

    prompt = f"""
    You are a natural language processing assistant. Extract structured data from the following math problem.
    
    Problem: "{user_input}"
    
    Return a JSON object with:
    - "operation" (one of: "sum", "delta", "product", "quotient", "modulo")
    - "num1" (first number as an integer)
    - "num2" (second number as an integer)

    If the input is ambiguous, respond with: {{"error": "Ambiguous input, needs clarification"}}.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}],
        api_key=OPENAI_API_KEY
    )

    try:
        parsed_response = json.loads(
            response["choices"][0]["message"]["content"])
        return parsed_response
    except Exception:
        return {"error": "Failed to parse input."}
