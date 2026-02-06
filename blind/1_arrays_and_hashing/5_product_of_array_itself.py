from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to
        the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.

        Example 1:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

        Example 2:
        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

        Constraints:
        2 <= nums.length <= 10^5
        -30 <= nums[i] <= 30
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

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(f"Input: {nums1}")
    print(f"Output: {solver.productExceptSelf(nums1)}")
    # Expected: [24, 12, 8, 6]

    # Test Case 2 (Zero handling)
    nums2 = [-1, 1, 0, -3, 3]
    print(f"\nInput: {nums2}")
    print(f"Output: {solver.productExceptSelf(nums2)}")
    # Expected: [0, 0, 9, 0, 0]
