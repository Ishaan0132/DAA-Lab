class Item:
    """Class to represent an item with a name, weight, value, and shelf life."""

    def __init__(self, name, weight, value, shelf_life):
        """Initialize an item with given properties.

        Args:
        name (str): Name of the item.
        weight (float): Weight of the item.
        value (float): Value of the item.
        shelf_life (int): Shelf life of the item in days.
        """
        self.name = name
        self.weight = weight
        self.value = value
        self.shelf_life = shelf_life
        # Avoid division by zero if weight is zero
        self.value_per_weight = value / weight if weight > 0 else float('inf')

    def __repr__(self):
        return (f"Item(name={self.name}, weight={self.weight}, "
                f"value={self.value}, shelf_life={self.shelf_life})")


def fractional_knapsack(items, max_capacity=200):
    """Calculates the maximum value obtainable within given weight capacity.

    Args:
    items (list[Item]): List of items to be considered.
    max_capacity (float): Maximum weight capacity of the knapsack.

    Returns:
    float or str: Maximum total value achievable with given items, or an error message if inputs are invalid.
    """
    # Negative Test Case 1: No items available
    if not items:
        return "Error: No items available to load."

    # Negative Test Case 2: All items have zero value
    if all(item.value == 0 for item in items):
        return "Error: All items have zero value."

    # Negative Test Case 3: Item(s) with zero weight
    if any(item.weight == 0 for item in items):
        return "Error: One or more items have zero weight"

    # Sort items by shelf life (ascending) and value-to-weight ratio (descending)
    items.sort(key=lambda item: (item.shelf_life, -item.value_per_weight))

    total_value = 0
    for item in items:
        if max_capacity <= 0:
            break
        if item.weight <= max_capacity:
            max_capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.value_per_weight * max_capacity
            max_capacity = 0
    return total_value


def test_fractional_knapsack():
    """Runs positive and negative test cases for the fractional_knapsack function."""

    # Positive Test Case 1: Items exactly fill the vehicle capacity with maximum value
    items1 = [Item("A", 100, 500, 2), Item("B", 100, 700, 1)]
    print(f"Test 1 Value: {fractional_knapsack(items1)}")

    # Positive Test Case 2: Items taken in fractional parts to maximize value
    items2 = [Item("C", 150, 750, 1), Item("D", 70, 280, 2), Item("E", 50, 400, 3)]
    print(f"Test 2 Value: {fractional_knapsack(items2)}")

    # Positive Test Case 3: High-value item with low shelf life is partially included
    items3 = [Item("F", 180, 1200, 1), Item("G", 50, 300, 3)]
    print(f"Test 3 Value: {fractional_knapsack(items3)}")

    # Negative Test Case 1: All items have zero value
    items4 = [Item("J", 50, 0, 1), Item("K", 100, 0, 2)]
    print(f"Test 4: {fractional_knapsack(items4)}")

    # Negative Test Case 2: No items to load
    items5 = []
    print(f"Test 5: {fractional_knapsack(items5)}")

    # Negative Test Case 3: One item has zero weight (invalid case)
    items6 = [Item("O", 0, 500, 1), Item("P", 100, 700, 2)]
    print(f"Test 6: {fractional_knapsack(items6)}")


# Run the tests
if __name__ == "__main__":
    test_fractional_knapsack()
