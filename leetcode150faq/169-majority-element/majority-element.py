class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nummap = defaultdict(int)
        for num in nums:
            nummap[num] = nummap.get(num,0)+1
            if nummap[num] > len(nums)//2: return num
        
