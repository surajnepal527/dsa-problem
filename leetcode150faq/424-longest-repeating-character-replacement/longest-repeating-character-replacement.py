class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        ans = 0
        count_map = {}
        for r in range(len(s)):
            count_map[s[r]] = count_map.get(s[r],0) + 1
            while (r-l+1 - max(count_map.values()) > k):
                count_map[s[l]] -= 1
                l +=1
            ans = max(ans, r-l+1)
        
        return ans
