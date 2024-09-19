class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l, r, start_l, req_count, n = 0, 0, -1, len(t),len(s)
        min_win = len(s) + 1
        char_map = {}
        for t_char in t:
            char_map[t_char] = char_map.get(t_char, 0) + 1
        
        while r < n:
            char_r = s[r]
            if char_map.get(char_r, 0) > 0:
                req_count -= 1
            char_map[char_r] = char_map.get(char_r, 0) - 1
            while req_count == 0:
                if min_win > r-l+1:
                    min_win = min(min_win, r-l+1)
                    start_l = l
                char_l = s[l]
                char_map[char_l] = char_map.get(char_l, 0) + 1
                if char_map.get(s[l], 0) > 0:
                    req_count += 1
                l += 1
            r += 1
        
        if min_win != n+1:
             return s[start_l: start_l+min_win]
        else:
             return ""
        