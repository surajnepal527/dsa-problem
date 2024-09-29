class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []
        start = 0
        nums.sort()
        def solve(start, ans):
            if start >= len(nums):
                if ans not in res:
                    res.append(ans.copy())
                return
            #skip
            solve(start+1, ans)
            #keep
            ans.append(nums[start])
            solve(start+1, ans)
            ans.pop()
        solve(start, ans)
        return res
            
        