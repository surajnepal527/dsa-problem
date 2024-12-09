class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_char = ''
        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                if num[i] > max_char:
                    max_char = num[i]
        return max_char*3

        