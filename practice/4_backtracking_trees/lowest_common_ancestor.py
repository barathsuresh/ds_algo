class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        PROBLEM DESCRIPTION:
        Find the lowest node T that has both p and q as descendants.
        """
        # TODO: Write logic
        # 1. Base Case: root is None? OR root is p? OR root is q? -> Return root
        if root is None:
            return None
        if root is p or root is q:
            return root
        # 2. Search Left and Right
        left_root = self.lowestCommonAncestor(root.left,p,q)
        right_root = self.lowestCommonAncestor(root.right,p,q)
        # 3. If left AND right are not None -> This root is the answer.
        if left_root and right_root:
            return root
        # 4. Otherwise return non-None child (or None if both are None)
        return left_root if left_root else right_root
    # --- Test Runner ---
def build_tree_from_list(values):
    """Helper to build a tree from a level-order list (LeetCode style)"""
    if not values: return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    root = nodes[0]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def find_node(root, val):
    """Helper to find the actual TreeNode object for a given value"""
    if not root: return None
    if root.val == val: return root
    left = find_node(root.left, val)
    if left: return left
    return find_node(root.right, val)

if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard Split
    # Tree: [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
    # LCA of 5 and 1 should be 3
    root1 = build_tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p1 = find_node(root1, 5)
    q1 = find_node(root1, 1)
    result1 = solver.lowestCommonAncestor(root1, p1, q1)
    print(f"Test Case 1: LCA of 5 and 1 -> Output: {result1.val if result1 else None}, Expected: 3")
    
    # Test Case 2: Ancestor is itself
    # LCA of 5 and 4 should be 5
    p2 = find_node(root1, 5)
    q2 = find_node(root1, 4)
    result2 = solver.lowestCommonAncestor(root1, p2, q2)
    print(f"Test Case 2: LCA of 5 and 4 -> Output: {result2.val if result2 else None}, Expected: 5")

    print("-" * 30)