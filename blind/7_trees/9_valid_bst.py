from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).

        A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with keys less than the node's key.
        - The right subtree of a node contains only nodes with keys greater than the node's key.
        - Both the left and right subtrees must also be binary search trees.

        Example 1:
        Input: root = [2,1,3]
        Output: true

        Example 2:
        Input: root = [5,1,4,null,null,3,6]
        Output: false
        Explanation: The root node's value is 5 but its right child's value is 4.
        """
        
        def validate(node, left_limit, right_limit):
            # Base Case: Empty node is valid
            if not node:
                return True
            
            # Check violation: Node value must be strictly between limits
            if not (left_limit < node.val < right_limit):
                return False
            
            # Recurse:
            # 1. Left child: must be greater than current left_limit, but smaller than current node
            # 2. Right child: must be greater than current node, but smaller than current right_limit
            return (validate(node.left, left_limit, node.val) and
                    validate(node.right, node.val, right_limit))
            
        # Initial call with infinite boundaries
        return validate(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1: Valid
    #    2
    #   / \
    #  1   3
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"Is Valid (Example 1): {solver.isValidBST(root1)}")
    # Expected: True
    
    # Example 2: Invalid (Standard Trap)
    #     5
    #    / \
    #   1   4  <-- 4 is in the right subtree of 5, but 4 < 5. Invalid.
    #      / \
    #     3   6
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4, TreeNode(3), TreeNode(6))
    
    print(f"Is Valid (Example 2): {solver.isValidBST(root2)}")
    # Expected: False