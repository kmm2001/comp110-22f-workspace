
if character_guess in word_guess:
    print(character_guess + " found at index " + str(word_guess.find(character_guess)))

if word_guess.index(character_guess) != -1:
    print(character_guess + " found at index " + str(word_guess.find(character_guess)))
else:
    print("game over")

python -m exercises.ex01_chardle

if character_guess in word_guess:
    print(character_guess + " found at index " + str(word_guess.find(character_guess)))

if character_guess in word_guess:
    print(character_guess + " found at index " + str(word_guess.index(character_guess)))

if character_guess in word_guess:
    print(character_guess + " found at index " + str(word_guess.find(character_guess)))
    print(character_guess + " found at index " + str(word_guess.count(character_guess)))

match: str = str(word_guess.count(character_guess))

if word_guess[0] or word_guess[1] or word_guess[2] or word_guess[3] or word_guess[4] == character_guess:
    print(character_guess + " found at index " + str(word_guess.find(character_guess)))
    #print(character_guess + " found at index " + match)


#if word_guess[0] and word_guess[1] and word_guess[2] and word_guess[3] and word_guess[4] != character_guess:
    #print("Character not found in word.")

match = str(word_guess[0] or word_guess[1] or word_guess[2] or word_guess[3] or word_guess[4] == character_guess)
#print(match)
if character_guess in word_guess[0]:
    match = match + 1
if character_guess in word_guess[1]:
    match = match + 1
if character_guess in word_guess[2]:
    match = match = 1
if character_guess in word_guess[3]:
    match = match + 1
if character_guess in word_guess[4]:
    match = match + 1
print(str(match))




match = word_guess[0].count(character_guess)

if character_guess == word_guess[1]:
   match = match + 1

if character_guess == word_guess[2]:
   match = match + 1

if character_guess in word_guess[3]:
   match = match + 1

if character_guess in word_guess[4]:
    match = match + 1

print(match)

match = str(word_guess.find(character_guess))
print(match)
#if match > 1:
    #match = match + 1