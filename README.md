# Project 1 Supplement

## Overview
This project implements and tests three Python functions as part of the supplement assignment:

1. `sum_two_numbers(a, b)` - Calculates the sum of two numbers.
2. `string_length(s)` - Returns the length of a given string.
3. `update_dict(d, key, value)` - Updates or adds a key-value pair in a dictionary.

## Functions

### 1. `sum_two_numbers(a, b)`
- **Description**: Calculates the sum of two numbers.
- **Parameters**:
  - `a` (int/float): First number
  - `b` (int/float): Second number
- **Returns**: `int/float` - The sum of the two numbers.

### 2. `string_length(s)`
- **Description**: Returns the length of a given string.
- **Parameters**:
  - `s` (str): Input string
- **Returns**: `int` - The length of the string.

### 3. `update_dict(d, key, value)`
- **Description**: Updates or adds a key-value pair in a dictionary.
- **Parameters**:
  - `d` (dict): The dictionary to update
  - `key` (str): The key to update or add
  - `value`: The value to assign to the key
- **Returns**: `None`

## Testing
Unit tests for each function are implemented in `test_main.py`. Use the following command to run the tests:
```bash
pytest test_main.py
