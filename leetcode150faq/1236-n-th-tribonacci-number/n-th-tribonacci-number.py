class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [-1] * (n + 1)
        return self.find(n, t)     
    
    def find(self, n, t):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        if t[n] != -1:
            return t[n]
        
        a = self.find(n-1,t)
        b = self.find(n-2, t)
        c = self.find(n-3,t)
        t[n] = a + b + c
        return t[n]
