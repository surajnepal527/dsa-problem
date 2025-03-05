class MedianFinder:

    def __init__(self):
        self.array = []
        

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        size = len(self.array)
        if size == 0:
            return 0
        self.array.sort()
        if size%2 == 0:
            mid = size//2
            return (self.array[mid] + self.array[mid-1])/2.0
        return self.array[size//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()