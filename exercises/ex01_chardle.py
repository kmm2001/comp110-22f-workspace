"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730314205"

word_guess: str = str(input("Enter a 5-character word: "))
if len(word_guess) < 5 or len(word_guess) > 5:
    print("Error: Word must contain 5 characters")
    exit()
character_guess: str = str(input("Enter a single character: "))
if len(character_guess) < 1 or len(character_guess) > 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character_guess + " in " + word_guess)

if word_guess[0] == character_guess:
    print(character_guess + " found at index " + str(word_guess.index(character_guess, 0)))
if word_guess[1] == character_guess:
    print(character_guess + " found at index " + str(word_guess.index(character_guess, 1)))
if word_guess[2] == character_guess:
    print(character_guess + " found at index " + str(word_guess.index(character_guess, 2)))
if word_guess[3] == character_guess:
    print(character_guess + " found at index " + str(word_guess.index(character_guess, 3)))
if word_guess[4] == character_guess:
    print(character_guess + " found at index " + str(word_guess.index(character_guess, 4)))

match_instances = 0

if character_guess == word_guess[0]:
    match_instances = match_instances + 1

if character_guess == word_guess[1]:
    match_instances = match_instances + 1

if character_guess == word_guess[2]:
    match_instances = match_instances + 1

if character_guess == word_guess[3]:
    match_instances = match_instances + 1

if character_guess == word_guess[4]:
    match_instances = match_instances + 1

if match_instances == 1:
    print(str(match_instances) + " instance of " + character_guess + " found in " + word_guess)
if match_instances > 1:
    print(str(match_instances) + " instances of " + character_guess + " found in " + word_guess)
if match_instances < 1:
    print("No instances of " + character_guess + " found in " + word_guess)