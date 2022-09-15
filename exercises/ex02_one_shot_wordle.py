"""EX02 - One-Shot Wordle."""

__author__ = "730314205"

variable: str = str("python")
# establish a secret
number_of_letters: str = str(len(variable))
# count the number of letters in the secret
guess = str(input(f"What is your {number_of_letters}-letter guess? "))
# prompt for a guess

while len(guess) < len(variable) or len(guess) > len(variable):
    guess = str(input(f"That was not {number_of_letters} letters! Try again: "))
# print a result prompting for a new guess if the number of characters in the guess is not equal to those in the secret
# keep printing until a guess with the correct number of characters is made

index = 0
emoji = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# establish variables and include the named constants

while index < len(variable):
    # run the loop while the index is lower than the secret's character count
    if guess[index] == variable[index]:
        emoji = emoji + GREEN_BOX
    # use the green box emoji if the character placement for the guess and secret are equal (increment)
    else:
        character_exists = False
        alternate_index = 0
        # establish new variables
        while character_exists is False and alternate_index < len(variable):
            # run the loop while the "character exists" variable is False and the alternate index is lower than the secret's character count
            if variable[alternate_index] == guess[index]:
                character_exists = True
            # assign a new value to the "character exists" variable if the alternate index for the secret and index for the guess are equal
            else:
                alternate_index = alternate_index + 1
            # if the alternate index for the secret and index for the guess aren't equal, increment the alternate index variable
        if character_exists is True:
            emoji = emoji + YELLOW_BOX
        # use the yellow box emoji if the character exists in the secret (but the character placement for the guess and secret aren't equal) (increment)
        else:
            emoji = emoji + WHITE_BOX
        # use the white box emoji if the character doesn't exist in the secret (increment)
    index = index + 1
    # assign a new value to the "index" variable (by incrementing), increasing the value by one so we don't have an infinite loop
print(emoji)
# print the resulting emojis

if guess == variable:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
# print a particular result for the guess depending on if the guess is equal to the variable