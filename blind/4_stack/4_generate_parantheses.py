from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Given n pairs of parentheses, write a function to generate all combinations 
        of well-formed parentheses.

        Example 1:
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]

        Example 2:
        Input: n = 1
        Output: ["()"]

        Constraints:
        1 <= n <= 8
        """
        stack = []
        res = []
        
        def backtrack(openN, closedN):
            # Base Case: Valid combination found
            if openN == n and closedN == n:
                res.append("".join(stack))
                return
            
            # Decision 1: Add Open Parenthesis
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() # Backtrack (cleanup)
                
            # Decision 2: Add Closed Parenthesis
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop() # Backtrack (cleanup)
                
        backtrack(0, 0)
        return res

if __name__ == "__main__":
    solver = Solution()
    n = 3
    print(f"Input: n={n}")
    print(f"Output: {solver.generateParenthesis(n)}")