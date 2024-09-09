import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        kth_largest = nums[0]
        for i in range(k):
            kth_largest = -heapq.heappop(max_heap)
        
        return kth_largest

        