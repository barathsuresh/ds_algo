from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Given two integer arrays preorder and inorder where preorder is the preorder traversal 
        of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

        Example 1:
        Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        Output: [3,9,20,null,null,15,7]

        Example 2:
        Input: preorder = [-1], inorder = [-1]
        Output: [-1]

        Constraints:
        1 <= preorder.length <= 3000
        preorder and inorder consist of unique values.
        """
        if not preorder or not inorder:
            return None
            
        # 1. The first element in preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. Find the index of the root in inorder to split the tree
        mid = inorder.index(root_val)
        
        # 3. Recursively build the subtrees
        # Left Subtree:
        # - Inorder: everything before 'mid'
        # - Preorder: skip the root (index 1), take the next 'mid' elements (size of left subtree)
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        # Right Subtree:
        # - Inorder: everything after 'mid'
        # - Preorder: everything after the left subtree chunk
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root

# Helper to print Level Order (to verify)
def print_level_order(root):
    if not root: return []
    q = [root]
    res = []
    while q:
        node = q.pop(0)
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    # Remove trailing Nones for cleaner output
    while res and res[-1] is None:
        res.pop()
    return res

if __name__ == "__main__":
    solver = Solution()
    
    # Target Tree:
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
    
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    
    root = solver.buildTree(preorder, inorder)
    print(f"Reconstructed: {print_level_order(root)}")
    # Expected: [3, 9, 20, None, None, 15, 7]