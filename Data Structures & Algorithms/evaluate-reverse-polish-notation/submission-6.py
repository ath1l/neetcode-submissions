class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s not in ['+','-','*','/']:
                stack.append(int(s))
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                if s == '+':
                    res = t2 + t1
                    stack.append(res)
                if s == '-':
                    res = t2 - t1
                    stack.append(res)
                if s == '*':
                    res = t2 * t1
                    stack.append(res)
                if s == '/':
                    res = int(t2 / t1)
                    stack.append(res)
        return stack.pop()                