import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        x = heapq.nlargest(k, nums)
        print(x)
        return x[k-1]

        