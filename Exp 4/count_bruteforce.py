def count_inversions(arr):
    """Count inversions in the array using a brute-force approach.

    Args:
        arr (list): The list of numbers to check for inversions.

    Returns:
        int: The number of inversions in the array.

    Raises:
        ValueError: If the array is empty or has less than 10 elements.
        TypeError: If any element in the array is not a number.
    """
    # Check for empty array
    if len(arr) == 0:
        raise ValueError("The array is empty.")
    
    # Check for array length
    if len(arr) < 10:
        raise ValueError("The array must have at least 10 elements.")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements of the array must be numbers.")
    
    inv_count = 0
    n = len(arr)
    # Iterate through each element and count inversions
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count

if __name__ == "__main__":
    test_cases = [
        [23491, 23571, 23497, 23321, 23499, 23731, 23892, 23554, 23901, 23956],  # Valid case
        [23231, 23321, 23345, 23452, 23552, 23567, 23681, 23790, 23888, 23991],  # Valid case
        [23590, 23791, 23214, 23413, 23521, 23771, 23839, 23415, 23115, 23557],  # Valid case
        [23390, 23591, 23431],  # Less than 10 elements
        [],  # Empty array
        [23590, 23791, 23214, 23413, 23521, 23771, 23839, 23415, 23115, "23557"],  # Non-numeric element
    ]

    for i, test_case in enumerate(test_cases):
        try:
            result = count_inversions(test_case)
            print(f"Test case {i + 1}: {test_case} -> Number of inversions: {result}")
        except (ValueError, TypeError) as e:
            print(f"Test case {i + 1}: {test_case} -> {e}")