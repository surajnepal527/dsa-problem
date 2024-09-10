class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        if len(piles) == 1:
            total_hrs = piles[0]//h
            if piles[0]%h != 0:
                return total_hrs + 1
        left = 1 
        right = piles[0]
        for pile in piles:
            right = max(right, pile)
        
        while left < right:
            mid = left + (right-left)//2
            total_hrs = 0
            for pile in piles:
                total_hrs += (pile//mid)
                if pile%mid != 0:
                    total_hrs += 1
            if total_hrs <= h:
                right = mid
            else:
                left = mid + 1
        
        return left



        