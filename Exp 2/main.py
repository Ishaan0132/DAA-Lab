def linear_search(arr, x):
    """Performs a linear search on the given list to find the element x.

    Args:
        arr (list): The list of elements to search through.
        x (int): The element to search for.

    Returns:
        int: The index of x if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def binary_search(arr, x, low, high):
    """Performs a binary search on the sorted list to find the element x.

    Args:
        arr (list): The sorted list of elements to search through.
        x (int): The element to search for.
        low (int): The lower index of the current subarray.
        high (int): The upper index of the current subarray.

    Returns:
        int: The index of x if found, otherwise -1.
    """
    if low > high:
        return -1
    
    mid = (high + low) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, x, low, mid - 1)
    else:
        return binary_search(arr, x, mid + 1, high)


def main():
    """Main function to handle user input and search operations."""
    arr = []
    n = int(input("Enter number of elements: "))
    
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))
    
    # Sort the array before performing binary search (binary search requires a sorted array)
    arr.sort()
    
    x = int(input("Enter element to search: "))
    
    print(f"Index of {x} using linear search: {linear_search(arr, x)}")
    print(f"Index of {x} using binary search: {binary_search(arr, x, 0, len(arr) - 1)}")


if __name__ == "__main__":
    main()
