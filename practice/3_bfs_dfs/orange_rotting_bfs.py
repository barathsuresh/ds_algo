from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_count = 0

        # 1. Initialization: Find all rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 2. BFS Loop
        while q and fresh_count > 0:
            # TODO: Write the logic to process ONE MINUTE (one layer)
            # Hint: Iterate through the current size of the queue (snapshot)
            # Pop orange -> Infect neighbors -> Add neighbors to queue -> Decrement fresh_count
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < rows and 0 <= col < cols:
                        if grid[row][col] == 1:
                            grid[row][col] = 2
                            q.append((row, col))
                            fresh_count -= 1
            minutes += 1

        return minutes if fresh_count == 0 else -1


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),  # Impossible case
        ([[0, 2]], 0),
    ]
    for i, (grid, expected) in enumerate(test_cases):
        print(
            f"Test Case {i+1}: Output={solver.orangesRotting(grid)}, Expected={expected}"
        )
