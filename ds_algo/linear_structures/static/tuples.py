"""
Python Tuples - Immutable Sequence Implementation and Analysis

This module demonstrates Python's built-in tuple operations, their complexities,
immutability concepts, and usage patterns as immutable sequences.
"""

from typing import Tuple, Any, List, Optional, Union
import sys
import time


class TupleOperations:
    """Class demonstrating tuple operations and their complexities"""

    def __init__(self):
        self.operations_count = 0

    def reset_counter(self):
        """Reset operations counter"""
        self.operations_count = 0

    def get_operations_count(self):
        """Get current operations count"""
        return self.operations_count

    # Tuple Creation Operations
    def create_empty_tuple(self) -> Tuple:
        """
        Create an empty tuple
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.operations_count += 1
        return ()

    def create_single_element_tuple(self, element: Any) -> Tuple[Any]:
        """
        Create tuple with single element (note the comma!)
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.operations_count += 1
        return (element,)  # Comma is essential!

    def create_tuple_from_iterable(self, iterable) -> Tuple:
        """
        Create tuple from any iterable
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = tuple(iterable)
        self.operations_count += len(result)
        return result

    def create_tuple_literal(self, *args) -> Tuple:
        """
        Create tuple using literal syntax
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        self.operations_count += len(args)
        return args

    # Access Operations - O(1)
    def access_element(self, tup: Tuple, index: int) -> Any:
        """
        Access element at given index
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.operations_count += 1
        if -len(tup) <= index < len(tup):
            return tup[index]
        raise IndexError(f"Index {index} out of range for tuple of length {len(tup)}")

    def access_multiple_elements(self, tup: Tuple, indices: List[int]) -> List[Any]:
        """
        Access multiple elements by indices
        Time Complexity: O(k) where k is number of indices
        Space Complexity: O(k)
        """
        result = []
        for index in indices:
            self.operations_count += 1
            result.append(tup[index])
        return result

    # Slicing Operations
    def slice_tuple(
        self, tup: Tuple, start: int = None, end: int = None, step: int = None
    ) -> Tuple:
        """
        Slice tuple to create new tuple
        Time Complexity: O(k) where k is slice size
        Space Complexity: O(k)
        """
        result = tup[start:end:step]
        self.operations_count += len(result)
        return result

    def reverse_tuple(self, tup: Tuple) -> Tuple:
        """
        Reverse tuple using slicing
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = tup[::-1]
        self.operations_count += len(result)
        return result

    # Search Operations
    def find_element(self, tup: Tuple, target: Any) -> int:
        """
        Find first occurrence of element
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i, element in enumerate(tup):
            self.operations_count += 1
            if element == target:
                return i
        return -1

    def count_occurrences(self, tup: Tuple, element: Any) -> int:
        """
        Count occurrences of element
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count = 0
        for item in tup:
            self.operations_count += 1
            if item == element:
                count += 1
        return count

    def check_membership(self, tup: Tuple, element: Any) -> bool:
        """
        Check if element exists in tuple
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for item in tup:
            self.operations_count += 1
            if item == element:
                return True
        return False

    # Tuple Concatenation and Repetition
    def concatenate_tuples(self, tup1: Tuple, tup2: Tuple) -> Tuple:
        """
        Concatenate two tuples
        Time Complexity: O(n + m)
        Space Complexity: O(n + m)
        """
        result = tup1 + tup2
        self.operations_count += len(result)
        return result

    def repeat_tuple(self, tup: Tuple, times: int) -> Tuple:
        """
        Repeat tuple n times
        Time Complexity: O(n * times)
        Space Complexity: O(n * times)
        """
        result = tup * times
        self.operations_count += len(result)
        return result

    # Comparison Operations
    def compare_tuples(self, tup1: Tuple, tup2: Tuple) -> dict:
        """
        Compare tuples lexicographically
        Time Complexity: O(min(n, m))
        Space Complexity: O(1)
        """
        self.operations_count += min(len(tup1), len(tup2))

        return {
            "equal": tup1 == tup2,
            "not_equal": tup1 != tup2,
            "less_than": tup1 < tup2,
            "less_equal": tup1 <= tup2,
            "greater_than": tup1 > tup2,
            "greater_equal": tup1 >= tup2,
        }

    # Tuple Conversion Operations
    def tuple_to_list(self, tup: Tuple) -> List[Any]:
        """
        Convert tuple to list
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = list(tup)
        self.operations_count += len(result)
        return result

    def list_to_tuple(self, lst: List[Any]) -> Tuple:
        """
        Convert list to tuple
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = tuple(lst)
        self.operations_count += len(result)
        return result

    # Advanced Tuple Operations
    def find_min_max(self, tup: Tuple[Union[int, float]]) -> Tuple[Any, Any]:
        """
        Find minimum and maximum elements
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not tup:
            return None, None

        min_val = max_val = tup[0]
        for element in tup[1:]:
            self.operations_count += 1
            if element < min_val:
                min_val = element
            if element > max_val:
                max_val = element

        return min_val, max_val

    def calculate_sum(self, tup: Tuple[Union[int, float]]) -> Union[int, float]:
        """
        Calculate sum of numeric tuple
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        total = 0
        for element in tup:
            self.operations_count += 1
            total += element
        return total


class NamedTupleDemo:
    """Demonstrate named tuples functionality"""

    @staticmethod
    def basic_named_tuple():
        """Demonstrate basic named tuple usage"""
        from collections import namedtuple

        print("Named Tuple Demo:")

        # Define a named tuple
        Person = namedtuple("Person", ["name", "age", "city"])

        # Create instances
        person1 = Person("Alice", 30, "New York")
        person2 = Person("Bob", 25, "San Francisco")

        print(f"   Person 1: {person1}")
        print(f"   Name: {person1.name}, Age: {person1.age}")

        # Named tuples are immutable
        try:
            person1.age = 31
        except AttributeError as e:
            print(f"   Immutability error: {e}")

        # Converting to dict
        person_dict = person1._asdict()
        print(f"   As dict: {person_dict}")

        return Person, person1, person2

    @staticmethod
    def advanced_named_tuple():
        """Demonstrate advanced named tuple features"""
        from collections import namedtuple

        print("\nAdvanced Named Tuple Features:")

        # With defaults (Python 3.7+)
        Point = namedtuple("Point", ["x", "y", "z"], defaults=[0, 0, 0])

        point1 = Point(1, 2)  # z defaults to 0
        point2 = Point(1, 2, 3)

        print(f"   Point with defaults: {point1}")
        print(f"   Full point: {point2}")

        # Using _replace to create modified copy
        point3 = point1._replace(z=5)
        print(f"   After _replace: {point3}")

        # Field information
        print(f"   Fields: {Point._fields}")
        print(f"   Defaults: {Point._field_defaults}")

        return Point, point1, point2, point3


def demonstrate_tuple_operations():
    """Demonstrate various tuple operations"""
    print("=== PYTHON TUPLE OPERATIONS DEMONSTRATION ===\n")

    tuple_ops = TupleOperations()

    # Tuple creation
    print("1. TUPLE CREATION:")
    empty_tup = tuple_ops.create_empty_tuple()
    single_tup = tuple_ops.create_single_element_tuple(42)
    from_list = tuple_ops.create_tuple_from_iterable([1, 2, 3, 4, 5])
    literal_tup = tuple_ops.create_tuple_literal(10, 20, 30, 40)

    print(f"   Empty tuple: {empty_tup}")
    print(f"   Single element: {single_tup}")
    print(f"   From list: {from_list}")
    print(f"   Literal: {literal_tup}")
    print(f"   Creation operations: {tuple_ops.get_operations_count()}\n")

    # Access operations
    print("2. ACCESS OPERATIONS:")
    test_tuple = (10, 20, 30, 40, 50)
    tuple_ops.reset_counter()

    first = tuple_ops.access_element(test_tuple, 0)
    last = tuple_ops.access_element(test_tuple, -1)
    multiple = tuple_ops.access_multiple_elements(test_tuple, [1, 3])

    print(f"   Test tuple: {test_tuple}")
    print(f"   First element: {first}")
    print(f"   Last element: {last}")
    print(f"   Elements at indices [1, 3]: {multiple}")
    print(f"   Access operations: {tuple_ops.get_operations_count()}\n")

    # Slicing operations
    print("3. SLICING OPERATIONS:")
    tuple_ops.reset_counter()

    first_three = tuple_ops.slice_tuple(test_tuple, 0, 3)
    last_two = tuple_ops.slice_tuple(test_tuple, -2)
    reversed_tup = tuple_ops.reverse_tuple(test_tuple)
    every_other = tuple_ops.slice_tuple(test_tuple, None, None, 2)

    print(f"   Original: {test_tuple}")
    print(f"   First three: {first_three}")
    print(f"   Last two: {last_two}")
    print(f"   Reversed: {reversed_tup}")
    print(f"   Every other: {every_other}")
    print(f"   Slicing operations: {tuple_ops.get_operations_count()}\n")

    # Concatenation and repetition
    print("4. CONCATENATION AND REPETITION:")
    tuple_ops.reset_counter()

    tup1 = (1, 2, 3)
    tup2 = (4, 5, 6)
    concatenated = tuple_ops.concatenate_tuples(tup1, tup2)
    repeated = tuple_ops.repeat_tuple((1, 2), 3)

    print(f"   Tuple 1: {tup1}")
    print(f"   Tuple 2: {tup2}")
    print(f"   Concatenated: {concatenated}")
    print(f"   (1, 2) repeated 3 times: {repeated}")
    print(f"   Operations: {tuple_ops.get_operations_count()}\n")


def tuple_immutability_demo():
    """Demonstrate tuple immutability concepts"""
    print("=== TUPLE IMMUTABILITY DEMONSTRATION ===\n")

    print("1. BASIC IMMUTABILITY:")
    test_tuple = (1, 2, 3)
    print(f"   Original tuple: {test_tuple}")

    try:
        test_tuple[0] = 10
    except TypeError as e:
        print(f"   Cannot modify: {e}")

    # But you can reassign the variable
    test_tuple = (10, 20, 30)
    print(f"   After reassignment: {test_tuple}")

    print("\n2. IMMUTABILITY WITH MUTABLE OBJECTS:")
    # Tuples themselves are immutable, but can contain mutable objects
    mutable_content = ([1, 2], [3, 4])
    print(f"   Tuple with lists: {mutable_content}")

    # Can't change tuple structure
    try:
        mutable_content[0] = [10, 20]
    except TypeError as e:
        print(f"   Cannot replace list: {e}")

    # But can modify the mutable objects inside
    mutable_content[0].append(100)
    print(f"   After modifying inner list: {mutable_content}")

    print("\n3. TUPLE AS DICTIONARY KEY:")
    # Tuples can be dictionary keys if all elements are hashable
    point_values = {}
    point_values[(0, 0)] = "origin"
    point_values[(1, 1)] = "diagonal"
    point_values[(0, 1)] = "y-axis"

    print(f"   Point dictionary: {point_values}")
    print(f"   Value at (0, 0): {point_values[(0, 0)]}")

    # This would fail with unhashable type
    try:
        bad_key = ([1, 2], [3, 4])
        point_values[bad_key] = "bad"
    except TypeError as e:
        print(f"   Cannot use tuple with lists as key: {e}")


def tuple_performance_analysis():
    """Analyze performance of tuple operations"""
    print("\n=== TUPLE PERFORMANCE ANALYSIS ===\n")

    tuple_ops = TupleOperations()
    sizes = [100, 1000, 10000]

    print("Performance analysis for different tuple sizes:")
    print(f"{'Size':<8} {'Create':<10} {'Access':<10} {'Search':<10} {'Slice':<10}")
    print("-" * 50)

    for size in sizes:
        # Create test data
        test_data = list(range(size))

        # Measure creation
        tuple_ops.reset_counter()
        test_tuple = tuple_ops.create_tuple_from_iterable(test_data)
        create_ops = tuple_ops.get_operations_count()

        # Measure access
        tuple_ops.reset_counter()
        element = tuple_ops.access_element(test_tuple, size // 2)
        access_ops = tuple_ops.get_operations_count()

        # Measure search
        tuple_ops.reset_counter()
        found = tuple_ops.find_element(test_tuple, size // 2)
        search_ops = tuple_ops.get_operations_count()

        # Measure slicing
        tuple_ops.reset_counter()
        slice_result = tuple_ops.slice_tuple(test_tuple, size // 4, 3 * size // 4)
        slice_ops = tuple_ops.get_operations_count()

        print(
            f"{size:<8} {create_ops:<10} {access_ops:<10} {search_ops:<10} {slice_ops:<10}"
        )


def memory_comparison():
    """Compare memory usage of tuples vs lists"""
    print("\n=== TUPLE VS LIST MEMORY COMPARISON ===\n")

    sizes = [10, 100, 1000, 10000]

    print("Memory usage comparison (Tuple vs List):")
    print(f"{'Size':<8} {'Tuple':<12} {'List':<12} {'Difference':<12} {'Ratio':<10}")
    print("-" * 55)

    for size in sizes:
        data = list(range(size))

        test_tuple = tuple(data)
        test_list = list(data)

        tuple_size = sys.getsizeof(test_tuple)
        list_size = sys.getsizeof(test_list)
        difference = list_size - tuple_size
        ratio = list_size / tuple_size if tuple_size > 0 else 0

        print(
            f"{size:<8} {tuple_size:<12} {list_size:<12} {difference:<12} {ratio:<10.2f}"
        )


def practical_tuple_examples():
    """Show practical examples of tuple usage"""
    print("\n=== PRACTICAL TUPLE EXAMPLES ===\n")

    print("1. RETURNING MULTIPLE VALUES:")

    def get_name_age():
        return "Alice", 25  # Returns a tuple

    name, age = get_name_age()  # Tuple unpacking
    print(f"   Name: {name}, Age: {age}")

    print("\n2. COORDINATES/POINTS:")
    points = [(0, 0), (1, 1), (2, 4), (3, 9)]
    print(f"   Points: {points}")

    # Calculate distances from origin
    distances = [((x**2 + y**2) ** 0.5) for x, y in points]
    print(f"   Distances from origin: {[round(d, 2) for d in distances]}")

    print("\n3. CONFIGURATION TUPLES:")
    # RGB color tuples
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    colors = {"red": RED, "green": GREEN, "blue": BLUE}
    print(f"   Color definitions: {colors}")

    print("\n4. DATABASE RECORDS:")
    # Simulating database rows as tuples
    employees = [
        (1, "Alice", "Engineering", 75000),
        (2, "Bob", "Marketing", 65000),
        (3, "Charlie", "Sales", 60000),
    ]

    print("   Employee records:")
    for emp_id, name, dept, salary in employees:
        print(f"      ID: {emp_id}, Name: {name}, Dept: {dept}, Salary: ${salary}")

    print("\n5. ENUMERATION:")
    fruits = ["apple", "banana", "orange"]
    for index, fruit in enumerate(fruits):
        print(f"      {index}: {fruit}")


if __name__ == "__main__":
    demonstrate_tuple_operations()
    tuple_immutability_demo()
    tuple_performance_analysis()
    memory_comparison()
    practical_tuple_examples()

    print("\n" + "=" * 60 + "\n")
    named_tuple_demo = NamedTupleDemo()
    named_tuple_demo.basic_named_tuple()
    named_tuple_demo.advanced_named_tuple()
