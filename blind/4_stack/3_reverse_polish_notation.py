from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.

        Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
        Note that division between two integers should truncate toward zero.

        Example 1:
        Input: tokens = ["2","1","+","3","*"]
        Output: 9
        Explanation: ((2 + 1) * 3) = 9

        Example 2:
        Input: tokens = ["4","13","5","/","+"]
        Output: 6
        Explanation: (4 + (13 / 5)) = 6

        Constraints:
        1 <= tokens.length <= 10^4
        tokens[i] is either an operator: "+", "-", "*", or "/", or an integer.
        """
        stack = []
        
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif t == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif t == "/":
                b = stack.pop()
                a = stack.pop()
                # In Python, // floors (rounds down), but we need to truncate toward zero.
                # int(a / b) achieves truncation toward zero.
                stack.append(int(a / b))
            
            else:
                # Token is a number
                stack.append(int(t))
                
        return stack[0]

if __name__ == "__main__":
    solver = Solution()
    
    # Test 1: (2 + 1) * 3
    t1 = ["2","1","+","3","*"]
    print(f"Input: {t1}")
    print(f"Output: {solver.evalRPN(t1)}") 
    # Expected: 9
    
    # Test 2: 4 + (13 / 5) -> 4 + 2 = 6
    t2 = ["4","13","5","/","+"]
    print(f"\nInput: {t2}")
    print(f"Output: {solver.evalRPN(t2)}")
    # Expected: 6