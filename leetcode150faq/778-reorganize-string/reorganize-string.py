from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [[-count, char] for char, count in count.items()]
        heapq.heapify(max_heap)
        res = ""
        prev = None
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            cnt, char = heapq.heappop(max_heap)
            res += char
            cnt += 1
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res

        