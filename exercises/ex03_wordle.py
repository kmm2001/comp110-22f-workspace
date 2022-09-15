"""EX03 - Structured Wordle."""

__author__ = "730314205"


def contains_char(guess: str, character: str) -> bool:
    """Returns True if the character is in the word, False if it is not."""
    # declare a function with parameters of two strings, the first of any length, the second a single character, give a description
    assert len(character) == 1
    # make sure the character's length is one
    index = 0
    # establish index variable
    while index < len(guess):
        # run the loop while the index is lower than the guess' character count
        if character == guess[index]:
            return True
        else:
            index = index + 1
            # return True if the character is found at any index of the guess
    return False
    # return False if the character is not found at any index of the guess


def emojified(guess: str, secret: str) -> str:
    """Prints the emoji boxes that correspond with the character postion in the word."""
    # declare a function with parameters of two strings, the first a guess and the second a secret, give a description
    assert len(guess) == len(secret)
    # make sure the guess and secret are the same length
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    emoji = ""
    # establish variables and and include the named constants
    while index < len(secret):
        # run the loop while the index is lower than the secret's length
        if guess[index] == secret[index]:
            emoji = emoji + GREEN_BOX
            # use the green box emoji if the character placement for the guess and secret are equal (increment)
        else:
            if contains_char(secret, guess[index]) is True:
                emoji = emoji + YELLOW_BOX
                # otherwise use the contain_char function to use the yellow emoji if the character exists in the secret but the guess and secret character placement isn't equal (increment)
            else:
                emoji = emoji + WHITE_BOX
                # otherwise use the white box emoji if the character doesn't exist in the secret (increment)
        index = index + 1
        # assign a new value to the "index" variable (by incrementing), increasing the value by one so we don't have an infinite loop and the loop works as intended
    return emoji
    # return the resulting emojis


def input_guess(length: int) -> str:
    """Prompts the user for a guess of a certain length until a guess of that length is given."""
    # declare a function with an integer representing expected length of a guess as a parameter, give a description
    guess = input(f"Enter a {length} character word: ")
    # prompt for a guess that has a number of characters of an expected length
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
        # while the length of the guess does not match the expected length, keep prompting for a new guess
    return guess
    # return the guess once a guess of expected length is given


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # define the main function and give a description
    secret: str = str("codes")
    turn = 1
    won = False
    # establish new variables that we need to keep track of in order to run the game
    while turn <= 6 and won is False:
        print(f"=== Turn {turn}/6 ===")
        guess = str(input_guess(len(secret)))
        print(emojified(guess, secret))
        # print the number of turns, use input_guess to prompt for a guess, and use emojified to print the related emojis while the user has turns left and hasn't won
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            won = True
            # if the guess is equal to the secret, print a statement explaining the user won in a certain number of turns and reassign the variable won to be True
        if turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
            # if the user runs out of turns and hasn't won, print a statement letting them know the game is over
        turn = turn + 1
        # assign a new value to the "turn" variable (by incrementing), increasing the value by one so we don't have an infinite loop and the loop works as intended


if __name__ == "__main__":
    main()
    # include code so that we can run the game as a module