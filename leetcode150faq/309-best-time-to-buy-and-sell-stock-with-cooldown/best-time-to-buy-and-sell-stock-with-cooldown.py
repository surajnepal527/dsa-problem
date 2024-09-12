class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        t = [-1 for _ in range(50001)]
        t[0] = 0
        t[1] = max(prices[1]- prices[0], 0)
        for i in range(2, n): 
            t[i] = t[i-1]
            for j in range(i):
                today_profit = prices[i] - prices[j]
                prev_profit = t[j-2] if j >= 2 else 0
                t[i] = max(t[i], today_profit + prev_profit)

        return t[n-1]
