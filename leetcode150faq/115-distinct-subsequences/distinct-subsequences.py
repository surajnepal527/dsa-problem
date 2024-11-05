class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len, t_len = len(s), len(t)
        memo = {}
        def solve(i, k):
            if k == t_len: return 1
            if i >= s_len: return 0
            if (i, k) in memo: return memo[(i,k)]
            ans = 0
            if s[i] == t[k]:
               ans +=  solve(i+1, k+1)
            ans += solve(i+1, k)
            memo[(i,k)] = ans
            return memo[(i,k)]
        return solve(0,0)
            
        