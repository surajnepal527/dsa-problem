from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        count_map = defaultdict(int)
        count_map[s[0]] += 1
        max_len, start, end = 1, 0, 1
        while end < len(s):
            ch = s[end]
            count_map[ch] += 1
            if count_map[ch] > 1:
                max_len = max(max_len , end-start)
                while count_map[ch] > 1:
                    count_map[s[start]] -= 1
                    start += 1
            else:
                max_len = max(max_len , end-start+1)
            end += 1
        return max_len


        