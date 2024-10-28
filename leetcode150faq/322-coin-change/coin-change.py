
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       
        dp = [[-1 for _ in range(len(coins))] for _ in range(amount+1)]
        def solve(i, target):
            if target == 0: return 0
            if i >= len(coins) or target < 0: return float('inf')
            if dp[target][i] != -1: return dp[target][i]
            take = 1 + solve(i, target- coins[i]) if target - coins[i] >= 0 else float('inf')
            skip = solve(i+1, target)
            dp[target][i] =  min(take, skip)
            return dp[target][i]
        ans =  solve(0, amount)
        return ans if ans != float('inf') else -1


        