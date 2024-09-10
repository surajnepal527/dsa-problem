class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        start_idx = 1
        ans = []
        tmp = []
        cur_count = 0
        self.solve(start_idx, n , k , cur_count, tmp, ans)
        return ans
    
    def solve(self, idx, n , k ,cur_count, tmp, ans):
        #if idx >= 10:
        #    return
        if cur_count == k:
            sum = 0
            for num in tmp:
                sum += num
            if sum == n:
                tmp_copy = tmp[:]
                ans.append(tmp_copy)
            return
        for i in range(idx, 10, 1):
            tmp.append(i)
            self.solve(i+1, n, k, cur_count + 1,tmp, ans)
            tmp.pop() 
