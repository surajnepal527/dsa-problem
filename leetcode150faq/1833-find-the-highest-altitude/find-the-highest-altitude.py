import sys
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_alt = 0
        prefix_sum = 0
        for alt in gain:
            prefix_sum += alt
            max_alt = max(max_alt, prefix_sum)
        return max_alt
        