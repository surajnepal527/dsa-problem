import heapq
class MedianFinder:

    def __init__(self):
        self.max_left_heap = []
        self.min_right_heap = []
        

    def addNum(self, num: int) -> None:
        if len(self.max_left_heap) == 0 or num < -self.max_left_heap[0]:
            heapq.heappush(self.max_left_heap, -num)
        else:
            heapq.heappush(self.min_right_heap, num)
        ##balancing heap
        if len(self.min_right_heap) > len(self.max_left_heap):
            heapq.heappush(self.max_left_heap, -heapq.heappop(self.min_right_heap))
        while len(self.max_left_heap) - len(self.min_right_heap) > 1:
            heapq.heappush(self.min_right_heap, -heapq.heappop(self.max_left_heap))
        
        

    def findMedian(self) -> float:
        if len(self.max_left_heap) == len(self.min_right_heap):
            return (-self.max_left_heap[0] + self.min_right_heap[0])/2.0
        else:
           return -self.max_left_heap[0]/1.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()