class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalJumps = 0
        destination = len(nums) - 1
        coverage = 0
        lastJumpIndex = 0

        if len(nums) == 1:
            return 0
        
        for i in range(0, len(nums)):
            coverage = max(coverage, nums[i] + i)

            if i == lastJumpIndex:
                lastJumpIndex = coverage
                totalJumps += 1
                
                if coverage >= destination:
                    return totalJumps