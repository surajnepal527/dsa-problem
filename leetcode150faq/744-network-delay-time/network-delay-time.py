import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}
        for u, v, w in times:
            adj[u].append((v,w))
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        min_heap = [(0,k)]
        while min_heap:
            wt_u, u = heapq.heappop(min_heap)
            for v, wt_v in adj[u]:
                n_wt = wt_u + wt_v
                if dist[v] > n_wt:
                    dist[v] = n_wt
                    heapq.heappush(min_heap,(n_wt, v))
        res = -1
        for i in range (1, len(dist)):
            if dist[i] == float('inf'):
                return -1
            res = max(res, dist[i])
        return res

        