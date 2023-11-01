"""dictionary."""

__author__ = "730521715"

def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """invert the keys and values of a dictionary.

    args:
        input_dict: a dictionary to invert.

    returns:
        a dictionary with keys and values inverted.

    raises:
        keyerror: if a value is not unique, i.e., it appears more than once.
    """
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise keyerror(f"value {value} is not unique.")
        inverted_dict[value] = key
    return inverted_dict  # make sure to return the inverted dictionary


def favorite_color(names_to_colors: dict[str, str]) -> str:
    """Find the most frequent color in the dictionary.

    Args:
        names_to_colors: A dictionary mapping names to favorite colors.

    Returns:
        The color that appears most frequently in the dictionary.
    """
    # Initialize a dictionary to count color occurrences.
    color_counts = {}

    # Iterate over all colors and count them.
    for color in names_to_colors.values():
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    # Find the color that appears most frequently.
    # If there is a tie, it will return the first one that appears most frequently.
    most_common_color = max(color_counts, key=lambda k: (color_counts[k], -list(names_to_colors.values()).index(k)))
    
    return most_common_color


def count(values_list: list[str]) -> dict[str, int]:
    """count the occurrences of each string in a list.

    args:
        values_list: a list of strings to count occurrences in.

    returns:
        a dictionary with keys as the unique strings from the list and values as the counts.
    """
    count_dict = {}
    for item in values_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

def alphabetizer(words_list: list[str]) -> dict[str, list[str]]:
    """organize words by their first letter.

    args:
        words_list: a list of words to categorize.

    returns:
        a dictionary where each key is a lowercase letter and each value is a list
        of words that start with that letter, sorted in the order they appeared in the input list.
    """
    alphabetized_dict = {}
    for word in words_list:
        # convert the first letter of the word to lowercase
        first_letter = word[0].lower()
        # if the first letter is not already a key in the dictionary, create a new entry
        if first_letter not in alphabetized_dict:
            alphabetized_dict[first_letter] = []
        # append the current word to the list that corresponds to the first letter
        alphabetized_dict[first_letter].append(word)
    return alphabetized_dict

def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """
    update the attendance record for a given day with the student's name.

    args:
        attendance_dict: a dictionary with days as keys and lists of students as values.
        day: the day of the week to update attendance for.
        student: the name of the student to add to the attendance.

    returns:
        the updated dictionary with the student added to the attendance for the specified day.
    """
    # if the day is already in the dictionary, append the student to that day's list
    if day in attendance_dict:
        # ensuring no duplicates if the student is already in the list for that day
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        # if the day is not in the dictionary, create a new entry with the student in a new list
        attendance_dict[day] = [student]