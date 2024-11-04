class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def solve(idx, cur_sum):
            if idx >= len(coins): return 0
            if cur_sum == amount: return 1
            if (idx, cur_sum) in memo: return memo[(idx, cur_sum)]
            total_count = 0
            if cur_sum + coins[idx] <= amount:
                total_count += solve(idx, cur_sum+coins[idx])
            total_count += solve(idx+1, cur_sum)
            memo[(idx, cur_sum)] =  total_count
            return memo[(idx, cur_sum)]

        return solve(0, 0)