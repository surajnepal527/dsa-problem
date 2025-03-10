class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        prev = self.countAndSay(n-1)
        #processing
        i = 0
        result = []
        while i < len(prev):
            count = 1
            while i+1 <len(prev) and prev[i] == prev[i+1]:
                count += 1
                i += 1
            result.append(f"{count}{prev[i]}")
            i += 1
        return "".join(result)
