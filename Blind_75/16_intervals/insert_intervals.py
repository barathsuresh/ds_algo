from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        PROBLEM DESCRIPTION:
        You are given an array of non-overlapping intervals `intervals` where intervals[i] = [start, end]
        represent the start and the end of the ith interval and intervals is sorted in ascending order by start.

        You are also given an interval `newInterval` = [start, end] that represents the start and end of another interval.

        Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by start
        and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

        Return intervals after the insertion.
        """
        if not intervals:
            intervals.append(newInterval)
            return intervals
        res = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1]),
            ]
            i += 1
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
        ([], [5, 7], [[5, 7]]),
        ([[1, 5]], [2, 3], [[1, 5]]),
        ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
    ]

    for i, (intervals, new_int, expected) in enumerate(test_cases):
        result = solver.insert(intervals, new_int)
        print(f"Test {i+1}: Input={intervals}, New={new_int}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print("-" * 30)