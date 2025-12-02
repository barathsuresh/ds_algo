from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        PROBLEM DESCRIPTION:
        Given two strings s and t of lengths m and n respectively, return the
        minimum window substring of s such that every character in t (including duplicates)
        is included in the window. If there is no such substring, return the empty string "".

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
        Since the largest window is "a", which only has one 'a', return empty string.
        """
        if len(t) > len(s) or t == "":
            return ""
        target_counts = Counter(t)
        window = defaultdict(int)
        res = [-1, -1]
        resLen = float("inf")
        left = 0
        have = 0
        need = len(target_counts)

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in target_counts and window[char] == target_counts[char]:
                have += 1

            while have == need:
                if right - left + 1 < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1

                if (
                    s[left] in target_counts
                    and window[s[left]] < target_counts[s[left]]
                ):
                    have -= 1

                left += 1

        left, right = res
        return s[left : right + 1] if resLen != float("inf") else ""


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("ab", "a", "a"),  # Smallest window is just "a"
        ("aa", "aa", "aa"),
    ]

    for i, (s, t, expected) in enumerate(test_cases):
        result = solver.minWindow(s, t)
        print(f"Test Case {i+1}:")
        print(f"  Input: s='{s}', t='{t}'")
        print(f"  Output: '{result}'")
        print(f"  Expected: '{expected}'")
        print("-" * 30)
