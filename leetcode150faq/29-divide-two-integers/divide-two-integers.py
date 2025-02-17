class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 -1
        sign = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            temp , i = divisor , 1
            while dividend >= temp<<1:
                temp <<= 1
                i <<= 1
            ans += i
            dividend -= temp
        
        if sign:
            ans  = -ans
        if ans < -2**31:
            return -2**31
        elif ans > 2**31 - 1:
            return 2**31 -1
        else:
            return ans
        