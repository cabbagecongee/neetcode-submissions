from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sort_l = [[] for _ in range(n + 1)]
        counts = Counter(nums)

        for num, c in counts.items():
            sort_l[c].append(num)
        
        output = []
        ok = 0
        for i in range(n, -1, -1):
            for j in sort_l[i]:
                output.append(j)
                ok += 1
            if ok == k:
                return output