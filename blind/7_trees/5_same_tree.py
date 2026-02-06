from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees p and q, write a function to check if they are the same or not.

        Two binary trees are considered the same if they are structurally identical, 
        and the nodes have the same value.

        Example 1:
        Input: p = [1,2,3], q = [1,2,3]
        Output: true

        Example 2:
        Input: p = [1,2], q = [1,null,2]
        Output: false

        Example 3:
        Input: p = [1,2,1], q = [1,1,2]
        Output: false

        Constraints:
        The number of nodes in both trees is in the range [0, 100].
        -10^4 <= Node.val <= 10^4
        """
        # 1. If both nodes are None, they are identical
        if not p and not q:
            return True
        
        # 2. If one is None but the other isn't, or values differ
        if not p or not q or p.val != q.val:
            return False
        
        # 3. Recursively check left and right subtrees
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

if __name__ == "__main__":
    solver = Solution()
    
    # Tree P:    Tree Q:
    #    1          1
    #   / \        / \
    #  2   3      2   3
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    
    print(f"Is Same: {solver.isSameTree(p, q)}")
    # Expected: True
    
    # Tree R:    Tree S:
    #    1          1
    #   /            \
    #  2              2
    r = TreeNode(1, TreeNode(2), None)
    s = TreeNode(1, None, TreeNode(2))
    
    print(f"Is Same (Structure mismatch): {solver.isSameTree(r, s)}")
    # Expected: False