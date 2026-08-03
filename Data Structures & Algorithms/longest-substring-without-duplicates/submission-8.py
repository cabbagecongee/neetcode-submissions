class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        i, j = 0, 0

        substring = ""
        while j < n:
            while s[j] in s[i:j]:
                i += 1
            substring = s[i:j]
            j += 1
            length = j - i
            max_len = max(length, max_len)
        
        return max_len

                