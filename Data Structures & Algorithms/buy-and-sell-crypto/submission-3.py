class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max_profit = 0
        while r < len(prices):
            difference = prices[r] - prices[l]
            if difference < 0:
                l = r
            max_profit = max(max_profit, difference)
            r += 1
        
        return max_profit


