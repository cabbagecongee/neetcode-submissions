class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', 
            '}': '{', 
            ']': '['}
        stack = []

        for c in s:
            if c in d.keys():
                if stack:
                    check = stack.pop()
                    if d[c] != check:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        return not stack