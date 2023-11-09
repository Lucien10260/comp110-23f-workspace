"""Dictionart_test."""

__author__ = "730521715"

def test_invert_with_valid_input():
    """Test invert function with a dictionary containing non-conflicting pairs."""
    assert invert({'a': '1', 'b': '2'}) == {'1': 'a', '2': 'b'}

def test_invert_with_non_string_values():
    """Test invert function with non-string values."""
    assert invert({1: 'a', 2: 'b'}) == {'a': 1, 'b': 2}

def test_invert_raises_key_error_on_duplicate_values():
    """Test invert function raises KeyError on duplicate values."""
    with pytest.raises(KeyError):
        invert({'a': '1', 'b': '1'})

def test_favorite_color_with_common_favorite():
    """Test favorite_color returns the most common color."""
    assert favorite_color({'Alice': 'blue', 'Bob': 'blue', 'Charlie': 'red'}) == 'blue'

def test_favorite_color_with_tie():
    """Test favorite_color returns one of the most common colors in case of a tie."""
    assert favorite_color({'Alice': 'blue', 'Bob': 'red', 'Charlie': 'red', 'David': 'blue'}) in ['blue', 'red']

def test_favorite_color_with_empty_dict():
    """Test favorite_color with an empty dictionary."""
    assert favorite_color({}) is None

def test_count_with_valid_list():
    """Test count function with a list of items."""
    assert count(['a', 'b', 'a', 'c', 'b', 'a']) == {'a': 3, 'b': 2, 'c': 1}

def test_count_with_empty_list():
    """Test count function with an empty list."""
    assert count([]) == {}

def test_count_with_non_hashable_elements():
    """Test count function with non-hashable elements in the list."""
    with pytest.raises(TypeError):
        count(['a', 'b', 'a', ['c', 'b'], 'a'])

def test_alphabetize_with_unsorted_list():
    """Test alphabetize function sorts the list alphabetically."""
    assert alphabetize(['banana', 'apple', 'cherry']) == ['apple', 'banana', 'cherry']

def test_alphabetize_with_already_sorted_list():
    """Test alphabetize function with an already sorted list."""
    assert alphabetize(['apple', 'banana', 'cherry']) == ['apple', 'banana', 'cherry']

def test_alphabetize_with_empty_list():
    """Test alphabetize function with an empty list."""
    assert alphabetize([]) == []

def test_update_attendance_with_present_student():
    """Test update_attendance marks a present student correctly."""
    attendance = {'Alice': 'absent', 'Bob': 'present'}
    update_attendance(attendance, 'Alice')
    assert attendance == {'Alice': 'present', 'Bob': 'present'}

def test_update_attendance_with_all_students_absent():
    """Test update_attendance with all students initially absent."""
    attendance = {'Alice': 'absent', 'Bob': 'absent'}
    update_attendance(attendance, 'Alice')
    assert attendance == {'Alice': 'present', 'Bob': 'absent'}

def test_update_attendance_with_nonexistent_student():
    """Test update_attendance with a student name not in the attendance."""
    attendance = {'Alice': 'absent', 'Bob': 'present'}
    with pytest.raises(KeyError):
        update_attendance(attendance, 'Charlie')