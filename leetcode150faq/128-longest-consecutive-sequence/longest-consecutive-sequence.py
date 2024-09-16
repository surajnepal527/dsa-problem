class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset = set()
        ans = 1
        for num in nums:
            hashset.add(num)
        
        for num in nums:
            cur = num
            if cur-1 not in hashset:
                lcs = 0
                while cur in hashset:
                    lcs += 1
                    cur = cur+1
                ans = max(ans, lcs)

        return ans        
                


        