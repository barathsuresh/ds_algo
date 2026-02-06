class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Given two strings text1 and text2, return the length of their longest common subsequence. 
        If there is no common subsequence, return 0.

        A subsequence of a string is a new string generated from the original string with some characters 
        (can be none) deleted without changing the relative order of the remaining characters.

        Example 1:
        Input: text1 = "abcde", text2 = "ace" 
        Output: 3  
        Explanation: The longest common subsequence is "ace" and its length is 3.

        Example 2:
        Input: text1 = "abc", text2 = "def"
        Output: 0
        """
        # Create a grid of size (len1 + 1) x (len2 + 1) initialized to 0
        # The extra row and column handle the "out of bounds" base case (empty string matches nothing)
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # Iterate backwards from the bottom-right
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    # Match: 1 + result of removing both chars (diagonal)
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # Mismatch: Max of removing one char from text1 OR text2
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # The result is at the start of both strings
        return dp[0][0]

if __name__ == "__main__":
    solver = Solution()
    
    t1 = "abcde"
    t2 = "ace" 
    print(f"LCS of '{t1}' and '{t2}': {solver.longestCommonSubsequence(t1, t2)}")
    # Expected: 3