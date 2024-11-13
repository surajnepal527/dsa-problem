class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        t = [[False for _ in range(n+1)] for _ in range(n+1)]
        t[n][0] = True
        for i in range(n-1, -1, -1):
            for open in range(n+1):
                isValid = False
                if s[i] == "*":
                    isValid = t[i+1][open]
                    if open > 0:
                        isValid =  isValid or t[i+1][open-1]
                    if open < n:
                        isValid = isValid or t[i+1][open+1]
                elif s[i] == "(":
                    if open < n:
                        isValid = t[i+1][open+1]
                elif open > 0:
                    isValid = t[i+1][open-1]
                t[i][open] = isValid
        return t[0][0]
        