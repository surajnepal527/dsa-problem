class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        ans = []
        if numRows == 1:
            res.append([1])
            return res
        elif numRows == 2:
            res.append([1])
            res.append([1,1])
            return res
        else:
            res.append([1])
            res.append([1,1])
            for n in range(3,numRows+1):
                ans = []
                tmp = 1
                ans.append(tmp)
                for i in range(1, n):
                    tmp = tmp * (n-i)
                    tmp = tmp/i
                    ans.append(int(tmp))
                res.append(ans.copy())
        return res

        
        