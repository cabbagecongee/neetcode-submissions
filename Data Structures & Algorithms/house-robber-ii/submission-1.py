import functools
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        @functools.lru_cache(None)
        def helper(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            return max(nums[i] + helper(i+2, flag), helper(i+1, flag))
        
        return max(helper(0, True), helper(1, False))
