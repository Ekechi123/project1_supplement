import main

def test_sum():
    assert main.sum_two_numbers(2, 3) == 5
    assert main.sum_two_numbers(-1, 1) == 0
    assert main.sum_two_numbers(0, 0) == 0
