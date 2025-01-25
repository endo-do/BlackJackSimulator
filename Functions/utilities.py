"""
Utilities Module

THis module provides a set of utility functions.

Functions:
    - find_key_to_value: Returns the key of the first occurence of a given value in a dict.
    - style_text: Returns a text as a given style.
"""


def find_key_to_value(dictionary, value, not_found=None):
    """
    Returns the key of the first occurence of a given value in a dict.

    Args:
        dictionary (dict): The dictionary to search in.
        value (str): The value to search for.
        not_found (any, optional): Value to return if the value is not found. Defaults to None.

    Returns:
        str or any: The key if found, otherwise the not_found value
    """
    for key, val in dictionary.items():
        if val == value:
            return key
    
    if not_found is None:
        return f"{value} not in {dictionary}"
    
    return not_found


def style_text(text, style):
    """
    Returns a text as a given style.

    Args:
        text (str): The text to be transformed.
        style (str): The style of the text.

    Returns:
        str: The text in the given style.
    """
    styles = {
        "normal":["", ""],
        "bold":["\033[1m", "\033[0m"],
        "italic":["\033[3m", "\033[0m"]
    }
    return f"{styles[style][0]}{text}{styles[style][1]}"
