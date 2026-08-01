from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse = True)
        items = sorted_counts[:k]
        output = []
        for item in items:
            output.append(item[0])

        return output