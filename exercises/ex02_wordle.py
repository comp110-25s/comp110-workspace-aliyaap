"""Let's play Wordle!"""

__author__: str = "730466316"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    current_turn: int = 1  # Keeps track of what turn the player is on

    # Loops through 6 turns of the game
    while current_turn <= 6:
        print(f"=== Turn {current_turn}/6 ===")
        guess: str = input_guess(expected_length=len(secret))

        print(emojified(guess_word=guess, secret=secret))
        if guess == secret:  # Player wins if their guess matches the secret word
            print(f"You won in {current_turn}/6 turns!")
            return  # Exits the function to end the game
        current_turn = current_turn + 1  # Updates turn number
    print(f"X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, letter: str) -> bool:
    """Check if the word contains the given letter."""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    idx: int = 0  # Keeps track of each letter's position in the word
    while idx < len(word):  # Checks the entire word for the given letter
        if word[idx] == letter:
            return True
        idx = idx + 1  # Updates index
    return False


def emojified(guess_word: str, secret: str) -> str:
    """Use emojis to indicate to player if their guess matches the secret word."""
    assert len(guess_word) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"  # Incorrect letter
    GREEN_BOX: str = "\U0001F7E9"  # Correct letter in the correct place
    YELLOW_BOX: str = "\U0001F7E8"  # Correct letter in the incorrect place

    result: str = ""  # Stores the result of each letter of the guess word
    idx: int = 0  # Keeps track of the position of letters in guess and secret
    # Loops through each letter in the guess word
    while idx < len(guess_word):
        if (
            guess_word[idx] == secret[idx]
        ):  # Checks if corresponding positions in guess and secret contain same letter
            result = result + GREEN_BOX
        else:
            if (
                contains_char(word=secret, letter=guess_word[idx]) is True
            ):  # Checks if letter is anywhere in the secret word
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX
        idx = idx + 1  # Updates index
    return result  # Returns the full string of results


def input_guess(expected_length: int) -> str:
    """Prompt player to input word of correct length."""
    guess: str = input(f"Enter a {expected_length} character word:")
    # Prompts player to try again when their guess is not the correct number of letters
    while len(guess) != expected_length:
        print(f"That wasn't {expected_length} chars! Try again:")
        guess = input()
    return guess  # If length of guess matches secret word, guess returns


if __name__ == "__main__":
    main(secret="codes")
