from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given an array of distinct integers candidates and a target integer target, return a list of all 
        unique combinations of candidates where the chosen numbers sum to target. 
        You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times. 
        Two combinations are unique if the frequency of at least one of the chosen numbers is different.

        Example 1:
        Input: candidates = [2,3,6,7], target = 7
        Output: [[2,2,3],[7]]

        Example 2:
        Input: candidates = [2,3,5], target = 8
        Output: [[2,2,2,2],[2,3,3],[3,5]]

        Constraints:
        1 <= candidates.length <= 30
        2 <= candidates[i] <= 40
        All elements of candidates are distinct.
        1 <= target <= 40
        """
        res = []
        
        # dfs function
        # i: current index in candidates
        # cur: current combination list
        # total: current sum of the combination
        def dfs(i, cur, total):
            # Base Case 1: Success
            if total == target:
                res.append(cur.copy()) # Important: append a COPY, not the reference
                return
            
            # Base Case 2: Failure (Overshot target or out of bounds)
            if i >= len(candidates) or total > target:
                return
            
            # DECISION 1: Include candidates[i]
            # We add it to 'cur' and call dfs. 
            # Note: We pass 'i' again because we can reuse the same element.
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            
            # Backtrack: Remove the element we just added to try the other path
            cur.pop()
            
            # DECISION 2: Skip candidates[i]
            # We don't add anything, and move index to i + 1
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)
        return res

if __name__ == "__main__":
    solver = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(f"Candidates: {candidates}, Target: {target}")
    print(f"Combinations: {solver.combinationSum(candidates, target)}")
    # Expected: [[2, 2, 3], [7]]