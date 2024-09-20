class Pair:
    def __init__(self, idx, height):
        self.idx = idx
        self.height = height

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        cur_pop_idx = -1
        n = len(heights)
        for r in range(len(heights)):
            if not stack or stack[-1].height <= heights[r]:
                stack.append(Pair(r,heights[r]))
            else:
                while stack and stack[-1].height > heights[r]:
                    cur_pop_idx = stack[-1].idx
                    cur_pop_height = stack[-1].height
                    max_area = max(max_area, cur_pop_height *(r-cur_pop_idx))
                    stack.pop()
                stack.append(Pair(cur_pop_idx, heights[r]))
        
        while stack:
            ht = stack[-1].height 
            idx = stack[-1].idx
            max_area = max(max_area, ht * (n-idx))
            stack.pop()
        
        return max_area


        