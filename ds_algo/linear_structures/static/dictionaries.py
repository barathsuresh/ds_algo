"""
Python Dictionaries - Hash Table Implementation and Analysis

This module demonstrates Python's built-in dictionary operations, their complexities,
hash table concepts, and advanced usage patterns.
"""

from typing import Dict, Any, List, Optional, Tuple
import sys
import time
from collections import defaultdict, OrderedDict, Counter


class DictionaryOperations:
    """Class demonstrating dictionary operations and their complexities"""

    def __init__(self):
        self.operations_count = 0

    def reset_counter(self):
        """Reset operations counter"""
        self.operations_count = 0

    def get_operations_count(self):
        """Get current operations count"""
        return self.operations_count

    # Basic Dictionary Operations - Average O(1)
    def create_dictionary(self, pairs: List[Tuple[Any, Any]]) -> Dict[Any, Any]:
        """
        Create dictionary from list of key-value pairs
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = {}
        for key, value in pairs:
            result[key] = value
            self.operations_count += 1
        return result

    def access_element(self, dictionary: Dict[Any, Any], key: Any) -> Any:
        """
        Access element by key
        Time Complexity: O(1) average, O(n) worst case
        Space Complexity: O(1)
        """
        self.operations_count += 1
        return dictionary.get(key)

    def insert_element(self, dictionary: Dict[Any, Any], key: Any, value: Any) -> None:
        """
        Insert or update key-value pair
        Time Complexity: O(1) average, O(n) worst case
        Space Complexity: O(1)
        """
        self.operations_count += 1
        dictionary[key] = value

    def delete_element(self, dictionary: Dict[Any, Any], key: Any) -> Any:
        """
        Delete element by key
        Time Complexity: O(1) average, O(n) worst case
        Space Complexity: O(1)
        """
        self.operations_count += 1
        if key in dictionary:
            return dictionary.pop(key)
        raise KeyError(f"Key '{key}' not found")

    def check_key_exists(self, dictionary: Dict[Any, Any], key: Any) -> bool:
        """
        Check if key exists in dictionary
        Time Complexity: O(1) average, O(n) worst case
        Space Complexity: O(1)
        """
        self.operations_count += 1
        return key in dictionary

    # Advanced Dictionary Operations
    def merge_dictionaries(
        self, dict1: Dict[Any, Any], dict2: Dict[Any, Any]
    ) -> Dict[Any, Any]:
        """
        Merge two dictionaries (dict2 overwrites dict1 for common keys)
        Time Complexity: O(n + m)
        Space Complexity: O(n + m)
        """
        result = dict1.copy()
        self.operations_count += len(dict1)

        for key, value in dict2.items():
            result[key] = value
            self.operations_count += 1

        return result

    def invert_dictionary(self, dictionary: Dict[Any, Any]) -> Dict[Any, Any]:
        """
        Create inverted dictionary (values become keys, keys become values)
        Time Complexity: O(n)
        Space Complexity: O(n)
        Note: Assumes values are hashable and unique
        """
        inverted = {}
        for key, value in dictionary.items():
            inverted[value] = key
            self.operations_count += 1
        return inverted

    def filter_dictionary(
        self, dictionary: Dict[Any, Any], condition_func
    ) -> Dict[Any, Any]:
        """
        Filter dictionary based on condition function
        Time Complexity: O(n)
        Space Complexity: O(k) where k is number of items that pass filter
        """
        filtered = {}
        for key, value in dictionary.items():
            self.operations_count += 1
            if condition_func(key, value):
                filtered[key] = value
        return filtered

    def sort_dictionary_by_keys(self, dictionary: Dict[Any, Any]) -> Dict[Any, Any]:
        """
        Sort dictionary by keys
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        sorted_items = sorted(dictionary.items())
        self.operations_count += len(dictionary) * max(1, len(dictionary).bit_length())
        return dict(sorted_items)

    def sort_dictionary_by_values(self, dictionary: Dict[Any, Any]) -> Dict[Any, Any]:
        """
        Sort dictionary by values
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        sorted_items = sorted(dictionary.items(), key=lambda item: item[1])
        self.operations_count += len(dictionary) * max(1, len(dictionary).bit_length())
        return dict(sorted_items)

    # Dictionary Traversal Operations
    def traverse_keys(self, dictionary: Dict[Any, Any]) -> List[Any]:
        """
        Traverse and collect all keys
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        keys = []
        for key in dictionary.keys():
            keys.append(key)
            self.operations_count += 1
        return keys

    def traverse_values(self, dictionary: Dict[Any, Any]) -> List[Any]:
        """
        Traverse and collect all values
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        values = []
        for value in dictionary.values():
            values.append(value)
            self.operations_count += 1
        return values

    def traverse_items(self, dictionary: Dict[Any, Any]) -> List[Tuple[Any, Any]]:
        """
        Traverse and collect all key-value pairs
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        items = []
        for key, value in dictionary.items():
            items.append((key, value))
            self.operations_count += 1
        return items

    # Set Operations on Dictionaries
    def dictionary_intersection(
        self, dict1: Dict[Any, Any], dict2: Dict[Any, Any]
    ) -> Dict[Any, Any]:
        """
        Find intersection of two dictionaries (common keys with values from dict1)
        Time Complexity: O(min(n, m))
        Space Complexity: O(min(n, m))
        """
        intersection = {}
        smaller_dict = dict1 if len(dict1) <= len(dict2) else dict2
        larger_dict = dict2 if smaller_dict is dict1 else dict1

        for key in smaller_dict:
            self.operations_count += 1
            if key in larger_dict:
                intersection[key] = dict1[key]  # Use value from dict1

        return intersection

    def dictionary_difference(
        self, dict1: Dict[Any, Any], dict2: Dict[Any, Any]
    ) -> Dict[Any, Any]:
        """
        Find difference of two dictionaries (keys in dict1 but not in dict2)
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        difference = {}
        for key, value in dict1.items():
            self.operations_count += 1
            if key not in dict2:
                difference[key] = value
        return difference


class SpecializedDictionaries:
    """Demonstrate specialized dictionary types"""

    @staticmethod
    def defaultdict_demo():
        """Demonstrate defaultdict usage"""
        print("DefaultDict Demo:")

        # Regular dict would raise KeyError
        dd = defaultdict(list)
        dd["fruits"].append("apple")
        dd["fruits"].append("banana")
        dd["vegetables"].append("carrot")

        print(f"   DefaultDict with lists: {dict(dd)}")

        # DefaultDict with int (for counting)
        counter = defaultdict(int)
        text = "hello world"
        for char in text:
            counter[char] += 1

        print(f"   Character count: {dict(counter)}")
        return dd, counter

    @staticmethod
    def ordereddict_demo():
        """Demonstrate OrderedDict (mostly historical, dicts are ordered in Python 3.7+)"""
        print("\nOrderedDict Demo:")

        od = OrderedDict()
        od["first"] = 1
        od["second"] = 2
        od["third"] = 3

        print(f"   OrderedDict: {od}")

        # Move to end
        od.move_to_end("first")
        print(f"   After move_to_end: {od}")

        return od

    @staticmethod
    def counter_demo():
        """Demonstrate Counter for counting hashable objects"""
        print("\nCounter Demo:")

        text = "hello world"
        char_counter = Counter(text)
        print(f"   Character counter: {char_counter}")

        # Most common
        print(f"   Most common 3: {char_counter.most_common(3)}")

        # Counter arithmetic
        counter1 = Counter(["a", "b", "c", "a"])
        counter2 = Counter(["a", "b", "b"])

        print(f"   Counter1: {counter1}")
        print(f"   Counter2: {counter2}")
        print(f"   Addition: {counter1 + counter2}")
        print(f"   Subtraction: {counter1 - counter2}")
        print(f"   Intersection: {counter1 & counter2}")
        print(f"   Union: {counter1 | counter2}")

        return char_counter, counter1, counter2


def demonstrate_dictionary_operations():
    """Demonstrate various dictionary operations"""
    print("=== PYTHON DICTIONARY OPERATIONS DEMONSTRATION ===\n")

    dict_ops = DictionaryOperations()

    # Create test dictionary
    pairs = [
        ("name", "John"),
        ("age", 30),
        ("city", "New York"),
        ("occupation", "Engineer"),
    ]
    test_dict = dict_ops.create_dictionary(pairs)

    print("1. BASIC DICTIONARY OPERATIONS:")
    print(f"   Created dictionary: {test_dict}")
    print(f"   Creation operations: {dict_ops.get_operations_count()}")

    # Access operations
    dict_ops.reset_counter()
    name = dict_ops.access_element(test_dict, "name")
    age = dict_ops.access_element(test_dict, "age")
    print(f"   Name: {name}, Age: {age}")
    print(f"   Access operations: {dict_ops.get_operations_count()}")

    # Insert operations
    dict_ops.reset_counter()
    dict_ops.insert_element(test_dict, "country", "USA")
    dict_ops.insert_element(test_dict, "age", 31)  # Update existing
    print(f"   After insertions: {test_dict}")
    print(f"   Insert operations: {dict_ops.get_operations_count()}\n")

    # Advanced operations
    print("2. ADVANCED DICTIONARY OPERATIONS:")

    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"b": 20, "d": 4, "e": 5}

    dict_ops.reset_counter()
    merged = dict_ops.merge_dictionaries(dict1, dict2)
    print(f"   Dict1: {dict1}")
    print(f"   Dict2: {dict2}")
    print(f"   Merged: {merged}")
    print(f"   Merge operations: {dict_ops.get_operations_count()}")

    dict_ops.reset_counter()
    filtered = dict_ops.filter_dictionary(test_dict, lambda k, v: isinstance(v, str))
    print(f"   Filtered (strings only): {filtered}")
    print(f"   Filter operations: {dict_ops.get_operations_count()}\n")


def dictionary_performance_analysis():
    """Analyze performance of dictionary operations"""
    print("=== DICTIONARY PERFORMANCE ANALYSIS ===\n")

    dict_ops = DictionaryOperations()
    sizes = [100, 1000, 10000]

    print("Performance analysis for different dictionary sizes:")
    print(f"{'Size':<8} {'Create':<10} {'Access':<10} {'Insert':<10} {'Delete':<10}")
    print("-" * 50)

    for size in sizes:
        # Create test data
        pairs = [(i, f"value_{i}") for i in range(size)]

        # Measure creation
        dict_ops.reset_counter()
        test_dict = dict_ops.create_dictionary(pairs)
        create_ops = dict_ops.get_operations_count()

        # Measure access
        dict_ops.reset_counter()
        value = dict_ops.access_element(test_dict, size // 2)
        access_ops = dict_ops.get_operations_count()

        # Measure insertion
        dict_ops.reset_counter()
        dict_ops.insert_element(test_dict, "new_key", "new_value")
        insert_ops = dict_ops.get_operations_count()

        # Measure deletion
        dict_ops.reset_counter()
        try:
            dict_ops.delete_element(test_dict, "new_key")
            delete_ops = dict_ops.get_operations_count()
        except KeyError:
            delete_ops = 1

        print(
            f"{size:<8} {create_ops:<10} {access_ops:<10} {insert_ops:<10} {delete_ops:<10}"
        )


def hash_collision_demonstration():
    """Demonstrate hash collisions and their effects"""
    print("\n=== HASH COLLISION DEMONSTRATION ===\n")

    print("Understanding Hash Collisions:")
    print("1. Hash function maps keys to bucket indices")
    print("2. Different keys can hash to same bucket (collision)")
    print("3. Python uses open addressing to resolve collisions\n")

    # Show hash values for different types
    test_keys = [1, "1", 1.0, True, (1,), frozenset([1])]

    print("Hash values for different key types:")
    print(f"{'Key':<15} {'Type':<15} {'Hash Value':<15}")
    print("-" * 45)
    for key in test_keys:
        try:
            hash_val = hash(key)
            print(f"{str(key):<15} {type(key).__name__:<15} {hash_val:<15}")
        except TypeError:
            print(f"{str(key):<15} {type(key).__name__:<15} {'Not hashable':<15}")

    print("\nNote: Some values have the same hash (1, 1.0, True)")
    print("This demonstrates potential hash collisions!")


def memory_analysis():
    """Analyze memory usage of dictionaries"""
    print("\n=== DICTIONARY MEMORY ANALYSIS ===\n")

    # Empty dictionary
    empty_dict = {}
    print(f"Empty dictionary size: {sys.getsizeof(empty_dict)} bytes")

    # Dictionaries with different sizes
    sizes = [10, 100, 1000, 10000]

    print("\nMemory usage by dictionary size:")
    print(
        f"{'Elements':<10} {'Total Size':<12} {'Per Element':<12} {'Load Factor':<12}"
    )
    print("-" * 50)

    for size in sizes:
        test_dict = {i: f"value_{i}" for i in range(size)}
        total_size = sys.getsizeof(test_dict)
        per_element = total_size / size if size > 0 else 0

        # Estimate load factor (simplified)
        # Python dicts resize when load factor > 2/3
        estimated_capacity = 2 ** (size - 1).bit_length()
        load_factor = size / estimated_capacity if estimated_capacity > 0 else 0

        print(f"{size:<10} {total_size:<12} {per_element:<12.2f} {load_factor:<12.3f}")


def practical_dictionary_examples():
    """Show practical examples of dictionary usage"""
    print("\n=== PRACTICAL DICTIONARY EXAMPLES ===\n")

    print("1. CACHING/MEMOIZATION:")
    cache = {}

    def fibonacci_cached(n):
        if n in cache:
            return cache[n]

        if n <= 1:
            result = n
        else:
            result = fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

        cache[n] = result
        return result

    print(f"   Fibonacci(10) = {fibonacci_cached(10)}")
    print(f"   Cache: {cache}")

    print("\n2. COUNTING/FREQUENCY:")
    text = "hello world hello python"
    word_count = {}

    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1

    print(f"   Text: '{text}'")
    print(f"   Word count: {word_count}")

    print("\n3. GROUPING DATA:")
    students = [
        {"name": "Alice", "grade": "A", "subject": "Math"},
        {"name": "Bob", "grade": "B", "subject": "Math"},
        {"name": "Charlie", "grade": "A", "subject": "Science"},
        {"name": "Diana", "grade": "B", "subject": "Science"},
    ]

    grouped_by_grade = {}
    for student in students:
        grade = student["grade"]
        if grade not in grouped_by_grade:
            grouped_by_grade[grade] = []
        grouped_by_grade[grade].append(student["name"])

    print(f"   Students grouped by grade: {grouped_by_grade}")

    print("\n4. CONFIGURATION/SETTINGS:")
    config = {
        "database": {"host": "localhost", "port": 5432, "name": "myapp"},
        "api": {"version": "1.0", "timeout": 30},
        "debug": True,
    }

    print(f"   Configuration: {config}")
    print(f"   Database host: {config['database']['host']}")


if __name__ == "__main__":
    demonstrate_dictionary_operations()
    print("\n" + "=" * 60 + "\n")
    dictionary_performance_analysis()
    hash_collision_demonstration()
    memory_analysis()
    practical_dictionary_examples()

    print("\n" + "=" * 60 + "\n")
    specialized = SpecializedDictionaries()
    specialized.defaultdict_demo()
    specialized.ordereddict_demo()
    specialized.counter_demo()
