import sys

class MatrixChainMultiplication:
    """Computes minimum scalar multiplications and optimal order for matrix chain multiplication.

    Attributes:
        dimensions (list): The list of dimensions where dimensions[i-1] and dimensions[i] are
            dimensions for the i-th matrix in the chain.
        n (int): Number of matrices in the chain.
        m (list): DP table where m[i][j] stores the minimum cost for multiplying matrices from i to j.
        s (list): DP table where s[i][j] stores the split point for the optimal cost in m[i][j].
    """

    def __init__(self, dimensions):
        """Initializes MatrixChainMultiplication with dimensions and validates input.

        Args:
            dimensions (list): List of matrix dimensions.
        
        Raises:
            ValueError: If dimensions contain invalid values (non-integer or non-positive).
        """
        self.dimensions = dimensions
        self.n = len(dimensions) - 1
        self._validate_dimensions()
        self.m = [[0] * self.n for _ in range(self.n)]
        self.s = [[0] * self.n for _ in range(self.n)]

    def _validate_dimensions(self):
        """Validates dimensions to ensure all elements are positive integers.

        Raises:
            ValueError: If any dimension is non-integer or non-positive.
        """
        if self.n < 1:
            raise ValueError("Input list must contain at least three dimensions to form two matrices.")
        if any(type(dim) != int for dim in self.dimensions):
            raise ValueError("All matrix dimensions must be integers.")
        if any(dim <= 0 for dim in self.dimensions):
            raise ValueError("All matrix dimensions must be positive.")

    def compute_min_cost(self):
        """Calculates the minimum scalar multiplications required to multiply the chain of matrices.

        Returns:
            int: The minimum number of scalar multiplications needed.
        """
        for chain_len in range(2, self.n + 1):
            for i in range(self.n - chain_len + 1):
                j = i + chain_len - 1
                self.m[i][j] = sys.maxsize
                for k in range(i, j):
                    cost = (self.m[i][k] + self.m[k + 1][j] +
                            self.dimensions[i] * self.dimensions[k + 1] * self.dimensions[j + 1])
                    if cost < self.m[i][j]:
                        self.m[i][j] = cost
                        self.s[i][j] = k
        return self.m[0][self.n - 1]

    def get_optimal_order(self):
        """Generates the optimal order of matrix multiplication.

        Returns:
            str: A string representation of the optimal multiplication order.
        """
        return self._build_order(0, self.n - 1)

    def _build_order(self, i, j):
        """Recursive helper to construct the optimal multiplication order.

        Args:
            i (int): Start index for matrix multiplication.
            j (int): End index for matrix multiplication.

        Returns:
            str: Substring of the optimal multiplication order for matrices from i to j.
        """
        if i == j:
            return f"A{i + 1}"
        else:
            return f"({self._build_order(i, self.s[i][j])} x {self._build_order(self.s[i][j] + 1, j)})"


class MatrixChainTest:
    """Manages and runs test cases for MatrixChainMultiplication."""

    def __init__(self):
        """Initializes the test cases for matrix chain multiplication."""
        self.test_cases = [
            {"p": [10, 20, 30, 40, 30, 20, 10]},      # Valid case with 6 matrices
            {"p": [30, 35, 15, 5, 10, 20, 25]},       # Valid case with 6 matrices
            {"p": [5, 10, 3, 12, 5, 50, 6]},          # Valid case with 6 matrices
            {"p": [10, "20", "30", 40, "30", 20, "10"]},  # Non-integer dimension
            {"p": [10, -20, 30, 0, -40, 50, -60]},    # Zero or negative dimension
            {"p": []}                                 # Empty input list
        ]

    def run_tests(self):
        """Runs each test case, printing results or errors for each."""
        for i, test in enumerate(self.test_cases):
            dimensions = test["p"]
            print(f"Test Case {i + 1}: p = {dimensions}")
            try:
                matrix_chain = MatrixChainMultiplication(dimensions)
                min_cost = matrix_chain.compute_min_cost()
                order = matrix_chain.get_optimal_order()
                print(f"Minimum cost: {min_cost}")
                print(f"Optimal order: {order}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            print()


# Run test cases
if __name__ == "__main__":
    MatrixChainTest().run_tests()
