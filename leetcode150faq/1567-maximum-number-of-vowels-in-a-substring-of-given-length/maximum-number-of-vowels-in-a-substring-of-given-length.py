class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0
        i = 0
        vow_map = {'a', 'e', 'i','o','u'}
        while i < k:
            if s[i] in vow_map:
                count += 1
            i += 1

        left = 0 
        max_count = count
        cur_count  = count
        for j in range(i, len(s)):
            if s[left] not in vow_map and s[j] in vow_map:
                cur_count += 1
                max_count = max(max_count, cur_count)
            elif s[left] in vow_map and s[j] not in vow_map:
                cur_count -= 1
        
            left += 1
        return max_count
