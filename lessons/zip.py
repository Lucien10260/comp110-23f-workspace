"""
This module provides a function to combine two lists into a dictionary.
"""

__author__ = "730521715"

from typing import List, Dict

def zip(strings: List[str], integers: List[int]) -> Dict[str, int]:
    """Combines two lists into a dictionary."""
    if len(strings) != len(integers):
        return {}

    combined = {}
    for i in range(len(strings)):
        combined[strings[i]] = integers[i]
    
    return combined


if __name__ == "__main__":
    result = zip(["Happy", "Tuesday"], [1, 2])
    print(result)  # Expected output: {"Happy": 1, "Tuesday": 2}