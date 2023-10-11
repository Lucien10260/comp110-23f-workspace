"""EX04 Utils."""

__author__ = "730521715"


def all(numbers: list[int], n: int) -> bool:
    """Check if all elements in a list match a given value.

    Args:
    - numbers: A list of integers.
    - n: An integer to match.

    Returns:
    - bool: True if all elements match n, False otherwise.
    """
    if len(numbers) == 0:
        return False

    i = 0
    while i < len(numbers):
        if numbers[i] != n:
            return False
        i += 1
    return True


def max(numbers: list[int]) -> int:
    """Find the maximum value in a list of integers.

    Args:
    - numbers: A list of integers.

    Returns:
    - int: The largest integer in the list.
    
    Raises:
    - ValueError: If the list is empty.
    """
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")

    i = 1
    largest = numbers[0]
    while i < len(numbers):
        if numbers[i] > largest:
            largest = numbers[i]
        i += 1
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Check if two lists are deeply equal.

    Args:
    - list1: First list of integers.
    - list2: Second list of integers.

    Returns:
    - bool: True if lists are equal, False otherwise.
    """
    if len(list1) != len(list2):
        return False
    
    i = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True
