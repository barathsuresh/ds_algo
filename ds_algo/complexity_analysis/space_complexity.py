"""
Space Complexity Analysis and Examples

This module demonstrates different space complexities with practical examples
showing how memory usage scales with input size.
"""

from typing import List, Any


def constant_space_example(arr: List[int]) -> int:
    """
    O(1) - Constant Space Complexity
    Finding maximum element using constant extra space
    """
    if not arr:
        return None

    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    return max_element


def linear_space_example(arr: List[int]) -> List[int]:
    """
    O(n) - Linear Space Complexity
    Creating a copy of the array
    """
    copied_array = []
    for element in arr:
        copied_array.append(element)
    return copied_array


def quadratic_space_example(n: int) -> List[List[int]]:
    """
    O(n²) - Quadratic Space Complexity
    Creating a 2D matrix
    """
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * n + j)
        matrix.append(row)
    return matrix


def logarithmic_space_example(arr: List[int]) -> List[int]:
    """
    O(log n) - Logarithmic Space Complexity
    Recursive binary search (call stack space)
    """

    def binary_search_recursive(arr, target, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)

    # Demonstration: search for middle element
    target = arr[len(arr) // 2] if arr else 0
    result_index = binary_search_recursive(arr, target, 0, len(arr) - 1)
    return [target, result_index]


def recursive_space_example(n: int) -> int:
    """
    O(n) - Linear Space Complexity (due to recursion stack)
    Recursive factorial calculation
    """
    if n <= 1:
        return 1
    return n * recursive_space_example(n - 1)


def demonstrate_space_complexities():
    """Demonstrate different space complexities"""
    print("=== SPACE COMPLEXITY DEMONSTRATIONS ===\n")

    test_array = list(range(1, 11))  # [1, 2, 3, ..., 10]

    print("1. O(1) - Constant Space:")
    print(f"   Input array: {test_array}")
    max_val = constant_space_example(test_array)
    print(f"   Maximum element: {max_val}")
    print("   Uses only a few variables regardless of input size\n")

    print("2. O(n) - Linear Space:")
    copied = linear_space_example(test_array)
    print(f"   Original: {test_array}")
    print(f"   Copied:   {copied}")
    print("   Memory usage grows linearly with input size\n")

    print("3. O(log n) - Logarithmic Space:")
    search_result = logarithmic_space_example(test_array)
    print(f"   Binary search result: {search_result}")
    print("   Recursion depth grows logarithmically\n")

    print("4. O(n) - Linear Space (Recursion):")
    factorial_5 = recursive_space_example(5)
    print(f"   5! = {factorial_5}")
    print("   Call stack depth grows linearly with input\n")

    print("5. O(n²) - Quadratic Space:")
    matrix_3x3 = quadratic_space_example(3)
    print("   3x3 Matrix:")
    for row in matrix_3x3:
        print(f"   {row}")
    print("   Memory usage grows quadratically with input size")


class SpaceComplexityAnalyzer:
    """Class to analyze and compare space complexities"""

    def __init__(self):
        self.complexity_examples = {
            "O(1)": constant_space_example,
            "O(log n)": logarithmic_space_example,
            "O(n)": linear_space_example,
            "O(n²)": lambda arr: quadratic_space_example(len(arr)),
        }

    def analyze_complexity(self, func_name: str, input_data: Any):
        """Analyze the space complexity of a given function"""
        if func_name in self.complexity_examples:
            result = self.complexity_examples[func_name](input_data)
            return result
        else:
            print(f"Function {func_name} not found in examples")
            return None

    def compare_complexities(self, sizes: List[int]):
        """Compare how different complexities scale with input size"""
        print("=== SPACE COMPLEXITY SCALING COMPARISON ===\n")

        for size in sizes:
            print(f"Input size: {size}")
            test_data = list(range(size))

            # O(1) - always uses constant space
            print(f"   O(1): Uses constant space regardless of size")

            # O(log n) - recursion depth
            import math

            log_depth = math.ceil(math.log2(size)) if size > 0 else 0
            print(f"   O(log n): Recursion depth ≈ {log_depth}")

            # O(n) - linear space
            print(f"   O(n): Space for {size} elements")

            # O(n²) - quadratic space
            print(f"   O(n²): Space for {size}² = {size**2} elements")
            print()


if __name__ == "__main__":
    demonstrate_space_complexities()
    print("\n" + "=" * 50 + "\n")

    analyzer = SpaceComplexityAnalyzer()
    analyzer.compare_complexities([10, 100, 1000])
