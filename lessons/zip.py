"""Combining two lists into a dictionary."""

__author__ = "730521715"

from typing import List, Dict
from builtins import zip as _zip


def zip(keys: List[str], values: List[int]) -> Dict[str, int]:
    """Combine two lists into a dictionary.

    If the input lists are of different lengths or are empty, it returns an empty dictionary.
    
    Args:
    - keys: List of strings to be used as dictionary keys.
    - values: List of integers to be used as dictionary values.

    Returns:
    Dictionary combining the provided keys and values.
    """
    if len(keys) != len(values) or not keys or not values:
        return {}
    
    return dict(_zip(keys, values))


if __name__ == "__main__":
    print(zip(["Happy", "Tuesday", "Today"], [1, 2, 3]))  # Expected output: {"Happy": 1, "Tuesday": 2, "Today": 3}