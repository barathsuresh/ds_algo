from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        PROBLEM DESCRIPTION:
        Write an efficient algorithm that searches for a value target in an m x n
        integer matrix. This matrix has the following properties:
        1. Integers in each row are sorted from left to right.
        2. The first integer of each row is greater than the last integer of the previous row.

        Example 1:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        Output: True
        """
        rows, cols = len(matrix), len(matrix[0])
        total_length = rows * cols
        left = 0
        right = total_length - 1
        while left <= right:
            mid = left + (right - left) // 2
            row = mid // cols
            col = mid % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1]], 1, True),
    ]

    for i, (matrix, target, expected) in enumerate(test_cases):
        result = solver.searchMatrix(matrix, target)
        print(f"Test Case {i+1}: Output={result}, Expected={expected}")
