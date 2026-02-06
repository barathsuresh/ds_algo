from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Given an array nums containing n distinct numbers in the range [0, n], 
        return the only number in the range that is missing from the array.

        Example 1:
        Input: nums = [3,0,1]
        Output: 2
        Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
        2 is the missing number in the range since it does not appear in nums.

        Example 2:
        Input: nums = [0,1]
        Output: 2
        Explanation: n = 2. 2 is missing.
        """
        # We initialize result with 'n' because the loop below 
        # only covers indices 0 to n-1. We need to include n in the XOR mix.
        res = len(nums)
        
        for i in range(len(nums)):
            # XOR the index 'i' with the value 'nums[i]'
            # Eventually, everything cancels out except the missing one.
            res = res ^ i ^ nums[i]
            
        return res

    # Alternative Math Solution (Also O(n))
    def missingNumberMath(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

if __name__ == "__main__":
    solver = Solution()
    
    # Expected: 0, 1, 2, 3
    # Actual:   3, 0, 1
    # XOR logic:
    # (0^0) ^ (1^1) ^ (3^3) ^ 2
    #  0    ^   0   ^   0   ^ 2 = 2
    nums = [3, 0, 1]
    print(f"Missing Number: {solver.missingNumber(nums)}")
    # Expected: 2