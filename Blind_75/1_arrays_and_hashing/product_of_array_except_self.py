from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Problem: Given an integer array nums, return an array answer such that answer[i]
        is equal to the product of all the elements of nums except nums[i].

        The algorithm must run in O(n) time and without using the division operation.

        Example 1:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

        Example 2:
        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]
        """
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([0, 0], [0, 0]),
    ]

    for i, (inputs, expected) in enumerate(test_cases):
        result = solver.productExceptSelf(inputs)
        print(f"Test Case {i+1}:")
        print(f"  Input: {inputs}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print("-" * 30)
