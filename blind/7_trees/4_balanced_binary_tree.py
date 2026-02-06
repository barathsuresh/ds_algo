from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Given a binary tree, determine if it is height-balanced.
        
        For this problem, a height-balanced binary tree is defined as:
        a binary tree in which the left and right subtrees of every node 
        differ in height by no more than 1.

        Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: true

        Example 2:
        Input: root = [1,2,2,3,3,null,null,4,4]
        Output: false

        Example 3:
        Input: root = []
        Output: true

        Constraints:
        The number of nodes in the tree is in the range [0, 5000].
        -10^4 <= Node.val <= 10^4
        """
        
        def dfs(root):
            # Base Case: An empty tree is balanced and has height 0
            if not root:
                return 0
            
            # Recursively check left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)
            
            # If any child returned -1, the tree is already known to be unbalanced
            if left == -1 or right == -1:
                return -1
            
            # If the current node is unbalanced
            if abs(left - right) > 1:
                return -1
            
            # Otherwise, return the height of this node
            return 1 + max(left, right)
            
        # If dfs returns -1, it's False. Otherwise True.
        return dfs(root) != -1

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1: Balanced
    #      3
    #     / \
    #    9  20
    #       / \
    #      15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(f"Is Balanced (Example 1): {solver.isBalanced(root)}") 
    # Expected: True

    # Example 2: Unbalanced
    #        1
    #       / \
    #      2   2
    #     / \
    #    3   3
    #   / \
    #  4   4
    root2 = TreeNode(1)
    root2.left = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3))
    root2.right = TreeNode(2)
    print(f"Is Balanced (Example 2): {solver.isBalanced(root2)}")
    # Expected: False