from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
        ans[i] is the number of 1's in the binary representation of i.

        Example 1:
        Input: n = 2
        Output: [0,1,1]
        Explanation:
        0 --> 0
        1 --> 1
        2 --> 10 (1 bit)

        Example 2:
        Input: n = 5
        Output: [0,1,1,2,1,2]
        """
        # Initialize dp array of size n+1
        dp = [0] * (n + 1)
        
        # Calculate bits for each number i
        for i in range(1, n + 1):
            # dp[i] = dp[i // 2] + (last bit of i)
            # i >> 1 is equivalent to i // 2
            # i & 1 checks if the last bit is 1 (odd number)
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp

if __name__ == "__main__":
    solver = Solution()
    
    # n=5
    # 0: 0
    # 1: dp[0] + 1 = 1
    # 2: dp[1] + 0 = 1
    # 3: dp[1] + 1 = 2
    # 4: dp[2] + 0 = 1
    # 5: dp[2] + 1 = 2
    print(f"Bits for 0 to 5: {solver.countBits(5)}")
    # Expected: [0, 1, 1, 2, 1, 2]