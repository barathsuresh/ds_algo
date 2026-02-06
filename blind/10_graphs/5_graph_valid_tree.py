from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Given n nodes labeled from 0 to n-1 and a list of undirected edges 
        (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

        Example 1:
        Input: n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]
        Output: true

        Example 2:
        Input: n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
        Output: false (Cycle exists: 1-2-3-1)
        """
        if not n:
            return True
        
        # 1. Build Adjacency List
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visit = set()
        
        # 2. DFS function
        # Returns True if no cycle found, False if cycle found
        def dfs(curr, prev):
            if curr in visit:
                return False # Cycle detected (visited node that isn't parent)
            
            visit.add(curr)
            
            for neighbor in adj[curr]:
                if neighbor == prev:
                    continue # Skip the edge coming from parent
                if not dfs(neighbor, curr):
                    return False
            
            return True
            
        # 3. Run DFS from node 0
        # If dfs returns False (cycle found), the whole thing is False
        if not dfs(0, -1):
            return False
        
        # 4. Check Connectivity
        # If we didn't visit all n nodes, it's disconnected
        return len(visit) == n

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1: Valid Tree
    #    0
    #  / | \
    # 1  2  3
    # |
    # 4
    edges1 = [[0,1], [0,2], [0,3], [1,4]]
    print(f"Is Valid Tree 1: {solver.validTree(5, edges1)}")
    # Expected: True

    # Example 2: Cycle (1-2-3-1)
    edges2 = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    print(f"Is Valid Tree 2: {solver.validTree(5, edges2)}")
    # Expected: False