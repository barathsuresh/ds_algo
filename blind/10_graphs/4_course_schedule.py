from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
        You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
        must take course bi first if you want to take course ai.

        Return true if you can finish all courses. Otherwise, return false.

        Example 1:
        Input: numCourses = 2, prerequisites = [[1,0]]
        Output: true
        Explanation: Take 0, then 1.

        Example 2:
        Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
        Output: false
        Explanation: Cycle detected (1->0->1).
        """
        # 1. Build Adjacency List
        preMap = { i: [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # 2. Track nodes in the current DFS path
        visitSet = set()
        
        def dfs(crs):
            # If currently visiting this node, we found a cycle
            if crs in visitSet:
                return False
            
            # If no prerequisites, this course can be completed
            if preMap[crs] == []:
                return True
            
            # Mark as visiting
            visitSet.add(crs)
            
            # Check all prerequisites recursively
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            # Remove from visiting set (Backtrack)
            visitSet.remove(crs)
            
            # Optimization: Mark as empty so we don't re-check this fully valid node later
            preMap[crs] = []
            return True
        
        # 3. Iterate through every course (graph might be disconnected)
        for crs in range(numCourses):
            if not dfs(crs):
                return False
                
        return True

if __name__ == "__main__":
    solver = Solution()
    
    # Cycle Example: 0 -> 1 -> 0
    n = 2
    prereqs = [[1, 0], [0, 1]]
    print(f"Can finish {prereqs}? {solver.canFinish(n, prereqs)}")
    # Expected: False
    
    # Valid Example: 0 -> 1
    prereqs_valid = [[1, 0]]
    print(f"Can finish {prereqs_valid}? {solver.canFinish(n, prereqs_valid)}")
    # Expected: True