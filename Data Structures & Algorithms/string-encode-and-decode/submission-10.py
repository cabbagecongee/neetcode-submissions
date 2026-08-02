class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            n = len(s)
            output += str(n) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        output = []

        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            output.append(s[j+1: j + length + 1])
            i = j + length + 1
        return output

            