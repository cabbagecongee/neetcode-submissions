import math 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)

        count = 1
        max_count = 0
        for num in nums:
            if num-1 not in numsset:
                curr = num
                while curr + 1 in numsset:
                    count += 1
                    curr += 1
                max_count = max(count, max_count)
                count = 1
        
        return max_count

