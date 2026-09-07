class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+","-","*","/"]:
                t1 = stack.pop()
                t2 = stack.pop()
                if i == "+":
                    res = t2 + t1
                elif i == "-":
                    res = t2 - t1
                elif i == "*":
                    res = t2 * t1
                elif i == "/":
                    res = int(t2 / t1)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack.pop()