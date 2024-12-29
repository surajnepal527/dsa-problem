class Solution:
    def maxArea(self, height: List[int]) -> int:
        s, e, = 0 , len(height)-1
        cur_area, max_area = 0,0
        while s < e:
            cur_area = min(height[s], height[e]) * (e-s)
            max_area = max(cur_area, max_area)
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return max_area