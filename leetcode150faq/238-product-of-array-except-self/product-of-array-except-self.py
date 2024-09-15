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
            if zero_count > 0 and nums[i] != 0:
                ans.append(0)
            elif zero_count > 1 and nums[i] == 0:
                ans.append(0)
            elif zero_count == 1 and nums[i] == 0:
                ans.append(product)
            else:
                ans.append(product//nums[i])
        
        return ans

        