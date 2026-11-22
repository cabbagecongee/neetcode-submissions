class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        substrings = {}
        def dp(substring):
            # two choices, either break the word up or dont break it up
            if substring == "":
                return True
            if substrings.get(substring) != None:
                    return substrings.get(substring)
            i = 0 
            while i <= len(substring):
                sub = substring[:i]
                if sub in wordDict:
                    ret = dp(substring[i:])
                    substrings[substring[i:]] = ret
                    if ret: return True
                i += 1
            substrings[substring] = False
            return False
        ret = dp(s)
        return ret