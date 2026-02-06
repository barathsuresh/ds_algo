from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
        return the minimum number of conference rooms required.

        Example 1:
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: 2
        Explanation:
        - At time 0: Meeting 1 starts. (Rooms: 1)
        - At time 5: Meeting 2 starts. Meeting 1 hasn't ended. (Rooms: 2)
        - At time 10: Meeting 2 ends. (Rooms: 1)
        - At time 15: Meeting 3 starts. (Rooms: 2)
        - At time 20: Meeting 3 ends. (Rooms: 1)
        - At time 30: Meeting 1 ends. (Rooms: 0)
        Peak was 2.

        Example 2:
        Input: intervals = [[7,10],[2,4]]
        Output: 1
        """
        if not intervals:
            return 0
            
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])
        
        s_ptr, e_ptr = 0, 0
        used_rooms = 0
        max_rooms = 0
        
        while s_ptr < len(intervals):
            # If a meeting starts before the earliest ending meeting finishes
            if start_times[s_ptr] < end_times[e_ptr]:
                used_rooms += 1
                s_ptr += 1
            else:
                # A meeting ended. One room becomes free.
                used_rooms -= 1
                e_ptr += 1
            
            max_rooms = max(max_rooms, used_rooms)
            
        return max_rooms

if __name__ == "__main__":
    solver = Solution()
    
    # Example: [[0,30],[5,10],[15,20]]
    # Starts: [0, 5, 15]
    # Ends:   [10, 20, 30]
    # 0 < 10 -> Rooms: 1
    # 5 < 10 -> Rooms: 2 (Peak)
    # 15 >= 10 -> Rooms: 1 (One ended)
    # 15 < 20 -> Rooms: 2 (New one started)
    print(f"Rooms needed: {solver.minMeetingRooms([[0,30],[5,10],[15,20]])}")
    # Expected: 2