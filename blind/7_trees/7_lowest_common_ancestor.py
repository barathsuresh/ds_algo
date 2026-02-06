class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

        According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between 
        two nodes p and q as the lowest node in T that has both p and q as descendants 
        (where we allow a node to be a descendant of itself)."

        Example 1:
        Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
        Output: 6
        Explanation: The LCA of nodes 2 and 8 is 6.

        Example 2:
        Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
        Output: 2
        Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself.

        Constraints:
        The number of nodes in the tree is in the range [2, 10^5].
        -10^9 <= Node.val <= 10^9
        All Node.val are unique.
        p != q
        p and q will exist in the BST.
        """
        curr = root

        while curr:
            # If both p and q are greater than curr, go Right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            
            # If both p and q are smaller than curr, go Left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            
            # We found the split point (or one of the nodes is the split point)
            else:
                return curr

if __name__ == "__main__":
    solver = Solution()
    
    # BST Structure:
    #       6
    #     /   \
    #    2     8
    #   / \   / \
    #  0   4 7   9
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    
    p = root.left       # Node 2
    q = root.right      # Node 8
    
    lca = solver.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {lca.val}")
    # Expected: 6