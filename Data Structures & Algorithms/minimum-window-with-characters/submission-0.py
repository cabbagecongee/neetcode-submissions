class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(t) == "":
            return ""
        
        window, dict_t = {}, {}

        for c in t:
            dict_t[c] = 1 + dict_t.get(c, 0)

        window_range, window_length = [-1, -1], float("inf")
        have, need = 0, len(dict_t)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in dict_t and window[c] == dict_t[c]: 
                have += 1
            while have == need: 
                if (r - l + 1) < window_length:
                    window_range = [l, r]
                    window_length = r - l + 1
                window[s[l]] -= 1
                if s[l] in dict_t and window[s[l]] < dict_t[s[l]]:
                    have -= 1
                l += 1
        
        return s[window_range[0]: window_range[1] + 1]

                
        
                    
        


