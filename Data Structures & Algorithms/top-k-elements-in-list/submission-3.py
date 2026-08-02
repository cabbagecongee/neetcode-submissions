from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in counts.items():
            buckets[val].append(key)
        output = []
        for i in range(len(nums), -1, -1):
            for n in buckets[i]:
                output.append(n)
                if len(output) == k:
                    return output