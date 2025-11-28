class Solution:
    def climbStairs(self, n: int) -> int:
        """
        PROBLEM DESCRIPTION:
        It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps.
        How many distinct ways can you climb to the top?
        """
        # The Notepad to store results {steps_left: number_of_ways}
        memo = {}

        def dp(steps_left):
            # TODO: Write the Top-Down Logic

            # 1. Base Cases
            # If steps_left is 0, we found a valid path (return 1).
            # If steps_left is negative, valid path (return 0).
            if steps_left == 0:
                return 1
            if steps_left < 0:
                return 0
            # 2. Check Memo (The "Notepad")
            # If we already calculated this 'steps_left', return the stored value.
            if steps_left in memo:
                return memo[steps_left]
            # 3. Recursive Step
            # Result = ways(steps - 1) + ways(steps - 2)
            res = dp(steps_left - 1) + dp(steps_left - 2)
            # 4. Save to Memo and Return
            memo[steps_left] = res
            return res

        return dp(n)
    
    def climbStairsBU(self, n: int) -> int:
        if n <= 2: return n
        
        prev = 1
        curr = 2
        
        for i in range(3, n + 1):
            # 1. Calculate the new step
            new_steps = prev + curr
            
            # 2. Shift our window forward
            prev = curr
            curr = new_steps
            
        return curr


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    print(f"Climb 2: Output={solver.climbStairsBU(2)}, Expected: 2")
    print(f"Climb 3: Output={solver.climbStairsBU(3)}, Expected: 3")
    print(f"Climb 5: Output={solver.climbStairsBU(5)}, Expected: 8")
    print(
        f"Climb 38: Output={solver.climbStairsBU(38)}, Expected: 63245986"
    )  # Large number test
