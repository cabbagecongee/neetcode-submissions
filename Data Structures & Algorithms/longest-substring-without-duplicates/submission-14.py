class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = {} # key:value -> char:idx in str
        l, r = 0, 0
        max_length = 0
        while r < len(s):
            if unique_chars.get(s[r]) != None:
                idx = unique_chars[s[r]]
                for i in range(l, idx):
                    unique_chars[s[i]] = None
                l = idx + 1
            else:
                length = r - l +1
                max_length = max(max_length, length)
            unique_chars[s[r]] = r
            r += 1
        return max_length
