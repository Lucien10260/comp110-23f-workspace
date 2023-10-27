"""Combining two lists into a dictionary."""

__author__ = "730521715"

from typing import List, Dict

def zip(strings: List[str], integers: List[int]) -> Dict[str, int]:
    """
    Combines two lists into a dictionary.

    Args:
    - strings (List[str]): List of strings to be used as keys in the dictionary.
    - integers (List[int]): List of integers to be used as values in the dictionary.

    Returns:
    - Dict[str, int]: Dictionary with strings as keys and integers as values.
                      Returns an empty dictionary if the input lists are different lengths or if they are empty.
    """
    if len(strings) != len(integers) or not strings or not integers:
        return {}

    combined = {}
    for i in range(len(strings)):
        combined[strings[i]] = integers[i]
    
    return combined

# Example usage:
if __name__ == "__main__":
    result = zip(["Happy", "Tuesday"], [1, 2])
    print(result)  # Expected output: {"Happy": 1, "Tuesday": 2}
