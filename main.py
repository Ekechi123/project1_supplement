def sum_two_numbers(a, b):
    """
    Calculate the sum of two numbers and return the result.

    Args:
        a (int/float): The first number.
        b (int/float): The second number.

    Returns:
        int/float: The sum of the two numbers.
    """
    return a + b


def string_length(s):
    """
    Return the length of a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the string.
    """
    return len(s)


def update_dict(d, key, value):
    """
    Update the value of a key in a dictionary. If the key doesn't exist, add it.

    Args:
        d (dict): The dictionary to update.
        key (str): The key to update/add.
        value: The value to assign to the key.

    Returns:
        None
    """
    d[key] = value
