def contains_char(guess: str, character: str) -> str:
    "Returns True if the character is in the word, False if it is not."
    assert len(character) == 1
    index = 0
    while index < len(guess):
        index = index + 1
        if character == guess[index]:
            return True
        if character != guess [index]:
            while index < len(guess):
                if character != guess[index]:
                    return False

def emojified(guess: str, secret: str) -> str:
    "Two characters of the same length."
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    emoji = ""
    while index < len(secret):
        if guess[index] == secret[index]:
            return GREEN_BOX
    #else:
        #if contains_char(guess) == True:
            #return YELLOW_BOX
        #else:
            #return WHITE_BOX
        #index = index + 1


def input_guess(length: int) -> int:
    print("Enter a _ character word")

while len(guess) < len(variable) or len(guess) > len(variable):
    guess: str = str(input("That was not 6 letters! Try again: "))
while len(guess) == len(variable):
    if guess == variable:
        print("Woo! You got it!")
        break
    else:
        print("Not quite. Play again soon!")
        break