"""Dictionary_test."""

__author__ = "730521715"

import pytest
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_normal():
    """Test invert with a normal dictionary."""
    assert invert({'a': '1', 'b': '2'}) == {'1': 'a', '2': 'b'}


def test_invert_single_item():
    """Test invert with a dictionary with one item."""
    assert invert({'a': '1'}) == {'1': 'a'}


def test_invert_raise_key_error():
    """Test invert should raise KeyError on duplicate values."""
    with pytest.raises(KeyError):
        invert({'a': 'apple', 'b': 'apple'})


def test_favorite_color_normal():
    """Test favorite_color with normal input."""
    assert favorite_color({'Alice': 'blue', 'Bob': 'green', 'Charlie': 'blue'}) == 'blue'


def test_favorite_color_tie():
    """Test favorite_color with a tie."""
    assert favorite_color({'Alice': 'blue', 'Bob': 'green', 'Charlie': 'green', 'David': 'blue'}) in ['blue', 'green']


def test_favorite_color_empty():
    """Test favorite_color with an empty dictionary."""
    with pytest.raises(ValueError):
        favorite_color({})


def test_count_normal_v1():
    """Test count with multiple duplicates."""
    assert count(['a', 'b', 'a', 'c', 'b', 'a']) == {'a': 3, 'b': 2, 'c': 1}


def test_count_single_item_v1():
    """Test count with a single item."""
    assert count(['a']) == {'a': 1}


def test_count_empty_v1():
    """Test count with an empty list."""
    assert count([]) == {}


def test_alphabetizer_normal():
    """Test alphabetizer with different first letters."""
    assert alphabetizer(['apple', 'banana', 'apricot', 'blueberry']) == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}


def test_alphabetizer_same_letter():
    """Test alphabetizer with words starting with the same letter."""
    assert alphabetizer(['apple', 'apricot']) == {'a': ['apple', 'apricot']}


def test_alphabetizer_empty():
    """Test alphabetizer with an empty list."""
    assert alphabetizer([]) == {}


def test_update_attendance_add_new_day():
    """Test update_attendance adding a student to a new day."""
    attendance = {}
    assert update_attendance(attendance, 'Monday', 'Alice') == {'Monday': ['Alice']}


def test_update_attendance_add_to_existing_day():
    """Test update_attendance adding a student to an existing day."""
    attendance = {'Monday': ['Alice']}
    assert update_attendance(attendance, 'Monday', 'Bob') == {'Monday': ['Alice', 'Bob']}


def test_update_attendance_add_duplicate():
    """Test update_attendance adding a duplicate entry."""
    attendance = {'Monday': ['Alice']}
    assert update_attendance(attendance, 'Monday', 'Alice') == {'Monday': ['Alice']}