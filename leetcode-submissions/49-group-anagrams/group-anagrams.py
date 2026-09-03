
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        res = []
        for i in strs:
            s = "".join(sorted(i))
            word_map[s].append(i)
        for index, (key, value) in enumerate(word_map.items()):
            res.append(value)
        return res