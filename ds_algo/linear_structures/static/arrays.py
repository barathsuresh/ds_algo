"""
Arrays in Python - Comprehensive Implementation and Analysis

This module demonstrates array operations, their time complexities,
and practical usage patterns in Python.
"""

from typing import List, Any, Optional
import sys


class ArrayOperations:
    """Class demonstrating various array operations and their complexities"""

    def __init__(self):
        self.operations_count = 0

    def reset_counter(self):
        """Reset operations counter"""
        self.operations_count = 0

    def get_operations_count(self):
        """Get current operations count"""
        return self.operations_count

    # Basic Access Operations - O(1)
    def access_element(self, arr: List[Any], index: int) -> Any:
        """
        Access element at given index
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.operations_count += 1
        if 0 <= index < len(arr):
            return arr[index]
        raise IndexError(f"Index {index} out of range for array of size {len(arr)}")

    def update_element(self, arr: List[Any], index: int, value: Any) -> None:
        """
        Update element at given index
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.operations_count += 1
        if 0 <= index < len(arr):
            arr[index] = value
        else:
            raise IndexError(f"Index {index} out of range for array of size {len(arr)}")

    # Search Operations
    def linear_search(self, arr: List[Any], target: Any) -> int:
        """
        Linear search for target element
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i, element in enumerate(arr):
            self.operations_count += 1
            if element == target:
                return i
        return -1

    def binary_search(self, arr: List[Any], target: Any) -> int:
        """
        Binary search (requires sorted array)
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            self.operations_count += 1
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # Insertion Operations
    def insert_at_end(self, arr: List[Any], element: Any) -> None:
        """
        Insert element at end of array
        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        """
        self.operations_count += 1
        arr.append(element)

    def insert_at_index(self, arr: List[Any], index: int, element: Any) -> None:
        """
        Insert element at specific index
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self.operations_count += len(arr) - index  # Shifting operations
        arr.insert(index, element)

    def insert_at_beginning(self, arr: List[Any], element: Any) -> None:
        """
        Insert element at beginning of array
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self.operations_count += len(arr)  # All elements need to be shifted
        arr.insert(0, element)

    # Deletion Operations
    def delete_from_end(self, arr: List[Any]) -> Any:
        """
        Delete element from end of array
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not arr:
            raise IndexError("Cannot delete from empty array")
        self.operations_count += 1
        return arr.pop()

    def delete_from_index(self, arr: List[Any], index: int) -> Any:
        """
        Delete element from specific index
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not (0 <= index < len(arr)):
            raise IndexError(f"Index {index} out of range")

        self.operations_count += len(arr) - index  # Shifting operations
        return arr.pop(index)

    def delete_from_beginning(self, arr: List[Any]) -> Any:
        """
        Delete element from beginning of array
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not arr:
            raise IndexError("Cannot delete from empty array")

        self.operations_count += len(arr) - 1  # All remaining elements shift
        return arr.pop(0)

    # Traversal Operations
    def traverse_forward(self, arr: List[Any]) -> List[Any]:
        """
        Traverse array from start to end
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = []
        for element in arr:
            self.operations_count += 1
            result.append(element)
        return result

    def traverse_backward(self, arr: List[Any]) -> List[Any]:
        """
        Traverse array from end to start
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = []
        for i in range(len(arr) - 1, -1, -1):
            self.operations_count += 1
            result.append(arr[i])
        return result

    # Utility Operations
    def find_minimum(self, arr: List[int]) -> Optional[int]:
        """
        Find minimum element in array
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not arr:
            return None

        min_element = arr[0]
        for element in arr[1:]:
            self.operations_count += 1
            if element < min_element:
                min_element = element
        return min_element

    def find_maximum(self, arr: List[int]) -> Optional[int]:
        """
        Find maximum element in array
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not arr:
            return None

        max_element = arr[0]
        for element in arr[1:]:
            self.operations_count += 1
            if element > max_element:
                max_element = element
        return max_element

    def calculate_sum(self, arr: List[int]) -> int:
        """
        Calculate sum of all elements
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        total = 0
        for element in arr:
            self.operations_count += 1
            total += element
        return total

    def reverse_array(self, arr: List[Any]) -> None:
        """
        Reverse array in-place
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1
        while left < right:
            self.operations_count += 1
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


def demonstrate_array_operations():
    """Demonstrate various array operations with examples"""
    print("=== ARRAY OPERATIONS DEMONSTRATION ===\n")

    arr_ops = ArrayOperations()
    test_array = [10, 20, 30, 40, 50]

    print(f"Initial array: {test_array}\n")

    # Access operations
    print("1. ACCESS OPERATIONS (O(1)):")
    arr_ops.reset_counter()
    element = arr_ops.access_element(test_array, 2)
    print(f"   Element at index 2: {element}")
    print(f"   Operations: {arr_ops.get_operations_count()}\n")

    # Search operations
    print("2. SEARCH OPERATIONS:")
    arr_ops.reset_counter()
    index = arr_ops.linear_search(test_array, 30)
    linear_ops = arr_ops.get_operations_count()
    print(f"   Linear search for 30: found at index {index}")
    print(f"   Linear search operations: {linear_ops}")

    arr_ops.reset_counter()
    sorted_array = [10, 20, 30, 40, 50]
    index = arr_ops.binary_search(sorted_array, 30)
    binary_ops = arr_ops.get_operations_count()
    print(f"   Binary search for 30: found at index {index}")
    print(f"   Binary search operations: {binary_ops}\n")

    # Insertion operations
    print("3. INSERTION OPERATIONS:")
    test_array_copy = test_array.copy()
    arr_ops.reset_counter()
    arr_ops.insert_at_end(test_array_copy, 60)
    print(f"   After inserting 60 at end: {test_array_copy}")
    print(f"   Operations: {arr_ops.get_operations_count()}")

    test_array_copy = test_array.copy()
    arr_ops.reset_counter()
    arr_ops.insert_at_index(test_array_copy, 2, 25)
    print(f"   After inserting 25 at index 2: {test_array_copy}")
    print(f"   Operations: {arr_ops.get_operations_count()}\n")

    # Deletion operations
    print("4. DELETION OPERATIONS:")
    test_array_copy = test_array.copy()
    arr_ops.reset_counter()
    deleted = arr_ops.delete_from_end(test_array_copy)
    print(f"   After deleting from end: {test_array_copy}")
    print(f"   Deleted element: {deleted}")
    print(f"   Operations: {arr_ops.get_operations_count()}")

    test_array_copy = test_array.copy()
    arr_ops.reset_counter()
    deleted = arr_ops.delete_from_index(test_array_copy, 2)
    print(f"   After deleting from index 2: {test_array_copy}")
    print(f"   Deleted element: {deleted}")
    print(f"   Operations: {arr_ops.get_operations_count()}\n")


def array_complexity_analysis():
    """Analyze time complexities of array operations"""
    print("=== ARRAY OPERATIONS TIME COMPLEXITY ===\n")

    complexities = [
        ("Access by Index", "O(1)", "Direct memory access"),
        ("Update by Index", "O(1)", "Direct memory access"),
        ("Insert at End", "O(1)*", "Amortized, may need resizing"),
        ("Insert at Index", "O(n)", "Need to shift elements"),
        ("Insert at Beginning", "O(n)", "Need to shift all elements"),
        ("Delete from End", "O(1)", "No shifting required"),
        ("Delete from Index", "O(n)", "Need to shift elements"),
        ("Delete from Beginning", "O(n)", "Need to shift all elements"),
        ("Linear Search", "O(n)", "May need to check all elements"),
        ("Binary Search", "O(log n)", "Only for sorted arrays"),
        ("Find Min/Max", "O(n)", "Need to check all elements"),
        ("Traverse", "O(n)", "Visit all elements"),
        ("Reverse", "O(n)", "Swap n/2 pairs"),
    ]

    print(f"{'Operation':<20} {'Time Complexity':<15} {'Notes':<30}")
    print("-" * 70)
    for operation, complexity, notes in complexities:
        print(f"{operation:<20} {complexity:<15} {notes:<30}")


def memory_efficiency_analysis():
    """Analyze memory usage of different array operations"""
    print("\n=== ARRAY MEMORY EFFICIENCY ===\n")

    # Create arrays of different sizes
    small_array = list(range(100))
    medium_array = list(range(1000))
    large_array = list(range(10000))

    print("Memory usage analysis:")
    print(f"Small array (100 elements): {sys.getsizeof(small_array)} bytes")
    print(f"Medium array (1000 elements): {sys.getsizeof(medium_array)} bytes")
    print(f"Large array (10000 elements): {sys.getsizeof(large_array)} bytes")

    # Calculate bytes per element
    small_per_element = sys.getsizeof(small_array) / len(small_array)
    medium_per_element = sys.getsizeof(medium_array) / len(medium_array)
    large_per_element = sys.getsizeof(large_array) / len(large_array)

    print(f"\nBytes per element:")
    print(f"Small array: {small_per_element:.2f} bytes/element")
    print(f"Medium array: {medium_per_element:.2f} bytes/element")
    print(f"Large array: {large_per_element:.2f} bytes/element")


if __name__ == "__main__":
    demonstrate_array_operations()
    print("\n" + "=" * 50 + "\n")
    array_complexity_analysis()
    memory_efficiency_analysis()
