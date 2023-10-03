"""EX03 Wordle."""
__author__ = "730521715"
WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"
def contains_char(word: str, char_to_check: str) -> bool:
    """
    Check if a single character (char_to_check) exists in the provided string.
    Args:
    - word: The string we want to check for the presence of the char_to_check.
    - char_to_check: A single character string we want to check the presence of.
    Returns:
    - bool: True if the char_to_check is found in word, False otherwise.
    """
    assert len(char_to_check) == 1, "char_to_check must be a single character"
    
    for char in word:
        if char == char_to_check:
            return True
    return False

def emojified(guess: str, secret: str) -> str:
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
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
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
