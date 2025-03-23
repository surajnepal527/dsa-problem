class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #approach was good but it seems more complicated.
        #lets just try to set and so the same 
        #as soon as we see cur char already exist in set before we even insert it
        #we try to remove all elmement from let till we remove the curent element
        #then we add new char and check for size
        char_set = set()
        left, res = 0, 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, len(char_set))
        return res


        