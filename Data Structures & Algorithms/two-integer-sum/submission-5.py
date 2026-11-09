class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for idx, num in enumerate(nums):
            dictionary[num] = idx
        
        for i, num in enumerate(nums):
            find = dictionary.get(target - num)
            if find and find != i:
                return [min(i, find), max(i, find)]
        
