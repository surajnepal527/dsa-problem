class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        XOR = 0
        for num in nums:
            XOR ^= num
        right_most_set_bit = XOR & -XOR
        num1, num2 = 0, 0
        for num in nums:
            if num & right_most_set_bit:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


        