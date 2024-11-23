class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_len, num = len(digits), 0
        for idx, digit in enumerate(digits):
            num += digit * (10 ** (num_len-1-idx))
        num += 1
        new_len = len(str(num))
        result = [0] * new_len
        i = new_len -1
        while num and i >= 0:
            result[i] = num % 10
            num = num //10
            i -= 1
        return result