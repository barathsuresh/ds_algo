from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the 
        sequence has an edge connecting them. A node can only appear in the sequence at most once. 
        Note that the path does not need to pass through the root.

        The path sum is the sum of the node's values in the path.

        Given the root of a binary tree, return the maximum path sum of any non-empty path.

        Example 1:
        Input: root = [1,2,3]
        Output: 6
        Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

        Example 2:
        Input: root = [-10,9,20,null,null,15,7]
        Output: 42
        Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
        """
        # Initialize with a very small number
        self.global_max = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursively get max path from left and right children
            # If a child returns a negative value, we ignore it (max with 0)
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            # 1. Calculate the path sum where THIS node is the peak (the "Split")
            # This path includes left child + node + right child
            current_path_sum = node.val + left_max + right_max
            
            # Update the global maximum result
            self.global_max = max(self.global_max, current_path_sum)
            
            # 2. Return the max path extending upwards to the parent (The "Continue")
            # We can only bring ONE child path with us up the tree
            return node.val + max(left_max, right_max)
            
        dfs(root)
        return self.global_max

if __name__ == "__main__":
    solver = Solution()
    
    # Tree:
    #      -10
    #      /  \
    #     9   20
    #        /  \
    #       15   7
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    print(f"Max Path Sum: {solver.maxPathSum(root)}")
    # Expected: 42 (15 -> 20 -> 7)