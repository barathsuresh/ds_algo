from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        PROBLEM DESCRIPTION:
        You are given an integer array coins representing coins of different denominations
        and an integer amount representing a total amount of money.

        Return the fewest number of coins that you need to make up that amount.
        If that amount of money cannot be made up by any combination of the coins, return -1.
        """
        # TODO: Write your Bottom-Up DP logic here
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1

    def coinChangeTD(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(rem):
            # 1. Base Cases
            if rem == 0: return 0           # Reached 0 exactly
            if rem < 0: return float('inf') # Overshot (Impossible)
            
            # 2. Check Memo
            if rem in memo:
                return memo[rem]
            
            # 3. Recursive Step: Try EVERY coin
            min_cost = float('inf')
            
            for c in coins:
                # Recurse: Cost is 1 (current coin) + cost for remainder
                res = dfs(rem - c)
                
                # Only update if the path was valid (not infinity)
                if res != float('inf'):
                    min_cost = min(min_cost, 1 + res)
            
            # 4. Save to Memo
            memo[rem] = min_cost
            return min_cost

        # Start the recursion with the full amount
        result = dfs(amount)
        
        # Convert 'inf' back to -1 if no solution found
        return result if result != float('inf') else -1
    
# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([1, 2, 5], 11, 3),  # 11 = 5 + 5 + 1
        ([2], 3, -1),  # Impossible
        ([1], 0, 0),  # 0 amount needs 0 coins
        ([186, 419, 83, 408], 6249, 20),  # Larger edge case
    ]

    for i, (coins, amount, expected) in enumerate(test_cases):
        result = solver.coinChangeTD(coins, amount)
        print(f"Test Case {i+1}:")
        print(f"  Input: coins={coins}, amount={amount}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print("-" * 30)
