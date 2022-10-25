"""EX06 - Choose your own adventure."""

__author__ = "730314205"


import random
player: str = ""
points: int = 100


def greet() -> None:
    """Greet the player."""
    global player
    player = input("What is your name? ")
    print(f"Hello, welcome to the game {player}!")


def main() -> None:
    """Establish main function and points variable."""
    global points
    greet()
    print(f"You have {points} hitpoints.")
    if points == 0:
        print("Reload the game on the terminal to play the game again.")
    while points > 0:
        go_to: str = str(input("Do you want to go to the forest, cave, or quit? "))
        if go_to == "forest":
            print(f"{player}, you've encountered a bear with an unknown amount of hitpoints!")
            next: int = int(input("You must attack! You must use some of your hitpoints as energy for your attack! How many points will you use? "))
            forest_function(next)
        elif go_to == "cave":
            print("You enter a large, dark cave. You see a tunnel.")
            cave_procedure()
        elif go_to == "quit":
            print("You have exited the game. Goodbye.")
            print(f"You had {points} points.")
            points = 0


def forest_function(next: int) -> int:
    """The forest path function."""
    global points
    global player
    bear_hitpoints: int = random.randint(1, 100)
    if next < bear_hitpoints:
        print(f"Bear hitpoints: {bear_hitpoints}")
        print("Your attack wasn't strong enough! The bear won. Play again later.")
        points = 0
    elif next > bear_hitpoints: 
        print(f"Bear hitpoints: {bear_hitpoints}")
        print("You won against the bear!")
        points = points - next
    return points


def cave_procedure() -> None:
    """The cave path function."""
    print(f"{player}, you've encountered a tunnel!")
    next: str = str(input("What will you choose, enter or leave? "))
    if next == "enter":
        enter()
    elif next == "leave":
        leave()


def enter() -> None:
    """You choose to enter."""
    outcome1 = str("You found treasure!")
    TREASURE: str = "\U0001F48E"
    SMILEY_FACE: str = "\U0001F600"
    print(outcome1)
    print(TREASURE)
    print(SMILEY_FACE)


def leave() -> None:
    """You choose to leave."""
    outcome2 = str("You left the cave.")
    print(outcome2)


if __name__ == "__main__":
    main()