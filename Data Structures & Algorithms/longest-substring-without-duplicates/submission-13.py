class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        n = len(s)
        char_set = set()

        longest = 0

        for j in range(n):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            char_set.add(s[j])
            longest = max(longest, j - i + 1)
        
        return longest