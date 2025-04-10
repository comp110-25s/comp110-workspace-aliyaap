"""Testing Dictionary Functions"""

__author__: str = "730466316"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest


# Unit tests for invert function
def test_invert_general_use() -> None:
    """Tests if function returns inverted dictionary."""
    awards: dict[str, str] = {"first": "gold", "second": "silver", "third": "bronze"}
    awards_inverted: dict[str, str] = {
        "gold": "first",
        "silver": "second",
        "bronze": "third",
    }
    assert invert(dictionary=awards) == awards_inverted


def test_invert_empty() -> None:
    """Tests function when an empty dictionary is given."""
    assert invert(dictionary={}) == {}


def test_invert_key_error() -> None:
    with pytest.raises(KeyError):
        invert(dictionary={"first": "gold", "second": "gold", "third": "bronze"})


# Unit tests for count function
def test_count_repeat() -> None:
    """Test counting for single item repeated in a list."""
    fruits: list[str] = [
        "apple",
        "apple",
    ]
    fruit_count: dict[str, int] = {"apple": 2}
    assert count(things=fruits) == fruit_count


def test_count_general_use() -> None:
    """Test if function adds new items to dictionary and updates their counts."""
    fruits: list[str] = ["apple", "apple", "banana", "kiwi", "grapes", "banana"]
    fruit_count: dict[str, int] = {"apple": 2, "banana": 2, "kiwi": 1, "grapes": 1}
    assert count(things=fruits) == fruit_count


def test_count_empty() -> None:
    """Tests function when an empty list is given."""
    fruits: list[str] = []
    fruit_count: dict[str, int] = {}
    assert count(things=fruits) == fruit_count


# Unit tests for favorite_color
def test_favorite_color_general() -> None:
    """Tests general use of function."""
    our_colors: dict[str, str] = {
        "Ann": "blue",
        "Emily": "green",
        "Aliyaa": "green",
        "Heeba": "pink",
    }
    assert favorite_color(names_colors=our_colors) == "green"


def test_favorite_color_tie(names_colors) -> None:
    """Tests function's use when there is a tie."""
    our_colors: dict[str, str] = {
        "Ann": "blue",
        "Emily": "green",
        "Aliyaa": "green",
        "Heeba": "blue",
    }
    assert favorite_color(names_colors=our_colors) == "blue"


def test_favorite_color_single_color() -> None:
    """Tests function's use when there is one color."""
    our_colors: dict[str, str] = {"Ann": "blue"}
    assert favorite_color(names_colors=our_colors) == "blue"


# Unit tests for bin_len function
def test_bin_len_general_use() -> None:
    """Tests function's general ability to bin lengths."""
    assert bin_len(["dog", "cat", "sparrow"]) == {3: {"dog", "cat"}, 7: {"sparrow"}}


def test_bin_len_duplicates() -> None:
    """Tests function's ability to bin lengths when there are duplicate words."""
    assert bin_len(["dog", "dog", "sparrow"]) == {3: {"dog"}, 7: {"sparrow"}}


def test_bin_len_empty() -> None:
    """Tests function's ability to bin lengths when an empty list is given."""
    assert bin_len([]) == {}
