class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            cal_sum = numbers[start] + numbers[end]
            if cal_sum > target:
                end-= 1
            elif cal_sum < target:
                start += 1
            else:
                return[start+1, end+1]
        