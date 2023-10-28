"""Combining two lists into a dictionary"""

__author__ = "=730521715"

from typing import List, Dict

def zip(keys: List[str], values: List[int]) -> Dict[str, int]:
    if len(keys) != len(values) or not keys or not values:
        return {}
    
    return dict(zip(keys, values))