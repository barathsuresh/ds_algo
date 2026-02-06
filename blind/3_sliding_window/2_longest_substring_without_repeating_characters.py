class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without repeating characters.

        Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Constraints:
        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols and spaces.
        """
        char_set = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            # If we found a duplicate, shrink the window from the left 
            # until the duplicate character is removed from the set.
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Add the new character to the set
            char_set.add(s[r])
            
            # Update the max length found so far
            # Window size = right_index - left_index + 1
            res = max(res, r - l + 1)
            
        return res

if __name__ == "__main__":
    solver = Solution()
    s = "abcabcbb"
    print(f"Input: {s}")
    print(f"Output: {solver.lengthOfLongestSubstring(s)}")
    # Expected: 3