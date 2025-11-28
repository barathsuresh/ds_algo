class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        PROBLEM DESCRIPTION:
        Given a string s, find the length of the longest substring
        without repeating characters.

        Example 1:
        Input: s = "abcabcbb"
        Output: 3 (The answer is "abc")

        Example 2:
        Input: s = "bbbbb"
        Output: 1 (The answer is "b")

        Example 3:
        Input: s = "pwwkew"
        Output: 3 (The answer is "wke", NOT "pwke")
        """
        n = len(s)
        max_len_sub = 0
        set_chars = set()
        left = 0
        for right in range(n):
            while s[right] in set_chars:
                set_chars.remove(s[left])
                left += 1

            set_chars.add(s[right])
            max_len_sub = max(max_len_sub, right - left + 1)
        return max_len_sub

    def lengthOfLongestSubstringOPT(self, s: str) -> int:
        max_len = 0
        left = 0
        chars_at_index = {}
        n = len(s)
        for right in range(n):
            char = s[right]

            if char in chars_at_index and chars_at_index[char] >= left:
                left = chars_at_index[char] + 1

            chars_at_index[char] = right
            max_len = max(max_len, right - left + 1)
        return  max_len


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),  # Tricky edge case
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = solver.lengthOfLongestSubstringOPT(s)
        print(f"Test Case {i+1}:")
        print(f"  Input: '{s}'")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print("-" * 30)
