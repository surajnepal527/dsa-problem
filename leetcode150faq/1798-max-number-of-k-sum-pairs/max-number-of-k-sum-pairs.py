class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}
        operation = 0
        for num in nums:
            complement = k - num
            if complement in count and count[complement] > 0:
                operation += 1
                count[complement] -= 1
            else:
                count[num] = count.get(num, 0) + 1
        
        return operation