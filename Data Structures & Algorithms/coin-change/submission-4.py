class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ts is not greedy
        coins = sorted(coins)
        cache = {} # curr : shortest
        def dp(curr):
            if cache.get(curr) != None:
                return cache[curr]
            if curr == amount:
                cache[curr] = 0
                return 0
            counts = []
            i = 0
            while i < len(coins) and curr + coins[i] <= amount:
                save = dp(curr+coins[i])
                if save != -1:
                    counts.append(1 + save)
                i += 1
            if counts:
                cache[curr] = min(counts)
                return cache[curr]
            else:
                cache[curr] = -1
                return -1
        dp(0)
        return dp(0)
