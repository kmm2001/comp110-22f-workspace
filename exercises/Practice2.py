while len(guess) < len(variable) or len(guess) > len(variable):
    guess: str = str(input("That was not 6 letters! Try again: "))
while len(guess) == len(variable):
    if guess == variable:
        print("Woo! You got it!")
        break
    else:
        print("Not quite. Play again soon!")
        break

if len(guess[index]) == number_of_letters:
    break

while len(str(index)) < len(variable):
    if guess[index] == variable[index]:
        emoji: print(f"{GREEN_BOX}")
        index = index + 1
    else:
        emoji: print(f"{WHITE_BOX}")
        index = index + 1
print(clear)

    if index <= (number_of_letters - 1):


while index < len(variable):
    if guess[index] == variable[index]:
        emoji = emoji + GREEN_BOX
        print(str(emoji))
    else:
        emoji = emoji + WHITE_BOX
        print(str(emoji))
    index = index + 1
print(emoji)


index = 0
emoji = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while index < len(variable):
    if guess[index] == variable[index]:
        emoji = emoji + GREEN_BOX
    else:
        emoji = emoji + WHITE_BOX
    index = index + 1
print(emoji)


boolean: guess.chr(index) in variable
alternate_indices = 0






"""EX02 - One-Shot Wordle."""

__author__ = "730314205"

variable: str = str("python")
number_of_letters: str = len(variable)
guess: str = str(input(f"What is your {number_of_letters}-letter guess? "))

index = 0
emoji = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) < len(variable) or len(guess) > len(variable):
    guess: str = str(input(f"That was not {number_of_letters} letters! Try again: "))

while index < len(variable):
    if guess[index] == variable[index]:
        emoji = emoji + GREEN_BOX
    else:
        emoji = emoji + WHITE_BOX
    index = index + 1
print(emoji)

if guess == variable:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")


while index < len(variable):
    if guess[index] == variable[index]:
        emoji = emoji + GREEN_BOX
    else:
        while boolean == False and index < len(variable):
            if variable[alternate_indices] == guess[index]:
                boolean = True
            else:
                alternate_indices = alternate_indices + 1
        if boolean == True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    index = index + 1
print(emoji)

if guess == variable:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")





boolean = False
alternate_indices = 0

while boolean == False and index < len(variable):
    if variable[alternate_indices] == guess[index]:
        boolean = True
    else:
        alternate_indices = alternate_indices + 1
if boolean == True:
    emoji.append(YELLOW_BOX)