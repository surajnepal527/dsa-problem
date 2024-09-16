class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = height[0]
        rmax = height[n-1]
        left = 1
        right = n - 2
        ans = 0
        while left <= right:
            if lmax <= rmax:
                possible_ans = min(lmax, rmax) - height[left]
                if possible_ans > 0:
                    ans += possible_ans
                if height[left] > lmax:
                    lmax = height[left]
                left += 1
            else:
                possible_ans = min(lmax, rmax) - height[right]
                if possible_ans > 0:
                    ans += possible_ans
                if height[right] > rmax:
                    rmax = height[right]
                right -= 1

        return ans
            
 

        