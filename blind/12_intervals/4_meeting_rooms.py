from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Given an array of meeting time intervals where intervals[i] = [starti, endi], 
        determine if a person could attend all meetings.

        Example 1:
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: false
        Explanation: 0-30 overlaps with 5-10.

        Example 2:
        Input: intervals = [[7,10],[2,4]]
        Output: true
        Explanation: Sorted: [2,4], [7,10]. No overlap.
        """
        # 1. Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        # 2. Check adjacent pairs
        for i in range(len(intervals) - 1):
            current_end = intervals[i][1]
            next_start = intervals[i+1][0]
            
            # If the next meeting starts before the current one ends...
            if next_start < current_end:
                return False
                
        return True

if __name__ == "__main__":
    solver = Solution()
    
    # Overlap example
    intervals = [[0,30],[5,10],[15,20]]
    print(f"Can attend all? {solver.canAttendMeetings(intervals)}")
    # Expected: False