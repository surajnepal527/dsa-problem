class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            profit = prices[i]-min_so_far
            min_so_far = min(min_so_far, prices[i])
            maxProfit = max(maxProfit, profit)
        return maxProfit


        