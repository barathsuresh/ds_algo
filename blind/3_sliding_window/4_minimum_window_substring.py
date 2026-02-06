from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Given two strings s and t of lengths m and n respectively, return the minimum window 
        substring of s such that every character in t (including duplicates) is included in the window. 
        If there is no such substring, return the empty string "".

        The testcases will be generated such that the answer is unique.

        Example 1:
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

        Example 2:
        Input: s = "a", t = "a"
        Output: "a"

        Example 3:
        Input: s = "a", t = "aa"
        Output: ""
        Explanation: Both 'a's from t must be included in the window.
        Since the largest window of s only has one 'a', return empty string.

        Constraints:
        m == s.length, n == t.length
        1 <= m, n <= 10^5
        s and t consist of uppercase and lowercase English letters.
        """
        if not t or not s:
            return ""

        # Dictionary to keep count of all the unique characters in t.
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        # Dictionary to keep a count of all the unique characters in the current window of s.
        window = {}
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        
        for r in range(len(s)):
            # Add character from the right to the window
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # If the frequency of the current character added equals to the desired count in t
            # then increment the formed count.
            if c in countT and window[c] == countT[c]:
                have += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while have == need:
                # Update our result if this window is smaller than the smallest we've seen
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                # Move the left pointer ahead, this would help to look for a new window.
                l += 1
        
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""

if __name__ == "__main__":
    solver = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(f"Input: s='{s}', t='{t}'")
    print(f"Output: '{solver.minWindow(s, t)}'")
    # Expected: "BANC"