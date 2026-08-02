from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_counts = sorted(counts.items(), key=lambda item:item[1], reverse=True)
        output = []
        for i in range(0, k):
            output.append(sorted_counts[i][0])
        return output
        