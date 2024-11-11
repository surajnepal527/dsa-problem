class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def solve(i, j):
            if i == len(s) and j == len(p): return True
            if (i,j) in dp: return dp[(i,j)]
            first_char_match = False
            if i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == "."):
                first_char_match = True
            
            if j+1 < len(p) and p[j+1] == "*":
                not_take = solve(i, j+2)
                take = first_char_match and solve(i+1, j)
                dp[(i,j)] = not_take or take
                return dp[(i,j)]

            dp[(i,j)] = first_char_match and solve(i+1, j+1)
            return dp[(i,j)]
        return solve(0,0)



        