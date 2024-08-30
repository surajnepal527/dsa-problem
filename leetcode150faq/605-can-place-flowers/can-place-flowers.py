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
            elif flowerbed[0] == 1 and n > 0:
                return False
            elif flowerbed[0] == 1 and n == 0:
                return True
            else:
                return False
            
        if flowerbed[0] == 0:
            if flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
        for i in range(1, len(flowerbed)):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and n > 0:
                if i == len(flowerbed) - 1 or flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        
        if n == 0:
            return True
        else:
            return False
            

            
        