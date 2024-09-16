class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        char_set = set()
        max_len = 0
        left = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[r])
            max_len = max(max_len, (r - left + 1))
        
        return max_len

        