class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max_profit = 0
        min_so_far = prices[0]
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_so_far)
            min_so_far = min(min_so_far, price)
        return max_profit


        