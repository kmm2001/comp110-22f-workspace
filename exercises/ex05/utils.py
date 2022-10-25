"""EX05 - `list` Utility Functions."""

__author__ = "730314205"


def only_evens(list1: list[int]) -> list:
    """Given a list, return a list containing only the even values from the original list."""
    even_list: list[int] = []
    number: int
    for number in list1:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def concat(list1: list[int], list2: list[int]) -> list:
    """Given two lists, generate a list with all of the elements of the first list followed by all the elements of the second list."""
    final_list: list[int] = []
    element: int
    for element in list1:
        final_list.append(element)
    for element in list2:
        final_list.append(element)
    return final_list


def sub(a_list: list[int], start: int, end: int) -> list:
    """Generate a List which is a subset of the given list, between the specified start index and the end index - 1."""
    final_list: list[int] = []
    if len(a_list) == 0 or len(a_list) <= start or end <= 0:
        final_list = []
    elif start < 0:
        final_list.append((a_list[0]))
        if len(a_list) > end:
            final_list.append((a_list[end - 1]))
        elif len(a_list) < end:
            final_list.append((a_list[len(a_list) - 1]))
    elif len(a_list) < end:
        final_list.append((a_list[start]))
        final_list.append((a_list[len(a_list) - 1]))
    else:
        final_list.append((a_list[start]))
        final_list.append((a_list[end - 1]))
    return final_list