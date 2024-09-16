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
                cur = left
                possible_ans = min(lmax, rmax) - height[cur]
                if possible_ans > 0:
                    ans += possible_ans
                if height[cur] > lmax:
                    lmax = height[cur]
                left += 1
            else:
                cur = right
                possible_ans = min(lmax, rmax) - height[cur]
                if possible_ans > 0:
                    ans += possible_ans
                if height[cur] >rmax:
                    rmax = height[cur]
                right -= 1

        return ans
            
 

        