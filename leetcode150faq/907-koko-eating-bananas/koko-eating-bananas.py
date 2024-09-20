class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        while left < right:
            mid = (left+right)//2
            total_hr = 0
            for pile in piles:
                total_hr += pile//mid
                if pile%mid > 0 :
                    total_hr += 1
            if total_hr <= h:
                right = mid
            else:
                left = mid + 1
        
        return right

        