# merge_sort.py

from typing import List, TypeVar, Comparable


# Define a generic type variable that can be any type that supports comparison
# (e.g., int, float, str).
T = TypeVar('T', bound=Comparable)


def _merge(left_half: List[T], right_half: List[T]) -> List[T]:
    """
    Merges two sorted lists into a single sorted list.

    This is the "conquer" step of the divide-and-conquer algorithm.

    Args:
        left_half: A sorted list of elements.
        right_half: Another sorted list of elements.

    Returns:
        A new list containing all elements from left_half and right_half
        in sorted order.
    """
    merged_array = []
    left_pointer, right_pointer = 0, 0

    # Loop while there are still elements in both lists to compare
    while left_pointer < len(left_half) and right_pointer < len(right_half):
        if left_half[left_pointer] <= right_half[right_pointer]:
            merged_array.append(left_half[left_pointer])
            left_pointer += 1
        else:
            merged_array.append(right_half[right_pointer])
            right_pointer += 1

    # At this point, one of the lists is exhausted. Append the remaining
    # elements from the other list. Python's slicing handles this elegantly.
    merged_array.extend(left_half[left_pointer:])
    merged_array.extend(right_half[right_pointer:])

    return merged_array


def merge_sort(arr: List[T]) -> List[T]:
    """
    Sorts a list in ascending order using the Merge Sort algorithm.

    Merge Sort is a stable, comparison-based, divide-and-conquer sorting
    algorithm. It works by recursively dividing the input list into two halves,
    calling itself for the two halves, and then merging the two sorted halves.

    Complexity:
        - Time: O(n log n) in all cases (best, average, and worst).
        - Space: O(n) for the auxiliary space required for merging.

    Args:
        arr: The list of elements to be sorted.

    Returns:
        A new list containing the elements of 'arr' in sorted order.
        Note: This implementation is not in-place; it returns a new list.
    """
    # Base case: A list with 0 or 1 elements is already sorted.
    if len(arr) <= 1:
        return arr

    # --- Divide Step ---
    # Find the middle point to divide the list into two halves.
    middle_index = len(arr) // 2
    left_half = arr[:middle_index]
    right_half = arr[middle_index:]

    # --- Recursive Step ---
    # Recursively sort both halves.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # --- Conquer Step ---
    # Merge the sorted halves back together.
    return _merge(sorted_left, sorted_right)


# This block allows the script to be run directly to test the algorithm.
if __name__ == "__main__":
    print("--- Testing Merge Sort Implementation ---")

    # Test Case 1: Standard unsorted list of integers
    sample_list = [38, 27, 43, 3, 9, 82, 10]
    print(f"\nOriginal list: {sample_list}")
    sorted_list = merge_sort(sample_list)
    print(f"Sorted list:   {sorted_list}")
    assert sorted_list == [3, 9, 10, 27, 38, 43, 82]

    # Test Case 2: List with duplicate elements
    sample_list_duplicates = [5, 2, 9, 5, 2, 8, 5]
    print(f"\nOriginal list with duplicates: {sample_list_duplicates}")
    sorted_list_duplicates = merge_sort(sample_list_duplicates)
    print(f"Sorted list with duplicates:   {sorted_list_duplicates}")
    assert sorted_list_duplicates == [2, 2, 5, 5, 5, 8, 9]

    # Test Case 3: Already sorted list
    sample_already_sorted = [1, 2, 3, 4, 5, 6, 7]
    print(f"\nAlready sorted list: {sample_already_sorted}")
    sorted_already = merge_sort(sample_already_sorted)
    print(f"Sorted result:         {sorted_already}")
    assert sorted_already == [1, 2, 3, 4, 5, 6, 7]
    
    # Test Case 4: Reverse sorted list
    sample_reverse_sorted = [10, 9, 8, 7, 6, 5]
    print(f"\nReverse sorted list: {sample_reverse_sorted}")
    sorted_reverse = merge_sort(sample_reverse_sorted)
    print(f"Sorted result:       {sorted_reverse}")
    assert sorted_reverse == [5, 6, 7, 8, 9, 10]

    # Test Case 5: Empty list and single-element list
    print("\nEdge cases:")
    print(f"Sorting an empty list []: {merge_sort([])}")
    assert merge_sort([]) == []
    print(f"Sorting a single-element list [42]: {merge_sort([42])}")
    assert merge_sort([42]) == [42]

    print("\n--- All tests passed successfully! ---")