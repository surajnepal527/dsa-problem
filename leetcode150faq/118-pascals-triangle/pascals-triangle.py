class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l1 = [1]
        l2 = [1,1]
        ans = []
        if numRows == 1:
            ans.append(l1)
            return ans
        elif numRows == 2:
            ans.append(l1)
            ans.append(l2)
            return ans
        else:
            ans.append(l1)
            ans.append(l2)
            for i in range(2, numRows):
                tmp_lst = []
                for j in range(i+1):
                    if j == 0 or j == i:
                        tmp_lst.append(1)
                    else:
                        tmp_lst.append(ans[i-1][j-1] + ans[i-1][j])
                ans.append(tmp_lst)
            return ans
            


        