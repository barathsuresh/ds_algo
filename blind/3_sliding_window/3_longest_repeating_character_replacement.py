from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        You are given a string s and an integer k. You can choose any character of the string 
        and change it to any other uppercase English character. You can perform this operation 
        at most k times.

        Return the length of the longest substring containing the same letter you can get 
        after performing the above operations.

        Example 1:
        Input: s = "ABAB", k = 2
        Output: 4
        Explanation: Replace the two 'A's with two 'B's or vice versa.

        Example 2:
        Input: s = "AABABBA", k = 1
        Output: 4
        Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
        The substring "BBBB" has length 4.

        Constraints:
        1 <= s.length <= 10^5
        s consists of only uppercase English letters.
        0 <= k <= s.length
        """
        count = {}
        res = 0
        l = 0
        max_f = 0
        
        for r in range(len(s)):
            # Update frequency of current character
            count[s[r]] = count.get(s[r], 0) + 1
            
            # Track the count of the most frequent character in the current window
            max_f = max(max_f, count[s[r]])
            
            # Check validity:
            # Window Size (r - l + 1) - Most Frequent Count > k
            # If true, we need more than k swaps, so the window is invalid.
            if (r - l + 1) - max_f > k:
                # Shrink window from the left
                count[s[l]] -= 1
                l += 1
            
            # Update max length (the window is guaranteed valid here)
            res = max(res, r - l + 1)
            
        return res

if __name__ == "__main__":
    solver = Solution()
    s = "AABABBA"
    k = 1
    print(f"Input: s='{s}', k={k}")
    print(f"Output: {solver.characterReplacement(s, k)}")
    # Expected: 4