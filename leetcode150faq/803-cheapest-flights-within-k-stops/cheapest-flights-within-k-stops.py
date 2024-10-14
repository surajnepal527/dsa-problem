import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for f, t, p in flights:
            adj[f].append([t, p])
        min_heap = [(-1, 0,src)]
        dist = [float('inf')] * n
        dist[src] = 0
        while min_heap:
            stop, src_price,src = heapq.heappop(min_heap)
            for nei, price  in adj[src]:
                new_price = price + src_price
                if dist[nei]> new_price and stop+1 <= k:
                    dist[nei] = new_price
                    heapq.heappush(min_heap, (stop+1,new_price,nei))
            
        return dist[dst] if dist[dst] != float('inf') else -1



        