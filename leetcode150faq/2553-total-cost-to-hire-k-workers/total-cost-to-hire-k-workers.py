import heapq
import sys
class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        ans = 0
        i = 0 
        j = len(costs) - 1
        hire = 0
        min_heap_left = []
        min_heap_right = []
        while hire < k:
            while len(min_heap_left) < candidates and i <= j:
                heapq.heappush(min_heap_left, costs[i])
                i += 1
            while len(min_heap_right) < candidates and j >= i:
                heapq.heappush(min_heap_right, costs[j])
                j -= 1

            left_min, right_min  = sys.maxsize, sys.maxsize
           
            if min_heap_left:
                left_min = min_heap_left[0]

            if  min_heap_right:
                right_min = min_heap_right[0]

            #value comparision between two min heaps
            if left_min <= right_min:
                ans += left_min
                heapq.heappop(min_heap_left)
            else:
                ans += right_min
                heapq.heappop(min_heap_right)
            
            hire += 1

        return ans        