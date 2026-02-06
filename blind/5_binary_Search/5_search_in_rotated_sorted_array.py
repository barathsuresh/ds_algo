from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
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

        Constraints:
        1 <= nums.length <= 5000
        -10^4 <= nums[i], target <= 10^4
        All values of nums are unique.
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the left portion is sorted
            if nums[l] <= nums[mid]:
                # If target is within the sorted left portion
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # Otherwise, the right portion must be sorted
            else:
                # If target is within the sorted right portion
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1

if __name__ == "__main__":
    solver = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(f"Input: nums={nums}, target={target}")
    print(f"Output: {solver.search(nums, target)}")
    # Expected: 4