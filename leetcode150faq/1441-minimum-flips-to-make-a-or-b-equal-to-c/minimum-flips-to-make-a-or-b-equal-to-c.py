class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flip = 0
        while c != 0 or b != 0 or a != 0:
            if c & 1 == 1:
                if a & 1 == 0 and b & 1 == 0:
                    flip += 1
            else:
                if a & 1 == 1:
                    flip += 1
                if b & 1 == 1:
                    flip += 1
            
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return flip

