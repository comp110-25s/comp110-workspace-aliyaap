"""Playing with Dictionaries"""

__author__: str = "730466316"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    inverted_dict: dict[str, str] = {}  # Create an empty dictionary for inversion

    for key in dictionary:  # Loop through each key in the original dictionary
        value = dictionary[key]  # Get the corresponding value

        if (
            value in inverted_dict
        ):  # If the value already exists in inverted_dict, raise KeyError
            raise KeyError(
                f"Duplicate value found: '{value}' is assigned to multiple keys."
            )

        inverted_dict[value] = key  # Swap key and value

    return inverted_dict


def count(things: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}  # Empty dictionary to store item counts
    idx: int = 0
    while idx <= (len(things) - 1):  # Loops through items in the list
        if things[idx] in result:
            result[things[idx]] += 1  # Updates count for items in the dictionary
        else:
            result[things[idx]] = 1  # Adds item to dictionary if not already there
        idx += 1
    return result


def favorite_color(names_colors: dict[str, str]) -> str:
    colors: list[str] = []  # Creates empty list to store colors

    idx = 0  # Index to keep track of names on list
    keys = list(names_colors)  # Creates list from dictionary keys
    while idx < len(keys):
        colors.append(names_colors[keys[idx]])  # Adds colors to a list of colors
        idx += 1  # Updates index
    color_counts = count(colors)  # Creates a dictionary of color frequencies
    most_common_color = ""
    highest_count = 0

    idx = 0
    color_keys = list(
        color_counts
    )  # Creates a list from dictionary returned by count fxn
    while idx < len(color_keys):  # Checks every color in the dictionary
        color = color_keys[idx]  # Retrieves color at current index of color list
        if (
            color_counts[color] > highest_count
        ):  # Checks if the current color appears more than current more frequent color
            highest_count = color_counts[color]  # Updates highest count
            most_common_color = (
                color  # Updates the most common color to the current color
            )
        idx += 1  # Updates index
    return most_common_color


def bin_len(word_list: list[str]) -> dict[int, set[str]]:
    """Bins strings by their lengths."""
    length_dict: dict[int, set[str]] = {}
    idx = 0
    while idx < len(word_list):
        item = word_list[idx]
        length = 0
        j = 0
        while j < len(item):
            length += 1
            j += 1
        if length in length_dict:
            current_set = length_dict[length]
            current_list = list(current_set)
            current_list.append(item)
            new_set = set(current_list)
            length_dict[length] = new_set
        else:
            length_dict[length] = {item}
        idx += 1
    return length_dict
