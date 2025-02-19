import random


def sum_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


def delta_numbers(a, b):
    """Returns the difference of two numbers."""
    return a - b


def product_numbers(a, b):
    """Returns the product of two numbers."""
    return a * b


def quotient_numbers(a, b):
    """Returns the quotient of two numbers, handling division by zero."""
    return a / b if b != 0 else None


def modulo_numbers(a, b):
    """Returns the remainder of division, handling division by zero."""
    return a % b if b != 0 else None


def unreliable_tool(a, b):
    """Performs addition but fails silently 40% of the time."""
    return sum_numbers(a, b) if random.random() > 0.4 else None
