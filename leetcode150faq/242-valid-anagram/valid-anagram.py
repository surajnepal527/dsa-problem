class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_arr_s = [0]*26
        freq_arr_t = [0]*26
        for char_s in s:
            freq_arr_s[ord(char_s)-ord('a')] += 1
        for char_t in t:
            freq_arr_t[ord(char_t) - ord('a')] += 1
        
        for i in range(26):
            if freq_arr_s[i] != freq_arr_t[i]:
                return False
        return True

        