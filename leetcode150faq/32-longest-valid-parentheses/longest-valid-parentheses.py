class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open_ct , close_ct , max_len = 0, 0, 0
        for ch in s:
            if ch == "(":
                open_ct += 1
            else:
                close_ct += 1
                if open_ct == close_ct:
                    max_len = max(max_len, close_ct*2)
                elif close_ct > open_ct:
                    open_ct, close_ct = 0 , 0
        open_ct, close_ct = 0 ,0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ")":
                close_ct += 1
            else:
                open_ct += 1
                if open_ct == close_ct:
                    max_len = max(max_len, open_ct*2)
                elif open_ct > close_ct:
                    open_ct, close_ct = 0 , 0
        return max_len
                     
        