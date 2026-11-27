class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {} # (x, y) : # unique paths from (x, y)

        def dp(x, y):
            if cache.get((x,y)) != None:
                return cache[(x, y)]
            
            if x == m - 1 and y == n - 1:
                cache[(x, y)] = 1
                return 1 
            
            ret1, ret2 = 0, 0
            if x < m - 1:
                ret1 = dp(x+1, y)
                cache[(x+1, y)] = ret1
            
            if y < n - 1:
                ret2 = dp(x, y+1)
                cache[(x, y+1)] = ret2
            
            cache[(x, y)] = ret1 + ret2
            return cache[(x, y)]
        
        return dp(0, 0)

            
            