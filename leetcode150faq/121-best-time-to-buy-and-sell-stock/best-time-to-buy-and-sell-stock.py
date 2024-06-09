class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_profit = 0
        max_profit = 0
        if len(prices) == 0:
            return max_profit
            
        min_min = prices[0]
        for i in range (1, len(prices)):
            if prices[i] < min_min:
                min_min = prices[i]
            cur_profit = prices[i] - min_min
            if cur_profit > max_profit:
                max_profit = cur_profit

        return max_profit

        

