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
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError(f"Value {value} is not unique.")
        inverted_dict[value] = key


def favorite_colors(names_to_colors: dict[str, str]) -> str:
    color_counts = {}
    for name, color in names_to_colors.items():
        if color not in color_counts:
            color_counts[color] = {'count': 0, 'first_index': len(color_counts)}
        color_counts[color]['count'] += 1

    # Sort colors by the highest count and then by the earliest appearance.
    sorted_colors = sorted(color_counts.items(), 
                           key=lambda item: (-item[1]['count'], item[1]['first_index']))


def count(values_list: list[str]) -> dict[str, int]:
    """Count the occurrences of each string in a list.

    Args:
        values_list: A list of strings to count occurrences in.

    Returns:
        A dictionary with keys as the unique strings from the list and values as the counts.
    """
    count_dict = {}
    for item in values_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1


def alphabetizer(words_list: list[str]) -> dict[str, list[str]]:
    """Organize words by their first letter.

    Args:
        words_list: A list of words to categorize.

    Returns:
        A dictionary where each key is a lowercase letter and each value is a list
        of words that start with that letter, sorted in the order they appeared in the input list.
    """
    alphabetized_dict = {}
    for word in words_list:
        # Convert the first letter of the word to lowercase
        first_letter = word[0].lower()
        # If the first letter is not already a key in the dictionary, create a new entry
        if first_letter not in alphabetized_dict:
            alphabetized_dict[first_letter] = []
        # Append the current word to the list that corresponds to the first letter
        alphabetized_dict[first_letter].append(word)

def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """
    Update the attendance record for a given day with the student's name.

    Args:
        attendance_dict: A dictionary with days as keys and lists of students as values.
        day: The day of the week to update attendance for.
        student: The name of the student to add to the attendance.

    Returns:
        The updated dictionary with the student added to the attendance for the specified day.
    """
    # If the day is already in the dictionary, append the student to that day's list
    if day in attendance_dict:
        # Ensuring no duplicates if the student is already in the list for that day
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        # If the day is not in the dictionary, create a new entry with the student in a new list
        attendance_dict[day] = [student]