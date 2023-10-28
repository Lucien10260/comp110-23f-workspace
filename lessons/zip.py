"""Combining two lists into a dictionary."""

__author__ = "730521715"


def zip(strings: list[str], integers: list[int]) -> dict[str, int]:
    """Combine two lists into a dictionary. The keys from the the first list and values are corresponding items from the second list."""
    if len(strings) != len(integers) or not strings or not integers:
        return {}

    final_dic = {}
    for i in range(len(strings)):
        final_dic[strings[i]] = integers[i]
    return final_dic