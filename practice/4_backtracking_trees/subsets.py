from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        PROBLEM DESCRIPTION:
        Given an integer array nums of unique elements, return all possible subsets (the power set).
        The solution set must not contain duplicate subsets. Return the solution in any order.
        
        Example:
        Input: nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        """
        res = []
        
        def dfs(index, path):
            # TODO: Implement Include/Exclude logic
            if index>=len(nums):
                res.append(path[:])
                return
            
            path.append(nums[index])
            dfs(index+1,path)

            path.pop()

            dfs(index+1,path)
            
        dfs(0, [])
        return res

# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([1, 2, 3], 8), # Expect 8 subsets
        ([0], 2)        # Expect 2 subsets
    ]
    
    for i, (nums, expected_count) in enumerate(test_cases):
        result = solver.subsets(nums)
        print(f"Test Case {i+1}: Input={nums}")
        print(f"  Output Count: {len(result)}")
        print(f"  Result: {result}")
        print("-" * 30)