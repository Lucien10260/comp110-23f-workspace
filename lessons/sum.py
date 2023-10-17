"""Summing the elements of a list using different loops."""

__author__ = "730521715"

# Part 1: w_sum() function
def w_sum(vals: list[float]) -> float:
    """
    Compute the sum of a list of floats using a while loop.
    
    Parameters:
        vals (list[float]): List of floats to be summed.

    Returns:
        float: Sum of the list elements.
    """
    total = 0.0
    i = 0
    while i < len(vals):
        total += vals[i]
        i += 1
    return total


# Part 2: f_sum() function
def f_sum(vals: list[float]) -> float:
    """
    Compute the sum of a list of floats using a for loop.
    
    Parameters:
        vals (list[float]): List of floats to be summed.

    Returns:
        float: Sum of the list elements.
    """
    total = 0.0
    for val in vals:
        total += val
    return total


# Part 3: f_range_sum() function
def f_range_sum(vals: list[float]) -> float:
    """
    Compute the sum of a list of floats using a for loop with range.
    
    Parameters:
        vals (list[float]): List of floats to be summed.

    Returns:
        float: Sum of the list elements.
    """
    total = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total