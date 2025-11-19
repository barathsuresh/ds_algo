"""
Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
Example 1:
Input: nums = [1,2,3,1]
Output: true
Example 2:
Input: nums = [1,2,3,4]
Output: false
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List, Dict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
    
    def hasAnotherDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))