def merge_and_count(arr, temp_arr, left, mid, right):
    """Merge two subarrays and count inversions.

    Args:
        arr (list): The array to merge and count inversions.
        temp_arr (list): A temporary array used for merging.
        left (int): Left index of the subarray.
        mid (int): Middle index of the subarray.
        right (int): Right index of the subarray.

    Returns:
        int: The number of inversions in the merged subarray.
    """
    i = left  # Starting index for left subarray
    j = mid + 1  # Starting index for right subarray
    k = left  # Starting index to be sorted
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # There are mid - i inversions
            inv_count += (mid - i + 1)
            temp_arr[k] = arr[j]
            j += 1
        k += 1

    # Copy remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements of right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray back into the original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def merge_sort_and_count(arr, temp_arr, left, right):
    """Recursively divide the array and count inversions.

    Args:
        arr (list): The array to sort and count inversions.
        temp_arr (list): A temporary array used for merging.
        left (int): Left index of the subarray.
        right (int): Right index of the subarray.

    Returns:
        int: The total number of inversions in the array.
    """
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    return inv_count


def count_inversions(arr):
    """Count inversions in the array.

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
    
    temp_arr = [0] * len(arr)
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)


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
