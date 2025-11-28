from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        PROBLEM DESCRIPTION:
        Given an m x n 2D binary grid representing a map of '1's (land)
        and '0's (water), return the number of islands.
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        # Helper function for DFS
        def dfs(r, c):
            # TODO: Write the logic here
            # 1. Base Case: Check bounds (r, c) and if grid[r][c] is water '0'.
            #    If out of bounds or water, return immediately.

            # 2. Mark as visited: Turn the '1' into a '0'.

            # 3. Recursion: Visit all 4 neighbors (up, down, left, right).
            if r <= -1 or c <= -1 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            print(r,c)
            grid[r][c] = "0"

            dfs(r, c - 1)  # up
            dfs(r, c + 1)  # down
            dfs(r - 1, c)  # left
            dfs(r + 1, c)  # right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # Found a new island!
                    count += 1
                    dfs(r, c)  # Sink the whole island

        return count


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    print(f"Test Case 1: Output={solver.numIslands(grid1)}, Expected=1")
