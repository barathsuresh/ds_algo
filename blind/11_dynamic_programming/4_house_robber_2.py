from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. 
        Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
        That means the first house is the neighbor of the last one.

        Given an integer array nums representing the amount of money of each house, 
        return the maximum amount of money you can rob tonight without alerting the police.

        Example 1:
        Input: nums = [2,3,2]
        Output: 3
        Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), 
        because they are adjacent neighbors.

        Example 2:
        Input: nums = [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.
        """
        # Edge case: If there is only one house, rob it.
        if len(nums) == 1:
            return nums[0]

        # Helper function (identical to House Robber I)
        def rob_linear(houses):
            rob1, rob2 = 0, 0
            for n in houses:
                new_rob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2

        # Compare the two scenarios:
        # 1. Skip the last house (nums[:-1])
        # 2. Skip the first house (nums[1:])
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

if __name__ == "__main__":
    solver = Solution()
    
    # Circular arrangement: [2, 3, 2]
    # If linear: 2 + 2 = 4.
    # Because circular: Can't take both 2s. Max is 3 (the middle one).
    print(f"Max Loot: {solver.rob([2, 3, 2])}")
    # Expected: 3