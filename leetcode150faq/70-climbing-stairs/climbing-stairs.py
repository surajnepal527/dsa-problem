class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [-1]*(n+1)
        memo[0] = 1
        def solve(n):
            if n == 0:
                return memo[n]
            if n < 0:
                return 0
            if memo[n] != -1:
                return memo[n] 
            stepone = solve(n-1)
            steptwo = solve(n-2)
            memo[n] = stepone + steptwo
            return memo[n]
        return solve(n)
    





        
        
        