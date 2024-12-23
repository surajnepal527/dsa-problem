class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = [0] * 32
        for num in nums:
            for i in range(32):
                if num & (1<<i):
                    count[i] += 1
        num = 0
        for i in range(32):
            count[i] %= 3
            num |= count[i]<<i
        
        if count[31] == 1:
            return num - (1<<32)
        return num



        