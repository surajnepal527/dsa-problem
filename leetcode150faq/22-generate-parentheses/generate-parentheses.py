class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stk = []
        res = []
        def backtracking(openN:int, closeN:int):
            if openN == closeN == n:
                res.append("".join(stk))
                return
            if openN < n:
                stk.append("(")
                backtracking(openN+1, closeN)
                stk.pop()
            
            if closeN < openN:
                stk.append(")")
                backtracking(openN, closeN+1)
                stk.pop()

        backtracking(0, 0)
        return res     
