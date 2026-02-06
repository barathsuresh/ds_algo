class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
        determine if the input string is valid.

        An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.

        Example 1:
        Input: s = "()"
        Output: true

        Example 2:
        Input: s = "()[]{}"
        Output: true

        Example 3:
        Input: s = "(]"
        Output: false

        Constraints:
        1 <= s.length <= 10^4
        s consists of parentheses only '()[]{}'.
        """
        stack = []
        # Map closing brackets to their corresponding opening brackets
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        
        for c in s:
            # If it's a closing bracket
            if c in closeToOpen:
                # Check if stack is not empty AND top of stack matches
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # If it's an opening bracket
            else:
                stack.append(c)
                
        # True if stack is empty, False otherwise
        return True if not stack else False

if __name__ == "__main__":
    solver = Solution()
    
    s1 = "()[]{}"
    print(f"Input: '{s1}'")
    print(f"Output: {solver.isValid(s1)}")
    # Expected: True

    s2 = "(]"
    print(f"Input: '{s2}'")
    print(f"Output: {solver.isValid(s2)}")
    # Expected: False