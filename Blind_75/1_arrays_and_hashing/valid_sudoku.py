from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Problem: Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
        according to the following rules:
        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        Note: A partially filled board could be valid but is not necessarily solvable.
        Only the filled cells need to be validated. Empty cells are filled with '.'.
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in squares[(r//3,c//3)]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3,c//3)].add(val)
        return True

# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ] # Expected: True

    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ] # Expected: False (The 8 in top-left matches 8 in 4th row, 1st col, wait... actually looking at board2, 
      # usually the example has an 8 in the top left corner [0,0] and an 8 in [0,4] or similar. 
      # Let's stick to the standard LeetCode example modification where [0,0] is 8 and [0,0] collision? 
      # Actually, let's use a clear row collision.
      # In board 2, let's make [0,0] = '8' and [0,1] = '8' for an obvious fail.)

    board2_obvious_fail = [
        ["8","8",".",".","7",".",".",".","."], # Collision in row 0
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    test_cases = [
        (board1, True),
        (board2_obvious_fail, False)
    ]

    for i, (inputs, expected) in enumerate(test_cases):
        result = solver.isValidSudoku(inputs)
        print(f"Test Case {i+1}:")
        # Not printing full board to keep output clean
        print(f"  Input: 9x9 Board") 
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print("-" * 30)