import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for wt in stones:
            heapq.heappush(max_heap, -wt)
        while max_heap:
            if len(max_heap) == 1:
                return -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            diff = y - x
            if diff > 0:
                heapq.heappush(max_heap, -diff)
        return 0
        