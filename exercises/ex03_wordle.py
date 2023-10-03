"""EX03 Wordle."""

__author__ = "730521715"

WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"


def contains_char(word: str, char_to_check: str) -> bool:
    """Check if a character exists in a string.

    Args:
        word (str): String to check for the presence of char_to_check.
        char_to_check (str): Character to check for in the word.

    Returns:
        bool: True if char_to_check is in word, False otherwise.
    """
    assert len(char_to_check) == 1, "char_to_check must be a single character"

    for char in word:
        if char == char_to_check:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """Convert the guess to emoji representation based on its match with the secret."""
    assert len(guess) == len(secret)
    result = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    return result


def input_guess(expected_length: int) -> str:
    """Prompt user for a guess and ensure it matches the expected length."""
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """Main function to execute the Wordle game."""
    secret_word = "codes"
    max_turns = len(secret_word) + 1
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