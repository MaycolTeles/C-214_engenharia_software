"""
Module containing the "calculate_fibonacci" function.
"""


def calculate_fibonacci(stop: int) -> int:
    """
    Function to calculate the fibonacci number until the stop received as argument.

    Parameters
    -----------
    stop : int
        The number to stop the fibonacci counting.

    Returns
    --------
    int
        The fibonacci number value.
    """
    if stop < 2:
        return stop

    return calculate_fibonacci(stop - 1) + calculate_fibonacci(stop - 2)
