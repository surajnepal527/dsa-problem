class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        m, n , N = len(s1), len(s2), len(s3)
        memo = {}
        def solve(i, j, k):
            if i == m and j == n and k == N: return True
            if k >= N: return False
            if (i, j, k) in memo: return memo[(i, j , k)]
            result = False
            if i < m and s1[i] == s3[k]:
                result = solve(i+1, j , k+1)
            if result:
                memo[(i, j, k)] = result
                return memo[(i, j,k)]   
            if j < n and  s2[j] == s3[k]:
                result = solve(i, j+1, k+1)
            memo[(i,j,k)] = result
            return memo[(i, j,k)]
        return solve(0,0,0)
        