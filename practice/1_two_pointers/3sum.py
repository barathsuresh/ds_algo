from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        PROBLEM DESCRIPTION:
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

        Example 1:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]

        Example 2:
        Input: nums = [0,1,1]
        Output: []

        Example 3:
        Input: nums = [0,0,0]
        Output: [[0,0,0]]
        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[right] + nums[left]
                if current_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif current_sum > 0:
                    right -= 1 # if sum is greater than zero then search for next least element
                else:
                    left += 1
        return res


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]

    for i, (input_nums, expected) in enumerate(test_cases):
        result = solver.threeSum(input_nums)
        print(f"Test Case {i+1}:")
        print(f"  Input: {input_nums}")
        print(f"  Output: {result}")
        # Note: Order of triplets might differ, which is fine,
        # but the contents should match the expected structure.
        print("-" * 30)
