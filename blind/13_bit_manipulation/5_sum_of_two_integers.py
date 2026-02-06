class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Given two integers a and b, return the sum of the two integers 
        without using the operators + and -.

        Example 1:
        Input: a = 1, b = 2
        Output: 3

        Example 2:
        Input: a = -1, b = 1
        Output: 0
        """
        # 32-bit mask in hexadecimal
        mask = 0xFFFFFFFF
        
        # Max positive integer for 32-bit (to handle overflow check later)
        # 0x7FFFFFFF is 2147483647
        
        while b != 0:
            # 1. Calculate the 'sum' without carry
            # (a ^ b) handles 0+1=1, 1+0=1, 0+0=0, 1+1=0
            temp = (a ^ b) & mask
            
            # 2. Calculate the carry
            # (a & b) finds where 1+1 happened
            # << 1 moves the carry to the next position
            b = ((a & b) << 1) & mask
            
            a = temp
            
        # In Python, if the result is negative in 32-bit representation (starts with 1),
        # Python will interpret it as a large positive number because of infinite precision.
        # We check if the 32nd bit is 1. If so, we convert it to the negative number.
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
            
        return a

if __name__ == "__main__":
    solver = Solution()
    
    # 1 (01) + 2 (10)
    # XOR: 01 ^ 10 = 11 (3)
    # AND: 01 & 10 = 00 (Carry 0)
    # b becomes 0, loop ends. Result 3.
    print(f"Sum of 1 + 2: {solver.getSum(1, 2)}")
    
    # -1 (11..11) + 1 (00..01)
    # This involves a ripple carry all the way up.
    print(f"Sum of -1 + 1: {solver.getSum(-1, 1)}")
    # Expected: 0