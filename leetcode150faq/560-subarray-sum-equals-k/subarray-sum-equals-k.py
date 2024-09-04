class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum, ans = 0 , 0
        map = {}
        map[0] = 1
        for num in nums:
            sum += num
            diff = sum - k
            if diff in map:
                ans += map[diff]

            map[sum] = map.get(sum, 0)+1
            
        return ans