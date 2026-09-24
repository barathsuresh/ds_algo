class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1]*len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(n-1,-1,-1):
            res[i] *= post
            post *= nums[i]
        
        return res