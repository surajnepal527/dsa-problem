class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        while True:
            if i == len(strs[0]): return res
            cur = strs[0][i]
            for st in strs:
                if i == len(st): return res
                if cur != st[i]: return res
            res += cur    
            i += 1
        return res

        