
user_string: str = input("Give me a string! ")

#the varibale i is a common counter variable name
i: int = 0


while i < len(user_string):
    print(user_string[i])
    i = i + 1

print("Done!")