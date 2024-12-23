class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        for i in range(32):
            if (a & 1<<i) | (b & 1<< i) != (c & 1<<i):
                if (c & 1<<i):
                    count += 1
                else:
                    if (a & 1<<i):
                         count += 1
                    if (b & 1<<i):
                        count += 1
        
        return count
        