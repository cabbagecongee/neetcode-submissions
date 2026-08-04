class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        
        for n in nums:
            if d.get(n) is None:
                d[n] = 1
            else:
                return True
            
        return False