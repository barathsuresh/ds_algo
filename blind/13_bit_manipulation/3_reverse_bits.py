class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse bits of a given 32 bits unsigned integer.

        Note: In Python, integers are arbitrarily large, so we must be careful 
        to treat the input essentially as a 32-bit stream.

        Example 1:
        Input: n = 00000010100101000001111010011100
        Output:    964176192 (00111001011110000010100101000000)
        """
        res = 0
        
        for _ in range(32):
            # 1. Shift result to the left to open up the '0' position
            res = res << 1
            
            # 2. Get the last bit of n
            bit = n & 1
            
            # 3. Add that bit to the 0 position of result
            res = res | bit
            
            # 4. Shift n to the right to process the next bit
            n = n >> 1
            
        return res

if __name__ == "__main__":
    solver = Solution()
    
    # Example: 43261596 
    # Binary: 00000010100101000001111010011100
    # Reversed: 00111001011110000010100101000000 (964176192)
    n = 43261596
    print(f"Original: {n}")
    print(f"Reversed: {solver.reverseBits(n)}")
    # Expected: 964176192