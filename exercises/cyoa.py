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
    stop = False
    if points == 0:
        print("You have regenerated.")
        points = 100
    while points > 0 and not stop:
        print(f"You have {points} energy points.")
        go_to: str = str(input("Do you want to go to the forest, cave, or quit? "))
        if go_to == "forest":
            print(f"{player}, you've encountered a bear with an unknown amount of hitpoints!")
            points = forest_function(points)
        elif go_to == "cave":
            print("You enter a large, dark cave. You see a tunnel.")
            cave_procedure()
        elif go_to == "quit":
            stop = True
            print("You have exited the game. Goodbye.")
            print(f"You had {points} energy points.")
        else:
            print("You must enter forest, cave, or quit")


def forest_function(value: int) -> int:
    """The forest path function."""
    global player
    bear_hitpoints: int = random.randint(1, 150)
    print(f"{player}, you must decide, fight or flight! If you decide to fight, your energy will take a hit by the amount of the bear's hitpoints. If you choose flight, who knows what will happen.")
    decision: str = str(input("Do you want to choose fight or flight? "))
    if decision == "fight":
        if value <= bear_hitpoints:
            print(f"Bear hitpoints: {bear_hitpoints}")
            print("Your attack wasn't strong enough! The bear won. Play again.")
            value = 0
            return value
        else: 
            print(f"Bear hitpoints: {bear_hitpoints}")
            print("You won against the bear!")
            value = value - bear_hitpoints
            return value
    elif decision == "flight":
        print("The bear caught up to you and attacked! Play again.")
        value = 0
        return value
    else:
        print("You must enter fight or flight")
        return value


def cave_procedure() -> None:
    """The cave path function."""
    global points
    print(f"{player}, you've encountered a tunnel! You must decide what to do next: enter or leave. Since you've been standing around trying to decide, you've gained additional energy points! However, it takes more energy to leave, so you will gain less energy overall if you leave.")
    next: str = str(input("What will you choose, enter or leave? "))
    if next == "enter":
        points = points + 20
        enter()
    elif next == "leave":
        points = points + 10
        leave()
    else:
        print("You must enter enter or leave")


def enter() -> None:
    """You choose to enter."""
    TREASURE: str = "\U0001F48E"
    SMILEY_FACE: str = "\U0001F600"
    print(f"You found treasure! {TREASURE} {SMILEY_FACE}")


def leave() -> None:
    """You choose to leave."""
    print("You left the cave.")


if __name__ == "__main__":
    main()