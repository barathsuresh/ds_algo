from typing import List
from collections import Counter, defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # TODO: Implement Sliding Window
        # Window constraints: Max 2 unique keys in the map
        left = 0
        curr_state = defaultdict(int)
        current_sum = 0
        for right in range(len(fruits)):
            curr_state[fruits[right]]+=1
            
            while len(curr_state) > 2:
                curr_state[fruits[left]]-=1
                if curr_state[fruits[left]] == 0:
                    del curr_state[fruits[left]]
                left+=1
            current_sum = max(current_sum,right-left+1)
        return current_sum