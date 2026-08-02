import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot_prod = 1
        output = [0] * len(nums)
        zeros = {}
        n_zeros = 0

        for idx, num in enumerate(nums):
            if num == 0:
                zeros[idx] = tot_prod * math.prod(nums[idx+1:])
                n_zeros += 1
                if n_zeros > 1:
                    return [0] * len(nums)
            tot_prod *= num

        for i in range(len(nums)):
            if i in zeros:
                output[i] = zeros[i]
            else:
                output[i] = int(tot_prod / nums[i])
        return output  
