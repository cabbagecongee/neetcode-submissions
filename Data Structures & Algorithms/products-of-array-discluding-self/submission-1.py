import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * len(nums)

        pre = 1
        for i in range(1, n):
            pre *= nums[i-1]
            output[i] = pre
        
        post = 1
        for i in range(n-2, -1, -1):
            post *= nums[i+1]
            output[i] *= post
        output[0] = post

        return output

