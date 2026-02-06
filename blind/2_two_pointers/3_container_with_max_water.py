from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        You are given an integer array height of length n. 
        Find two lines that together with the x-axis form a container, 
        such that the container contains the most water.
        
        Example 1:
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The max area is between index 1 (height 8) and index 8 (height 7).
        Width = 8 - 1 = 7. Height = min(8, 7) = 7. Area = 7 * 7 = 49.

        Example 2:
        Input: height = [1,1]
        Output: 1
        """
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            # Calculate current area
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            
            # Greedy Strategy: Move the shorter line inward
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res

if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1
    h1 = [1,8,6,2,5,4,8,3,7]
    print(f"Input: {h1}")
    print(f"Output: {solver.maxArea(h1)}")
    # Expected: 49