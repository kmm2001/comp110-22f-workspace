

from utils import concat


def concat_empty() -> None:
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def concat_different() -> None:
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]


def concat_some_same() -> None:
    list1: list[int] = [1, 4, 3]
    list2: list[int] = [4, 4, 4]
    assert concat(list1, list2) == [1, 4, 3, 4, 4, 4]