import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_freq = defaultdict(int)
        res = []
        for i in nums:
            count_freq[i] += 1
        for x,v in count_freq.items():
            heapq.heappush(res,(v,x))
            if len(res) > k:
                heapq.heappop(res)
        
        return [val for freq, val in res]