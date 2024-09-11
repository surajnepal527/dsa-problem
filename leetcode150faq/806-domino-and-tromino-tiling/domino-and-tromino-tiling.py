class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod_val = (10 ** 9) + 7
        t = [-1] * (n + 1)
        return self.solve(n, mod_val, t)

    def solve(self, n, mod_val, t):
        if n == 1 or n == 2:
            return n
        if n == 3:
            return 5

        if t[n] != -1:
            return t[n]
        
        t[n] =  ((2 * self.solve(n-1, mod_val, t)) % mod_val + (self.solve(n-3, mod_val, t)) % mod_val)%mod_val
        
        return t[n]