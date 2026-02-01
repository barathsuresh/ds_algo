from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Problem: Given n non-negative integers representing an elevation map where the width 
        of each bar is 1, compute how much water it can trap after raining.

        Example 1:
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6

        Example 2:
        Input: height = [4,2,0,3,2,5]
        Output: 9
        """
        


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([4, 2, 3], 1),
    ]

    for i, (inputs, expected) in enumerate(test_cases):
        result = solver.trap(inputs)
        print(f"Test Case {i+1}:")
        print(f"  Input: {inputs}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print("-" * 30)