class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t = [ [0 for _ in range(n+1)] for _ in range(m+1)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c == n-1:
                    t[r][c] = 1
                else:
                    t[r][c] = t[r+1][c] + t[r][c+1]
        return t[0][0]

        