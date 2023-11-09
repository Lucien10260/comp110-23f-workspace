"""Dictionart_test."""

__author__ = "730521715"

import pytest

# Assuming the functions are defined in a file named `functions.py` which is in the same directory.
from functions import invert, favorite_color, count, alphabetize, update_attendance

# Unit tests for invert
def test_invert_normal_case() -> None:
    assert invert({'a': 1, 'b': 2, 'c': 3}) == {1: 'a', 2: 'b', 3: 'c'}

def test_invert_empty_dict() -> None:
    assert invert({}) == {}

def test_invert_value_collision() -> None:
    with pytest.raises(ValueError):
        invert({'a': 1, 'b': 1})

# Unit tests for favorite_color
def test_favorite_color_normal_case() -> None:
    assert favorite_color({'Alice': 'blue', 'Bob': 'green', 'Charlie': 'blue'}) == 'blue'

def test_favorite_color_empty_dict() -> None:
    assert favorite_color({}) == None

def test_favorite_color_tie() -> None:
    assert favorite_color({'Alice': 'blue', 'Bob': 'green', 'Charlie': 'green'}) in ['blue', 'green']

# Unit tests for count
def test_count_normal_case() -> None:
    assert count(['red', 'blue', 'red', 'green', 'blue', 'blue']) == {'red': 2, 'blue': 3, 'green': 1}

def test_count_empty_list() -> None:
    assert count([]) == {}

def test_count_single_element() -> None:
    assert count(['red']) == {'red': 1}

# Unit tests for alphabetizer
def test_alphabetizer_normal_case() -> None:
    assert alphabetize(['hello', 'apple', 'banana']) == ['apple', 'banana', 'hello']

def test_alphabetizer_empty_list() -> None:
    assert alphabetize([]) == []

def test_alphabetizer_case_insensitivity() -> None:
    assert alphabetize(['Hello', 'apple']) == ['apple', 'Hello']

# Unit tests for update_attendance
def test_update_attendance_normal_case() -> None:
    attendance = {'Monday': ['Alice', 'Bob'], 'Wednesday': [], 'Friday': ['Alice', 'Charlie']}
    update_attendance(attendance, 'Monday', 'Charlie')
    assert attendance == {'Monday': ['Alice', 'Bob', 'Charlie'], 'Wednesday': [], 'Friday': ['Alice', 'Charlie']}

def test_update_attendance_new_day() -> None:
    attendance = {}
    update_attendance(attendance, 'Tuesday', 'Alice')
    assert attendance == {'Tuesday': ['Alice']}

def test_update_attendance_empty_case() -> None:
    attendance = {'Monday': []}
    update_attendance(attendance, 'Monday', 'Bob')
    assert attendance == {'Monday': ['Bob']}
