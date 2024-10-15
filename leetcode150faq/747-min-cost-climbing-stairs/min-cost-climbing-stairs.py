class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #brute force top down approach
        k = len(cost)
        memo = [-1] * (k+1)
        def solve(pos):
            if pos >= k :
                return 0
            if memo[pos] != -1: return memo[pos]
            oneStep = cost[pos] + solve(pos+1)
            twoStep = cost[pos] + solve(pos+2)
            memo[pos] =  min(oneStep, twoStep)
            return memo[pos]
        start_zero = solve(0)
        start_one = solve(1)
        return min(start_zero, start_one)

        