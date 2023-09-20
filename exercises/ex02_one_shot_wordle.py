"""EX01_one_shot_wordle."""
__author__ = "730521715"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret = "bullet"
guess = input(f"What is your {len(secret)}-letter guess? ")
while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")
result_string = ""
idx = 0
while idx < len(secret):
    if guess[idx] == secret[idx]:
        result_string += GREEN_BOX
    else:
        # Check if letter exists in other positions
        found = False
        alt_idx = 0
        while not found and alt_idx < len(secret):
            if guess[idx] == secret[alt_idx] and idx != alt_idx:
                found = True
            alt_idx += 1
        if found:
            result_string += YELLOW_BOX
        else:
            result_string += WHITE_BOX
    idx += 1
print(result_string)
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")