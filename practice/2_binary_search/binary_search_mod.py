from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        PROBLEM DESCRIPTION:
        There is an integer array nums sorted in ascending order (with distinct values).
        Prior to being passed to your function, nums is possibly rotated at an unknown
        pivot index k (1 <= k < nums.length).

        Given the array nums after the possible rotation and an integer target,
        return the index of target if it is in nums, or -1 if it is not in nums.

        You must write an algorithm with O(log n) runtime complexity.

        Example 1:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4

        Example 2:
        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1

        Example 3:
        Input: nums = [1], target = 0
        Output: -1
        """
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1, 3], 3, 1),
        ([5, 1, 3], 5, 0),
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = solver.search(nums, target)
        print(f"Test Case {i+1}:")
        print(f"  Input: nums={nums}, target={target}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print("-" * 30)
