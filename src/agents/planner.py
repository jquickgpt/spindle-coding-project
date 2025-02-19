import json
import openai
import os
from dotenv import load_dotenv
from src.utils.vector_db import find_similar_problem, store_solution

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def parse_math_problem(user_input):
    """Uses OpenAI API to parse a math problem, but first checks VDB for reuse."""

    cached_solution = find_similar_problem(user_input)
    if cached_solution:
        return {"cached": True, "solution": cached_solution}

    system_prompt = """
    You are an AI assistant designed to extract structured data from natural language math problems.
    Given a problem like "three plus four", return a JSON object with:
    - "operation" (one of: "sum", "delta", "product", "quotient", "modulo")
    - "num1" (first number as an integer)
    - "num2" (second number as an integer)

    If the input is ambiguous or unclear, respond with:
    {"error": "Ambiguous input, needs clarification"}
    """

    client = openai.Client(api_key=OPENAI_API_KEY)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )

        parsed_response = json.loads(response.choices[0].message.content)
        return parsed_response
    except Exception as e:
        return {"error": f"Failed to parse input: {str(e)}"}
