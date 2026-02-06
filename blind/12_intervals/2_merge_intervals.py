from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
        and return an array of the non-overlapping intervals that cover all the intervals in the input.

        Example 1:
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

        Example 2:
        Input: intervals = [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.
        """
        # 1. Sort by start time. Critical step.
        intervals.sort(key=lambda x: x[0])
        
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            # Get the last interval we added to the output
            lastEnd = output[-1][1]
            
            # Check for overlap
            if start <= lastEnd:
                # Merge: Extend the end of the last interval
                output[-1][1] = max(lastEnd, end)
            else:
                # No overlap: Add the new interval
                output.append([start, end])
                
        return output

if __name__ == "__main__":
    solver = Solution()
    
    # Example: [[1,3],[2,6],[8,10],[15,18]]
    # 1. Sort -> Same.
    # 2. Start with [1,3].
    # 3. Next [2,6]. 2 <= 3. Merge -> [1, 6].
    # 4. Next [8,10]. 8 > 6. Add [1, 6] is done. New active: [8, 10].
    # 5. Next [15,18]. 15 > 10. Add [8, 10] is done. New active: [15, 18].
    # End.
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(f"Merged: {solver.merge(intervals)}")
    # Expected: [[1, 6], [8, 10], [15, 18]]