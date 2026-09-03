from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        # we are creating like a key value such that. the in alphabets and all snd storing the values as we encounter a match
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return list(result.values()) # Takes of O(m*n) complexity becuz m is the number of. items and n is avg characters for the strings