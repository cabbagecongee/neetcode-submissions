class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        n = len(s)

        longest = 0

        while j < n:
            substring = s[i:j]
            while s[j] in substring:
                i += 1
                substring = s[i:j]
            j += 1
            length = j - i
            longest = max(longest, length)
        
        return longest