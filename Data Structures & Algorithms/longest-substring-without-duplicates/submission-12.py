class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        n = len(s)
        char_set = set()

        longest = 0

        while j < n:
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            char_set.add(s[j])
            j+=1
            longest = max(longest, j - i)
        
        return longest