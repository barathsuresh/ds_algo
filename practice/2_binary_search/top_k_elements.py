from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        PROBLEM DESCRIPTION:
        Given an integer array nums and an integer k, return the kth largest element in the array.

        Note that it is the kth largest element in the sorted order, not the kth distinct element.

        Can you solve it without sorting?

        Example 1:
        Input: nums = [3,2,1,5,6,4], k = 2
        Output: 5

        Example 2:
        Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
        Output: 4
        """
        if nums == []:
            return -1
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        return heap[0]


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        result = solver.findKthLargest(nums, k)
        print(f"Test Case {i+1}: Output={result}, Expected={expected}")
        