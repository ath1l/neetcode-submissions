class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['{','[','(']:
                stack.append(c)
            if c in ['}',']',')']:
                if not stack:
                    return False
                r = {'{':'}','(':')','[':']'}
                res = stack.pop()
                if r[res] != c:
                    return False
        if not stack:
            return True
        else:
            return False