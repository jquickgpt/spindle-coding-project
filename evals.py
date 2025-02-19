import json
from src.agents.planner import parse_math_problem
from src.agents.executor import execute_operation
from src.agents.error_handler import detect_failure


def evaluate():
    """Runs a predefined set of math problems to test system accuracy."""
    test_cases = [
        ("three plus four", 7),
        ("eight minus two", 6),
        ("five times six", 30),
        ("nine divided by three", 3),
        ("ten modulo three", 1)
    ]

    results = []

    for user_input, expected in test_cases:
        parsed_data = parse_math_problem(user_input)

        # Handle errors from planner
        if "error" in parsed_data:
            results.append(
                {"input": user_input, "error": parsed_data["error"]})
            continue

        # Ensure required keys exist before unpacking
        if not all(k in parsed_data for k in ["operation", "num1", "num2"]):
            results.append(
                {"input": user_input, "error": "Missing keys in parsed response."})
            continue

        operation, num1, num2 = parsed_data["operation"], parsed_data["num1"], parsed_data["num2"]
        computed_result = execute_operation(operation, num1, num2)

        # Handle execution errors
        if "error" in computed_result:
            results.append(
                {"input": user_input, "error": computed_result["error"]})
            continue

        failure_check = detect_failure([computed_result["result"]])

        results.append({
            "input": user_input,
            "expected": expected,
            "computed": computed_result["result"],
            "status": failure_check["status"]
        })

    # Print structured JSON
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    evaluate()
