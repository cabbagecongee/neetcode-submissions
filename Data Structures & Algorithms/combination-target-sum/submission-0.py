class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curr, total):
            if i >= len(nums) or total > target:
                return None
            if total == target:
                res.append(curr)
                return None
                
            backtrack(i, curr + [nums[i]], total + nums[i])
            backtrack(i + 1, curr, total)
            return None
        
        backtrack(0, [], 0)
        return res