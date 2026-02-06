from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2D binary grid grid which represents a map of '1's (land) 
        and '0's (water), return the number of islands.

        An island is surrounded by water and is formed by connecting adjacent 
        lands horizontally or vertically. You may assume all four edges of the 
        grid are all surrounded by water.

        Example 1:
        Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        Output: 1

        Example 2:
        Input: grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Output: 3
        """
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            # Base Cases: 
            # 1. Out of bounds
            # 2. It is water ('0')
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return
            
            # Mark as visited by sinking the island (turning '1' to '0')
            # This saves us O(M*N) memory by not needing a separate visited set.
            grid[r][c] = "0"
            
            # Visit all adjacent neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # We found a new island!
                    islands += 1
                    # Sink the entire island so we don't count it again
                    dfs(r, c)
                    
        return islands

if __name__ == "__main__":
    solver = Solution()
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    print(f"Number of Islands: {solver.numIslands(grid)}")
    # Expected: 3