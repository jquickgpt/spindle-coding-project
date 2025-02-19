import json
from src.agents.planner import parse_math_problem
from src.agents.executor import execute_operation
from src.agents.error_handler import detect_failure


def main():
    """Main function to process user input and return structured JSON results."""
    print("\nEnter a math problem (e.g., 'three plus four'). Type 'exit' to quit.")

    while True:
        user_input = input("\nUser: ")

        if user_input.lower() == "exit":
            print("\nExiting program.")
            break

        # Step 1: Parse user input using OpenAI-powered planner
        parsed_data = parse_math_problem(user_input)

        # If cached solution exists, use it
        if "cached" in parsed_data and parsed_data["cached"]:
            cached_solution = parsed_data["solution"]
            result = cached_solution
        else:
            if "error" in parsed_data:
                print(json.dumps({"error": parsed_data["error"]}, indent=2))
                continue

            operation, num1, num2 = parsed_data["operation"], parsed_data["num1"], parsed_data["num2"]

            # Step 2: Execute the operation using redundant computation
            result = execute_operation(operation, num1, num2)

            if "error" in result:
                print(json.dumps({"error": result["error"]}, indent=2))
                continue

        # Step 3: Run error detection to check for failures
        failure_check = detect_failure([result["result"]])

        # Step 4: Output structured JSON response
        final_output = {
            "input": user_input,
            "parsed": parsed_data if "cached" not in parsed_data else "Cached result used",
            "computed_result": result,
            "failure_analysis": failure_check
        }

        print(json.dumps(final_output, indent=2))


if __name__ == "__main__":
    main()
