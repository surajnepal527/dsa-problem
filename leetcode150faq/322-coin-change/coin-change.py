
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        def solve(i, target):
            if target == 0: return 0
            if i >= len(coins) or target < 0: return float('inf')
            if dp[i][target] != -1: return dp[i][target]
            take = 1 + solve(i, target- coins[i]) if target - coins[i] >= 0 else float('inf')
            skip = solve(i+1, target)
            dp[i][target] =  min(take, skip)
            return dp[i][target]
        ans =  solve(0, amount)
        return ans if ans != float('inf') else -1


        