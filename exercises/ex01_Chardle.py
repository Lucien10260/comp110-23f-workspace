"""EX01 - Chardle."""
__author__ = "730521715"
word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + word)
count = 0
if word[0] == character:
    print(character + " found at index 0")
    count += 1
if word[1] == character:
    print(character + " found at index 1")
    count += 1
if word[2] == character:
    print(character + " found at index 2")
    count += 1
if word[3] == character:
    print(character + " found at index 3")
    count += 1
if word[4] == character:
    print(character + " found at index 4")
    count += 1
if count == 0:
    print("No instances of " + character + " found in " + word)
elif count == 1:
    print("1 instance of " + character + " found in " + word)
else:
    print(str(count) + " instances of " + character + " found in " + word)