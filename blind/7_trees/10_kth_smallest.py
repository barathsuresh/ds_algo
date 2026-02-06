from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Given the root of a binary search tree, and an integer k, return the kth 
        smallest value (1-indexed) of all the values of the nodes in the tree.

        Example 1:
        Input: root = [3,1,4,null,2], k = 1
        Output: 1

        Example 2:
        Input: root = [5,3,6,2,4,null,null,1], k = 3
        Output: 3

        Constraints:
        The number of nodes in the tree is n.
        1 <= k <= n <= 10^4
        0 <= Node.val <= 10^4
        """
        stack = []
        curr = root
        
        # We continue while there are nodes to process or items in the stack
        while curr or stack:
            # 1. Go as far LEFT as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Pop the top node (this is the next smallest)
            curr = stack.pop()
            k -= 1
            
            # 3. If k is 0, we found the kth smallest
            if k == 0:
                return curr.val
            
            # 4. Move RIGHT
            curr = curr.right
            
        return -1 # Should not reach here given valid constraints

if __name__ == "__main__":
    solver = Solution()
    
    # Tree:
    #       5
    #     /   \
    #    3     6
    #   / \
    #  2   4
    # /
    # 1
    # In-order: 1, 2, 3, 4, 5, 6
    root = TreeNode(5)
    root.right = TreeNode(6)
    root.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
    
    k = 3
    print(f"The {k}rd smallest element is: {solver.kthSmallest(root, k)}")
    # Expected: 3