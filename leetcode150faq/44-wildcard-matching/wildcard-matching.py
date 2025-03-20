class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def backtrack(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(s) and j == len(p):
                memo[(i,j)] =  True
                return memo[(i,j)]
            elif j == len(p):
                memo[(i,j)] = False
                return memo[(i,j)]
            elif i == len(s):
                memo[(i,j)] = all(x == "*" for x in p[j:])
                return memo[(i,j)]
            
            if s[i] == p[j] or p[j] == "?":
                memo[(i,j)] = backtrack(i+1, j+1)
                return memo[(i,j)]
            elif p[j] == "*":
                memo[(i,j)] = backtrack(i, j+1) or backtrack(i+1, j)
                return memo[(i,j)]
            memo[(i,j)] = False
            return memo[(i,j)]
            
        return backtrack(0,0)
        