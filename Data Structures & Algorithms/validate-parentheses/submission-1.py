from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        OPEN = ["(", "{", "["]
        CLOSE = [")", "}", "]"]

        st = deque()
        for small in s:
            if small in OPEN:
                st.appendleft(small)
            else:
                try:
                    x = st.popleft()
                except IndexError:
                    return False
                if small == ")" and x != "(":
                    return False
                elif small == "}" and x != "{":
                    return False
                elif small == "]" and x != "[":
                    return False
        if not st:
            return True
        return False