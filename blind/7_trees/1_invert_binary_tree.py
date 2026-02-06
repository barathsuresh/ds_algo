from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Given the root of a binary tree, invert the tree, and return its root.

        Example 1:
        Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]

        Example 2:
        Input: root = [2,1,3]
        Output: [2,3,1]

        Example 3:
        Input: root = []
        Output: []

        Constraints:
        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100
        """
        # Base Case: If the tree is empty
        if not root:
            return None
        
        # Swap the children
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# Helper to print level order (to verify the structure)
def print_tree(root):
    if not root:
        return "[]"
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    # Clean up trailing nulls for display
    return result

if __name__ == "__main__":
    solver = Solution()
    
    # Tree:
    #      4
    #    /   \
    #   2     7
    root = TreeNode(4, TreeNode(2), TreeNode(7))
    
    print(f"Original: {print_tree(root)}")
    
    solver.invertTree(root)
    
    print(f"Inverted: {print_tree(root)}")
    # Expected: [4, 7, 2, 'null', 'null', 'null', 'null'] -> effectively 4 -> (7, 2)