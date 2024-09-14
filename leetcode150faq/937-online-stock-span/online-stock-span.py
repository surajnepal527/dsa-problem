class Pair:
    def __init__(self, price, span):
        self.price = price
        self.span = span
        
class StockSpanner(object):

    def __init__(self):
        self.stack = []
        
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        while len(self.stack) != 0 and self.stack[-1].price <= price:
            span = span + self.stack[-1].span
            self.stack.pop()
        pair = Pair(price, span)
        self.stack.append(pair)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)