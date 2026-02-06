from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        You have a graph of n nodes. You are given an integer n and an array edges 
        where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

        Return the number of connected components in the graph.

        Example 1:
        Input: n = 5, edges = [[0,1], [1,2], [3,4]]
        Output: 2
        
        Example 2:
        Input: n = 5, edges = [[0,1], [1,2], [2,3], [3,4]]
        Output: 1
        """
        # Initially, each node is its own parent
        parent = [i for i in range(n)]
        # Rank is used to optimize the tree height (all start at 1)
        rank = [1] * n
        
        def find(node):
            # Path Compression: Point node directly to root
            curr = node
            while curr != parent[curr]:
                # Optimization: Point to grandparent to shorten path
                parent[curr] = parent[parent[curr]] 
                curr = parent[curr]
            return curr
        
        def union(n1, n2):
            root1, root2 = find(n1), find(n2)
            
            # If they are already in the same set, do nothing
            if root1 == root2:
                return 0
            
            # Union by Rank: Attach smaller tree to larger tree
            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]
                
            return 1 # Successful merge
            
        # Start with 'n' separate components
        res = n
        for n1, n2 in edges:
            # Every successful union decreases the count by 1
            res -= union(n1, n2)
            
        return res

if __name__ == "__main__":
    solver = Solution()
    
    # Component 1: 0-1-2
    # Component 2: 3-4
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    
    print(f"Connected Components: {solver.countComponents(n, edges)}")
    # Expected: 2