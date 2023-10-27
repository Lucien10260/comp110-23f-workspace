"""
Combining two lists into a dictionary
"""

__author__ = "730521715"

from typing import List, Dict

def zip(strings: List[str], numbers: List[int]) -> Dict[str, int]:
    # Return an empty dictionary if the input lists are of different lengths or empty
    if len(strings) != len(numbers) or not strings or not numbers:
        return {}

    return {strings[i]: numbers[i] for i in range(len(strings))}

# Testing the function
if __name__ == "__main__":
    result = zip(["Happy", "Tuesday"], [1, 2])
    print(result)  # Expected: {"Happy": 1, "Tuesday": 2}
