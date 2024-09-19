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
            if char_map.get(s[r], 0) > 0:
                req_count -= 1
            char_map[s[r]] = char_map.get(s[r], 0) - 1
            while req_count == 0:
                if min_win > r-l+1:
                    min_win = min(min_win, r-l+1)
                    start_l = l
                char_map[s[l]] += 1
                if char_map[s[l]] > 0:
                    req_count += 1
                l += 1
            r += 1
        
        return s[start_l:start_l+min_win] if min_win != n+1 else ""
        #if min_win != n+1:
        #     return s[start_l: start_l+min_win]
        #else:
        #     return ""
        