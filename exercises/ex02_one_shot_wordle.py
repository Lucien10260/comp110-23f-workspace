"""EX01_one_shot_wordle."""
__author__ = "730521715"
secret_word = "python"

guess = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"

result_emoji = ""
index = 0
while index < len(secret_word):
    if guess[index] == secret_word[index]:
        result_emoji += GREEN_BOX
    else:
        result_emoji += WHITE_BOX
    index += 1
index = 0
while index < len(secret_word):
    if guess[index] != secret_word[index]:
        found = False
        alt_index = 0
        while not found and alt_index < len(secret_word):
            if guess[index] == secret_word[alt_index] and index != alt_index:
                found = True
                result_emoji = result_emoji[:index] + YELLOW_BOX + result_emoji[index + 1:]
            alt_index += 1
    index += 1

print(result_emoji)

if result_emoji == GREEN_BOX * len(secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")