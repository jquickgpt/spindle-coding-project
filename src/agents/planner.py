import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()  # Load OpenAI API key from .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def parse_math_problem(user_input):
    """Uses OpenAI API to parse a natural language math problem and extract structured data."""

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

        response_text = response.choices[0].message.content.strip()

        # Ensure the response is valid JSON
        try:
            parsed_response = json.loads(response_text)
            return parsed_response
        except json.JSONDecodeError:
            return {"error": "Invalid response format from OpenAI."}

    except openai.OpenAIError as e:
        return {"error": f"OpenAI API error: {str(e)}"}

    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
