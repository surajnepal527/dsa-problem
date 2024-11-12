class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def solve(i, oc):
            if oc < 0: return False
            if i >= len(s): return oc == 0
            if (i,oc) in dp: return dp[(i,oc)]
            isValid = False
            if s[i] == "*":
                isValid = solve(i+1, oc+1) or solve(i+1, oc-1) or solve(i+1, oc) 
            elif s[i] == "(":
                isValid =  solve(i+1, oc+1)
            else:
                isValid = solve(i+1, oc-1)
            dp[(i,oc)] = isValid
            return dp[(i,oc)] 
        return solve(0,0)

        
        