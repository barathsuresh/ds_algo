class Solution:
    def numDecodings(self, s: str) -> int:
        """
        A message containing letters from A-Z can be encoded into numbers using the mapping:
        'A' -> "1", 'B' -> "2", ... 'Z' -> "26".

        Given a string s containing only digits, return the number of ways to decode it.

        Example 1:
        Input: s = "12"
        Output: 2
        Explanation: "AB" (1 2) or "L" (12).

        Example 2:
        Input: s = "226"
        Output: 3
        Explanation: "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

        Example 3:
        Input: s = "06"
        Output: 0
        Explanation: "06" cannot be mapped to "F" because "6" is different from "06".
        """
        # Dictionary to memoize results
        # Base case: The empty string at the end has 1 valid way to "finish"
        dp = { len(s) : 1 }

        # Iterate backwards from the last digit to the first
        for i in range(len(s) - 1, -1, -1):
            # Case 1: Starts with '0' -> Invalid.
            if s[i] == "0":
                dp[i] = 0
            else:
                # Take result from next index (single digit decoding)
                dp[i] = dp[i + 1]

            # Case 2: Check for valid two-digit decoding (10-26)
            if (i + 1 < len(s) and (s[i] == "1" or 
               (s[i] == "2" and s[i + 1] in "0123456"))):
                dp[i] += dp[i + 2]
                
        return dp[0]

if __name__ == "__main__":
    solver = Solution()
    
    # "12" -> A, B (1, 2) or L (12)
    print(f"Ways to decode '12': {solver.numDecodings('12')}")
    # Expected: 2
    
    # "226" -> BZ (2, 26), VF (22, 6), BBF (2, 2, 6)
    print(f"Ways to decode '226': {solver.numDecodings('226')}")
    # Expected: 3