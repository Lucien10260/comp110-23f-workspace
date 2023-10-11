"""EX04 Utils."""

__author__ = "730521715"

def all(numbers: list[int], n: int) -> bool:
    if len(numbers) == 0:
        return False
    i = 0
    while i < len(numbers):
        if numbers[i] != n:
            return False
        i += 1
    return True
def max(numbers: list[int]) -> int:
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
    if len(list1) != len(list2):
        return False
    i = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True
