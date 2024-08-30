class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            else:
                return False
            
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and n > 0:
                if (i == 0 and flowerbed[i+1] == 0) or (i == len(flowerbed) - 1 and flowerbed[i-1] == 0) or (flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
        
        if n == 0:
            return True
        else:
            return False
            

            
        