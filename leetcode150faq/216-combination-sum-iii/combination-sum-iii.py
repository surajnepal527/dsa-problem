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
        self.solve(start_idx, n , k ,tmp, ans)
        return ans
    
    def solve(self, idx, target , k , tmp, ans):
        if len(tmp) == k and target == 0: 
            ans.append(tmp[:])
            return
        
        if len(tmp) >= k or target <= 0 :
            return

        for i in range(idx, 10, 1):
            tmp.append(i)
            self.solve(i+1, target - i, k,tmp, ans)
            tmp.pop() 
