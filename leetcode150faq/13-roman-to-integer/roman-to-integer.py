class Solution:
    def romanToInt(self, s: str) -> int:
        r_map = {
            "M": 1000,
            "CM" : 900,
           "D":  500,
            "CD" : 400,
             "C" : 100,
            "XC" : 90,
             "L" : 50,
             "XL" : 40,
             "X" : 10,
            "IX" : 9,
            "V" : 5 ,
           "IV"  :4,
             "I" : 1
        }
        res = 0
        i = 0
        for rom,num in r_map.items():
            tmp = 0
            while i < len(s) and rom == s[i:i+len(rom)]:
                res += num
                i += len(rom)
        return res



