class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(idx, cur):
            if idx == len(s):
                res.append(cur.copy())
                return
            for i in range(idx, len(s)):
                subString = s[idx:i+1]
                if self.isPalindrom(subString):
                    cur.append(subString)
                    dfs(i+1, cur)
                    cur.pop()
        dfs(0,[])
        return res

    def isPalindrom(self,s:str):
        return s == s[::-1]
            




















    
        