"""Dictionary."""

__author__ = "730521715"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary.

    Args:
        input_dict: A dictionary to invert.

    Returns:
        A dictionary with keys and values inverted.

    Raises:
        KeyError: If a value is not unique, i.e., it appears more than once.
    """
    inverted_dict: dict[str, str] = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError(f"Value {value} is not unique.")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(names_to_colors: dict[str, str]) -> str:
    """Find the most frequent color in the dictionary.

    Args:
        names_to_colors: A dictionary mapping names to favorite colors.

    Returns:
        The color that appears most frequently in the dictionary.
    """
    color_counts: dict[str, int] = {}
    for color in names_to_colors.values():
        color_counts[color] = color_counts.get(color, 0) + 1
    most_common_color = max(color_counts, key=lambda k: (color_counts[k], -list(names_to_colors.values()).index(k)))
    return most_common_color


def count(values_list: list[str]) -> dict[str, int]:
    """Count the occurrences of each string in a list.

    Args:
        values_list: A list of strings to count occurrences in.

    Returns:
        A dictionary with keys as the unique strings from the list and values as the counts.
    """
    count_dict: dict[str, int] = {}
    for item in values_list:
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict


def alphabetizer(words_list: list[str]) -> dict[str, list[str]]:
    """Organize words by their first letter.

    Args:
        words_list: A list of words to categorize.

    Returns:
        A dictionary where each key is a lowercase letter and each value is a list
        of words that start with that letter, sorted in the order they appeared in the input list.
    """
    alphabetized_dict: dict[str, list[str]] = {}
    for word in words_list:
        first_letter = word[0].lower()
        if first_letter not in alphabetized_dict:
            alphabetized_dict[first_letter] = []
        alphabetized_dict[first_letter].append(word)
    return alphabetized_dict


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Update the attendance record for a given day with the student's name.

    Args:
        attendance_dict: A dictionary with days as keys and lists of students as values.
        day: The day of the week to update attendance for.
        student: The name of the student to add to the attendance.

    Returns:
        The updated dictionary with the student added to the attendance for the specified day.
    """
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return attendance_dict
