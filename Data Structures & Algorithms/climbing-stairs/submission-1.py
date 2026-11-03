class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache = {1: 1,
                      2: 2}
        paths = 0
        def dynamic(steps_left):
            try: 
                self.cache[steps_left]
                return self.cache[steps_left]
            except:
                pass
            if steps_left == 1:
                return 1
            elif steps_left == 2:
                return 2
            else:
                p1 = dynamic(steps_left - 1)
                p2 = dynamic(steps_left - 2)
                self.cache[steps_left] = p1 + p2
                return self.cache[steps_left]
        
        return dynamic(n)