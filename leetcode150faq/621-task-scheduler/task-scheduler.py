import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        tf_map = {}
        ans = 0
        for task in tasks:
            tf_map[task] = tf_map.get(task, 0) + 1
        for task, freq in tf_map.items():
            heapq.heappush(max_heap, -freq)
        
        while max_heap:
            k = 0
            tmp_task_arr = []
            while max_heap and k < n+1:
              freq = -heapq.heappop(max_heap)
              ans += 1
              k += 1
              freq -= 1
              if freq > 0:
                tmp_task_arr.append(freq)
            if tmp_task_arr:
                ans += n+1-k
            for fre in tmp_task_arr:
                heapq.heappush(max_heap, -fre)
        
        return ans
































        