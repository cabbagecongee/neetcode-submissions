import functools
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        @functools.lru_cache(None)
        def helper(i):
            # so i can either add or not add
            if i>= len(nums):
                return 0
            return max(nums[i] + helper(i+2), helper(i+1))

        return helper(0)
            
            

            
            
            
