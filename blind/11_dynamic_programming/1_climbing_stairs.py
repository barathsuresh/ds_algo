class Solution:
    def climbStairs(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. 
        In how many distinct ways can you climb to the top?

        Example 1:
        Input: n = 2
        Output: 2
        Explanation: (1+1), (2)

        Example 2:
        Input: n = 3
        Output: 3
        Explanation: (1+1+1), (1+2), (2+1)
        """
        if n <= 2:
            return n
        
        # Base cases
        # one_step_before represents ways to reach n-1
        # two_steps_before represents ways to reach n-2
        one_step_before = 2
        two_steps_before = 1
        
        for i in range(3, n + 1):
            # Calculate current steps
            current = one_step_before + two_steps_before
            
            # Shift variables for next iteration
            two_steps_before = one_step_before
            one_step_before = current
            
        return one_step_before

if __name__ == "__main__":
    solver = Solution()
    n = 5
    # Sequence: 1, 2, 3, 5, 8...
    print(f"Ways to climb {n} stairs: {solver.climbStairs(n)}")
    # Expected: 8