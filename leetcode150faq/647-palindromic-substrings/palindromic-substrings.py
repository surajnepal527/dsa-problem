class Solution:
    def countSubstrings(self, s: str) -> int:
        #let write down solution for previous problem and see if we can do something with it for current problem
        n = len(s)
        memo = [[-1 for _ in range(n)] for _ in range(n)]
        ans = 0
        solved = set()
        def solve(i, j):
            if i >= j:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            elif s[i] == s[j]:
                memo[i][j] =  solve(i+1, j-1)
                return memo[i][j]
            else:
                memo[i][j] = 0
                return memo[i][j]
        
        for i in range(n):
            for j in range(i, n):
                if solve(i,j) == 1:
                    ans += 1
        
        return ans

        