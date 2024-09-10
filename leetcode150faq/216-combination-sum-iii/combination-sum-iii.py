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
        cur_sum = 0
        self.solve(start_idx, n , k , cur_count, tmp, ans, cur_sum)
        return ans
    
    def solve(self, idx, n , k ,cur_count, tmp, ans, cur_sum):
        if cur_count < k and cur_sum >= n:
            return
        if cur_count == k and cur_sum == n:
            tmp_copy = tmp[:]
            ans.append(tmp_copy)
            return
        
        if cur_count >= k and cur_sum != n :
            return

        for i in range(idx, 10, 1):
            tmp.append(i)
            cur_sum += i
            self.solve(i+1, n, k, cur_count + 1,tmp, ans, cur_sum)
            cur_sum -= i
            tmp.pop() 
