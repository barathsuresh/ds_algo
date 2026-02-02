from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once.

        Example 1:
        Input: s = "anagram", t = "nagaram"
        Output: true

        Example 2:
        Input: s = "rat", t = "car"
        Output: false

        Constraints:
        1 <= s.length, t.length <= 5 * 10^4
        s and t consist of lowercase English letters.
        """
        # Optimization: If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
            
        char_count = defaultdict(int)
        
        # 1. Count frequencies for string 's'
        for char in s:
            char_count[char] += 1  # FIX: Add 1, not the current value
            
        # 2. Subtract frequencies for string 't'
        for char in t:
            # If char is not in map or count is already 0, we have too many of this char
            if char_count[char] == 0:
                return False
            char_count[char] -= 1  # FIX: Subtract 1
            
        # Since lengths are equal and we successfully subtracted everything, 
        # the map must be empty (all zeros).
        if sum(char_count.values()) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Valid Anagram
    print(f"Test 1 (anagram, nagaram): {solver.isAnagram('anagram', 'nagaram')}")
    # Expected: True

    # Test Case 2: Invalid Anagram
    print(f"Test 2 (rat, car): {solver.isAnagram('rat', 'car')}")
    # Expected: False