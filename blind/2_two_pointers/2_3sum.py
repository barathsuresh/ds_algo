from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.
        
        Example 1:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        """
        res = []
        nums.sort()  # Step 1: Sort the array to use Two Pointers
        
        for i, a in enumerate(nums):
            # Optimization: If the current number is > 0, we can't sum to 0
            # because the array is sorted (remaining numbers are also > 0).
            if a > 0:
                break
                
            # Skip duplicates for the first number
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Step 2: Standard Two Pointers on the remaining array
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                
                if threeSum > 0:
                    right -= 1  # Too big? Decrease the sum.
                elif threeSum < 0:
                    left += 1  # Too small? Increase the sum.
                else:
                    # Found a triplet!
                    res.append([a, nums[left], nums[right]])
                    
                    # Update pointers
                    left += 1
                    right -= 1
                    
                    # Critical Step: Skip duplicates for the second number
                    # (We don't need to check 'r' because checking 'l' implicitly handles it)
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res

if __name__ == "__main__":
    solver = Solution()
    print(f"Output: {solver.threeSum([-1,0,1,2,-1,-4])}")