from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_heap = []
        res = []
        for num, freq in count.items():
            heapq.heappush(max_heap, (freq, num))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        while max_heap:
            freq, num = heapq.heappop(max_heap)
            res.append(num)

        return res


        