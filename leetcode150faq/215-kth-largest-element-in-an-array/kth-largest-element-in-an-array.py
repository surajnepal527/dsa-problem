import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            if len(max_heap) < k:
                heapq.heappush(max_heap, num)
            elif max_heap[0] < num:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, num)
        
        return max_heap[0]

        