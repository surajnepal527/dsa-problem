class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_so_far = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            cur_profit = prices[i] - min_so_far
            max_profit = max(max_profit, cur_profit)
            min_so_far = min(min_so_far, prices[i])
        
        return max_profit
        