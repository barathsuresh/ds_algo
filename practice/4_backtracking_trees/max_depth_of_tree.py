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
        PROBLEM DESCRIPTION:
        Given the root of a binary tree, return its maximum depth.
        """
        # TODO: Write logic
        # 1. Base Case
        if root is None:
            return 0
        # 2. Recursive calls
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # 3. Return 1 + max
        return 1 + max(left_depth,right_depth) 

# --- Test Runner ---
def build_tree(values):
    if not values: return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    solver = Solution()
    # Tree: [3, 9, 20, null, null, 15, 7]
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(f"Max Depth: {solver.maxDepth(root)}, Expected: 3")