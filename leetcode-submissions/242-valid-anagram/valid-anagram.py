class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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