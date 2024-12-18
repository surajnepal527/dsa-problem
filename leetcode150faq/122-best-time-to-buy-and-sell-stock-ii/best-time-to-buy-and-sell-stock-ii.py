class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for p in range(1, len(prices)):
            cur_profit = prices[p] - prices[p-1]
            if cur_profit > 0:
                max_profit += cur_profit
        return max_profit
        