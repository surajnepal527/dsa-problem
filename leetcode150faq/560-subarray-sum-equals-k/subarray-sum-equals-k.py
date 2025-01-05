
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        prefixSumMap = {0:1}
        count = 0
        for num in nums:
            prefixSum += num
            diff = prefixSum - k
            count += prefixSumMap.get(diff, 0)
            prefixSumMap[prefixSum] = prefixSumMap.get(prefixSum,0) +1
        return count
