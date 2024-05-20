class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 1:
            return 0
        max_profit = 0
        max_price = prices[len(prices) - 1]
        i = len(prices) - 2
        while i >= 0:
            if max_price < prices[i + 1]:
                max_price = prices[i  + 1]
            current_profit = max_price - prices[i]
            if current_profit > max_profit:
                max_profit = current_profit
            i = i - 1
        return max_profit

        