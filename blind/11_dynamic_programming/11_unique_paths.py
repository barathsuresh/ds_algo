class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        There is a robot on an m x n grid. The robot is initially located at the 
        top-left corner (i.e., grid[0][0]). The robot tries to move to the 
        bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move 
        either down or right at any point in time.

        Given the two integers m and n, return the number of possible unique paths 
        that the robot can take to reach the bottom-right corner.

        Example 1:
        Input: m = 3, n = 7
        Output: 28

        Example 2:
        Input: m = 3, n = 2
        Output: 3
        Explanation:
        1. Right -> Down -> Down
        2. Down -> Down -> Right
        3. Down -> Right -> Down
        """
        # Create a 2D DP grid initialized with 1s.
        # While strictly only the first row/col need to be 1, filling it all 
        # doesn't hurt and simplifies initialization.
        dp = [[1] * n for _ in range(m)]
        
        # Start from (1,1) since row 0 and col 0 are fixed at 1
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
                
        return dp[m-1][n-1]

    # Space Optimized Version (O(n) space)
    # We only need the previous row to calculate the current row.
    def uniquePathsOptimized(self, m: int, n: int) -> int:
        row = [1] * n
        
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(1, n):
                newRow[j] = newRow[j-1] + row[j]
            row = newRow
            
        return row[-1]

if __name__ == "__main__":
    solver = Solution()
    m, n = 3, 7
    print(f"Unique Paths for {m}x{n} grid: {solver.uniquePaths(m, n)}")
    # Expected: 28