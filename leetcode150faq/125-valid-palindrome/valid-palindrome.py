class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isValidAscii(ch:chr)->bool:
            ascii_val = ord(ch)
            return (ascii_val >= ord('0') and ascii_val <= ord('9')) or (ascii_val >= ord('a') and ascii_val <= ord('z')) or (ascii_val >= ord('A') and ascii_val <= ord('Z'))
        left, right = 0, len(s)-1
        while left < right:
            while not isValidAscii(s[left]) and left < right:
                left += 1
            while not isValidAscii(s[right]) and left < right:
                right -=1
            if left == right:
                return True
            left_char = (s[left]).lower()
            right_char = (s[right]).lower()
            if left_char != right_char:
                return False
            left += 1
            right -= 1
        return True


    

        