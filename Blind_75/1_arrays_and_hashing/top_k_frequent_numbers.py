from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Problem: Given an integer array nums and an integer k, return the k most
        frequent elements. You may return the answer in any order.

        Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

        Example 2:
        Input: nums = [1], k = 1
        Output: [1]
        """
        num_count = defaultdict(int)
        for i in nums:
            num_count[i] += 1
        sorted_items = sorted(num_count.items(), key=lambda item: item[1], reverse=True)
        items = [x[0] for x in sorted_items]
        return items[:k]

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


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        (
            [4, 4, 4, 1, 1, 2, 2, 3],
            2,
            [4, 1],
        ),  # Note: Order doesn't strictly matter for the problem
    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        result = solver.topKFrequentBucketSort(nums, k)
        print(f"Test Case {i+1}:")
        print(f"  Input: nums={nums}, k={k}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected} (or equivalent)")
        print("-" * 30)
