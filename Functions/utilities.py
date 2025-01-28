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


def center_prompt(prompt, length, space=" "):
    """
    Centers a prompt with evenly distributed spaces around it.

    Args:
        prompt (str): The prompt to be centered.
        length (int): The total length of the resulting string.
        space (str, optional): The character used for padding. Defaults to a single space.

    Returns:
        str: The string with the centered prompt. If the prompt's length exceeds
             the specified total length, it raises a ValueError.
    """
    if len(prompt) >= length:
        raise ValueError(f"The word '{prompt}' exceeds the maximum length of {length} chars")
    
    padding = length - len(prompt)
    left_padding = padding // 2
    right_padding = padding - left_padding

    return f"{space * left_padding}{prompt}{space * right_padding}"
