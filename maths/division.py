def perform_operation(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero.")
    return dividend / divisor