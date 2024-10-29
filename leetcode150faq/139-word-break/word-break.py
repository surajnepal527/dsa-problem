class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1] * 302
        def solve(i, st):
            if i == len(s) : return True
            if dp[i] != -1: return dp[i]
            if st in wordDict:
                dp[i] = True
                return dp[i]
            for k in range(len(st)):
                tmp = st[:k]
                if tmp in wordDict and solve(i+len(tmp),st[len(tmp):]):
                    dp[i] = True
                    return dp[i]
            dp[i] = False
            return dp[i]
        
        return solve(0, s)