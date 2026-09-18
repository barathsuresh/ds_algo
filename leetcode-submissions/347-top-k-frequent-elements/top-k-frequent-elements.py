import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # heap implementation 
        # count_freq = defaultdict(int)
        # res = []
        # for i in nums:
        #     count_freq[i] += 1
        # for x,v in count_freq.items():
        #     heapq.heappush(res,(v,x))
        #     if len(res) > k:
        #         heapq.heappop(res)
        
        # return [val for freq, val in res]

        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    def topKFrequentBucketSort(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(i)
                if len(res) == k:
                    return res