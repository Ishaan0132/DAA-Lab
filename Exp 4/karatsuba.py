def karatsuba(x, y):
    """Recursive Karatsuba multiplication algorithm.

    Args:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        int: The product of x and y.
    """
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y

    # Calculate the size of the numbers
    max_len = max(len(str(x)), len(str(y)))
    half_len = max_len // 2

    # Split the digit sequences about the half_len
    x_high = x // (10 ** half_len)
    x_low = x % (10 ** half_len)
    y_high = y // (10 ** half_len)
    y_low = y % (10 ** half_len)

    # 3 recursive calls
    z0 = karatsuba(x_low, y_low)  # Low parts
    z1 = karatsuba(x_low + x_high, y_low + y_high)  # Cross parts
    z2 = karatsuba(x_high, y_high)  # High parts

    # Combine the results using the Karatsuba formula
    return (z2 * (10 ** (2 * half_len))) + \
           ((z1 - z2 - z0) * (10 ** half_len)) + z0


if __name__ == "__main__":
    while True:
        try:
            num1 = input("Enter the first integer: ")
            num2 = input("Enter the second integer: ")

            # Convert inputs to integers
            num1 = int(num1)
            num2 = int(num2)

            result = karatsuba(num1, num2)
            print(f"The result of {num1} * {num2} using Karatsuba is: {result}")
            break  # Exit loop after successful calculation
        except ValueError:
            print("Please enter valid integers.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")