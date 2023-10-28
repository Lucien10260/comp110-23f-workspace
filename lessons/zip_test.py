"""Test my zip function."""

__author__ = "730521715"

from lessons.zip import zip


def test_zip_mismatched_length_lists() -> None:
    """Tests the case where the two lists are of different lengths."""
    strings: list[str] = ["a", "b"]
    integers: list[int] = [1]
    assert zip(strings, integers) == {}


def test_zip_normal_case() -> None:
    """Tests a normal use case where two lists of the same length are combined."""
    strings: list[str] = ["a", "b", "c"]
    integers: list[int] = [1, 2, 3]
    assert zip(strings, integers) == {"a": 1, "b": 2, "c": 3}


def test_zip_empty_lists() -> None:
    """Tests the edge case where both lists are empty."""
    strings: list[str] = []
    integers: list[int] = []
    assert zip(strings, integers) == {}


if __name__ == "__main__":
    test_zip_mismatched_length_lists()
    test_zip_normal_case()
    test_zip_empty_lists()
