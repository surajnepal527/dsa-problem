class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def solve(i, oc):
            if oc < 0: return False
            if i >= len(s) and oc != 0: return False
            if i >= len(s) and oc == 0: return True
            if (i,oc) in dp: return dp[(i,oc)]
            if s[i] == "*":
                take_open = solve(i+1, oc+1)
                take_close = solve(i+1, oc-1)
                take_empty = solve(i+1, oc)
                dp[(i, oc)] =  take_open or take_close or take_empty
                return dp[(i, oc)]
            elif s[i] == "(":
                dp[(i, oc)] =  solve(i+1, oc+1)
                return dp[(i, oc)]
            else:
                dp[(i, oc)] = solve(i+1, oc-1)
                return dp[(i,oc)]
        return solve(0,0)

        
        