from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t not in "+-*/":
                # If it's not an operator, it MUST be a number.
                # int() handles both "11" and "-11" correctly.
                stack.append(int(t))
            else:
                # It is an operator. Pop last two.
                num_2 = stack.pop()
                num_1 = stack.pop()
                
                if t == "+":
                    stack.append(num_1 + num_2)
                elif t == "-":
                    stack.append(num_1 - num_2)
                elif t == "*":
                    stack.append(num_1 * num_2)
                elif t == "/":
                    # CRITICAL: Use int() casting for truncate-toward-zero
                    # instead of // which is floor division.
                    stack.append(int(num_1 / num_2))
                    
        return stack[0]

# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)
    ]

    for i, (tokens, expected) in enumerate(test_cases):
        result = solver.evalRPN(tokens)
        print(f"Test Case {i+1}:")
        print(f"  Input: {tokens}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print("-" * 30)