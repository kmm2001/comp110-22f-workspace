"""EX04 - `list` Utility Functions."""

__author__ = "730314205"


def all(lists: list[int], character: int) -> bool:
    """Return a bool indicating whether or not all the ints in the list are the same as the given int."""
    index = 0
    value = True
    while index < len(lists):
        if character == lists[index]:
            value = True
        else:
            return False
        index = index + 1
    if len(lists) == 0:
        return False
    return value


def max(input: list[int]) -> int:
    """Given a list of ints, max should return the largest in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index1 = 0
    largest_number = input[0]
    while index1 < len(input):
        if input[index1] > largest_number:
            largest_number = input[index1]
        else:
            largest_number = largest_number
        index1 = index1 + 1
    return largest_number


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    index = 0
    value = True
    while index < len(list1) and index < len(list2):
        if list1[index] == list2[index]:
            value = True
        else:
            value = False
        index = index + 1
        if len(list1) is not len(list2):
            value = False
    if len(list1) == 0 and len(list2) != 0:
        value = False
    if len(list2) == 0 and len(list1) != 0:
        value = False
    return value