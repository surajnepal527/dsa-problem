class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1] * 302
        def solve(st, i):
            if i >= len(s): return True
            if dp[i] != -1: return dp[i]
            for w in wordDict:
                if st[:len(w)] == w:
                    if solve(st[len(w):], i+len(w)):
                        dp[i] = True
                        return dp[i]
            dp[i] = False
            return dp[i]
        return solve(s,0)

        