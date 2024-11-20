class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        val_cnt = 0
        for num in nums:
            if num == val: val_cnt += 1
        if val_cnt == 0 : return len(nums)
        i, j = 0 , len(nums) -1
        while i < j:
            if nums[j] == val:
                j -= 1
            elif nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else:
                i += 1
        return len(nums) - val_cnt



        