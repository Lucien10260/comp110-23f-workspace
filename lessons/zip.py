"""Combining two lists into a dictionary."""

__author__ = "YOUR_PID"

from typing import List, Dict


def zip(strings: List[str], numbers: List[int]) -> Dict[str, int]:
    """Combine two lists into a dictionary.
    
    Parameters:
    strings (List[str]): A list of strings to be used as dictionary keys.
    numbers (List[int]): A list of integers to be used as dictionary values.

    Returns:
    Dict[str, int]: A dictionary with strings as keys and numbers as values.
    If the input lists are of different lengths or empty, it returns an empty dictionary.
    """
    
    if len(strings) != len(numbers) or not strings or not numbers:
        return {}

    return {strings[i]: numbers[i] for i in range(len(strings))}


# Testing the function
if __name__ == "__main__":
    result = zip(["Happy", "Tuesday"], [1, 2])
    print(result)  # Expected: {"Happy": 1, "Tuesday": 2}