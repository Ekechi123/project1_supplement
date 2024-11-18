import main

def test_sum_two_numbers():
    assert main.sum_two_numbers(2, 3) == 5
    assert main.sum_two_numbers(-1, 1) == 0
    assert main.sum_two_numbers(0, 0) == 0
    assert main.sum_two_numbers(1.5, 2.5) == 4.0

def test_string_length():
    assert main.string_length("hello") == 5
    assert main.string_length("") == 0
    assert main.string_length(" ") == 1
    assert main.string_length("Python") == 6

def test_update_dict():
    d = {"key1": 1}
    main.update_dict(d, "key1", 2)
    assert d["key1"] == 2

    main.update_dict(d, "key2", 3)
    assert d["key2"] == 3

    d = {}
    main.update_dict(d, "new_key", 5)
    assert d["new_key"] == 5
