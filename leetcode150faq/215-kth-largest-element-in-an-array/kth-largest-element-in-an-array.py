class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        L = 0
        R = length - 1
        privot_idx = L

        while(True):
            pivot_idx = self.getPivotIndex(nums, L, R)
            if pivot_idx == k -1:
                break
            elif pivot_idx < k-1:
                L = pivot_idx+1
            else:
                R = pivot_idx - 1
        
        return nums[pivot_idx]
    
    def getPivotIndex(self,nums, L , R):
        i = L+1
        j = R
        pivot_idx = L
        while i <= j:
            if nums[i] < nums[pivot_idx] and nums[j] > nums[pivot_idx]:
                nums[i], nums[j] = nums[j], nums[i]
                i +=- 1
                j -= 1
            
            if nums[i] >= nums[pivot_idx]:
                i += 1
            
            if nums[j] <= nums[pivot_idx]:
                j -= 1
        
        nums[j], nums[pivot_idx] = nums[pivot_idx], nums[j]
        return j

