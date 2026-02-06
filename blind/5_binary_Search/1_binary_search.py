from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Given an array of integers nums which is sorted in ascending order, and an integer target, 
        write a function to search target in nums. If target exists, then return its index. 
        Otherwise, return -1.

        You must write an algorithm with O(log n) runtime complexity.

        Example 1:
        Input: nums = [-1,0,3,5,9,12], target = 9
        Output: 4
        Explanation: 9 exists in nums and its index is 4

        Example 2:
        Input: nums = [-1,0,3,5,9,12], target = 2
        Output: -1
        Explanation: 2 does not exist in nums so return -1

        Constraints:
        1 <= nums.length <= 10^4
        -10^4 <= nums[i], target <= 10^4
        All the integers in nums are unique.
        nums is sorted in ascending order.
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # Calculate mid (using l + (r-l)//2 prevents overflow in other languages,
            # though Python handles large integers automatically)
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                # Target is in the left half
                r = mid - 1
            
            else:
                # Target is in the right half
                l = mid + 1
        
        return -1

if __name__ == "__main__":
    solver = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(f"Input: nums={nums}, target={target}")
    print(f"Output: {solver.search(nums, target)}")
    # Expected: 4