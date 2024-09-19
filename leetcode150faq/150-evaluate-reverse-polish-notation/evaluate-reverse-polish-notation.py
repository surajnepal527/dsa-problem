class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        add ="+"
        sub = "-"
        mul = "*"
        div = "/"
        op_set = set()
        op_set.add(add)
        op_set.add(sub)
        op_set.add(mul)
        op_set.add(div)
        stk = []
        for ch in tokens:
            if ch == "+":
                stk.append(stk.pop() + stk.pop())
            elif ch == "-":
                a,b = stk.pop(), stk.pop()
                stk.append(b-a)
            elif ch == "*":
                stk.append(stk.pop() * stk.pop())
            elif ch == "/":
                a,b = stk.pop(), stk.pop()
                stk.append(int(b/a))
            else:
                stk.append(int(ch))
                
        return stk[-1]        



        