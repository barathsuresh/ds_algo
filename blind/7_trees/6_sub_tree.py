from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees root and subRoot, return true if there is a subtree 
        of root with the same structure and node values of subRoot and false otherwise.

        A subtree of a binary tree tree is a tree that consists of a node in tree and all of 
        this node's descendants. The tree tree could also be considered as a subtree of itself.

        Example 1:
        Input: root = [3,4,5,1,2], subRoot = [4,1,2]
        Output: true

        Example 2:
        Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
        Output: false

        Constraints:
        root nodes: [1, 2000]
        subRoot nodes: [1, 1000]
        -10^4 <= val <= 10^4
        """
        if not subRoot: return True
        if not root: return False

        # Check if the trees match starting from the current node
        if self.isSameTree(root, subRoot):
            return True
        
        # If not, keep searching in the left or right children
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Helper function from Problem 32
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

if __name__ == "__main__":
    solver = Solution()
    
    # Construct "Root" Tree
    #      3
    #     / \
    #    4   5
    #   / \
    #  1   2
    root = TreeNode(3)
    root.right = TreeNode(5)
    root.left = TreeNode(4, TreeNode(1), TreeNode(2))

    # Construct "SubRoot" Tree
    #    4
    #   / \
    #  1   2
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    
    print(f"Is Subtree: {solver.isSubtree(root, subRoot)}")
    # Expected: True