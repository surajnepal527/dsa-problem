class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []
        def solve(ans):
            if len(ans) == len(nums):
                res.append(ans.copy())
            for i in range(len(nums)):
                if nums[i] not in ans:
                    ans.append(nums[i])
                    solve(ans)
                    ans.pop()
            
        solve(ans)
        return res
        
        
        