from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
        represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
        You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

        Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
        and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

        Example 1:
        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]

        Example 2:
        Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        Output: [[1,2],[3,10],[12,16]]
        Explanation: The new interval [4,8] overlaps with [3,5],[6,7],[8,10].
        """
        res = []
        
        for i in range(len(intervals)):
            # Unpack for clarity
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            new_start, new_end = newInterval[0], newInterval[1]
            
            # Case 1: New interval is strictly BEFORE current (No overlap)
            # Since the list is sorted, if new ends before curr starts, 
            # all subsequent intervals will also be after. We can return immediately.
            if new_end < curr_start:
                res.append(newInterval)
                return res + intervals[i:]
            
            # Case 2: New interval is strictly AFTER current (No overlap)
            # Current interval is safe to add.
            elif new_start > curr_end:
                res.append(intervals[i])
                
            # Case 3: Overlap
            # Merge intervals: update newInterval to encompass both
            else:
                newInterval = [
                    min(new_start, curr_start),
                    max(new_end, curr_end)
                ]
        
        # If we loop through everything without returning, the newInterval goes at the end
        res.append(newInterval)
        return res

if __name__ == "__main__":
    solver = Solution()
    
    # Example 2:
    # Existing: [1,2], [3,5], [6,7], [8,10], [12,16]
    # Insert: [4,8]
    # - [1,2] is left. Add.
    # - [3,5] overlaps. Merge -> [3, 8]
    # - [6,7] overlaps [3, 8]. Merge -> [3, 8]
    # - [8,10] overlaps [3, 8]. Merge -> [3, 10]
    # - [12,16] is right. Add [3, 10] then return rest.
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    
    print(f"Result: {solver.insert(intervals, newInterval)}")
    # Expected: [[1, 2], [3, 10], [12, 16]]