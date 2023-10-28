"""Test my zip function."""
__author__ = "730521715"

from lessons.zip import zip

def test_zip_mismatched_length_lists():
    """Tests the case where the two lists are of different lengths."""
    strings = ["a", "b"]
    integers = [1]
    assert zip(strings, integers) == {}

def test_zip_normal_case():
    """Tests a normal use case where two lists of the same length are combined."""
    strings = ["a", "b", "c"]
    integers = [1, 2, 3]
    assert zip(strings, integers) == {"a": 1, "b": 2, "c": 3}

def test_zip_empty_lists():
    """Tests the edge case where both lists are empty."""
    strings = []
    integers = []
    assert zip(strings, integers) == {}

if __name__ == "__main__":
    test_zip_mismatched_length_lists()
    test_zip_normal_case()
    test_zip_empty_lists()
