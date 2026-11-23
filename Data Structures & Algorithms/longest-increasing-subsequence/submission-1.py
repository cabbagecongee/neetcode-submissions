class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # only delete if it is not increasing
        cache = {} # i : max size at idx i

        def dp(i, prev): 
            # two choices for current: keep or don't keep
            # must skip if it is not strictly increasing
            if cache.get((i, prev)) != None:
                return cache.get((i, prev))
            if i >= len(nums):
                return 0
            if i == 0:
                size = max(dp(1, -1), dp(1, 0)+1)
                cache[(i, prev)] = size
                return size
            size = 0
            if prev == -1:
                size = max(dp(i+1, -1), dp(i+1 , i)+1)

            else:
                if nums[i] > nums[prev]:
                    size = max(dp(i+1, i)+1, dp(i+1 , prev))
                else:
                    size = dp(i+1 , prev)
            cache[(i, prev)] = size
            return size

        return dp(0, -1)
        