from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        You are given an integer array coins representing coins of different denominations 
        and an integer amount representing a total amount of money.

        Return the fewest number of coins that you need to make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return -1.

        You may assume that you have an infinite number of each kind of coin.

        Example 1:
        Input: coins = [1,2,5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1

        Example 2:
        Input: coins = [2], amount = 3
        Output: -1
        """
        # Initialize DP array with a value higher than any possible solution
        # (amount + 1) is effectively infinity here
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins needed to make amount 0
        dp[0] = 0
        
        # Iterate through every amount from 1 to target
        for a in range(1, amount + 1):
            # Try every coin denomination
            for c in coins:
                if a - c >= 0:
                    # Update minimum: Current vs (1 coin + best way to make remainder)
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        # If dp[amount] is still the default value, we never found a solution
        return dp[amount] if dp[amount] != amount + 1 else -1

if __name__ == "__main__":
    solver = Solution()
    
    # Example: coins=[1, 2, 5], amount=11
    # dp[1] = 1 (1)
    # dp[2] = 1 (2)
    # ...
    # dp[5] = 1 (5)
    # ...
    # dp[11] = 3 (5+5+1)
    print(f"Min coins for 11: {solver.coinChange([1, 2, 5], 11)}")
    # Expected: 3