class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sort = {}
        for n in nums:
            if sort.get(n) != None:
                return True
            else:
                sort[n] = 1
        return False