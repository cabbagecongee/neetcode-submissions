from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        n = len(s)
        i, j = 0, 0
        freq = {}

        while j < n:
            if freq.get(s[j]) is None:
                freq[s[j]] = 1
            else:
                freq[s[j]] += 1
            
            max_freq = max(freq.values())
            replacements = (j - i + 1) - max_freq
            if replacements > k:
                freq[s[i]] -= 1
                i +=1
            j += 1
            max_length = max(j - i, max_length)

        return max_length
