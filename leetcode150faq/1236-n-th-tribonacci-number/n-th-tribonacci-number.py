class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1
            
        a = 0
        b = 1
        c = 1
        d = 1
        for i in range(3, n+1, 1):
            d = a+b+c
            a = b
            b = c
            c = d
        
        return d
        