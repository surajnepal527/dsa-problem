class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, char_set =0, set()
        left = 0
        for right, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(char)    
            res = max(res, len(char_set))
        return res

        