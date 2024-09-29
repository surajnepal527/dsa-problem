class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ans = []
        start = 0
        cur_sum = 0
        def solve(start, cur_sum, ans):
            if cur_sum > target or start >= len(candidates):
                return
            elif cur_sum == target:
                res.append(ans.copy())
                return
            ans.append(candidates[start])
            solve(start, cur_sum+ candidates[start], ans)
            ans.pop()
            solve(start+1, cur_sum, ans)
        
        solve(start, cur_sum, ans)
        return res

            


            
        