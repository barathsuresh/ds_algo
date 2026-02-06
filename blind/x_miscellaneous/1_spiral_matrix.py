from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Given an m x n matrix, return all elements of the matrix in spiral order.

        Example 1:
        Input: matrix = [[1,2,3],
                         [4,5,6],
                         [7,8,9]]
        Output: [1,2,3,6,9,8,7,4,5]

        Example 2:
        Input: matrix = [[1,2,3,4],
                         [5,6,7,8],
                         [9,10,11,12]]
        Output: [1,2,3,4,8,12,11,10,9,5,6,7]
        """
        res = []
        if not matrix:
            return res
            
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            # 1. Traverse Right (Top Row)
            # range is [left, right)
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # 2. Traverse Down (Right Col)
            # range is [top, bottom)
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            # CHECK: A critical check to ensure we haven't crossed pointers
            # after the first two moves.
            if not (left < right and top < bottom):
                break
                
            # 3. Traverse Left (Bottom Row)
            # range is reversed: starts at right-1, goes down to left-1
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # 4. Traverse Up (Left Col)
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res

if __name__ == "__main__":
    solver = Solution()
    
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"Spiral: {solver.spiralOrder(mat)}")
    # Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]