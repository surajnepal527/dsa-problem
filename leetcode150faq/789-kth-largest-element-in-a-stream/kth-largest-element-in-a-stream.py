import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = []
        self.k = k
        for num in nums:
            if len(self.max_heap) < k:
                heapq.heappush(self.max_heap,num)
            elif self.max_heap[0] < num:
                heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, num)
        

        

    def add(self, val: int) -> int:
            if len(self.max_heap) < self.k:
                heapq.heappush(self.max_heap,val)
            elif self.max_heap[0] < val:
                heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, val)
            return self.max_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)