"""
Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Example 2:
Input: height = [1,1]
Output: 1
Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = width * min(heights[left], heights[right])

            max_area = max(max_area, current_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area