"""
Python Lists - Dynamic Array Implementation and Analysis

This module demonstrates Python's built-in list operations, their complexities,
and advanced usage patterns. Lists in Python are dynamic arrays that can
resize automatically.
"""

from typing import List, Any, Optional, Iterator
import sys
import time


class PythonListOperations:
    """Class demonstrating Python list operations and their complexities"""

    def __init__(self):
        self.operations_count = 0

    def reset_counter(self):
        """Reset operations counter"""
        self.operations_count = 0

    def get_operations_count(self):
        """Get current operations count"""
        return self.operations_count

    # List Creation Operations
    def create_empty_list(self) -> List[Any]:
        """
        Create an empty list
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.operations_count += 1
        return []

    def create_list_with_size(self, size: int, default_value: Any = None) -> List[Any]:
        """
        Create list with specific size and default value
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        self.operations_count += size
        return [default_value] * size

    def create_list_from_range(self, start: int, end: int, step: int = 1) -> List[int]:
        """
        Create list from range
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = list(range(start, end, step))
        self.operations_count += len(result)
        return result

    # Advanced List Operations
    def list_comprehension_demo(self, data: List[int]) -> List[int]:
        """
        Demonstrate list comprehension
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Square all even numbers
        result = [x**2 for x in data if x % 2 == 0]
        self.operations_count += len(data)
        return result

    def nested_list_operations(self, rows: int, cols: int) -> List[List[int]]:
        """
        Create and manipulate nested lists (2D array)
        Time Complexity: O(rows * cols)
        Space Complexity: O(rows * cols)
        """
        # Create 2D list
        matrix = [[i * cols + j for j in range(cols)] for i in range(rows)]
        self.operations_count += rows * cols
        return matrix

    def list_slicing_operations(self, lst: List[Any]) -> dict:
        """
        Demonstrate various list slicing operations
        Time Complexity: O(k) where k is slice size
        Space Complexity: O(k)
        """
        results = {}
        n = len(lst)

        if n > 0:
            # Basic slicing
            results["first_half"] = lst[: n // 2]
            results["second_half"] = lst[n // 2 :]
            results["reverse"] = lst[::-1]
            results["every_second"] = lst[::2]
            results["last_three"] = lst[-3:]

            self.operations_count += n  # Approximate operations for slicing

        return results

    # List Modification Operations
    def extend_vs_append(self, base_list: List[Any], items: List[Any]) -> dict:
        """
        Compare extend vs append operations
        extend: O(k) where k is length of items
        append: O(1) for each item, O(k) total
        """
        # Test extend
        list1 = base_list.copy()
        start_time = time.time()
        list1.extend(items)
        extend_time = time.time() - start_time
        self.operations_count += len(items)

        # Test multiple appends
        list2 = base_list.copy()
        start_time = time.time()
        for item in items:
            list2.append(item)
        append_time = time.time() - start_time
        self.operations_count += len(items)

        return {
            "extend_result": list1,
            "append_result": list2,
            "extend_time": extend_time,
            "append_time": append_time,
            "lists_equal": list1 == list2,
        }

    def list_concatenation(self, list1: List[Any], list2: List[Any]) -> List[Any]:
        """
        Concatenate two lists using + operator
        Time Complexity: O(n + m)
        Space Complexity: O(n + m)
        """
        result = list1 + list2
        self.operations_count += len(list1) + len(list2)
        return result

    def list_multiplication(self, lst: List[Any], times: int) -> List[Any]:
        """
        Multiply list (repeat elements)
        Time Complexity: O(n * times)
        Space Complexity: O(n * times)
        """
        result = lst * times
        self.operations_count += len(lst) * times
        return result

    # Search and Query Operations
    def count_occurrences(self, lst: List[Any], element: Any) -> int:
        """
        Count occurrences of element
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count = lst.count(element)
        self.operations_count += len(lst)
        return count

    def find_all_indices(self, lst: List[Any], element: Any) -> List[int]:
        """
        Find all indices where element occurs
        Time Complexity: O(n)
        Space Complexity: O(k) where k is number of occurrences
        """
        indices = [i for i, x in enumerate(lst) if x == element]
        self.operations_count += len(lst)
        return indices

    def check_membership(self, lst: List[Any], element: Any) -> bool:
        """
        Check if element is in list
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = element in lst
        self.operations_count += len(lst)  # Worst case
        return result

    # Sorting and Ordering Operations
    def sort_list_inplace(self, lst: List[Any], reverse: bool = False) -> None:
        """
        Sort list in place
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        lst.sort(reverse=reverse)
        self.operations_count += len(lst) * max(
            1, len(lst).bit_length()
        )  # Approximate n log n

    def sort_list_return_new(self, lst: List[Any], reverse: bool = False) -> List[Any]:
        """
        Return new sorted list
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        result = sorted(lst, reverse=reverse)
        self.operations_count += len(lst) * max(
            1, len(lst).bit_length()
        )  # Approximate n log n
        return result

    def reverse_list_inplace(self, lst: List[Any]) -> None:
        """
        Reverse list in place
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        lst.reverse()
        self.operations_count += len(lst) // 2

    # List Filtering and Transformation
    def filter_list(self, lst: List[int], condition_func) -> List[int]:
        """
        Filter list based on condition
        Time Complexity: O(n)
        Space Complexity: O(k) where k is number of elements that pass filter
        """
        result = [x for x in lst if condition_func(x)]
        self.operations_count += len(lst)
        return result

    def map_list(self, lst: List[Any], transform_func) -> List[Any]:
        """
        Transform all elements in list
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = [transform_func(x) for x in lst]
        self.operations_count += len(lst)
        return result


def demonstrate_list_operations():
    """Demonstrate various list operations"""
    print("=== PYTHON LIST OPERATIONS DEMONSTRATION ===\n")

    list_ops = PythonListOperations()

    # Basic operations
    print("1. LIST CREATION:")
    empty_list = list_ops.create_empty_list()
    sized_list = list_ops.create_list_with_size(5, "default")
    range_list = list_ops.create_list_from_range(1, 11)

    print(f"   Empty list: {empty_list}")
    print(f"   Sized list: {sized_list}")
    print(f"   Range list: {range_list}")
    print(f"   Creation operations: {list_ops.get_operations_count()}\n")

    # List comprehension
    print("2. LIST COMPREHENSION:")
    list_ops.reset_counter()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_squares = list_ops.list_comprehension_demo(numbers)
    print(f"   Original: {numbers}")
    print(f"   Even squares: {even_squares}")
    print(f"   Operations: {list_ops.get_operations_count()}\n")

    # Slicing operations
    print("3. LIST SLICING:")
    list_ops.reset_counter()
    test_list = list(range(10))
    slicing_results = list_ops.list_slicing_operations(test_list)
    print(f"   Original: {test_list}")
    for operation, result in slicing_results.items():
        print(f"   {operation}: {result}")
    print(f"   Operations: {list_ops.get_operations_count()}\n")

    # Extend vs append
    print("4. EXTEND vs APPEND:")
    list_ops.reset_counter()
    base = [1, 2, 3]
    items_to_add = [4, 5, 6]
    comparison = list_ops.extend_vs_append(base, items_to_add)
    print(f"   Base list: {base}")
    print(f"   Items to add: {items_to_add}")
    print(f"   Extend result: {comparison['extend_result']}")
    print(f"   Append result: {comparison['append_result']}")
    print(f"   Results equal: {comparison['lists_equal']}")
    print(f"   Operations: {list_ops.get_operations_count()}\n")


def list_performance_analysis():
    """Analyze performance of different list operations"""
    print("=== LIST PERFORMANCE ANALYSIS ===\n")

    list_ops = PythonListOperations()

    # Test different sizes
    sizes = [100, 1000, 10000]

    print("Performance comparison for different operations:")
    print(f"{'Size':<8} {'Create':<10} {'Search':<10} {'Sort':<10} {'Reverse':<10}")
    print("-" * 50)

    for size in sizes:
        # Create test data
        test_list = list(range(size))

        # Measure creation
        list_ops.reset_counter()
        new_list = list_ops.create_list_from_range(0, size)
        create_ops = list_ops.get_operations_count()

        # Measure search
        list_ops.reset_counter()
        found = list_ops.check_membership(test_list, size // 2)
        search_ops = list_ops.get_operations_count()

        # Measure sorting
        list_ops.reset_counter()
        sorted_list = list_ops.sort_list_return_new(test_list.copy())
        sort_ops = list_ops.get_operations_count()

        # Measure reverse
        list_ops.reset_counter()
        test_copy = test_list.copy()
        list_ops.reverse_list_inplace(test_copy)
        reverse_ops = list_ops.get_operations_count()

        print(
            f"{size:<8} {create_ops:<10} {search_ops:<10} {sort_ops:<10} {reverse_ops:<10}"
        )


def list_memory_analysis():
    """Analyze memory usage of lists"""
    print("\n=== LIST MEMORY ANALYSIS ===\n")

    # Empty list
    empty_list = []
    print(f"Empty list size: {sys.getsizeof(empty_list)} bytes")

    # Lists with different sizes
    sizes = [10, 100, 1000, 10000]

    print("\nMemory usage by list size:")
    print(f"{'Elements':<10} {'Total Size':<12} {'Per Element':<12} {'Overhead':<10}")
    print("-" * 50)

    for size in sizes:
        test_list = list(range(size))
        total_size = sys.getsizeof(test_list)
        per_element = total_size / size if size > 0 else 0
        overhead = total_size - (size * sys.getsizeof(0))

        print(f"{size:<10} {total_size:<12} {per_element:<12.2f} {overhead:<10}")


def advanced_list_techniques():
    """Demonstrate advanced list techniques"""
    print("\n=== ADVANCED LIST TECHNIQUES ===\n")

    # List as stack (LIFO)
    print("1. List as Stack:")
    stack = []
    stack.append(1)  # Push
    stack.append(2)  # Push
    stack.append(3)  # Push
    print(f"   After pushes: {stack}")

    popped = stack.pop()  # Pop
    print(f"   After pop: {stack}, popped: {popped}")

    # List as queue (FIFO) - not efficient
    print("\n2. List as Queue (inefficient):")
    queue = []
    queue.append(1)  # Enqueue
    queue.append(2)  # Enqueue
    queue.append(3)  # Enqueue
    print(f"   After enqueues: {queue}")

    dequeued = queue.pop(0)  # Dequeue (O(n) operation!)
    print(f"   After dequeue: {queue}, dequeued: {dequeued}")

    # List flattening
    print("\n3. List Flattening:")
    nested = [[1, 2], [3, 4], [5, 6]]
    flattened = [item for sublist in nested for item in sublist]
    print(f"   Nested: {nested}")
    print(f"   Flattened: {flattened}")

    # List with mixed types
    print("\n4. Mixed Type Lists:")
    mixed = [1, "hello", 3.14, [1, 2, 3], {"key": "value"}]
    print(f"   Mixed list: {mixed}")
    print(f"   Types: {[type(item).__name__ for item in mixed]}")


if __name__ == "__main__":
    demonstrate_list_operations()
    print("\n" + "=" * 60 + "\n")
    list_performance_analysis()
    list_memory_analysis()
    advanced_list_techniques()
