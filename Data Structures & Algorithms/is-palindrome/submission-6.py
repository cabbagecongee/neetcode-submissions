class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        n = len(s)
        i, j = 0, n-1
        while i < n and j > -1:
            while i < n and not s[i].isalnum():
                i += 1
            while  j > -1 and not s[j].isalnum():
                j -= 1
            if i < n and j > -1:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
        return True