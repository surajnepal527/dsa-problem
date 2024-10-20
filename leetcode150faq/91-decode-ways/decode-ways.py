class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * (len(s) + 1)
        def solve(i):
            if i == len(s): return 1
            if memo[i] != -1: return memo[i]
            if s[i] == '0': return 0          
            memo[i] =  solve(i+1)
            if i + 1 < len(s) and  (s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6)):
                memo[i] += solve(i+2)
            return memo[i]
        
        return solve(0)
        