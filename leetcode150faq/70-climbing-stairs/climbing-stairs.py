class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [-1]*(n+1)
        memo[0] = 1
        def solve(n):
            if n <= 0:
                return memo[n]
            if memo[n] != -1:
                return memo[n] 
            stepone = solve(n-1)
            if n >= 2:
                steptwo = solve(n-2)
                memo[n] = stepone + steptwo
                return memo[n]
            memo[n] = stepone
            return memo[n]
        return solve(n)
    





        
        
        