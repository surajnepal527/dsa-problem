class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        cur_one_count = 0
        max_one_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_one_count += 1
                max_one_count = max(max_one_count, cur_one_count)
            else:
                if k > 0:
                    k -= 1
                    cur_one_count += 1
                    max_one_count = max(max_one_count, cur_one_count)
                else:
                    if nums[left] == 0:
                        left += 1
                    else:
                        while nums[left] != 0 and left < len(nums):
                            left += 1
                            cur_one_count -= 1
                        left += 1

        return max_one_count

            

        