class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = True
        t = [[-1 for _ in range(2)] for _ in range(50001)]

        return self.solve(prices, fee, 0, buy, t)
    
    def solve(self, prices, fee, day, buy, t):
        if day >= len(prices):
            return 0
        
        if t[day][buy] != -1:
            return t[day][buy]
        profit = 0
        if buy:
            take =  self.solve(prices,fee, day+1, False, t ) - prices[day]
            not_take = self.solve(prices, fee, day+1, True , t)
            profit = max(profit, take, not_take)
        
        else:
            sell = prices[day] - fee + self.solve(prices, fee, day+1, True,t)
            not_sell = self.solve(prices, fee, day+1, False, t)
            profit = max(profit, sell, not_sell)
        
        t[day][buy] = profit
        return t[day][buy]
