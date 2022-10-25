"""EX07 - Dictionary Functions."""

__author__ = "730314205"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], return a dict[str, str] that inverts the keys and the values."""
    dict2: dict[str, str] = {}
    for key in dict1:
        if dict1[key] in dict2:
            raise KeyError("Cannot have duplicate key values")
        dict2[dict1[key]] = key
    return dict2


def count(list1: list[str]) -> dict[str, int]:
    """Given a list[str], produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    dict2: dict[str, int] = {}
    for i in list1:
        if i in dict2:
            dict2[i] += 1
        else:
            dict2[i] = 1
    return dict2


def favorite_color(dict1: dict[str, str]) -> str:
    """Return a str which is the color that appears most frequently."""  
    list1: list[str] = []
    favorite1: dict[str, int]
    for key in dict1:
        list1.append(dict1[key])
    favorite1 = count(list1)
    largest_number = 0
    final: str
    for key in favorite1:
        if favorite1[key] > largest_number:
            largest_number = favorite1[key]
            final = key
    return final