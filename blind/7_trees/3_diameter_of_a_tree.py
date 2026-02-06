from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the length of the diameter of the tree.

        The diameter of a binary tree is the length of the longest path between any two nodes 
        in a tree. This path may or may not pass through the root.

        The length of a path between two nodes is represented by the number of edges between them.

        Example 1:
        Input: root = [1,2,3,4,5]
        Output: 3
        Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

        Example 2:
        Input: root = [1,2]
        Output: 1
        """
        self.res = 0
        
        def dfs(curr):
            # Base Case: Height of null is 0
            if not curr:
                return 0
            
            # Recursively find height of left and right subtrees
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            # 1. Update the global maximum diameter found so far
            # The path through THIS node is left_height + right_height
            self.res = max(self.res, left + right)
            
            # 2. Return the height of this node to its parent
            # Height = 1 (itself) + max height of its children
            return 1 + max(left, right)
            
        dfs(root)
        return self.res

if __name__ == "__main__":
    solver = Solution()
    
    # Tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    # Longest path is 4 -> 2 -> 1 -> 3 (Length 3)
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    
    print(f"Diameter: {solver.diameterOfBinaryTree(root)}")
    # Expected: 3