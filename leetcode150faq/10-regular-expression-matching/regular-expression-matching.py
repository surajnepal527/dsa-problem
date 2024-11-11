class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def solve(i, j):
            if i == len(s) and j == len(p): return True
            first_char_match = False
            if i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == "."):
                first_char_match = True
            
            if j+1 < len(p) and p[j+1] == "*":
                not_take = solve(i, j+2)
                take = first_char_match and solve(i+1, j)
                return not_take or take

            return first_char_match and solve(i+1, j+1)
        return solve(0,0)



        