"""
Asymptotic Notation Analysis

This module explains and demonstrates Big O, Big Omega, and Big Theta notations
with practical examples and mathematical foundations.
"""

import math
from typing import List, Callable, Any


class AsymptoticAnalyzer:
    """Class for analyzing asymptotic behavior of algorithms"""

    def __init__(self):
        self.algorithms = {}

    def register_algorithm(self, name: str, func: Callable, complexity_class: str):
        """Register an algorithm for analysis"""
        self.algorithms[name] = {"function": func, "complexity": complexity_class}

    def analyze_growth(self, algorithm_name: str, input_sizes: List[int]):
        """Analyze how algorithm performance grows with input size"""
        if algorithm_name not in self.algorithms:
            print(f"Algorithm {algorithm_name} not registered")
            return

        algo_info = self.algorithms[algorithm_name]
        print(f"\n=== ANALYZING: {algorithm_name} ===")
        print(f"Theoretical Complexity: {algo_info['complexity']}")
        print("Input Size -> Operations Count")

        for size in input_sizes:
            test_input = list(range(size))
            # This is a simplified operation count - in practice you'd instrument the code
            operations = self._estimate_operations(algo_info["function"], test_input)
            print(f"{size:8d} -> {operations:10d}")


def big_o_examples():
    """Demonstrate Big O notation with concrete examples"""
    print("=== BIG O NOTATION (Upper Bound) ===\n")

    print("Big O describes the worst-case performance")
    print("f(n) = O(g(n)) means f(n) ≤ c·g(n) for large n\n")

    # O(1) examples
    print("1. O(1) - Constant Time Examples:")
    print("   - Array element access: arr[0]")
    print("   - Hash table lookup (average case)")
    print("   - Stack push/pop operations")
    print("   - Mathematical operations: +, -, *, /\n")

    # O(log n) examples
    print("2. O(log n) - Logarithmic Time Examples:")
    print("   - Binary search in sorted array")
    print("   - Tree operations in balanced BST")
    print("   - Finding element in balanced heap")
    print("   - Divide and conquer algorithms\n")

    # O(n) examples
    print("3. O(n) - Linear Time Examples:")
    print("   - Linear search through array")
    print("   - Traversing linked list")
    print("   - Finding min/max in unsorted array")
    print("   - Counting occurrences\n")

    # O(n log n) examples
    print("4. O(n log n) - Linearithmic Time Examples:")
    print("   - Merge sort, heap sort, quick sort (average)")
    print("   - Building a heap from array")
    print("   - Optimal comparison-based sorting\n")

    # O(n²) examples
    print("5. O(n²) - Quadratic Time Examples:")
    print("   - Bubble sort, selection sort, insertion sort")
    print("   - Nested loops over same data")
    print("   - Naive string matching algorithms")
    print("   - Finding all pairs in array\n")


def big_omega_examples():
    """Demonstrate Big Omega notation (lower bound)"""
    print("=== BIG OMEGA NOTATION (Lower Bound) ===\n")

    print("Big Omega describes the best-case performance")
    print("f(n) = Ω(g(n)) means f(n) ≥ c·g(n) for large n\n")

    print("Examples:")
    print("1. Comparison-based sorting is Ω(n log n)")
    print("   - Cannot sort n elements faster than n log n comparisons")
    print("   - This is a theoretical lower bound\n")

    print("2. Searching unsorted array is Ω(n)")
    print("   - Must examine at least one element")
    print("   - In worst case, might need to check all elements\n")

    print("3. Matrix multiplication is Ω(n²)")
    print("   - Must read all n² elements at least once")
    print("   - Output itself is n² elements\n")


def big_theta_examples():
    """Demonstrate Big Theta notation (tight bound)"""
    print("=== BIG THETA NOTATION (Tight Bound) ===\n")

    print("Big Theta describes exact asymptotic behavior")
    print("f(n) = Θ(g(n)) means c₁·g(n) ≤ f(n) ≤ c₂·g(n)\n")

    print("Examples where best and worst case match:")
    print("1. Merge Sort: Θ(n log n)")
    print("   - Always divides array in half")
    print("   - Always merges all elements")
    print("   - Performance is consistent\n")

    print("2. Matrix multiplication (standard): Θ(n³)")
    print("   - Always performs exactly n³ multiplications")
    print("   - No input dependency for operation count\n")

    print("3. Finding sum of array: Θ(n)")
    print("   - Must visit every element exactly once")
    print("   - No shortcuts possible\n")


def complexity_comparison_table():
    """Display complexity comparison table"""
    print("=== COMPLEXITY COMPARISON TABLE ===\n")

    complexities = [
        ("O(1)", "Constant", "Excellent", "Hash table access"),
        ("O(log n)", "Logarithmic", "Good", "Binary search"),
        ("O(n)", "Linear", "Fair", "Linear search"),
        ("O(n log n)", "Linearithmic", "Acceptable", "Merge sort"),
        ("O(n²)", "Quadratic", "Slow", "Bubble sort"),
        ("O(2ⁿ)", "Exponential", "Very Slow", "Fibonacci (naive)"),
        ("O(n!)", "Factorial", "Extremely Slow", "Traveling salesman"),
    ]

    print(f"{'Notation':<12} {'Name':<15} {'Performance':<15} {'Example':<20}")
    print("-" * 70)
    for notation, name, performance, example in complexities:
        print(f"{notation:<12} {name:<15} {performance:<15} {example:<20}")
    print()


def practical_examples():
    """Show practical examples with sample inputs"""
    print("=== PRACTICAL COMPLEXITY EXAMPLES ===\n")

    # Input sizes for demonstration
    sizes = [10, 100, 1000, 10000]

    print("Theoretical operation counts for different complexities:")
    print(
        f"{'n':<8} {'O(1)':<10} {'O(log n)':<12} {'O(n)':<10} {'O(n²)':<12} {'O(2ⁿ)':<15}"
    )
    print("-" * 70)

    for n in sizes:
        constant = 1
        logarithmic = math.ceil(math.log2(n)) if n > 0 else 0
        linear = n
        quadratic = n * n
        exponential = "Too large" if n > 20 else str(2**n)

        print(
            f"{n:<8} {constant:<10} {logarithmic:<12} {linear:<10} {quadratic:<12} {exponential:<15}"
        )
    print()


def asymptotic_rules():
    """Explain rules for asymptotic analysis"""
    print("=== ASYMPTOTIC ANALYSIS RULES ===\n")

    print("1. Drop Constants:")
    print("   3n + 5 = O(n), not O(3n)")
    print("   10n² = O(n²), not O(10n²)\n")

    print("2. Drop Lower Order Terms:")
    print("   n² + n + 1 = O(n²)")
    print("   n³ + n² + n + 1 = O(n³)\n")

    print("3. Focus on Dominant Term:")
    print("   For large n, higher order terms dominate")
    print("   n² grows much faster than n\n")

    print("4. Common Rules:")
    print("   O(1) + O(1) = O(1)")
    print("   O(n) + O(n) = O(n)")
    print("   O(n) × O(m) = O(n·m)")
    print("   O(n) + O(n²) = O(n²)\n")


def main():
    """Main demonstration function"""
    print("ASYMPTOTIC NOTATION COMPREHENSIVE GUIDE")
    print("=" * 50)

    big_o_examples()
    print("\n" + "=" * 50 + "\n")

    big_omega_examples()
    print("\n" + "=" * 50 + "\n")

    big_theta_examples()
    print("\n" + "=" * 50 + "\n")

    complexity_comparison_table()
    print("\n" + "=" * 50 + "\n")

    practical_examples()
    print("\n" + "=" * 50 + "\n")

    asymptotic_rules()


if __name__ == "__main__":
    main()
