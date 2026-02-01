from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Problem: Find two numbers in a sorted array that add up to target.
        Return their 1-based indices.

        The solution must use only constant extra space.

        Example 1:
        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2] (2 + 7 = 9)

        Example 2:
        Input: numbers = [2,3,4], target = 6
        Output: [1,3] (2 + 4 = 6)
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            if current_sum < target:
                left += 1
            else:
                right -= 1
        return []


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = solver.twoSum(nums, target)
        print(f"Test Case {i+1}:")
        print(f"  Input: nums={nums}, target={target}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print("-" * 30)
