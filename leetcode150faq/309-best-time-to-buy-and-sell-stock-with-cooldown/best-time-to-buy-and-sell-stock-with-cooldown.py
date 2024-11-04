class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0  or n == 1: return 0
        t = [0] * n
        t[1] = max(prices[1]- prices[0], 0)
        for i in range(2, n):
            t[i] = t[i-1]
            for j in range(0, i):
                today_profit = prices[i] - prices[j]
                prev_profit = t[j-2] if j-2 >= 0 else 0 
                t[i] = max(t[i], today_profit+ prev_profit)
        return t[n-1]

        
        