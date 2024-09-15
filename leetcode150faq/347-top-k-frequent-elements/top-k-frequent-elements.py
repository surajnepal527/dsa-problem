import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map, ans , max_heap = {}, [],[]
       
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num_fre in freq_map:
            key = num_fre
            value = freq_map[key]
            heapq.heappush(max_heap, (-value, key))
        
        for i in range(k):
            neg_value, key = heapq.heappop(max_heap)
            ans.append(key)

        return ans



        

        
        
         