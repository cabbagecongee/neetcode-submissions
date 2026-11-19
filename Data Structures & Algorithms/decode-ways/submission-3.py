class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J', '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z',
}
        memo = {}
        self.count = 0
        def dynamic_programming(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            
            ways = 0
            # length 1
            if mapping.get(s[i:i+1]) != None:
                ways += dynamic_programming(i+1)
            
            # length 2
            if i + 1 < len(s) and mapping.get(s[i:i+2]) != None:
                ways += dynamic_programming(i+2)            

            memo[i] = ways
            return memo[i]
        dynamic_programming(0)
        return dynamic_programming(0)