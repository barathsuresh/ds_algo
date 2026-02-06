from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
        Once you pay the cost, you can either climb one or two steps.

        You can either start from the step with index 0, or the step with index 1.
        Return the minimum cost to reach the top of the floor.

        Example 1:
        Input: cost = [10,15,20]
        Output: 15
        Explanation: Start at index 1 -> Pay 15 -> Top. Total 15.

        Example 2:
        Input: cost = [1,100,1,1,1,100,1,1,100,1]
        Output: 6
        """
        # dp[0] represents min cost to reach step n-2
        # dp[1] represents min cost to reach step n-1
        
        # We start looking at the step *after* the first two
        # The cost to reach index 0 is 0.
        # The cost to reach index 1 is 0.
        down_two = 0
        down_one = 0
        
        for i in range(2, len(cost) + 1):
            # To reach step 'i', we take the min of coming from i-1 or i-2
            # plus the cost we paid to leave those steps.
            temp = min(down_one + cost[i - 1], down_two + cost[i - 2])
            
            down_two = down_one
            down_one = temp
            
        return down_one

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    # Top is index 3.
    # Opt 1: 0 -> 2 (pay 10) -> Top (pay 20). Total 30.
    # Opt 2: 1 -> Top (pay 15). Total 15.
    cost = [10, 15, 20]
    print(f"Min Cost: {solver.minCostClimbingStairs(cost)}")
    # Expected: 15