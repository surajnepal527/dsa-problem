class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1
        ans = []
        for num in nums:
            if num == 0:
                zero_count += 1 
            else:
                product = product * num
        
        for i in range(len(nums)):
            cur_num = nums[i]
            if zero_count > 0:
                if zero_count == 1 and cur_num == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                ans.append(product//cur_num)


        
        return ans

        