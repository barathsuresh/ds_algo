from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly increasing subsequence.

        A subsequence is a sequence that can be derived from an array by deleting some or no elements 
        without changing the order of the remaining elements.

        Example 1:
        Input: nums = [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

        Example 2:
        Input: nums = [0,1,0,3,2,3]
        Output: 4
        """
        # Initialize DP array with 1 (each element is its own LIS of length 1)
        dp = [1] * len(nums)
        
        # Iterate through every element
        for i in range(len(nums)):
            # Check all previous elements
            for j in range(i):
                # If current number is larger than previous, we can extend that sequence
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        # The answer is the maximum value found in the entire DP array
        return max(dp) if nums else 0

if __name__ == "__main__":
    solver = Solution()
    
    # Sequence: [10, 9, 2, 5, 3, 7, 101, 18]
    # LIS ending at 5 is [2, 5] (len 2)
    # LIS ending at 7 is [2, 5, 7] or [2, 3, 7] (len 3)
    # LIS ending at 18 is [2, 3, 7, 18] (len 4)
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Length of LIS: {solver.lengthOfLIS(nums)}")
    # Expected: 4