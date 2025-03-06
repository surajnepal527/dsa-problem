import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == 0 or num < -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        #balance heap
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        if len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0]+self.large[0])/2.0
        return -self.small[0]/1.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()