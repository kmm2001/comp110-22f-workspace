"""EX05 - `list` Utility Functions."""

__author__ = "730314205"


from dictionary import invert, favorite_color, count
import pytest


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_invert_multiple_key_and_letter_words() -> None:
    """Test when there are multiple keys and values that are full words."""
    dict1: dict[str, str] = {'kris': 'jordan', 'michael': 'smith', 'john': 'greene'}
    assert invert(dict1) == {'jordan': 'kris', 'smith': 'michael', 'greene': 'john'}


def test_invert_multiple_keys_and_values_letters() -> None:
    """Test when there are multiple keys and values that are letters."""
    dict1: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(dict1) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_one_key_value_pair() -> None:
    """Test when there is only one key value pair."""
    dict1: dict[str, str] = {'apple': 'cat'}
    assert invert(dict1) == {'cat': 'apple'}


def test_favorite_colors_mutiple_same_color() -> None:
    """Test when people have shared favorite colors."""
    dict1: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(dict1) == "blue"


def test_favorite_colors_different_colors() -> None:
    """Test when no two people have the same favorite colors (there is a tie)."""
    dict1: dict[str, str] = {"Marc": "yellow", "Ezri": "green", "Kris": "blue"}
    assert favorite_color(dict1) == "yellow"


def test_favorite_colors_all_same() -> None:
    """Test when everyone has the same favorite colors."""
    dict1: dict[str, str] = {"Marc": "yellow", "Ezri": "yellow", "Kris": "yellow"}
    assert favorite_color(dict1) == "yellow"


def count_once() -> None:
    """Test when each value appears in the input list once."""
    list1: list[str] = ["10", "20", "30", "40"]
    assert count(list1) == {"10": 1, "20": 1, "30": 1, "40": 1}


def count_mix() -> None:
    """Test when there are a mix of values that appear one and more times."""
    list1: list[str] = ["10", "20", "20", "40"]
    assert count(list1) == {"10": 1, "20": 2, "40": 1}


def count_all_same() -> None:
    """Test when the list is comprised entirely of the same value."""
    list1: list[str] = ["40", "40", "40", "40"]
    assert count(list1) == {"40": 4}