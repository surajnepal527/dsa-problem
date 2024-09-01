class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        uni_set = set()
        uni_map = {}
        for num in arr:
            uni_map[num] = uni_map.get(num,0) + 1
        
        for value in uni_map.values():
            if value not in uni_set:
                uni_set.add(value)
            else:
                return False
                
        return True

        