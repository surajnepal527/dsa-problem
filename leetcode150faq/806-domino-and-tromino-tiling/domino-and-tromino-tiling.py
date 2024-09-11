class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod_val = 10 ** 9 + 7
        if n == 1 or n == 2:
            return n
        t = [-1] *(n+1)
        t[1] = 1
        t[2] = 2
        t[3] = 5

        for i in range(4, n+1):
            t[i] = ((2 * t[i-1]) % mod_val) + (t[i-3] % mod_val) % mod_val
        
        return t[n] % mod_val



        