from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Given an array of intervals where intervals[i] = [starti, endi], return the minimum number of intervals 
        you need to remove to make the rest of the intervals non-overlapping.

        Example 1:
        Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
        Output: 1
        Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

        Example 2:
        Input: intervals = [[1,2],[1,2],[1,2]]
        Output: 2
        Explanation: You need to remove two [1,2] to make the rest non-overlapping.
        """
        if not intervals:
            return 0
            
        intervals.sort()
        
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            # Overlap Logic
            if start < prevEnd:
                res += 1
                # The Greedy Step:
                # We effectively "remove" the interval that ends later.
                # So we update prevEnd to be the MIN of the two.
                prevEnd = min(prevEnd, end)
            else:
                # No overlap, just move our pointer
                prevEnd = end
                
        return res

if __name__ == "__main__":
    solver = Solution()
    
    # Example: [[1,2], [2,3], [3,4], [1,3]]
    # Sorted:  [[1,2], [1,3], [2,3], [3,4]]
    # 1. Compare [1,2] and [1,3]. Overlap.
    #    Remove [1,3] (ends later). Keep [1,2]. Count = 1.
    # 2. Compare [1,2] and [2,3]. No overlap (2 is not < 2).
    #    prevEnd becomes 3.
    # 3. Compare [2,3] and [3,4]. No overlap.
    #    prevEnd becomes 4.
    # Total removed: 1
    intervals = [[1,2], [2,3], [3,4], [1,3]]
    print(f"Minimum removals: {solver.eraseOverlapIntervals(intervals)}")
    # Expected: 1