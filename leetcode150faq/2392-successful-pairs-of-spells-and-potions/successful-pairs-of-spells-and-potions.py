import math
import sys
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        #1. Sort the portion array 
        #2. Implement the binary search in potion arry to find the lower bound index
        #3. find the mid point on poition for lower bound
        potions.sort()
        ans = []
        for spell in spells:
            mid_potion = math.ceil(float(success)/spell)
            if potions[-1] < mid_potion:
                ans.append(0)
            else:
                mid_potion_index = self.getLowerBoundIndex(potions, mid_potion)
                ans.append(len(potions)-mid_potion_index)
        
        return ans
    
    def getLowerBoundIndex(self, arr, mid_potion):
        left = 0
        right = len(arr) - 1
        possible_index = -1
        while left <= right:
            mid = left + (right - left) / 2
            if arr[mid] >= mid_potion:
                possible_index = mid
                right = mid - 1
            else:
                left = mid + 1
        return possible_index

                


        