#!/usr/bin/env python3
"""
A Python script to find the maximum number in a list of numbers.

This script provides a function `find_maximum` that implements the logic
from scratch and demonstrates its usage with various examples.
"""

from typing import List, Union, Optional

# Define a type alias for a list of numbers for cleaner type hints.
NumericList = List[Union[int, float]]

def find_maximum(numbers: NumericList) -> Optional[Union[int, float]]:
    """
    Finds the maximum number in a list of integers and/or floats.

    This function iterates through the list to find the maximum value
    without using the built-in `max()` function.

    Args:
        numbers: A list of numbers (integers or floats).

    Returns:
        The maximum number found in the list.
        Returns `None` if the input list is empty.

    Example:
        >>> find_maximum([1, 5, 2, 9, 3])
        9
        >>> find_maximum([-10, -5, -2, -15])
        -2
        >>> find_maximum([]) is None
        True
    """
    # --- Edge Case Handling ---
    # If the list is empty, there is no maximum number.
    if not numbers:
        return None

    # --- Algorithm ---
    # 1. Initialize a variable `max_so_far` with the first element of the list.
    #    This gives us a starting point for comparison.
    max_so_far = numbers[0]

    # 2. Iterate through the rest of the list (starting from the second element).
    #    We can slice the list from index 1 (`numbers[1:]`).
    for number in numbers[1:]:
        # 3. For each number, compare it to our current maximum.
        if number > max_so_far:
            # 4. If the current number is greater, update `max_so_far`.
            max_so_far = number
            
    # 5. After checking all numbers, `max_so_far` will hold the largest value.
    return max_so_far

# The `if __name__ == "__main__":` block ensures this code only runs
# when you execute the script directly (e.g., `python max.py`), not when
# it's imported as a module into another file.
if __name__ == "__main__":
    print("--- Finding the Maximum Number in a List ---")

    # Example 1: A list of positive integers
    list1 = [10, 2, 78, 43, 101, 32]
    max1 = find_maximum(list1)
    print(f"
List: {list1}")
    print(f"Maximum number: {max1}") # Expected: 101

    # Example 2: A list including negative numbers and floats
    list2 = [-5, 15.5, 0, -20.2, 3.14]
    max2 = find_maximum(list2)
    print(f"
List: {list2}")
    print(f"Maximum number: {max2}") # Expected: 15.5

    # Example 3: A list where all numbers are negative
    list3 = [-1, -5, -100, -2]
    max3 = find_maximum(list3)
    print(f"
List: {list3}")
    print(f"Maximum number: {max3}") # Expected: -1

    # Example 4: An empty list (edge case)
    list4 = []
    max4 = find_maximum(list4)
    print(f"
List: {list4}")
    print(f"Maximum number: {max4}") # Expected: None

    # --- Note on Python's Built-in `max()` ---
    print("
" + "-"*40)
    print("Note: In a real-world application, you would typically use")
    print("Python's highly optimized built-in max() function:")
    print(f"max({list1}) = {max(list1)}")
    print("-" * 40)
