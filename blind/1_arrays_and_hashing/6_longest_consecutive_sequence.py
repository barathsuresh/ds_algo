from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

        You must write an algorithm that runs in O(n) time.

        Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

        Example 2:
        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9

        Constraints:
        0 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
        """
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest


if __name__ == "__main__":
    solver = Solution()

    # Test Case 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print(f"Input: {nums1}")
    print(f"Output: {solver.longestConsecutive(nums1)}")
    # Expected: 4

    # Test Case 2 (Edge case: Empty or duplicates)
    nums2 = [0, 0]
    print(f"\nInput: {nums2}")
    print(f"Output: {solver.longestConsecutive(nums2)}")
    # Expected: 1
