import main

def test_sum_two_numbers():
    """ 
    Test the sum_two_numbers function to ensure it correctly sums two numbers.
    """
    assert main.sum_two_numbers(2, 3) == 5
    assert main.sum_two_numbers(-1, 1) == 0
    assert main.sum_two_numbers(0, 0) == 0
    assert main.sum_two_numbers(1.5, 2.5) == 4.0


def test_string_length():
    """ 
    Test the string_length function to ensure it correctly calculates the length of a string.
    """
    assert main.string_length("hello") == 5
    assert main.string_length("") == 0
    assert main.string_length(" ") == 1
    assert main.string_length("Python") == 6


def test_update_dict():
    """
    Test the update_dict function to ensure it correctly updates or adds key-value pairs in the dictionary.
    """
    d = {"key1": 1}
    main.update_dict(d, "key1", 2)  # Increment value of 'key1' by 2
    assert d["key1"] == 3  # New value of 'key1' should be 3
    main.update_dict(d, "key2", 3)  # Add 'key2' with value 3
    assert d["key2"] == 3
    d = {}
    main.update_dict(d, "new_key", 5)  # Add 'new_key' with value 5 to an empty dictionary
    assert d["new_key"] == 5
