class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        tmp = (a|b)^c
        res = (a&b)&tmp
        ans = 0
        while tmp!=0:
            if tmp&1 == 1:
                ans += 1
            tmp = tmp>>1
        
        while res != 0:
            if res&1 == 1:
                ans += 1
            res = res>>1
        
        return ans

