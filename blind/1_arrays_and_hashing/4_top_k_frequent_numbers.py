from typing import List
import heapq
from collections import defaultdict
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
        count_freq = defaultdict(int)
        res = []
        for i in nums:
            count_freq[i] += 1
        for x,v in enumerate(count_freq):
            heapq.heappush(res,(v,x))
            if len(res) > k:
                heapq.heappop(res)
        
        return [val for freq, val in res]
    
    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for n in nums:
            count[n] += 1

        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

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