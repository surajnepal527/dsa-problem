class Solution:
    def maxArea(self, height: List[int]) -> int:
        cur_area, max_area , s , e = 0, 0, 0, len(height)-1
        while s < e:
            cur_area = min(height[s], height[e])*(e-s)
            max_area = max(cur_area, max_area)
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return max_area
        