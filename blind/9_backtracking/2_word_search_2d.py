from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Given an m x n grid of characters board and a string word, return true if word exists in the grid.

        The word can be constructed from letters of sequentially adjacent cells, where adjacent cells 
        are horizontally or vertically neighboring. The same letter cell may not be used more than once.

        Example 1:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        Output: true

        Example 2:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
        Output: true

        Example 3:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
        Output: false
        """
        ROWS, COLS = len(board), len(board[0])
        # To keep track of current path to prevent reusing cells
        path = set()
        
        def dfs(r, c, i):
            # Base Case 1: We found the entire word
            if i == len(word):
                return True
            
            # Base Case 2: Boundary/Validity Checks
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or 
                (r, c) in path):
                return False
            
            # Action: Add to path
            path.add((r, c))
            
            # Explore all 4 directions
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            # Backtrack: Remove from path so other searches can use it
            path.remove((r, c))
            
            return res
        
        # Iterate through every cell to find the starting point
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                    
        return False

if __name__ == "__main__":
    solver = Solution()
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCCED"
    print(f"Grid: {board}")
    print(f"Searching for '{word}': {solver.exist(board, word)}")
    # Expected: True