class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        XOR = 0
        for ch in s:
            XOR ^= ord(ch)
        for ch in t:
            XOR ^= ord(ch)
        return chr(XOR)


        