from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Given a string s and a dictionary of strings wordDict, return true if s can be 
        segmented into a space-separated sequence of one or more dictionary words.

        Note that the same word in the dictionary may be reused multiple times in the segmentation.

        Example 1:
        Input: s = "leetcode", wordDict = ["leet","code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".

        Example 2:
        Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
        Output: false
        """
        # Convert list to set for O(1) lookups
        words = set(wordDict)
        
        # dp[i] means s[:i] is valid
        # Size is len(s) + 1 to handle the empty string base case
        dp = [False] * (len(s) + 1)
        
        # Base case: Empty string is always valid
        dp[0] = True

        # i represents the END of the substring we are checking (1 to len(s))
        for i in range(1, len(s) + 1):
            # j represents the START of the current word candidate
            for j in range(i):
                # If s[:j] was valid (dp[j] is True)
                # AND the substring s[j:i] is in our dictionary
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break # We found one valid way to reach i, stop checking other 'j's

        return dp[len(s)]

if __name__ == "__main__":
    solver = Solution()
    
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(f"Can break '{s}'? {solver.wordBreak(s, wordDict)}")
    # Expected: True (apple + pen + apple)