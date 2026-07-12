class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens.pop())
        for s in tokens:
            if s  in ["*","/","-","+"]:
                num1 = stack.pop()
                num2 = stack.pop()
                if s == "+":
                    ans = (num2 + num1)
                if s == "-":
                    ans = (num2 - num1)
                if s == "*":
                    ans = (num2 * num1)
                if s == "/":
                    ans = int(num2 / num1)
    
                stack.append(ans)
            else:
                stack.append(int(s))
        return ans
        
            


