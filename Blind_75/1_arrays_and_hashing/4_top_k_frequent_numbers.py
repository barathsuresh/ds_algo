from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements.
        You may return the answer in any order.

        Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

        Example 2:
        Input: nums = [1], k = 1
        Output: [1]

        Constraints:
        1 <= nums.length <= 10^5
        k is in the range [1, the number of unique elements in the array].
        It is guaranteed that the answer is unique.
        
        Follow up: Your algorithm's time complexity must be better than O(n log n), 
        where n is the array's size.
        """
        

if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard
    nums1 = [1,1,1,2,2,3]
    k1 = 2
    print(f"Input: nums={nums1}, k={k1}")
    print(f"Output: {solver.topKFrequent(nums1, k1)}")
    # Expected: [1, 2]

    # Test Case 2: Negative numbers
    nums2 = [4,4,4, -1, -1, 5]
    k2 = 2
    print(f"\nInput: nums={nums2}, k={k2}")
    print(f"Output: {solver.topKFrequent(nums2, k2)}")
    # Expected: [4, -1]