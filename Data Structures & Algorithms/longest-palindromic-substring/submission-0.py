class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        length = 0

        for i in range(len(s)):
            # check odd
            r, l = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > length:
                    length =  r - l + 1
                    output = s[l:r+1]
                r+=1
                l-=1
            
            # check even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > length:
                    length = r - l + 1
                    output = s[l:r+1]
                r += 1
                l -= 1
            
        return output