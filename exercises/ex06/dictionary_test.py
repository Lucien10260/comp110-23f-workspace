"""Dictionary_test module: Unit tests for dictionary utility functions."""


__author__ = "730521715"


import pytest


from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance



# Unit tests for invert
def test_invert_normal_case() -> None:
    """Test inverting a dictionary with distinct key-value pairs."""
    assert invert({'a': 1, 'b': 2, 'c': 3}) == {1: 'a', 2: 'b', 3: 'c'}


def test_invert_empty_dict() -> None:
    """Test inverting an empty dictionary."""
    assert invert({}) == {}


def test_invert_value_collision() -> None:
    """Test inverting a dictionary with value collisions raises a ValueError."""
    with pytest.raises(ValueError):
        invert({'a': 1, 'b': 1})


# Unit tests for favorite_color
def test_favorite_color_normal_case() -> None:
    """Test favorite_color with a clear winner color."""
    assert favorite_color({'Alice': 'blue', 'Bob': 'green', 'Charlie': 'blue'}) == 'blue'


def test_favorite_color_empty_dict() -> None:
    """Test favorite_color with an empty dictionary."""
    assert favorite_color({}) is None


def test_favorite_color_tie() -> None:
    """Test favorite_color when there is a tie in colors."""
    assert favorite_color({'Alice': 'blue', 'Bob': 'green', 'Charlie': 'green'}) in ['blue', 'green']


# Unit tests for count
def test_count_normal_case() -> None:
    """Test counting elements in a list with multiple occurrences."""
    assert count(['red', 'blue', 'red', 'green', 'blue', 'blue']) == {'red': 2, 'blue': 3, 'green': 1}


def test_count_empty_list() -> None:
    """Test counting elements in an empty list."""
    assert count([]) == {}


def test_count_single_element() -> None:
    """Test counting elements in a list with a single element."""
    assert count(['red']) == {'red': 1}


# Unit tests for alphabetize
def test_alphabetize_normal_case() -> None:
    """Test alphabetizing a list of strings."""
    assert alphabetize(['hello', 'apple', 'banana']) == ['apple', 'banana', 'hello']


def test_alphabetize_empty_list() -> None:
    """Test alphabetizing an empty list."""
    assert alphabetize([]) == []


def test_alphabetize_case_insensitivity() -> None:
    """Test alphabetizing a list of strings with varying case."""
    assert alphabetize(['Hello', 'apple']) == ['apple', 'Hello']


# Unit tests for update_attendance
def test_update_attendance_normal_case() -> None:
    """Test updating attendance with a new name on an existing day."""
    attendance = {'Monday': ['Alice', 'Bob'], 'Wednesday': [], 'Friday': ['Alice', 'Charlie']}
    update_attendance(attendance, 'Monday', 'Charlie')
    assert attendance == {'Monday': ['Alice', 'Bob', 'Charlie'], 'Wednesday': [], 'Friday': ['Alice', 'Charlie']}


def test_update_attendance_new_day() -> None:
    """Test updating attendance by adding a new day with a name."""
    attendance = {}
    update_attendance(attendance, 'Tuesday', 'Alice')
    assert attendance == {'Tuesday': ['Alice']}


def test_update_attendance_empty_case() -> None:
    """Test updating attendance with a new name on an empty day."""
    attendance = {'Monday': []}
    update_attendance(attendance, 'Monday', 'Bob')
    assert attendance == {'Monday': ['Bob']}