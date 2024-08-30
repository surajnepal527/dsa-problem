class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candie = candies[0]
        for i in range(len(candies)):
            if candies[i] > max_candie:
                max_candie = candies[i]
        ans = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candie:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
