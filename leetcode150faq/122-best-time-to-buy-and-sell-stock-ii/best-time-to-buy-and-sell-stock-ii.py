class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        total_profit = 0
        i = len(prices) - 2
        j = len(prices) - 1
        current_max = prices[j]
        while i >= 0:
            if prices[i] >= current_max:
                current_max = prices[i]
            else:
                current_profit = current_max - prices[i]
                total_profit = total_profit + current_profit
                current_max = prices[i]
            i = i - 1
            j = j - 1
        return total_profit