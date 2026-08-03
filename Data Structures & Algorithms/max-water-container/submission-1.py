class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amt = 0
        i, j = 0, len(heights)-1

        while i < j:
            area = (j-i) * min(heights[i], heights[j])
            max_amt = max(area, max_amt)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_amt
        
