class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o_c = "("
        c_c = ")"
        o_s = "["
        c_s = "]"
        o_cr = "{"
        c_cr= "}"
        for char in s:
            if char == o_c or char == o_s or char == o_cr:
                stack.append(char)
            else:
                if not stack:
                    return False
                pop_char = stack.pop()
                if not ((char == c_c and pop_char == o_c) or (char == c_s and pop_char == o_s) or (char == c_cr and pop_char == o_cr)):
                    return False
        if stack:
            return False
        
        return True
        

        