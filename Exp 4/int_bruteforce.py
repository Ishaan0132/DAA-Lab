def multiply(a, b):
    """Multiply two integers using a for loop.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of a and b.
    """
    result = 0
    for _ in range(abs(b)):  # Repeat for the absolute value of b
        result += a  # Add a to the result for each iteration
    # If b is negative, negate the result
    if b < 0:
        result = -result
    return result


def main():
    """Main function to execute the multiplication."""
    try:
        # Input: Get two integers from the user
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        # Process: Multiply the two integers
        result = multiply(num1, num2)

        # Output: Display the result
        print(f"The result of {num1} * {num2} is: {result}")
    except ValueError:
        print("Please enter valid integers.")


if __name__ == "__main__":
    main()
