def is_close(a, b, rel_tol=1e-09, abs_tol=0.0):
    """
    Check if two numbers are approximately equal.

    Args:
        a: The first number to compare.
        b: The second number to compare.
        rel_tol: The relative tolerance (default: 1e-09).
        abs_tol: The absolute tolerance (default: 0.0).

    Returns:
        True if the numbers are approximately equal, False otherwise.

    Raises:
        TypeError: If the inputs are not numeric.
    """

    # Check if the inputs are numeric
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric.")

    # Handle special cases when a or b are infinite or NaN
    if a == b or abs(a - b) <= abs_tol:
        return True
    if abs(a) == float("inf") or abs(b) == float("inf"):
        return False
    if a != a or b != b:
        return False

    # Calculate the relative tolerance and compare
    diff = abs(a - b)
    max_abs = max(abs(a), abs(b))
    if diff <= max(abs_tol, rel_tol * max_abs):
        # Uncomment the following line to see the difference
        #print(f'diff: {diff}')
        return True
    else:
        # Uncomment the following line to see the difference
        #print(f'diff: {diff}')
        return False


# Test function
a = 2.000000000342
b = 2.000000000953
print(is_close(a, b))  # True with a relative tolerance of 2e-9

