class Solution:
    def romanToInt(self, s: str) -> int:
        r_map = {
            "M": 1000,
            #"CM" : 900,
           "D":  500,
            #"CD" : 400,
             "C" : 100,
            "#XC" : 90,
             "L" : 50,
             #"XL" : 40,
             "X" : 10,
            #"IX" : 9,
            "V" : 5 ,
           #"IV"  :4,
             "I" : 1
        }
        res = 0
        prev = 0
        i = len(s) - 1
        while i >= 0:
            cur = r_map[s[i]]
            if cur >= prev:
                res += cur
            else:
                res -= cur
            prev = cur
            i -= 1
        return res





