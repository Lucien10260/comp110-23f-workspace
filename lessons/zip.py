"""Combining two lists into a dictionary."""
__author__ = "730521715"

from typing import List, Dict

def zip(strings: List[str], integers: List[int]) -> Dict[str, int]:
    if len(strings) != len(integers) or not strings or not integers:
        return {}
    
    return dict(zip(strings, integers))

# Example usage:
print(zip(["Happy", "Tuesday"], [1, 2]))  # {"Happy": 1, "Tuesday": 2}