class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    l = sorted([nums[i],nums[j],nums[k]])
                    if sum(l) == 0 and l not in output:
                        output.append(l)
        return output
