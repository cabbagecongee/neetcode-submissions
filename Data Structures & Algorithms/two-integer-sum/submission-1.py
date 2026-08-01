class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        d = {}
        for i, num in enumerate(nums):
            diff = target - num
            if d.get(diff) != None:
                return [d[diff], i]
            d[num] = i

