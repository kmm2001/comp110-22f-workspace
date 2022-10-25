"""EX05 - `list` Utility Functions."""

__author__ = "730314205"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Test when list1 is empty."""
    list1: list[int] = []
    assert only_evens(list1) == []


def test_only_evens_all_evens() -> None:
    """Test when list1 has only even numbers."""
    list1: list[int] = [4, 4, 4]
    assert only_evens(list1) == [4, 4, 4]


def test_only_evens_all_odds() -> None:
    """Test when list1 has only odd numbers."""
    list1: list[int] = [1, 5, 3]
    assert only_evens(list1) == []


def test_only_evens_mix() -> None:
    """Test when list1 is a mix of odd and even numbers."""
    list1: list[int] = [1, 2, 3]
    assert only_evens(list1) == [2]


def concat_empty() -> None:
    """Test when list1 and list2 are empty."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def concat_different() -> None:
    """Test when list1 and list2 contain all different numbers."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]


def concat_some_same() -> None:
    """Test when list1 and list2 contain some same numbers."""
    list1: list[int] = [1, 4, 3]
    list2: list[int] = [4, 4, 4]
    assert concat(list1, list2) == [1, 4, 3, 4, 4, 4]


def sub_empty() -> None:
    """Test when a_list is empty."""
    a_list: list[int] = []
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == []


def sub_end_0() -> None:
    """Test when end is 0."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 0
    assert sub(a_list, start, end) == []


def sub_start_special_end_special() -> None:
    """Test when start is under the length of the list and end is over the length of the list."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = -5
    end: int = 5
    assert sub(a_list, start, end) == [10, 40]


def sub_start_greater_than_list_length() -> None:
    """Test when start is greater than the length of the list."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 5
    end: int = 3
    assert sub(a_list, start, end) == []


def sub_regular() -> None:
    """Test when there are not special cases."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == [20, 30]