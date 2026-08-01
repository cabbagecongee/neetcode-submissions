class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]