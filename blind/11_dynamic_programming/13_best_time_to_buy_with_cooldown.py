from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        Find the maximum profit you can achieve. You may complete as many transactions as you like 
        (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

        - After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

        Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock 
        before you buy again).

        Example 1:
        Input: prices = [1,2,3,0,2]
        Output: 3
        Explanation: transactions = [buy, sell, cooldown, buy, sell]
        """
        # Dictionary for caching state results
        # key: (index, buying_boolean) -> val: max_profit
        dp = {} 
        
        def dfs(i, buying):
            # Base Case: Out of bounds (cannot make any more profit)
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                # Choice 1: Buy (Pay price[i], move to i+1, state becomes 'selling')
                # Choice 2: Cooldown (Don't buy, stay in 'buying' state for next day)
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # Choice 1: Sell (Gain price[i], move to i+2 because of mandatory cooldown!)
                # Choice 2: Cooldown (Don't sell, keep holding)
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
                
            return dp[(i, buying)]
            
        return dfs(0, True)

if __name__ == "__main__":
    solver = Solution()
    
    # [1, 2, 3, 0, 2]
    # Buy at 1, Sell at 2 (profit 1) -> Cooldown at 3 -> Buy at 0 -> Sell at 2 (profit 2). Total 3.
    # BETTER: Buy at 1, Sell at 3 (profit 2) -> Cooldown at 0 -> Buy at ? (Can't buy at 0).
    # OPTIMAL: Buy 1, Sell 2 (profit 1), CD 3, Buy 0, Sell 2 (profit 2) = 3. 
    # WAIT: Buy 1, Sell 3 is profit 2. Wait at 0. End. Total 2.
    # The example explanation is: buy(1), sell(2), cd, buy(0), sell(2) -> -1 + 2 + 0 - 0 + 2 = 3.
    prices = [1, 2, 3, 0, 2]
    print(f"Max Profit: {solver.maxProfit(prices)}")
    # Expected: 3