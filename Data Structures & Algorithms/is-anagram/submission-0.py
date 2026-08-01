class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_key = "".join(sorted(s))
        t_key = "".join(sorted(t))

        return s_key == t_key