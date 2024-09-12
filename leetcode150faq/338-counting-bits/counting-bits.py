class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n+1):
            if i == 0:
                ans.append(0)
            elif i % 2 == 0:
                ans.append(ans[i//2])
            else:
                ans.append(ans[i//2] + 1)
        return ans
