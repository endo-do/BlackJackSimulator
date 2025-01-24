""" Functions to handle data """


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
