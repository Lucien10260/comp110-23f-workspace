"""EX03 Wordle."""
__author__ = "730521715"
WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"
def contains_char(a: str, b: str) -> bool:
    """
    Check if a single character (b) exists in the provided string.
    Args:
    - a: The string we want to check for the presence of the b.
    - b: A single character string we want to check the presence of.
    Returns:
    - bool: True if the b is found in a, False otherwise.
    """
    assert len(b) == 1, "b must be a single character"
    for char in a:
        if char == b:
            return True
    return False

def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)

    result = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result.append(GREEN_BOX)
        elif contains_char(secret, guess[i]):
            result.append(YELLOW_BOX)
        else:
            result.append(WHITE_BOX)
    return ''.join(result)

def input_guess(expected_length: int) -> str:
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
    secret_word = "codes"
    max_turns = 6
    turns_taken = 0
    has_won = False

    while turns_taken < max_turns and not has_won:
        turns_taken += 1
        print(f"=== Turn {turns_taken}/{max_turns} ===")
        guess = input_guess(len(secret_word))
        emoji_result = emojified(guess, secret_word)
        print(emoji_result)

        if guess == secret_word:
            has_won = True

    if has_won:
        print(f"You won in {turns_taken}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()