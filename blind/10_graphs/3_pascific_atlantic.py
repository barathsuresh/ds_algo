from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
        The Pacific Ocean touches the island's left and top edges.
        The Atlantic Ocean touches the island's right and bottom edges.

        The island is partitioned into a grid of square cells. You are given an m x n integer matrix 
        heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

        Rain water can flow to neighboring cells directly north, south, east, and west if the neighboring 
        cell's height is less than or equal to the current cell's height. Water can flow from any cell 
        adjacent to an ocean into the ocean.

        Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water 
        can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

        Example 1:
        Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        """
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight): # Water can't flow "up" to us (reverse logic)
                return
            
            visit.add((r, c))
            
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            
        # Start from the edges
        for c in range(COLS):
            # Top edge (Pacific)
            dfs(0, c, pac, heights[0][c])
            # Bottom edge (Atlantic)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
            
        for r in range(ROWS):
            # Left edge (Pacific)
            dfs(r, 0, pac, heights[r][0])
            # Right edge (Atlantic)
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
            
        # The answer is the intersection
        return list(pac.intersection(atl))

if __name__ == "__main__":
    solver = Solution()
    heights = [
      [1,2,2,3,5],
      [3,2,3,4,4],
      [2,4,5,3,1],
      [6,7,1,4,5],
      [5,1,1,2,4]
    ]
    # Cells (3,0) [Height 6] and (4,0) [Height 5] can clearly flow everywhere
    print(f"Result: {solver.pacificAtlantic(heights)}")