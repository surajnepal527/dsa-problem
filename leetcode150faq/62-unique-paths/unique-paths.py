class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t = [[-1 for _ in range(n)] for _ in range(m)]
        def solve(r, c):
            if r == m-1 and c == n-1: return 1
            if r >= m or c >= n: return 0
            if t[r][c] != -1: return t[r][c]
            t[r][c] = solve(r+1, c) + solve(r, c+1)
            return t[r][c]
        return solve(0, 0)
