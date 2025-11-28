from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        PROBLEM DESCRIPTION:
        Given an array nums of distinct integers, return all possible permutations.
        """
        res = []

        # Helper Function
        def backtrack(path):
            # TODO: Write the logic
            # 1. Base Case: If path length equals nums length, we have a complete permutation.

            # 2. Loop through nums
            #    If num is NOT in path:
            #       a. Add num to path
            #       b. Recurse
            #       c. Remove num from path (Backtrack)

            if len(path) == len(nums):
                res.append(path[:])
                return path

            for i in nums:
                if i not in path:
                    path.append(i)
                    backtrack(path)
                    path.pop()

        backtrack([])
        return res


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([1, 2, 3], 6),  # Expect 6 permutations
        ([0, 1], 2),  # Expect 2 permutations
        ([1], 1),
    ]

    for i, (nums, expected_count) in enumerate(test_cases):
        result = solver.permute(nums)
        print(f"Test Case {i+1}: Input={nums}")
        print(f"  Output Count: {len(result)}")
        print(f"  First 3 results: {result[:3]}")
        print("-" * 30)
