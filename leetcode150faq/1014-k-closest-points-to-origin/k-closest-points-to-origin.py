import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        ans = []
        for idx,pt in enumerate(points):
            dist = ((pt[0]*pt[0]) +(pt[1]*pt[1]))**0.5
            if len(min_heap) < k:
                heapq.heappush(min_heap,(-abs(dist),idx))
            else:
                min_dist, min_idx = min_heap[0]
                if abs(min_dist) > abs(dist):
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,(-abs(dist), idx))
        while min_heap:
            dist, index = heapq.heappop(min_heap)
            ans.append(points[index])
        return ans



        