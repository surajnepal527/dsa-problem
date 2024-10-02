class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digit_map = {"2": "abc","3":"def","4":"ghi","5":"jkl", "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def backtrack(cur_idx, ans):
            if len(ans) == len(digits):
                res.append("".join(ans))
                return
            for ch in digit_map[digits[cur_idx]]:
                ans.append(ch)
                backtrack(cur_idx+1, ans)
                ans.pop()
        backtrack(0,[])
        return res