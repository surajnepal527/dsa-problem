class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid_char = {"+","-","/","*"}
        for ch in tokens:
            if ch in valid_char:
                a, b = stack.pop(), stack.pop()
                if ch == "+":
                    stack.append(a+b)
                elif ch == "*":
                    stack.append(a*b)
                elif ch == "/":
                    stack.append(int(b/a))
                else:
                    stack.append(b-a)
            else:
                stack.append(int(ch))
        return stack[-1]
                
                
                
 
        