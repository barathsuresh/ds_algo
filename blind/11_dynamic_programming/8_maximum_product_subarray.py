from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find a subarray that has the largest product, 
        and return the product.

        Example 1:
        Input: nums = [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.

        Example 2:
        Input: nums = [-2,0,-1]
        Output: 0
        Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
        """
        # Initialize result with the first number (in case array has only 1 element)
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            if n == 0:
                # Reset chains if we hit a zero, but 0 itself might be the max
                curMin, curMax = 1, 1
                continue
            
            # Store curMax temporarily because we are about to update it
            tmp = curMax * n
            
            # Calculate new Max and Min
            # We compare 3 values: 
            # 1. n (starting fresh)
            # 2. n * curMax (continuing a positive chain)
            # 3. n * curMin (flipping a negative chain)
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            
            res = max(res, curMax)
            
        return res

if __name__ == "__main__":
    solver = Solution()
    
    # Example: [-2, 3, -4]
    # i=-2: Max=-2, Min=-2
    # i=3:  Max=3,  Min=-6
    # i=-4: Max=24 (from -6 * -4), Min=-12
    nums = [-2, 3, -4]
    print(f"Max Product: {solver.maxProduct(nums)}")
    # Expected: 24