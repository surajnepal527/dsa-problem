import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set([0,0])
        min_heap = [(grid[0][0], 0 ,0)]
        directions = [(1,0), (-1,0),(0,1),(0,-1)]
        while min_heap:
            t,row, col = heapq.heappop(min_heap)
            if row == n - 1 and col == n-1:
                return t
            for dr, dc in directions:
                neiR, neiC = row + dr, col + dc
                #check boundaries:
                if any([0 > neiR , neiR == n , 0 > neiC , neiC == n , (neiR, neiC) in visited]):
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(min_heap, (max(t, grid[neiR][neiC]),neiR, neiC))
        return -1
