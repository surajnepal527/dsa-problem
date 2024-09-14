class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #frequency array
        char_arr = [0]*26
        for i in range(len(s)):
            cur_idx = ord(s[i]) - 97
            char_arr[cur_idx] += 1
        
        for j in range(len(t)):
            cur_idx = ord(t[j]) - 97
            char_arr[cur_idx] -=1
            if char_arr[cur_idx] == -1:
                return False
        
        for k in range(26):
            if char_arr[k] != 0:
                return False
        
        return True
        