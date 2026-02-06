from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return its maximum depth.

        A binary tree's maximum depth is the number of nodes along the longest path 
        from the root node down to the farthest leaf node.

        Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: 3
        Explanation: The path 3 -> 20 -> 15 (or 7) has 3 nodes.

        Example 2:
        Input: root = [1,null,2]
        Output: 2

        Constraints:
        The number of nodes in the tree is in the range [0, 10^4].
        -100 <= Node.val <= 100
        """
        # Base Case: Empty tree has depth 0
        if not root:
            return 0
        
        # Recursive Step: 1 (current) + max depth of children
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    solver = Solution()
    
    # Tree:
    #      3
    #    /   \
    #   9     20
    #        /  \
    #       15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    print(f"Max Depth: {solver.maxDepth(root)}")
    # Expected: 3