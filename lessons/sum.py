"""Summing the elements of a list using different loops."""

__author__ = "730521715"


def w_sum(vals: list[float]) -> float:
    """Compute the sum of a list of floats using a while loop.

    Args:
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


def f_sum(vals: list[float]) -> float:
    """Compute the sum of a list of floats using a for loop.

    Args:
        vals (list[float]): List of floats to be summed.

    Returns:
        float: Sum of the list elements.
    """
    total = 0.0
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """Compute the sum of a list of floats using a for loop with range.

    Args:
        vals (list[float]): List of floats to be summed.

    Returns:
        float: Sum of the list elements.
    """
    total = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total