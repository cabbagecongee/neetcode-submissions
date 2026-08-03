class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        n = len(prices)

        if n < 2:
            return 0

        max_profit = 0
        while i < n and j < n:
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

            if prices[i] > prices[j]: 
                i = j
            
            j += 1
        return max_profit
        