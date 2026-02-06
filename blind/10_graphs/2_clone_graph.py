from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Given a reference of a node in a connected undirected graph.
        Return a deep copy (clone) of the graph.

        Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

        Example 1:
        Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: [[2,4],[1,3],[2,4],[1,3]]
        """
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            # Create the copy
            copy = Node(node.val)
            # Add to map immediately to handle cycles
            oldToNew[node] = copy
            
            # Recursively copy neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy

        return dfs(node) if node else None

if __name__ == "__main__":
    solver = Solution()
    
    # Constructing a simple graph: 1 -- 2
    node1 = Node(1)
    node2 = Node(2)
    node1.neighbors.append(node2)
    node2.neighbors.append(node1)
    
    clone = solver.cloneGraph(node1)
    
    print(f"Original Node: {node1.val}, Neighbors: {[n.val for n in node1.neighbors]}")
    print(f"Cloned Node:   {clone.val}, Neighbors: {[n.val for n in clone.neighbors]}")
    print(f"Is Original == Clone? {node1 == clone}") 
    # Expected: False (Different objects, same data)