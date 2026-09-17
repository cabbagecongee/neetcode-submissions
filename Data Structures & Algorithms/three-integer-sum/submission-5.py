class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_n = sorted(nums)
        result = []

        for idx, num in enumerate(sort_n):
            if idx > 0 and num == sort_n[idx - 1]:
                continue
            
            l, r = idx + 1, len(sort_n) - 1

            while l < r:
                three_sum = sort_n[idx] + sort_n[l] + sort_n[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([sort_n[idx], sort_n[l], sort_n[r]])
                    l += 1
                    while sort_n[l - 1] == sort_n[l] and l < r:
                        l += 1

        return result
