from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group the anagrams together. 
        You can return the answer in any order.

        Example 1:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        Constraints:
        1 <= strs.length <= 10^4
        0 <= strs[i].length <= 100
        strs[i] consists of lowercase English letters.
        """
        # Map: Key (Tuple) -> Value (List of strings)
        anagram_map = defaultdict(list)
        
        for s in strs:
            key = tuple(sorted(s)) # lists are mutable that's why we use tuple here
            w ="".join(key)
            anagram_map[w].append(s)
            
        return list(anagram_map.values())

if __name__ == "__main__":
    solver = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(f"Input: {strs}")
    print(f"Output: {solver.groupAnagrams(strs)}")