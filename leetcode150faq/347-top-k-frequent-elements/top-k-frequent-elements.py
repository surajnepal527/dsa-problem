import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res, max_heap, freq_map = [], [],{}
        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
        for key in freq_map:
            value = freq_map[key]
            heapq.heappush(max_heap,(-value, key))
        for i in range(k):
            neg_value, num = heapq.heappop(max_heap)
            res.append(num)
        return res
        