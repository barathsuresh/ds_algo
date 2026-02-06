from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
        You must do it in place.

        Example 1:
        Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
        Output: [[1,0,1],[0,0,0],[1,0,1]]

        Example 2:
        Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False # Flag for the very first row
        
        # 1. Mark the headers (and determine if first row needs zeroing)
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # Mark the column header
                    matrix[0][c] = 0
                    
                    if r > 0:
                        # Mark the row header
                        matrix[r][0] = 0
                    else:
                        # If it's in the first row, we can't use matrix[0][0] 
                        # because that tracks the first column. Use boolean.
                        rowZero = True
                        
        # 2. Use headers to set inner matrix (start from 1,1)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # If either header is 0, this cell becomes 0
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        # 3. Handle the First Column (using matrix[0][0])
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        # 4. Handle the First Row (using boolean)
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

if __name__ == "__main__":
    solver = Solution()
    
    # 0 in middle (1,1)
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    solver.setZeroes(matrix)
    print(f"Result: {matrix}")
    # Expected: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]