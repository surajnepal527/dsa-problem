import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #let create an adjacency list
        adj = {i:[] for i in range(len(points))}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                wt = abs(xj - xi) + abs(yj- yi)
                adj[i].append((wt, j))
                adj[j].append((wt, i))
        
        visited = set()
        min_heap = []
        sum_wt = 0
        heapq.heappush(min_heap,(0,0))
        while min_heap:
            wt, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            sum_wt  += wt
            visited.add(node)
            for wt, nd in adj[node]:
                if nd not in visited:
                    heapq.heappush(min_heap, (wt, nd))
        return sum_wt

        