from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        You are given an m x n integer matrix matrix with the following two properties:
        1. Each row is sorted in non-decreasing order.
        2. The first integer of each row is greater than the last integer of the previous row.

        Given an integer target, return true if target is in matrix or false otherwise.

        You must write a solution in O(log(m * n)) time complexity.

        Example 1:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        Output: true

        Example 2:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
        Output: false
        """
        if not matrix:
            return False
            
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Treat the matrix as a sorted list from index 0 to (ROWS * COLS - 1)
        l, r = 0, (ROWS * COLS) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # Convert 1D index 'mid' back to (row, col)
            r_idx = mid // COLS
            c_idx = mid % COLS
            val = matrix[r_idx][c_idx]
            
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False

if __name__ == "__main__":
    solver = Solution()
    mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(f"Input: {mat}, Target: {target}")
    print(f"Output: {solver.searchMatrix(mat, target)}")
    # Expected: True