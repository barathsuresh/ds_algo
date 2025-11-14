"""
Time Complexity Analysis and Examples

This module demonstrates different time complexities with practical examples
and explains Big O notation concepts with code implementations.
"""

import time
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Any


def constant_time_example(arr: List[Any]) -> Any:
    """
    O(1) - Constant Time Complexity
    Accessing first element regardless of array size
    """
    return arr[0] if arr else None


def linear_time_example(arr: List[Any], target: Any) -> int:
    """
    O(n) - Linear Time Complexity
    Linear search through array
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def quadratic_time_example(arr: List[int]) -> List[List[int]]:
    """
    O(n²) - Quadratic Time Complexity
    Nested loops to find all pairs
    """
    pairs = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append([arr[i], arr[j]])
    return pairs


def logarithmic_time_example(arr: List[int], target: int) -> int:
    """
    O(log n) - Logarithmic Time Complexity
    Binary search in sorted array
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def linearithmic_time_example(arr: List[int]) -> List[int]:
    """
    O(n log n) - Linearithmic Time Complexity
    Merge sort implementation
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = linearithmic_time_example(arr[:mid])
    right = linearithmic_time_example(arr[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Helper function for merge sort"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def exponential_time_example(n: int) -> int:
    """
    O(2^n) - Exponential Time Complexity
    Naive fibonacci implementation
    """
    if n <= 1:
        return n
    return exponential_time_example(n - 1) + exponential_time_example(n - 2)


def factorial_time_example(arr: List[Any]) -> List[List[Any]]:
    """
    O(n!) - Factorial Time Complexity
    Generate all permutations
    """
    if len(arr) <= 1:
        return [arr]

    permutations = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i + 1 :]
        for p in factorial_time_example(rest):
            permutations.append([arr[i]] + p)
    return permutations


def demonstrate_time_complexities():
    """Demonstrate different time complexities with timing measurements"""
    print("=== TIME COMPLEXITY DEMONSTRATIONS ===\n")

    # Test data
    small_array = list(range(100))
    medium_array = list(range(1000))
    large_array = list(range(10000))

    print("1. O(1) - Constant Time:")
    start = time.time()
    result = constant_time_example(large_array)
    end = time.time()
    print(f"   Result: {result}, Time: {end - start:.6f} seconds")

    print("\n2. O(log n) - Logarithmic Time:")
    start = time.time()
    result = logarithmic_time_example(large_array, 5000)
    end = time.time()
    print(f"   Found at index: {result}, Time: {end - start:.6f} seconds")

    print("\n3. O(n) - Linear Time:")
    start = time.time()
    result = linear_time_example(medium_array, 500)
    end = time.time()
    print(f"   Found at index: {result}, Time: {end - start:.6f} seconds")

    print("\n4. O(n log n) - Linearithmic Time:")
    test_array = [64, 34, 25, 12, 22, 11, 90]
    start = time.time()
    result = linearithmic_time_example(test_array)
    end = time.time()
    print(f"   Sorted: {result}, Time: {end - start:.6f} seconds")

    print("\n5. O(n²) - Quadratic Time:")
    small_test = list(range(50))
    start = time.time()
    pairs = quadratic_time_example(small_test)
    end = time.time()
    print(f"   Generated {len(pairs)} pairs, Time: {end - start:.6f} seconds")


if __name__ == "__main__":
    demonstrate_time_complexities()
