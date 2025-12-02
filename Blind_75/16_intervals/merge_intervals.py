from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        PROBLEM: Merge all overlapping intervals.
        """
        if not intervals:
            return []
        # 1. Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = []
        merged.append(intervals[0])
        # 2. Iterate and Merge
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            prev_interval = merged[-1]
            if current_interval[0] > prev_interval[1]:
                merged.append(current_interval)
            else:
                merged[-1] = [
                    prev_interval[0],
                    max(current_interval[1], prev_interval[1]),
                ]
        return merged


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 4]], [[0, 4]]),  # Unsorted input check
        ([[1, 4], [2, 3]], [[1, 4]]),  # One fully inside another
    ]

    for i, (intervals, expected) in enumerate(test_cases):
        # We pass a copy because the function sorts in-place
        result = solver.merge([x[:] for x in intervals])
        print(f"Test {i+1}: Input={intervals}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print("-" * 30)
