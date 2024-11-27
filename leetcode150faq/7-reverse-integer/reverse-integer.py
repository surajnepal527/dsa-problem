import sys
class Solution:
    def reverse(self, x: int) -> int:
        maxValue = 2147483647
        posNum = True
        if x < 0: posNum = False
        i = 0
        if posNum:
            n = len(str(x))
        else:
            n = len(str(x)) - 1
            x *= -1
        rNum = 0
        while i < n:
            num = x%10
            x = x//10
            rNum += num * (10**(n-i-1))
            i += 1
        if rNum > maxValue  : return 0
        return rNum if posNum else rNum*-1

        