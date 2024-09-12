class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t = [[-1 for _ in range(2)] for _ in range(5001)]
        buy = True
        return self.solve(prices,0,buy, t)

    def solve(self, prices, day, buy, t):
        if day >= len(prices):
            return 0
        
        if t[day][buy] != -1:
            return t[day][buy]

        profit = 0
        if buy:
            take = self.solve(prices,day+1, False, t) - prices[day]
            not_take = self.solve(prices,day+1, True, t)
            profit =  max(profit,take, not_take)
        else:
            sell = prices[day] + self.solve(prices, day+2, True, t)
            not_sell= self.solve(prices, day+1, False, t)
            profit =  max(profit, sell, not_sell)
        
        t[day][buy] = profit
        return t[day][buy]
        