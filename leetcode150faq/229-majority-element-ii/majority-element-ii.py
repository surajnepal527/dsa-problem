class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj1,maj2, cnt1, cnt2 = None, None, 0 , 0
        for num in nums:
            if num == maj1:
                cnt1 += 1
            elif num == maj2:
                cnt2 += 1
            elif cnt1 == 0:
                maj1 = num
                cnt1 += 1
            elif cnt2 == 0:
                maj2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        #verification
        ver_cnt1, ver_cnt2 = 0, 0 
        for num in nums:
            if num == maj1:
                ver_cnt1 += 1
            if num == maj2:
                ver_cnt2 += 1
        n = len(nums)
        output= []
        if ver_cnt1 > n//3:
            output.append(maj1)
        if ver_cnt2 > n//3:
            output.append(maj2)
        return output

        