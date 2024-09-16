class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_s = ""
        n = len(s)
        if n <=1:
            return True

        for i in range(len(s)):
            cur_ascii_char = ord(s[i])
            if cur_ascii_char >= 65 and cur_ascii_char <= 90:
                formatted_s += chr(cur_ascii_char+32)
            elif cur_ascii_char >= 97 and cur_ascii_char <= 122 or (cur_ascii_char >= 48 and cur_ascii_char <= 57):
                formatted_s += s[i]

        left,right = 0 , len(formatted_s) - 1
        while left < right:
            if formatted_s[left] != formatted_s[right]:
                return False
            left += 1
            right -= 1
        
        return True