class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {} # number : index
        result = set()

        for idx, num in enumerate(nums):
            d[num] = idx
        
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                val = d.get(-(nums[i] + nums[j]), False)
                if i != j and val and val != i and val != j:
                    sort_t = sorted([nums[i], nums[j], nums[val]])
                    result.add(tuple(sort_t))
        
        return list(result)
