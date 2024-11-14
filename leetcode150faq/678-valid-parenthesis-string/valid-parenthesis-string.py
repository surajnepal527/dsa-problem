class Solution:
    def checkValidString(self, s: str) -> bool:
        #trickt solution where we maintain count of open and close bracket for left to right and right to left
        open_count, close_count, n  = 0, 0, len(s)
        for i in range(n):
            if s[i] == "(" or s[i] == "*":
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return False
        for i in range(n-1, -1, -1):
            if s[i] == ")" or s[i] == "*":
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False
        return True
        