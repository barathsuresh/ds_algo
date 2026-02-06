class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Given a string s, return the longest palindromic substring in s.

        Example 1:
        Input: s = "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.

        Example 2:
        Input: s = "cbbd"
        Output: "bb"
        """
        res = ""
        resLen = 0

        for i in range(len(s)):
            # Case 1: Odd Length Palindromes (Center is s[i])
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # Case 2: Even Length Palindromes (Center is gap between s[i] and s[i+1])
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

if __name__ == "__main__":
    solver = Solution()
    
    s = "babad"
    print(f"Longest Palindrome in '{s}': {solver.longestPalindrome(s)}")
    # Expected: "bab" or "aba"
    
    s2 = "cbbd"
    print(f"Longest Palindrome in '{s2}': {solver.longestPalindrome(s2)}")
    # Expected: "bb"