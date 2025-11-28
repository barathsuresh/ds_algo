from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        PROBLEM DESCRIPTION:
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
        You are given an array prerequisites where prerequisites[i] = [a, b] 
        indicates that you must take course b first if you want to take course a.
        
        Return true if you can finish all courses. Otherwise, return false (if cycle exists).
        """
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            
            if pre_map[crs] == []:
                return True
            
            visiting.add(crs)

            for pre in pre_map[crs]:
                if not dfs(pre): return False
            
            visiting.remove(crs)
            pre_map[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        
        return True


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        (2, [[1, 0]], True),                  # 0 -> 1 (Valid)
        (2, [[1, 0], [0, 1]], False),         # 0 <-> 1 (Cycle)
        (5, [[0,1], [0,2], [1,3], [1,4], [3,4]], True), # Complex Valid
        (3, [[0,1], [1,2], [2,0]], False),    # 0 -> 1 -> 2 -> 0 (Cycle)
        (1, [], True)                         # No prereqs
    ]
    
    for i, (n, prereqs, expected) in enumerate(test_cases):
        result = solver.canFinish(n, prereqs)
        print(f"Test Case {i+1}: Output={result}, Expected={expected}")
        print("-" * 30)