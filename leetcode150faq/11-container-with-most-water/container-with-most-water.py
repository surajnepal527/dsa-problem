class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, cur_area = 0,0
        left, right = 0, len(height) - 1
        while left < right:
            width = right-left
            length = min(height[left], height[right])
            cur_area =  width*length
            max_area = max(max_area, cur_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

        