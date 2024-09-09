import heapq
class SmallestInfiniteSet(object):

    def __init__(self):
        self.min_heap = []
        self.hashset = set()

        for i in range(1,10001):
            self.hashset.add(i)
            heapq.heappush(self.min_heap, i)

    def popSmallest(self):
        """
        :rtype: int
        """
        smallest_num = heapq.heappop(self.min_heap)
        self.hashset.remove(smallest_num)
        return smallest_num
        
    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.hashset:
            self.hashset.add(num)
            heapq.heappush(self.min_heap,num)
            

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)