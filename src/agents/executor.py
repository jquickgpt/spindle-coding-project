from src.tools.math_tools import (
    sum_numbers, delta_numbers, product_numbers,
    quotient_numbers, modulo_numbers
)
from src.utils.vector_db import store_solution


def execute_operation(operation, a, b, trials=100):
    """Executes an operation multiple times, stores in VDB, and returns the most common result."""

    operations = {
        "sum": sum_numbers,
        "delta": delta_numbers,
        "product": product_numbers,
        "quotient": quotient_numbers,
        "modulo": modulo_numbers
    }

    operation_func = operations.get(operation)

    if not operation_func:
        return {"error": "Invalid operation type"}

    results = [operation_func(a, b) for _ in range(trials)]

    # Filter out None values (silent failures)
    filtered_results = [r for r in results if r is not None]

    if not filtered_results:
        return {"error": "Too many failures, unable to compute"}

    # Return the most common result
    final_result = max(set(filtered_results), key=filtered_results.count)

    # Store problem and result in VDB
    problem = f"{a} {operation} {b}"
    solution = {"operation": operation, "num1": a,
                "num2": b, "result": final_result}
    store_solution(problem, solution)

    return solution
