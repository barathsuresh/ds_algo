"""
Top K Frequent Numbers
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
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

import heapq
from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]

    def topKFrequentOpt(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for i in nums:
            count_map[i] += 1
        
        ele = []
        for num in count_map.keys():
            heapq.heappush(ele,(count_map[num],num))
            if len(ele) > k:
                heapq.heappop(ele)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(ele)[1])
        return res


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
