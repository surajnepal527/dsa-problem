class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        tmp = 1
        n = rowIndex +1
        res = [1]
        for i in range(1, n):
            tmp = tmp * (n-i)
            tmp = tmp/i
            res.append(int(tmp))
        return res

        