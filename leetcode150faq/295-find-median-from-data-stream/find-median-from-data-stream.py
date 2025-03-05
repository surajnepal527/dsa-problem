class MedianFinder:

    def __init__(self):
        self.array = []
        self.size = 0
        

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.size += 1

    def findMedian(self) -> float:
        if self.size == 0:
            return 0
        self.array.sort()
        if self.size%2 == 0:
            mid = self.size//2
            return (self.array[mid] + self.array[mid-1])/2.0
        return self.array[self.size//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()