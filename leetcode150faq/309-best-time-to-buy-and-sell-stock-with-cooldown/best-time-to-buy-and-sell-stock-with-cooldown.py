class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, dp = len(prices), {}
        def solve(idx, buying):
            if idx >= n: return 0
            if (idx, buying) in dp: return dp[(idx, buying)]
            if buying:
                buy_profit = solve(idx+1, not buying) - prices[idx]
                not_buy_profit = solve(idx+1, buying)
                dp[(idx, buying)] = max(buy_profit, not_buy_profit)
            else:
                sell_profit = solve(idx+2, not buying) + prices[idx]
                not_sell_profit = solve(idx+1, buying)
                dp[(idx, buying)] = max(sell_profit, not_sell_profit)
            return dp[(idx, buying)]
        return solve(0, True)
        