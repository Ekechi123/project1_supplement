import main

def test_sum_two_numbers():
    """ 
    Test the sum_two_numbers function to ensure it correctly sums two numbers.
    This includes:
    - Adding two positive numbers.
    - Adding a negative and a positive number.
    - Adding zeros.
    - Adding floating point numbers.
    """
    assert main.sum_two_numbers(2, 3) == 5  # 2 + 3 = 5
    assert main.sum_two_numbers(-1, 1) == 0  # -1 + 1 = 0
    assert main.sum_two_numbers(0, 0) == 0   # 0 + 0 = 0
    assert main.sum_two_numbers(1.5, 2.5) == 4.0  # 1.5 + 2.5 = 4.0

def test_string_length():
    """ 
    Test the string_length function to ensure it correctly calculates the length of a string.
    This includes:
    - Calculating the length of a non-empty string.
    - Calculating the length of an empty string.
    - Calculating the length of a string with only a space.
    - Calculating the length of a multi-character string.
    """
    assert main.string_length("hello") == 5  # "hello" has 5 characters
    assert main.string_length("") == 0   # Empty string has length 0
    assert main.string_length(" ") == 1  # A space is considered one character
    assert main.string_length("Python") == 6  # "Python" has 6 characters

def test_update_dict():
    """ 
    Test the update_dict function to ensure it correctly updates or adds key-value pairs in the dictionary.
    This includes:
    - Updating the value of an existing key.
    - Adding a new key-value pair.
    - Handling an empty dictionary and adding a key-value pair.
    """
    d = {"key1": 1}
    main.update_dict(d, "key1", 2)  # Update value of 'key1' to 2
    assert d["key1"] == 2
    main.update_dict(d, "key2", 3)  # Add 'key2' with value 3
    assert d["key2"] == 3
    d = {}
    main.update_dict(d, "new_key", 5)  # Add 'new_key' with value 5 to an empty dictionary
    assert d["new_key"] == 5
