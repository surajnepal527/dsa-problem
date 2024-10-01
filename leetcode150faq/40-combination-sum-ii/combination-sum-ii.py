class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def solve(cur, ans, cur_sum):
            if cur_sum == target:
                res.append(ans.copy())
                return
            if cur >= len(candidates) or cur_sum > target:
                return

            #keep
            ans.append(candidates[cur])
            solve(cur+1, ans, cur_sum+candidates[cur])
            ans.pop()
            #skip
            next_cur = cur+1
            while next_cur < len(candidates) and candidates[next_cur] == candidates[cur]:
                next_cur += 1
            solve(next_cur, ans, cur_sum)
        solve(0,[],0)
        return res
