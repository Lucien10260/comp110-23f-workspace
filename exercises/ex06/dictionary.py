"Dictionary exercise."

__author__ = "730521715"

def invert(input_dict):
    # Initialize an empty dictionary for the output
    output_dict = {}
    
    # Iterate over items in the input dictionary
    for key, value in input_dict.items():
        # Check if the value is already a key in the output dictionary (which means a duplicate)
        if value in output_dict:
            # Raise a KeyError since we cannot have duplicate keys
            raise KeyError(f"Duplicate key found: {value}")
        
        # Add the inverted key-value pair to the output dictionary
        output_dict[value] = key
    
    return output_dict

def favorite_color(colors_dict):
    # This dictionary will hold the count of each color
    color_count = {}

    # This will keep track of the order in which each color appears
    color_order = []

    # Iterate over each name and color in the input dictionary
    for name, color in colors_dict.items():
        # If the color is already in the count dictionary, increment its count
        if color in color_count:
            color_count[color] += 1
        else:
            # Otherwise, add the color to the count dictionary and set its count to 1
            color_count[color] = 1
            # Also, record the color's first appearance order
            color_order.append(color)

    # Find the maximum count of any color
    max_count = max(color_count.values())
    
    # Filter the colors that have the maximum count
    max_colors = [color for color, count in color_count.items() if count == max_count]

    # Iterate through the color order list and return the first color that has the maximum count
    for color in color_order:
        if color in max_colors:
            return color

    # If there are no colors, we can return a default value or raise an error
    raise ValueError("No colors provided")

def main():
    # Sample usage of the favorite_color function
    print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))

# This allows the module to be run directly from the command line
if __name__ == "__main__":
    main()

def count(values):
# Establish an empty dictionary to store the result
result = {}
    
# Loop through each item in the input list
for item in values:
    # Check to see if the item is already a key in the result dictionary
    if item in result:
        # Increase the count associated with that key by 1
        result[item] += 1
    else:
        # Assign an initial count of 1 to that key in the result dictionary
        result[item] = 1
            
    # Return the resulting dictionary
    return result

def alphabetizer(words):
    categorized_words = {}
    for word in words:
        # Convert the first letter of the word to lowercase
        first_letter = word[0].lower()
        # Append the word to the appropriate list, creating a new list if necessary
        if first_letter not in categorized_words:
            categorized_words[first_letter] = [word]
        else:
            categorized_words[first_letter].append(word)
    return categorized_words

def update_attendance(attendance, day, student):
    # If the day is not in the dictionary, add it with a new list containing the student
    if day not in attendance:
        attendance[day] = [student]
    else:
        # Add the student to the existing list for the day, if they're not already listed
        if student not in attendance[day]:
            attendance[day].append(student)
    return attendance