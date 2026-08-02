class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in seen.keys():
                return [seen.get(diff), idx]
            seen[val] = idx
